import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API_HOST = "api.linkedin.com"
API_BASE = "https://" + API_HOST
LINKEDIN_VERSION = "202312"
ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "docs" / "privado" / "linkedin" / "api"
SNAPSHOT_DIR = OUT_DIR / "snapshot"
STATE_FILE = OUT_DIR / "state.json"
CHANGELOG_FILE = OUT_DIR / "changelog.jsonl"
ALLOWED_RESOURCES = {"memberAuthorizations", "memberSnapshotData", "memberChangeLogs"}
MAX_PAGES = 200
CHANGELOG_COUNT = 10

CORE_DOMAINS = [
    "PROFILE",
    "POSITIONS",
    "EDUCATION",
    "SKILLS",
    "CERTIFICATIONS",
    "PROJECTS",
    "COURSES",
    "LANGUAGES",
    "HONORS",
    "PUBLICATIONS",
    "VOLUNTEERING_EXPERIENCES",
    "RECOMMENDATIONS",
    "ENDORSEMENTS",
    "CONNECTIONS",
    "INVITATIONS",
    "MEMBER_SHARE_INFO",
    "INSTANT_REPOSTS",
    "ALL_COMMENTS",
    "ALL_LIKES",
    "COMPANY_FOLLOWS",
    "MEMBER_FOLLOWING",
    "SAVED_JOBS",
    "JOB_APPLICATIONS",
    "JOB_SEEKER_PREFERENCES",
    "EVENTS",
    "GROUPS",
    "ARTICLES",
    "RICH_MEDIA",
]

PRIVATE_DOMAINS = ["INBOX", "SEARCHES", "PREMIUM_NOTES", "AD_TARGETING", "EMAIL_ADDRESSES", "PHONE_NUMBERS"]

sys.stdout.reconfigure(encoding="utf-8")


def fail(message, code=1):
    print("ERROR: " + message)
    raise SystemExit(code)


class NoData(Exception):
    pass


def read_dotenv():
    path = ROOT / ".env"
    values = {}
    if not path.exists():
        return values
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def get_token():
    token = os.environ.get("LINKEDIN_DMA_TOKEN", "").strip()
    if token:
        return token
    token = read_dotenv().get("LINKEDIN_DMA_TOKEN", "").strip()
    if token:
        return token
    fail("falta LINKEDIN_DMA_TOKEN en el entorno o en .env")


def build_url(resource, params):
    query = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return API_BASE + "/rest/" + resource + "?" + query


def request_json(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != API_HOST:
        fail("host no permitido: " + parsed.netloc)
    resource = parsed.path.strip("/").split("/")[-1]
    if resource not in ALLOWED_RESOURCES:
        fail("recurso no permitido: " + resource)
    request = urllib.request.Request(url, method="GET")
    request.add_header("Authorization", "Bearer " + get_token())
    request.add_header("Linkedin-Version", LINKEDIN_VERSION)
    request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        if error.code == 404 and "No data found" in body:
            raise NoData(body[:200])
        hint = {
            401: "token caducado, revocado o mal copiado",
            403: "consentimiento no concedido o scope ausente",
            426: "version de API no admitida",
            429: "limite de peticiones alcanzado",
        }.get(error.code, "revisa la respuesta")
        fail("HTTP " + str(error.code) + " (" + hint + "): " + body[:400])
    except urllib.error.URLError as error:
        fail("sin conexion con la API: " + str(error.reason))
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        fail("respuesta no es JSON: " + body[:200])


def next_link(payload):
    for link in payload.get("paging", {}).get("links", []) or []:
        if link.get("rel") == "next" and link.get("href"):
            href = link["href"]
            if href.startswith("/"):
                return API_BASE + href
            return href
    return None


def cmd_check():
    payload = request_json(build_url("memberAuthorizations", {"q": "memberAndApplication"}))
    elements = payload.get("elements", [])
    if not elements:
        print("Sin autorizacion registrada para esta aplicacion y este token.")
        return
    for element in elements:
        key = element.get("memberComplianceAuthorizationKey", {})
        regulated = element.get("regulatedAt")
        when = datetime.fromtimestamp(regulated / 1000, tz=timezone.utc).isoformat() if regulated else "desconocido"
        print("Miembro:      " + str(key.get("member")))
        print("Aplicacion:   " + str(key.get("developerApplication")))
        print("Scopes:       " + ", ".join(element.get("memberComplianceScopes", [])))
        print("Desde:        " + when)
    print("Consentimiento activo.")


def cmd_domains(show_private):
    print("Dominios de perfil y actividad:")
    for domain in CORE_DOMAINS:
        print("  " + domain)
    if show_private:
        print("Dominios con datos sensibles, solo por peticion explicita:")
        for domain in PRIVATE_DOMAINS:
            print("  " + domain)


def fetch_domain(domain):
    elements = []
    url = build_url("memberSnapshotData", {"q": "criteria", "domain": domain})
    pages = 0
    try:
        while url and pages < MAX_PAGES:
            payload = request_json(url)
            pages += 1
            batch = payload.get("elements", []) or []
            if not batch:
                break
            elements.extend(batch)
            url = next_link(payload)
    except NoData:
        return [], pages, "pendiente"
    return elements, pages, "ok"


def dedupe(rows):
    seen = set()
    unique = []
    for row in rows:
        key = json.dumps(row, sort_keys=True, ensure_ascii=False, default=str)
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique


def cmd_snapshot(domains):
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    fetched_at = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
    summary = []
    for domain in domains:
        print("Descargando " + domain + " ...", flush=True)
        elements, pages, status = fetch_domain(domain)
        raw_rows = []
        for element in elements:
            data = element.get("snapshotData")
            if isinstance(data, list):
                raw_rows.extend(data)
            elif data is not None:
                raw_rows.append(data)
        rows = dedupe(raw_rows)
        record = {
            "domain": domain,
            "status": status,
            "fetchedAt": fetched_at,
            "pages": pages,
            "elementCount": len(elements),
            "rawRowCount": len(raw_rows),
            "rowCount": len(rows),
            "rows": rows,
        }
        target = SNAPSHOT_DIR / (domain + ".json")
        target.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        summary.append((domain, len(rows), status, len(raw_rows) - len(rows)))
        if status == "pendiente":
            print("  sin datos todavia: LinkedIn aun no ha procesado este dominio")
        else:
            note = ""
            if len(raw_rows) != len(rows):
                note = " (" + str(len(raw_rows) - len(rows)) + " duplicados de paginacion descartados)"
            print("  " + str(len(rows)) + " filas en " + str(pages) + " pagina(s) -> " + target.name + note)
    print("")
    print("Resumen:")
    for domain, count, status, discarded in summary:
        label = "pendiente" if status == "pendiente" else str(count) + " filas"
        print("  " + domain.ljust(24) + label)


def read_state():
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def write_state(state):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def cmd_changelog():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    state = read_state()
    start = state.get("changelogStartTime") or 0
    collected = []
    while True:
        params = {"q": "memberAndApplication", "count": CHANGELOG_COUNT}
        if start:
            params["startTime"] = start
        payload = request_json(build_url("memberChangeLogs", params))
        batch = payload.get("elements", []) or []
        if not batch:
            break
        collected.extend(batch)
        processed = [item.get("processedAt") for item in batch if item.get("processedAt")]
        if not processed:
            break
        new_start = max(processed)
        if new_start == start:
            break
        start = new_start
        if len(batch) < CHANGELOG_COUNT:
            break
    if not collected:
        print("Sin eventos nuevos.")
        return
    with CHANGELOG_FILE.open("a", encoding="utf-8") as handle:
        for item in collected:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    state["changelogStartTime"] = start
    state["changelogUpdatedAt"] = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
    write_state(state)
    print(str(len(collected)) + " eventos anadidos a " + CHANGELOG_FILE.name)
    for item in collected:
        print("  " + str(item.get("resourceName")).ljust(20) + str(item.get("method")).ljust(16) + str(item.get("capturedAt")))


def cmd_describe():
    if not SNAPSHOT_DIR.exists():
        print("Todavia no hay snapshots descargados.")
        return
    for path in sorted(SNAPSHOT_DIR.glob("*.json")):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(path.name + ": ilegible")
            continue
        rows = record.get("rows", [])
        print(record.get("domain", path.stem) + ": " + str(len(rows)) + " filas")
        if rows and isinstance(rows[0], dict):
            print("  campos: " + ", ".join(list(rows[0].keys())[:12]))
    if CHANGELOG_FILE.exists():
        lines = CHANGELOG_FILE.read_text(encoding="utf-8").count("\n")
        print("changelog: " + str(lines) + " eventos")


def main():
    parser = argparse.ArgumentParser(description="Cliente de solo lectura para la API de portabilidad de LinkedIn.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check", help="Comprueba el consentimiento y el token.")
    domains_parser = sub.add_parser("domains", help="Lista los dominios disponibles.")
    domains_parser.add_argument("--private", action="store_true", help="Incluye los dominios sensibles.")
    snapshot_parser = sub.add_parser("snapshot", help="Descarga dominios del snapshot.")
    snapshot_parser.add_argument("domains", nargs="*", help="Dominios concretos.")
    snapshot_parser.add_argument("--core", action="store_true", help="Descarga el conjunto de perfil y actividad.")
    sub.add_parser("changelog", help="Descarga los eventos de los ultimos 28 dias.")
    sub.add_parser("describe", help="Resume lo descargado sin salir a la red.")

    args = parser.parse_args()

    if args.command == "check":
        cmd_check()
    elif args.command == "domains":
        cmd_domains(args.private)
    elif args.command == "snapshot":
        selected = [domain.upper() for domain in args.domains]
        if args.core:
            selected = CORE_DOMAINS
        if not selected:
            fail("indica al menos un dominio o usa --core")
        unknown = [domain for domain in selected if domain not in CORE_DOMAINS and domain not in PRIVATE_DOMAINS]
        if unknown:
            fail("dominio no reconocido: " + ", ".join(unknown))
        cmd_snapshot(selected)
    elif args.command == "changelog":
        cmd_changelog()
    elif args.command == "describe":
        cmd_describe()


if __name__ == "__main__":
    main()
