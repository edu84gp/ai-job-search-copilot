import argparse
import csv
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORT_ROOT = ROOT / "docs" / "privado" / "linkedin" / "exportaciones"
NORMALIZED_DIRNAME = "_normalizado"
SENSITIVE_FILES = {
    "messages.csv",
    "Email Addresses.csv",
    "PhoneNumbers.csv",
    "Ad_Targeting.csv",
    "Notes.csv",
    "Logins.csv",
    "SearchQueries.csv",
    "Security Challenges.csv",
    "Inferences_about_you.csv",
    "Ads Clicked.csv",
    "LAN Ads Engagement.csv",
}
SENSITIVE_PREFIXES = ("guide_messages", "learning_coach_messages", "learning_role_play_messages")

sys.stdout.reconfigure(encoding="utf-8")


def fail(message, code=1):
    print("ERROR: " + message)
    raise SystemExit(code)


def strip_notes_block(text):
    if not text.startswith("Notes:"):
        return text
    lines = text.splitlines()
    index = 0
    while index < len(lines) and not (index > 0 and lines[index].strip() == ""):
        index += 1
    return "\n".join(lines[index + 1:])


def read_csv(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig", errors="replace")
    text = strip_notes_block(text)
    reader = csv.DictReader(io.StringIO(text))
    rows = []
    for row in reader:
        cleaned = {}
        for key, value in row.items():
            if key is None:
                continue
            cleaned[key.strip()] = (value or "").strip()
        if any(cleaned.values()):
            rows.append(cleaned)
    return rows, [field.strip() for field in (reader.fieldnames or [])]


def is_sensitive(name):
    return name in SENSITIVE_FILES or name.startswith(SENSITIVE_PREFIXES)


def cmd_inventory(source, include_sensitive):
    folder = source if source.is_absolute() else ROOT / source
    if not folder.is_dir():
        fail("no existe la carpeta: " + str(folder))
    target = folder / NORMALIZED_DIRNAME
    target.mkdir(exist_ok=True)
    report = []
    for path in sorted(folder.glob("*.csv")):
        name = path.name
        if is_sensitive(name) and not include_sensitive:
            report.append({"file": name, "rows": None, "fields": [], "sensitive": True})
            continue
        rows, fields = read_csv(path)
        report.append({"file": name, "rows": len(rows), "fields": fields, "sensitive": False})
        payload = {
            "source": name,
            "importedAt": datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
            "rowCount": len(rows),
            "fields": fields,
            "rows": rows,
        }
        out = target / (path.stem.replace(" ", "-").lower() + ".json")
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Exportacion: " + folder.name)
    print("")
    print("  " + "fichero".ljust(30) + "filas".rjust(6) + "  campos")
    total = 0
    for item in report:
        if item["sensitive"]:
            print("  " + item["file"].ljust(30) + "     -" + "  sensible, no normalizado")
            continue
        total += item["rows"]
        print("  " + item["file"].ljust(30) + str(item["rows"]).rjust(6) + "  " + ", ".join(item["fields"])[:70])
    print("")
    print(str(total) + " filas normalizadas en " + str(target.relative_to(ROOT)))
    if not include_sensitive:
        skipped = [item["file"] for item in report if item["sensitive"]]
        if skipped:
            print("Omitidos por contener datos privados: " + ", ".join(skipped))
    return report


def main():
    parser = argparse.ArgumentParser(description="Inventario y normalizacion de una exportacion de datos de LinkedIn.")
    parser.add_argument("source", help="Carpeta de la exportacion, relativa a la raiz o absoluta.")
    parser.add_argument("--include-sensitive", action="store_true", help="Incluye mensajes, correos y telefonos.")
    args = parser.parse_args()
    cmd_inventory(Path(args.source), args.include_sensitive)


if __name__ == "__main__":
    main()
