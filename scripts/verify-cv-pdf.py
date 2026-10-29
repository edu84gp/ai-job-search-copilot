import argparse
import json
import re
import sys
import zlib
from pathlib import Path

MAX_DECOMPRESSED = 8 * 1024 * 1024
MAX_STREAMS = 200
MAX_TEXT = 40000

PAGE_RE = re.compile(rb"/Type\s*/Page(?![sA-Za-z])")
MEDIABOX_RE = re.compile(rb"/MediaBox")
FONT_RE = re.compile(rb"/BaseFont\s*/([A-Za-z0-9+\-_,]+)")
IMAGE_RE = re.compile(rb"/Subtype\s*/Image")
UNICODE_RE = re.compile(rb"/ToUnicode")
URI_RE = re.compile(rb"/URI\s*\(([^)]*)\)")
TJ_ARRAY_RE = re.compile(rb"\[((?:[^\[\]\\]|\\.)*)\]\s*TJ")
TJ_STRING_RE = re.compile(rb"\((?:\\.|[^\\()])*\)\s*Tj")
TEXT_TOKEN_RE = re.compile(rb"\[((?:[^\[\]\\]|\\.)*)\]\s*TJ|(\((?:\\.|[^\\()])*\)\s*Tj)")
IN_ARRAY_TOKEN_RE = re.compile(rb"\(((?:\\.|[^\\()])*)\)|<([0-9A-Fa-f\s]+)>")
LITERAL_RE = re.compile(rb"\((?:\\.|[^\\()])*\)")
LINE_BREAK_RE = re.compile(rb"\bT[mDd]\b|T\*")
CMAP_CHAR_RE = re.compile(rb"beginbfchar(.*?)endbfchar", re.S)
CMAP_RANGE_RE = re.compile(rb"beginbfrange(.*?)endbfrange", re.S)
ESCAPES = {b"n": b"\n", b"r": b"\r", b"t": b"\t", b"b": b"\b", b"f": b"\f", b"(": b"(", b")": b")", b"\\": b"\\"}
ACCENTS = set("áéíóúüñÁÉÍÓÚÜÑ")


def force_utf8():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:
            pass


def unescape(raw):
    out = bytearray()
    i = 0
    while i < len(raw):
        char = raw[i:i + 1]
        if char != b"\\":
            out += char
            i += 1
            continue
        nxt = raw[i + 1:i + 2]
        if nxt in ESCAPES:
            out += ESCAPES[nxt]
            i += 2
        elif nxt.isdigit():
            digits = raw[i + 1:i + 4]
            take = 0
            value = b""
            while take < 3 and take < len(digits) and digits[take:take + 1].isdigit():
                value += digits[take:take + 1]
                take += 1
            out.append(int(value, 8) & 0xFF)
            i += 1 + take
        elif nxt in (b"\n", b"\r"):
            i += 2
        else:
            out += nxt
            i += 2
    return bytes(out)


def decompress_streams(data):
    streams = []
    for match in re.finditer(rb"stream\r?\n", data):
        start = match.end()
        end = data.find(b"endstream", start)
        if end == -1:
            continue
        body = data[start:end]
        if body.endswith(b"\r\n"):
            body = body[:-2]
        elif body.endswith(b"\n") or body.endswith(b"\r"):
            body = body[:-1]
        try:
            obj = zlib.decompressobj()
            out = obj.decompress(body, MAX_DECOMPRESSED)
        except zlib.error:
            continue
        if out:
            streams.append(out)
        if len(streams) >= MAX_STREAMS:
            break
    return streams


def looks_like_content(stream):
    sample = stream[:4096]
    if not sample:
        return False
    printable = sum(1 for byte in sample if 9 <= byte <= 126 or byte in (10, 13))
    return printable / len(sample) > 0.9


def decode_utf16(hex_text):
    try:
        return bytes.fromhex(hex_text.decode()).decode("utf-16-be", errors="replace")
    except ValueError:
        return ""


def build_cid_map(streams):
    mapping = {}
    for stream in streams:
        if b"beginbfchar" not in stream and b"beginbfrange" not in stream:
            continue
        for block in CMAP_CHAR_RE.findall(stream):
            for source, target in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
                mapping[int(source, 16)] = decode_utf16(target)
        for block in CMAP_RANGE_RE.findall(stream):
            for low, high, target in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
                start, end = int(low, 16), int(high, 16)
                base = int(target, 16)
                for offset in range(end - start + 1):
                    mapping[start + offset] = chr(base + offset)
            for low, high, group in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*\[([^\]]*)\]", block):
                start = int(low, 16)
                for offset, item in enumerate(re.findall(rb"<([0-9A-Fa-f]+)>", group)):
                    mapping[start + offset] = decode_utf16(item)
    return mapping


def decode_hex_codes(token, cid_map, stats):
    codes = re.sub(rb"\s+", b"", token).decode()
    out = []
    for index in range(0, len(codes), 4):
        chunk = codes[index:index + 4]
        if len(chunk) < 4:
            break
        cid = int(chunk, 16)
        stats["cid"] += 1
        if cid in cid_map:
            out.append(cid_map[cid])
        else:
            stats["sin_mapa"] += 1
            out.append("?")
    return "".join(out)


def extract_text(streams, cid_map):
    lines = []
    total = 0
    stats = {"cid": 0, "sin_mapa": 0}
    for stream in streams:
        if b"TJ" not in stream and b"Tj" not in stream:
            continue
        if not looks_like_content(stream):
            continue
        buffer = []
        cursor = 0
        for match in TEXT_TOKEN_RE.finditer(stream):
            between = stream[cursor:match.start()]
            if buffer and LINE_BREAK_RE.search(between):
                text = "".join(buffer).strip()
                if text:
                    lines.append(text)
                    total += len(text)
                buffer = []
            cursor = match.end()
            array = match.group(1)
            if array is not None:
                for token in IN_ARRAY_TOKEN_RE.finditer(array):
                    if token.group(1) is not None:
                        buffer.append(unescape(token.group(1)).decode("latin-1"))
                    else:
                        buffer.append(decode_hex_codes(token.group(2), cid_map, stats))
            else:
                literal = match.group(2)
                start = literal.find(b"(")
                end = literal.rfind(b")")
                buffer.append(unescape(literal[start + 1:end]).decode("latin-1"))
            if total >= MAX_TEXT:
                break
        text = "".join(buffer).strip()
        if text:
            lines.append(text)
            total += len(text)
        if total >= MAX_TEXT:
            break
    return lines, stats


def count_words(text):
    return len(re.findall(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", text))


def markdown_words(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[#*`>]", " ", text)
    return count_words(text)


def analyse(path, markdown=None):
    data = path.read_bytes()
    streams = decompress_streams(data)
    haystack = data + b"\n".join(streams)

    pages = len(PAGE_RE.findall(haystack)) or len(MEDIABOX_RE.findall(haystack))
    fonts = sorted({m.group(1).decode("latin-1") for m in FONT_RE.finditer(haystack)})
    images = len(IMAGE_RE.findall(haystack))
    tounicode = len(UNICODE_RE.findall(haystack))
    links = sorted({m.group(1).decode("latin-1") for m in URI_RE.finditer(haystack)})

    lines, cid_stats = extract_text(streams, build_cid_map(streams))
    text = "\n".join(lines)

    md_words = markdown_words(markdown) if markdown else None
    normalized = count_words(text)
    delta = normalized - md_words if md_words is not None else None

    problems = []
    if not data.startswith(b"%PDF-"):
        problems.append("El archivo no empieza por %PDF-, la cabecera no es válida.")
    if pages != 1:
        problems.append(f"El PDF declara {pages} páginas; un CV junior debe tener una.")
    if not fonts:
        problems.append("No se detectan fuentes embebidas, el texto podría no ser extraíble.")
    if images:
        problems.append(f"Se detectan {images} imágenes incrustadas.")
    if len(text) < 400:
        problems.append(f"Solo se extraen {len(text)} caracteres de texto; el PDF podría ser una imagen.")
    if "\ufffd" in text:
        problems.append("El texto extraído contiene caracteres de reemplazo, la codificación no se resuelve.")
    if cid_stats["sin_mapa"]:
        problems.append(f"{cid_stats['sin_mapa']} caracteres usan códigos CID sin mapa ToUnicode y no se pueden extraer.")
    if delta is not None and abs(delta) > 20:
        problems.append(f"El PDF tiene {normalized} palabras y el Markdown {md_words}: difieren en {abs(delta)}.")

    accents = sum(1 for char in text if char in ACCENTS)

    return {
        "archivo": str(path),
        "bytes": len(data),
        "version": data[:8].decode("latin-1").strip(),
        "paginas": pages,
        "fuentes": fonts,
        "fuentes_con_tounicode": tounicode,
        "imagenes": images,
        "enlaces": links,
        "caracteres_texto": len(text),
        "palabras": normalized,
        "palabras_markdown": md_words,
        "delta_palabras": delta,
        "lineas": len(lines),
        "acentos": accents,
        "caracteres_reemplazo": text.count("\ufffd"),
        "cid_decodificados": cid_stats["cid"] - cid_stats["sin_mapa"],
        "cid_sin_mapa": cid_stats["sin_mapa"],
        "muestra": lines[:6],
        "problemas": problems,
        "veredicto": "APTO" if not problems else "CORREGIR",
    }


def main():
    force_utf8()
    parser = argparse.ArgumentParser(description="Verifica un CV en PDF de forma determinista para ATS.")
    parser.add_argument("pdf", help="Ruta del PDF que se va a verificar.")
    parser.add_argument("--md", help="Ruta del Markdown de origen para comparar contenido.")
    parser.add_argument("--json", action="store_true", help="Devuelve la salida en JSON.")
    args = parser.parse_args()

    path = Path(args.pdf)
    if not path.is_file():
        print(json.dumps({"error": f"No existe el archivo {path}"}, ensure_ascii=False))
        return 2

    markdown = Path(args.md) if args.md else None
    if markdown is not None and not markdown.is_file():
        print(json.dumps({"error": f"No existe el archivo {markdown}"}, ensure_ascii=False))
        return 2

    report = analyse(path, markdown)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Archivo: {report['archivo']}")
        print(f"Tamaño: {report['bytes']} bytes | Versión: {report['version']}")
        print(f"Páginas: {report['paginas']}")
        print(f"Fuentes: {', '.join(report['fuentes']) or 'ninguna'} | Con ToUnicode: {report['fuentes_con_tounicode']}")
        print(f"Imágenes: {report['imagenes']}")
        print(f"Enlaces: {len(report['enlaces'])}")
        print(f"Texto extraído: {report['caracteres_texto']} caracteres, {report['palabras']} palabras, {report['lineas']} líneas")
        print(f"Acentos conservados: {report['acentos']} | Caracteres de reemplazo: {report['caracteres_reemplazo']}")
        if report["palabras_markdown"] is not None:
            print(f"Markdown: {report['palabras_markdown']} palabras | Diferencia: {report['delta_palabras']}")
        print("Muestra:")
        for line in report["muestra"]:
            print(f"  {line}")
        if report["problemas"]:
            print("Problemas:")
            for problem in report["problemas"]:
                print(f"  - {problem}")
        print(f"Veredicto: {report['veredicto']}")

    return 0 if report["veredicto"] == "APTO" else 1


if __name__ == "__main__":
    sys.exit(main())
