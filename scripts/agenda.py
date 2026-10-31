import argparse
import json
import re
import sqlite3
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENDA_DIR = ROOT / "docs" / "privado" / "agenda"
DB_PATH = AGENDA_DIR / "agenda.db"
SEED_PATH = AGENDA_DIR / "seed.json"
HOY_PATH = AGENDA_DIR / "hoy.md"
SEMANA_PATH = AGENDA_DIR / "semana.md"
ICS_PATH = AGENDA_DIR / "agenda.ics"
GOOGLE_CONFIG_PATH = AGENDA_DIR / "google.json"
GOOGLE_CREDENTIALS_DIR = Path.home() / ".google_workspace_mcp" / "credentials"
GOOGLE_TASKS_API = "https://tasks.googleapis.com/tasks/v1"
GOOGLE_LIST_TITLE = "Employment Workshop"
ESTADO_PATH = ROOT / "docs" / "memoria" / "estado-actual.md"
CANDIDATURAS_DB = ROOT / "docs" / "candidaturas" / "candidaturas.db"

AREAS = {
    "curso": "Curso",
    "busqueda": "Búsqueda",
    "linkedin": "LinkedIn",
    "networking": "Networking",
    "ingles": "Inglés",
    "portfolio": "Portfolio",
    "entrevista": "Entrevista",
    "admin": "Admin",
}

WEEKDAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
SHORT_WEEKDAYS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
MONTHS = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]
SHORT_MONTHS = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
BYDAY = {"1": "MO", "2": "TU", "3": "WE", "4": "TH", "5": "FR", "6": "SA", "7": "SU"}

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  area TEXT NOT NULL,
  due_date TEXT,
  due_time TEXT,
  duration_min INTEGER DEFAULT 30,
  priority INTEGER DEFAULT 2,
  status TEXT DEFAULT 'pending',
  source TEXT,
  ref TEXT UNIQUE,
  notes TEXT,
  created_at TEXT,
  done_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_tasks_due ON tasks(due_date, status);

CREATE TABLE IF NOT EXISTS recurrences (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  area TEXT NOT NULL,
  days_of_week TEXT NOT NULL,
  start_time TEXT,
  duration_min INTEGER DEFAULT 30,
  start_date TEXT NOT NULL,
  end_date TEXT NOT NULL,
  active INTEGER DEFAULT 1,
  ref TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS recurrence_done (
  recurrence_id INTEGER NOT NULL,
  on_date TEXT NOT NULL,
  done_at TEXT,
  PRIMARY KEY (recurrence_id, on_date)
);
"""


def force_utf8():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:
            pass


def connect():
    AGENDA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_schema(conn):
    conn.executescript(SCHEMA)
    conn.commit()


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def parse_day(value):
    if not value:
        return date.today()
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise SystemExit(f"Fecha no válida: {value}. Usa el formato YYYY-MM-DD.")


def format_day(day):
    return f"{WEEKDAYS[day.weekday()]} {day.day} de {MONTHS[day.month - 1]} de {day.year}"


def capitalize_first(text):
    return text[0].upper() + text[1:] if text else text


def format_short(day):
    return f"{SHORT_WEEKDAYS[day.weekday()]} {day.day:02d} {SHORT_MONTHS[day.month - 1]}"


def seed(conn):
    if not SEED_PATH.exists():
        return 0
    data = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    created = now_iso()
    inserted = 0
    for item in data.get("tasks", []):
        cur = conn.execute(
            """
            INSERT OR IGNORE INTO tasks
              (title, area, due_date, due_time, duration_min, priority, source, ref, notes, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item["title"],
                item["area"],
                item.get("due_date"),
                item.get("due_time"),
                item.get("duration_min", 30),
                item.get("priority", 2),
                item.get("source", "seed"),
                item.get("ref"),
                item.get("notes"),
                created,
            ),
        )
        inserted += cur.rowcount
    for item in data.get("recurrences", []):
        cur = conn.execute(
            """
            INSERT OR IGNORE INTO recurrences
              (title, area, days_of_week, start_time, duration_min, start_date, end_date, active, ref)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1, ?)
            """,
            (
                item["title"],
                item["area"],
                item["days_of_week"],
                item.get("start_time"),
                item.get("duration_min", 30),
                item["start_date"],
                item["end_date"],
                item.get("ref"),
            ),
        )
        inserted += cur.rowcount
    conn.commit()
    return inserted


def sync_candidaturas(conn):
    if not CANDIDATURAS_DB.exists():
        return 0
    uri = f"file:{CANDIDATURAS_DB.as_posix()}?mode=ro"
    source = sqlite3.connect(uri, uri=True)
    source.row_factory = sqlite3.Row
    rows = source.execute(
        "SELECT id, fecha, empresa, rol, estado, contacto, proximo_paso FROM candidaturas"
    ).fetchall()
    source.close()
    updated = 0
    for row in rows:
        match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", row["proximo_paso"] or "")
        if not match:
            continue
        notes = f"{row['rol']} · {row['estado']} el {row['fecha']}"
        if row["contacto"]:
            notes += f" · {row['contacto']}"
        cur = conn.execute(
            """
            INSERT INTO tasks
              (title, area, due_date, duration_min, priority, source, ref, notes, created_at)
            VALUES (?, 'busqueda', ?, 15, 1, 'candidaturas', ?, ?, ?)
            ON CONFLICT(ref) DO UPDATE SET
              due_date = excluded.due_date,
              notes = excluded.notes
            WHERE tasks.status = 'pending'
              AND (tasks.due_date != excluded.due_date OR tasks.notes != excluded.notes)
            """,
            (
                f"Seguimiento de {row['empresa']}",
                match.group(1),
                f"cand-{row['id']}-seguimiento",
                notes,
                now_iso(),
            ),
        )
        updated += cur.rowcount
    conn.commit()
    return updated


def tasks_for(conn, day, status="pending"):
    return conn.execute(
        "SELECT * FROM tasks WHERE status = ? AND due_date = ? ORDER BY due_time IS NULL DESC, due_time, priority",
        (status, day.isoformat()),
    ).fetchall()


def overdue_tasks(conn, day):
    return conn.execute(
        """
        SELECT * FROM tasks
        WHERE status = 'pending' AND due_date IS NOT NULL AND due_date < ?
        ORDER BY due_date, priority
        """,
        (day.isoformat(),),
    ).fetchall()


def backlog_tasks(conn, limit=6):
    return conn.execute(
        """
        SELECT * FROM tasks
        WHERE status = 'pending' AND due_date IS NULL
        ORDER BY priority, id
        LIMIT ?
        """,
        (limit,),
    ).fetchall()


def recurrences_for(conn, day):
    rows = conn.execute(
        """
        SELECT * FROM recurrences
        WHERE active = 1 AND start_date <= ? AND end_date >= ?
        ORDER BY start_time
        """,
        (day.isoformat(), day.isoformat()),
    ).fetchall()
    weekday = str(day.isoweekday())
    result = []
    for row in rows:
        if weekday not in [part.strip() for part in row["days_of_week"].split(",")]:
            continue
        done = conn.execute(
            "SELECT 1 FROM recurrence_done WHERE recurrence_id = ? AND on_date = ?",
            (row["id"], day.isoformat()),
        ).fetchone()
        result.append({"row": row, "done": done is not None})
    return result


def next_tasks(conn, after, limit=3):
    return conn.execute(
        """
        SELECT * FROM tasks
        WHERE status = 'pending' AND due_date > ?
        ORDER BY due_date, priority, due_time
        LIMIT ?
        """,
        (after.isoformat(), limit),
    ).fetchall()


def area_label(value):
    return AREAS.get(value, value)


def task_line(task):
    time = task["due_time"] or "todo el día"
    duration = f" ({task['duration_min']} min)" if task["duration_min"] else ""
    line = f"  [ ] {task['id']:>3}  {time:<10}  {area_label(task['area']):<10}  {task['title']}{duration}"
    if task["notes"]:
        line += f"\n           {task['notes']}"
    return line


def recurrence_line(item):
    row = item["row"]
    mark = "x" if item["done"] else " "
    duration = f" ({row['duration_min']} min)" if row["duration_min"] else ""
    return f"  [{mark}] r{row['id']:<2}  {row['start_time'] or 'todo el día':<10}  {area_label(row['area']):<10}  {row['title']}{duration}"


def day_entries(conn, day):
    tasks = tasks_for(conn, day)
    recs = recurrences_for(conn, day)
    entries = []
    for item in recs:
        entries.append((item["row"]["start_time"] or "00:00", recurrence_line(item)))
    for task in tasks:
        entries.append((task["due_time"] or "00:00", task_line(task)))
    entries.sort(key=lambda pair: pair[0])
    return entries


def render_hoy(conn, day, write_file=True):
    entries = day_entries(conn, day)
    overdue = overdue_tasks(conn, day)
    backlog = backlog_tasks(conn)
    lines = [capitalize_first(format_day(day)), ""]
    total = 0
    for item in recurrences_for(conn, day):
        total += item["row"]["duration_min"] or 0
    for task in tasks_for(conn, day):
        total += task["duration_min"] or 0
    if entries:
        lines.extend(line for _, line in entries)
        if total:
            if total < 60:
                carga = f"{total} min"
            else:
                carga = f"{total // 60} h {total % 60:02d} min"
            lines.append("")
            lines.append(f"  Carga del día: {carga}.")
    else:
        lines.append("  Sin tareas programadas. Revisa el backlog o añade una con `agenda.py add`.")
    if overdue:
        lines.append("")
        lines.append("ATRASADAS")
        for task in overdue:
            due = date.fromisoformat(task["due_date"])
            line = task_line(task).replace("todo el día", format_short(due))
            lines.append(line)
    if backlog:
        lines.append("")
        lines.append("SIN FECHA (backlog)")
        for task in backlog:
            lines.append(f"  [ ] {task['id']:>3}  {area_label(task['area']):<10}  {task['title']}")
    lines.append("")
    lines.append("Día mínimo si no hay 4 h: 1 h de curso, 30 min de búsqueda y 10 min de inglés.")
    text = "\n".join(lines)
    if write_file:
        HOY_PATH.write_text(
            f"# Hoy: {capitalize_first(format_day(day))}\n\nVista generada por `scripts/agenda.py`. Marca con `/hecho <id>`; no edites este fichero.\n\n```text\n{text}\n```\n",
            encoding="utf-8",
        )
    return text


def render_semana(conn, start):
    lines = [f"Semana del {format_day(start)} al {format_day(start + timedelta(days=6))}", ""]
    for offset in range(7):
        day = start + timedelta(days=offset)
        entries = day_entries(conn, day)
        total = 0
        for item in recurrences_for(conn, day):
            total += item["row"]["duration_min"] or 0
        for task in tasks_for(conn, day):
            total += task["duration_min"] or 0
        if total == 0:
            hours = "sin carga"
        elif total < 60:
            hours = f"{total} min"
        else:
            hours = f"{total // 60} h {total % 60:02d} min"
        label = "bloque" if len(entries) == 1 else "bloques"
        lines.append(f"{format_short(day)}  ·  {len(entries)} {label}  ·  {hours}")
        if entries:
            for _, line in entries:
                lines.append(line.replace("  [ ] ", "    "))
        else:
            lines.append("    Sin tareas programadas.")
        lines.append("")
    text = "\n".join(lines).rstrip() + "\n"
    SEMANA_PATH.write_text(
        f"# Semana\n\nVista generada por `scripts/agenda.py`. Marca con `/hecho <id>`.\n\n```text\n{text}```\n",
        encoding="utf-8",
    )
    return text


def mark_task_done(conn, task_id, status="done"):
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if not task:
        raise SystemExit(f"No existe la tarea {task_id}.")
    if task["status"] != "pending":
        print(f"La tarea {task_id} ya estaba en estado {task['status']}.")
        return
    conn.execute(
        "UPDATE tasks SET status = ?, done_at = ? WHERE id = ?",
        (status, now_iso(), task_id),
    )
    conn.commit()
    print(f"{'Hecho' if status == 'done' else 'Omitido'}: [{task_id}] {task['title']}")


def mark_recurrence_done(conn, rec_id, day):
    row = conn.execute("SELECT * FROM recurrences WHERE id = ?", (rec_id,)).fetchone()
    if not row:
        raise SystemExit(f"No existe la recurrencia r{rec_id}.")
    conn.execute(
        "INSERT OR REPLACE INTO recurrence_done (recurrence_id, on_date, done_at) VALUES (?, ?, ?)",
        (rec_id, day.isoformat(), now_iso()),
    )
    conn.commit()
    print(f"Hecho: r{rec_id} {row['title']} ({day.isoformat()})")


def add_task(conn, args):
    if args.area not in AREAS:
        raise SystemExit(f"Área no válida: {args.area}. Usa una de: {', '.join(AREAS)}.")
    due_date = args.date or None
    due_time = args.time or None
    if due_date:
        try:
            date.fromisoformat(due_date)
        except ValueError:
            raise SystemExit(f"Fecha no válida: {due_date}. Usa el formato YYYY-MM-DD.")
    if due_time:
        try:
            datetime.strptime(due_time, "%H:%M")
        except ValueError:
            raise SystemExit(f"Hora no válida: {due_time}. Usa el formato HH:MM.")
    cur = conn.execute(
        """
        INSERT INTO tasks
          (title, area, due_date, due_time, duration_min, priority, source, notes, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'manual', ?, ?)
        """,
        (
            args.title,
            args.area,
            due_date,
            due_time,
            args.duration,
            args.priority,
            args.notes,
            now_iso(),
        ),
    )
    conn.commit()
    print(f"Añadida: [{cur.lastrowid}] {args.title}")


def ics_escape(text):
    value = text or ""
    value = value.replace("\\", "\\\\")
    value = value.replace(";", "\\;")
    value = value.replace(",", "\\,")
    value = value.replace("\n", "\\n")
    return value


def fold_line(line):
    encoded = line.encode("utf-8")
    if len(encoded) <= 75:
        return line
    parts = []
    current = ""
    for char in line:
        if len((current + char).encode("utf-8")) > 75:
            parts.append(current)
            current = " " + char
        else:
            current += char
    parts.append(current)
    return "\r\n".join(parts)


def ics_event(uid, summary, description, start_day, start_time=None, duration_min=30, rrule=None, alarm=True):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{stamp}",
    ]
    if start_time:
        begin = datetime.combine(start_day, datetime.strptime(start_time, "%H:%M").time())
        end = begin + timedelta(minutes=duration_min or 30)
        lines.append(f"DTSTART:{begin.strftime('%Y%m%dT%H%M%S')}")
        lines.append(f"DTEND:{end.strftime('%Y%m%dT%H%M%S')}")
    else:
        lines.append(f"DTSTART;VALUE=DATE:{start_day.strftime('%Y%m%d')}")
        lines.append(f"DTEND;VALUE=DATE:{(start_day + timedelta(days=1)).strftime('%Y%m%d')}")
    if rrule:
        lines.append(f"RRULE:{rrule}")
    lines.append(f"SUMMARY:{ics_escape(summary)}")
    if description:
        lines.append(f"DESCRIPTION:{ics_escape(description)}")
    lines.append("STATUS:CONFIRMED")
    lines.append("TRANSP:OPAQUE")
    if start_time and alarm:
        lines.append("BEGIN:VALARM")
        lines.append("TRIGGER:-PT15M")
        lines.append("ACTION:DISPLAY")
        lines.append(f"DESCRIPTION:{ics_escape(summary)}")
        lines.append("END:VALARM")
    lines.append("END:VEVENT")
    return lines


def build_ics(conn, start, end):
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//ai-job-search-copilot//Agenda//ES",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Agenda Employment Workshop 2026",
        "X-WR-TIMEZONE:Europe/Madrid",
    ]
    events = 0
    tasks = conn.execute(
        """
        SELECT * FROM tasks
        WHERE status = 'pending' AND due_date BETWEEN ? AND ?
        ORDER BY due_date, due_time
        """,
        (start.isoformat(), end.isoformat()),
    ).fetchall()
    for task in tasks:
        day = date.fromisoformat(task["due_date"])
        description = task["notes"] or ""
        if task["ref"]:
            description = f"{description}\nRef: {task['ref']}".strip()
        lines.extend(
            ics_event(
                f"agenda-task-{task['id']}@ai-job-search-copilot",
                f"{area_label(task['area'])} · {task['title']}",
                description,
                day,
                task["due_time"],
                task["duration_min"],
            )
        )
        events += 1
    recurrences = conn.execute(
        """
        SELECT * FROM recurrences
        WHERE active = 1 AND end_date >= ? AND start_date <= ?
        ORDER BY start_time
        """,
        (start.isoformat(), end.isoformat()),
    ).fetchall()
    for row in recurrences:
        first = max(date.fromisoformat(row["start_date"]), start)
        days = [part.strip() for part in row["days_of_week"].split(",")]
        while first <= end and str(first.isoweekday()) not in days:
            first += timedelta(days=1)
        if first > end or not row["start_time"]:
            continue
        byday = ",".join(BYDAY[part] for part in days if part in BYDAY)
        rrule = f"FREQ=WEEKLY;BYDAY={byday};UNTIL={row['end_date'].replace('-', '')}T235959"
        lines.extend(
            ics_event(
                f"agenda-rec-{row['id']}@ai-job-search-copilot",
                f"{area_label(row['area'])} · {row['title']}",
                f"Bloque recurrente de {row['duration_min']} min.",
                first,
                row["start_time"],
                row["duration_min"],
                rrule,
                alarm=False,
            )
        )
        events += 1
    lines.append("END:VCALENDAR")
    content = "\r\n".join(fold_line(line) for line in lines) + "\r\n"
    ICS_PATH.write_text(content, encoding="utf-8", newline="")
    return events


def update_memoria(conn, day):
    if not ESTADO_PATH.exists():
        print("No existe docs/memoria/estado-actual.md; no se actualiza el bloque.")
        return
    titles = []
    for item in recurrences_for(conn, day):
        titles.append((item["row"]["start_time"] or "00:00", item["row"]["title"]))
    for task in tasks_for(conn, day):
        titles.append((task["due_time"] or "00:00", task["title"]))
    titles.sort(key=lambda pair: pair[0])
    titles = [title for _, title in titles[:3]]
    tomorrow = day + timedelta(days=1)
    tomorrow_tasks = tasks_for(conn, tomorrow)
    if tomorrow_tasks:
        tomorrow_title = tomorrow_tasks[0]["title"]
    else:
        tomorrow_recs = recurrences_for(conn, tomorrow)
        if tomorrow_recs:
            label = "bloque" if len(tomorrow_recs) == 1 else "bloques"
            tomorrow_title = f"{len(tomorrow_recs)} {label} de rutina"
        else:
            tomorrow_title = "sin tareas programadas"
    next_task = conn.execute(
        """
        SELECT * FROM tasks
        WHERE status = 'pending' AND due_date > ?
        ORDER BY due_date, priority, due_time
        LIMIT 1
        """,
        (tomorrow.isoformat(),),
    ).fetchone()
    block_lines = [
        "<!-- agenda:inicio -->",
        f"_Agenda generada por `scripts/agenda.py` el {day.isoformat()}._",
        "",
        f"- **Hoy:** {'; '.join(titles) if titles else 'sin tareas programadas'}.",
        f"- **Mañana:** {tomorrow_title}.",
    ]
    if next_task:
        block_lines.append(
            f"- **Siguiente hito:** {next_task['due_date']} · {next_task['title']}."
        )
    block_lines.append("<!-- agenda:fin -->")
    block = "\n".join(block_lines)
    raw = ESTADO_PATH.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8")
    if "<!-- agenda:inicio -->" in text and "<!-- agenda:fin -->" in text:
        text = re.sub(
            r"<!-- agenda:inicio -->.*?<!-- agenda:fin -->",
            block.replace("\n", newline),
            text,
            flags=re.S,
        )
    else:
        first_break = text.find(newline)
        insert_at = first_break + len(newline) if first_break != -1 else len(text)
        block_text = newline + block.replace("\n", newline) + newline
        text = text[:insert_at] + block_text + text[insert_at:]
    ESTADO_PATH.write_bytes(text.encode("utf-8"))
    print(f"Bloque de agenda actualizado en {ESTADO_PATH.relative_to(ROOT)}.")


def command_init(args):
    conn = connect()
    init_schema(conn)
    seeded = seed(conn)
    synced = sync_candidaturas(conn)
    total = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    recs = conn.execute("SELECT COUNT(*) FROM recurrences").fetchone()[0]
    conn.close()
    print(f"Base creada en {DB_PATH.relative_to(ROOT)}.")
    print(f"Tareas: {total}. Recurrencias: {recs}. Registros nuevos: {seeded}. Seguimientos: {synced}.")


def command_seed(args):
    conn = connect()
    init_schema(conn)
    seeded = seed(conn)
    conn.close()
    print(f"Carga inicial aplicada: {seeded} registros nuevos.")


def command_sync(args):
    conn = connect()
    init_schema(conn)
    synced = sync_candidaturas(conn)
    conn.close()
    print(f"Seguimientos sincronizados: {synced}.")


def command_hoy(args):
    day = parse_day(args.date)
    conn = connect()
    text = render_hoy(conn, day)
    if args.memoria:
        update_memoria(conn, day)
    conn.close()
    print(text)


def command_semana(args):
    day = parse_day(args.date)
    conn = connect()
    text = render_semana(conn, day)
    conn.close()
    print(text)


def command_done(args):
    day = parse_day(args.date)
    conn = connect()
    value = str(args.id).strip().lower()
    try:
        if value.startswith("r"):
            mark_recurrence_done(conn, int(value[1:]), day)
        else:
            mark_task_done(conn, int(value))
    except ValueError:
        conn.close()
        raise SystemExit(f"Id no válido: {args.id}. Usa un número o rN.")
    conn.close()


def command_skip(args):
    conn = connect()
    mark_task_done(conn, int(args.id), status="skipped")
    conn.close()


def command_add(args):
    conn = connect()
    add_task(conn, args)
    conn.close()


def command_set(args):
    conn = connect()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (args.id,)).fetchone()
    if not task:
        conn.close()
        raise SystemExit(f"No existe la tarea {args.id}.")
    updates = []
    values = []
    for field, value in (
        ("title", args.title),
        ("due_date", args.date),
        ("due_time", args.time),
        ("notes", args.notes),
    ):
        if value is not None:
            if field in ("due_date", "due_time") and value == "":
                value = None
            if field == "due_date" and value:
                try:
                    date.fromisoformat(value)
                except ValueError:
                    conn.close()
                    raise SystemExit(f"Fecha no válida: {value}. Usa el formato YYYY-MM-DD.")
            if field == "due_time" and value:
                try:
                    datetime.strptime(value, "%H:%M")
                except ValueError:
                    conn.close()
                    raise SystemExit(f"Hora no válida: {value}. Usa el formato HH:MM.")
            updates.append(f"{field} = ?")
            values.append(value)
    if not updates:
        conn.close()
        raise SystemExit("No hay cambios que aplicar.")
    values.append(args.id)
    conn.execute(f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?", values)
    conn.commit()
    conn.close()
    print(f"Actualizada: [{args.id}] {args.title or task['title']}")


def command_ics(args):
    start = parse_day(args.from_date)
    end = parse_day(args.to_date)
    if start > end:
        raise SystemExit("La fecha inicial no puede ser posterior a la final.")
    conn = connect()
    events = build_ics(conn, start, end)
    conn.close()
    print(f"Calendario generado: {ICS_PATH.relative_to(ROOT)} ({events} eventos).")
    print(f"Rango: {start.isoformat()} a {end.isoformat()}.")


def command_memoria(args):
    day = parse_day(args.date)
    conn = connect()
    update_memoria(conn, day)
    conn.close()


def ensure_google_column(conn):
    columns = [row[1] for row in conn.execute("PRAGMA table_info(tasks)")]
    if "google_id" in columns:
        return False
    conn.execute("ALTER TABLE tasks ADD COLUMN google_id TEXT")
    conn.commit()
    return True


def google_load_config():
    if not GOOGLE_CONFIG_PATH.exists():
        return {}
    return json.loads(GOOGLE_CONFIG_PATH.read_text(encoding="utf-8"))


def google_save_config(config):
    GOOGLE_CONFIG_PATH.write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def google_resolve_email(config, override):
    if override:
        return override
    if config.get("email"):
        return config["email"]
    files = [path for path in sorted(GOOGLE_CREDENTIALS_DIR.glob("*.json"))]
    files = [path for path in files if path.name != "oauth_states.json"]
    if not files:
        raise SystemExit(
            "No hay cuentas autorizadas. Abre opencode y autoriza el MCP google-calendar."
        )
    if len(files) > 1:
        raise SystemExit(
            "Hay varias cuentas autorizadas. Elige una con --email: "
            + ", ".join(path.stem for path in files)
        )
    return files[0].stem


def google_access_token(email):
    path = GOOGLE_CREDENTIALS_DIR / f"{email}.json"
    if not path.exists():
        raise SystemExit(f"No existe credencial autorizada para {email}.")
    data = json.loads(path.read_text(encoding="utf-8"))
    payload = urllib.parse.urlencode(
        {
            "client_id": data["client_id"],
            "client_secret": data["client_secret"],
            "refresh_token": data["refresh_token"],
            "grant_type": "refresh_token",
        }
    ).encode()
    request = urllib.request.Request(
        data.get("token_uri") or "https://oauth2.googleapis.com/token",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            token = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")[:300]
        raise SystemExit(
            "Google rechazó el token. Si la autorización tiene más de siete días, "
            "vuelve a lanzarla desde opencode.\n" + detail
        )
    return token["access_token"]


def google_request(token, method, path, body=None):
    headers = {"Authorization": "Bearer " + token}
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(
        GOOGLE_TASKS_API + path, data=data, headers=headers, method=method
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")[:400]
        raise SystemExit(f"Google devolvió {error.code} en {method} {path}.\n{detail}")
    return json.loads(raw) if raw else {}


def google_find_list(token, title):
    data = google_request(token, "GET", "/users/@me/lists?maxResults=100")
    for item in data.get("items", []):
        if item.get("title") == title:
            return item["id"]
    created = google_request(token, "POST", "/users/@me/lists", {"title": title})
    return created["id"]


def google_fetch_tasks(token, list_id):
    found = {}
    page = None
    while True:
        path = f"/lists/{list_id}/tasks?maxResults=100&showCompleted=true&showHidden=true"
        if page:
            path += "&pageToken=" + urllib.parse.quote(page)
        data = google_request(token, "GET", path)
        for item in data.get("items", []):
            found[item["id"]] = item
        page = data.get("nextPageToken")
        if not page:
            break
    return found


def google_payload(task):
    return {
        "title": task["title"],
        "notes": task["notes"] or "",
        "due": f"{task['due_date']}T00:00:00.000Z" if task["due_date"] else None,
    }


def google_sync(conn, token, list_id, dry_run=False):
    remote = google_fetch_tasks(token, list_id)
    rows = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    claimed = {row["google_id"] for row in rows if row["google_id"]}
    orphans = {}
    for google_id, item in remote.items():
        if google_id in claimed:
            continue
        orphans.setdefault(item.get("title"), []).append(google_id)

    created = adopted = updated = completed = 0
    for task in rows:
        google_id = task["google_id"]
        payload = google_payload(task)

        if not google_id and task["status"] == "pending":
            candidates = orphans.get(payload["title"])
            if candidates:
                google_id = candidates.pop(0)
                if not dry_run:
                    conn.execute(
                        "UPDATE tasks SET google_id = ? WHERE id = ?", (google_id, task["id"])
                    )
                adopted += 1

        if task["status"] == "pending":
            if google_id and google_id in remote:
                current = remote[google_id]
                differs = (
                    current.get("title") != payload["title"]
                    or (current.get("notes") or "") != payload["notes"]
                    or (current.get("due") or "") != (payload["due"] or "")
                )
                if differs or current.get("status") == "completed":
                    if not dry_run:
                        body = dict(payload)
                        if current.get("status") == "completed":
                            body["status"] = "needsAction"
                        google_request(token, "PATCH", f"/lists/{list_id}/tasks/{google_id}", body)
                    updated += 1
            else:
                if not dry_run:
                    fresh = {key: value for key, value in payload.items() if value is not None}
                    new = google_request(token, "POST", f"/lists/{list_id}/tasks", fresh)
                    conn.execute(
                        "UPDATE tasks SET google_id = ? WHERE id = ?", (new["id"], task["id"])
                    )
                created += 1
        elif google_id and google_id in remote and remote[google_id].get("status") != "completed":
            if not dry_run:
                google_request(
                    token, "PATCH", f"/lists/{list_id}/tasks/{google_id}", {"status": "completed"}
                )
            completed += 1

    if not dry_run:
        conn.commit()
    return created, adopted, updated, completed


def command_google(args):
    config = google_load_config()
    email = google_resolve_email(config, args.email)
    list_title = args.list_title or config.get("list_title") or GOOGLE_LIST_TITLE
    conn = connect()
    if ensure_google_column(conn):
        print("Añadida la columna google_id a la tabla tasks.")
    token = google_access_token(email)
    list_id = config.get("list_id") if config.get("list_title") == list_title else None
    if not list_id:
        list_id = google_find_list(token, list_title)
        print(f"Lista lista: {list_title} ({list_id}).")
    if not args.dry_run:
        google_save_config({"email": email, "list_title": list_title, "list_id": list_id})
    created, adopted, updated, completed = google_sync(conn, token, list_id, args.dry_run)
    conn.close()
    prefix = "Simulación. " if args.dry_run else ""
    print(f"{prefix}Cuenta: {email}")
    print(f"{prefix}Lista: {list_title} ({list_id})")
    print(
        f"{prefix}Enlazadas: {adopted} · Creadas: {created} · "
        f"Actualizadas: {updated} · Completadas: {completed}."
    )


def build_parser():
    parser = argparse.ArgumentParser(description="Agenda diaria del Employment Workshop 2026.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Crea la base y aplica la carga inicial.")
    p_init.set_defaults(func=command_init)

    p_seed = sub.add_parser("seed", help="Reimporta seed.json sin duplicar.")
    p_seed.set_defaults(func=command_seed)

    p_sync = sub.add_parser("sync", help="Sincroniza los seguimientos de candidaturas.")
    p_sync.set_defaults(func=command_sync)

    p_hoy = sub.add_parser("hoy", help="Muestra las tareas del día.")
    p_hoy.add_argument("--date", help="Fecha ISO; por defecto hoy.")
    p_hoy.add_argument("--memoria", action="store_true", help="Actualiza el bloque de estado-actual.md.")
    p_hoy.set_defaults(func=command_hoy)

    p_semana = sub.add_parser("semana", help="Muestra la semana que contiene la fecha.")
    p_semana.add_argument("--date", help="Fecha ISO; por defecto hoy.")
    p_semana.set_defaults(func=command_semana)

    p_done = sub.add_parser("done", help="Marca una tarea o recurrencia como hecha.")
    p_done.add_argument("id", help="Id numérico o rN para una recurrencia.")
    p_done.add_argument("--date", help="Fecha ISO para la recurrencia; por defecto hoy.")
    p_done.set_defaults(func=command_done)

    p_skip = sub.add_parser("skip", help="Marca una tarea como omitida.")
    p_skip.add_argument("id", help="Id numérico.")
    p_skip.set_defaults(func=command_skip)

    p_add = sub.add_parser("add", help="Añade una tarea.")
    p_add.add_argument("title")
    p_add.add_argument("--date", help="Fecha ISO; sin fecha queda en backlog.")
    p_add.add_argument("--time", help="Hora HH:MM.")
    p_add.add_argument("--area", default="admin", choices=sorted(AREAS))
    p_add.add_argument("--duration", type=int, default=30, help="Duración en minutos.")
    p_add.add_argument("--priority", type=int, default=2, choices=[1, 2, 3])
    p_add.add_argument("--notes")
    p_add.set_defaults(func=command_add)

    p_set = sub.add_parser("set", help="Cambia fecha, hora, título o notas de una tarea.")
    p_set.add_argument("id", type=int)
    p_set.add_argument("--date")
    p_set.add_argument("--time")
    p_set.add_argument("--title")
    p_set.add_argument("--notes")
    p_set.set_defaults(func=command_set)

    p_ics = sub.add_parser("ics", help="Genera agenda.ics.")
    p_ics.add_argument("--from", dest="from_date", help="Fecha inicial ISO; por defecto hoy.")
    p_ics.add_argument("--to", dest="to_date", default="2026-12-31", help="Fecha final ISO.")
    p_ics.set_defaults(func=command_ics)

    p_memoria = sub.add_parser("memoria", help="Actualiza el bloque de agenda en estado-actual.md.")
    p_memoria.add_argument("--date", help="Fecha ISO; por defecto hoy.")
    p_memoria.set_defaults(func=command_memoria)

    p_google = sub.add_parser("google", help="Sincroniza las tareas con Google Tasks.")
    p_google.add_argument("--email", help="Cuenta autorizada; por defecto la de google.json.")
    p_google.add_argument("--list", dest="list_title", help="Nombre de la lista en Google Tasks.")
    p_google.add_argument("--dry-run", action="store_true", help="Muestra lo que haría sin escribir.")
    p_google.set_defaults(func=command_google)

    return parser


def main():
    force_utf8()
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
