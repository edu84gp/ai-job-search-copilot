# Agenda diaria

La agenda convierte el plan de estudios, el calendario de LinkedIn y los seguimientos de candidaturas en una lista que se abre cada día y se marca. La fuente de verdad es una base SQLite privada; los markdown siguen explicando el porqué.

## Dónde vive

| Ruta | Función | Git |
| --- | --- | --- |
| `docs/privado/agenda/agenda.db` | Tareas, recurrencias y hábitos hechos | Ignorada |
| `docs/privado/agenda/seed.json` | Carga inicial del plan | Ignorada |
| `docs/privado/agenda/hoy.md` | Vista del día | Ignorada |
| `docs/privado/agenda/semana.md` | Vista de los próximos siete días | Ignorada |
| `docs/privado/agenda/agenda.ics` | Calendario para importar | Ignorada |
| `scripts/agenda.py` | Script único, sin dependencias | Versionado |
| `.opencode/commands/hoy.md` | Comando `/hoy` | Versionado |
| `.opencode/commands/hecho.md` | Comando `/hecho` | Versionado |

`docs/privado/` está en `.gitignore`, así que ni la base ni las vistas salen del equipo. El script y los comandos no contienen datos personales.

## Abrir el día

Tres formas, todas sobre la misma base:

1. **En opencode:** `/hoy`. Ejecuta el script, muestra el día y actualiza el bloque de agenda de `docs/memoria/estado-actual.md`.
2. **En terminal:** `python scripts/agenda.py hoy`.
3. **En el editor:** abre `docs/privado/agenda/hoy.md`. Es una vista generada; no la edites.

La salida agrupa lo que tiene hora, lo atrasado y el backlog sin fecha:

```text
Viernes 30 de octubre de 2026

  [ ]   2  08:30       LinkedIn    Publicar Story #3 Mistake Confession (30 min)
  [ ] r1   09:00       Curso       Curso: Employment Workshop (150 min)
  [ ] r2   11:30       Búsqueda    Búsqueda, portfolio y GitHub (40 min)
  [ ] r3   12:10       LinkedIn    20 min de comentarios en LinkedIn (20 min)
  [ ] r4   12:30       Inglés      Rutina de inglés (30 min)

  Carga del día: 6 h 00 min.
```

Los identificadores son los que se usan para marcar: `2` es una tarea y `r1` una recurrencia.

## Marcar lo hecho

- **En opencode:** `/hecho 2` marca la tarea 2. `/hecho r1` marca el bloque de curso de hoy.
- **En terminal:** `python scripts/agenda.py done 2` y `python scripts/agenda.py done r1`.
- **Omitir sin contar como hecho:** `python scripts/agenda.py skip 2`.

Al marcar, la tarea desaparece de `hoy.md` y queda con `status = done` y `done_at` en la base. No se borra: el historial se conserva y se puede consultar.

Si una tarea estaba atrasada y ya no tiene sentido, `skip` la cierra sin falsear el progreso.

## Ver la semana

- **En opencode:** `/hoy semana`.
- **En terminal:** `python scripts/agenda.py semana`.
- **En el editor:** `docs/privado/agenda/semana.md`.

La vista arranca hoy y cubre siete días, con la carga total de cada jornada. No muestra los días pasados de la semana en curso para no llenar la pantalla de ceros.

## Añadir tareas

```powershell
python scripts/agenda.py add "Preparar preguntas para Patricia" --date 2026-10-31 --area entrevista --duration 30
python scripts/agenda.py add "Revisar la oferta de la semana" --date 2026-11-03 --time 10:00 --area busqueda
python scripts/agenda.py add "Ordenar el escritorio" --area admin --priority 3
```

Sin `--date`, la tarea entra en el backlog y aparece al final de `hoy.md`. Las áreas disponibles son `curso`, `busqueda`, `linkedin`, `networking`, `ingles`, `portfolio`, `entrevista` y `admin`.

Para las publicaciones de LinkedIn, añade una tarea con hora después de generar el plan semanal con `/li-plan`. Son dos o tres altas por semana y evita depender de un parser de tablas.

## Cambiar una tarea

```powershell
python scripts/agenda.py set 3 --time 10:00
python scripts/agenda.py set 3 --date 2026-11-01 --notes "Confirmada la hora con Patricia"
```

El identificador se ve en `hoy.md` o en la salida de `/hoy`. `set` cambia fecha, hora, título o notas, pero no el estado; para cerrar una tarea se usa `done`.

La entrevista con Patricia está dada de alta el 31 de octubre como evento de día completo porque aún no hay hora confirmada. Cuando la tengas, `set 3 --time HH:MM` la convierte en un evento con hora y aviso.

## Sincronizar candidaturas

`python scripts/agenda.py sync` lee `docs/candidaturas/candidaturas.db` en modo solo lectura, busca una fecha `YYYY-MM-DD` en el campo `proximo_paso` y crea o actualiza la tarea de seguimiento. La referencia `cand-<id>-seguimiento` evita duplicados.

La tarea de IGNIS del 4 de noviembre entra por esta vía. Si cambias la fecha en la base de candidaturas, vuelve a ejecutar `sync` y la tarea se reprograma mientras siga pendiente.

## Calendario ICS

### Generar el fichero

```powershell
python scripts/agenda.py ics
```

Genera `docs/privado/agenda/agenda.ics` desde hoy hasta el 31 de diciembre de 2026. Para incluir el plazo de abril de 2027:

```powershell
python scripts/agenda.py ics --to 2027-04-30
```

El calendario incluye todas las tareas pendientes con fecha y las cinco recurrencias de la semana tipo. Las tareas con hora llevan aviso 15 minutos antes; las recurrencias no llevan aviso para no disparar cinco notificaciones cada mañana. Si quieres un aviso para el bloque de curso, se añade una vez en Google Calendar sobre el evento recurrente.

### Importar en Google Calendar

1. Abre Google Calendar en el navegador de escritorio.
2. Entra en **Configuración** con el engranaje.
3. En el menú izquierdo, elige **Importar y exportar**.
4. En **Importar**, pulsa **Seleccionar archivo** y elige `docs/privado/agenda/agenda.ics`.
5. En **Añadir al calendario**, crea uno nuevo llamado `Agenda EW 2026`. No lo mezcles con el calendario personal.
6. Pulsa **Importar**.
7. En el móvil, abre la app de Calendar con la misma cuenta y activa `Agenda EW 2026` en la lista de calendarios.

La importación es una copia, no una suscripción. Cuando cambies tareas, vuelve a generar el `.ics` e impórtalo. Para evitar duplicados, la vía limpia es borrar el calendario secundario y volver a importar; Google identifica los eventos por `UID`, pero la importación no garantiza una actualización perfecta.

### Importar en Outlook

En Outlook clásico: **Archivo > Abrir y exportar > Importar o exportar > Importar un archivo iCalendar (.ics)**. Elige el fichero y guárdalo en un calendario nuevo. En el Outlook nuevo, la ruta está en **Calendario > Añadir calendario > Cargar desde archivo** y cambia según la versión.

### Importar en Apple Calendar

**Archivo > Importar**, selecciona `agenda.ics` y elige un calendario nuevo. En el iPhone aparece al sincronizar iCloud.

### Por qué no hay suscripción automática

Suscribirse a un calendario exige una URL que Google o Outlook puedan alcanzar. `localhost` no lo es. Publicar el `.ics` en un Gist o en un servidor lo haría accesible a cualquiera que tenga el enlace, y el fichero contiene la entrevista, las empresas y los plazos personales. Por eso la vía recomendada es la importación manual. Si más adelante quieres notificaciones nativas y sincronización real, la alternativa es una app externa con API, no este fichero.

Las horas se generan sin zona horaria explícita, así que el calendario las interpreta en la zona del dispositivo. En España se ven correctamente y no hay que ajustar nada al cambiar de horario.

## Google Tasks vía MCP

La agenda también se refleja en Google Tasks mediante el MCP `google-calendar`, configurado en `opencode.json`. Es un espejo de solo ida: la base SQLite sigue siendo la fuente de verdad y Google muestra una copia.

### Qué se copia y qué no

| Elemento | Se copia | Motivo |
| --- | --- | --- |
| Tareas pendientes | Sí, con título, notas y fecha | Son las que tienen equivalente directo |
| Tareas sin fecha | Sí, sin fecha | Google Tasks admite tareas sin vencimiento |
| Tareas hechas | Sí, marcadas como completadas | El estado viaja en la sincronización |
| Recurrencias | **No** | Google Tasks no soporta repetición |
| Área y prioridad | **No** | Google Tasks no tiene etiquetas ni campo de prioridad |

El volcado del 2026-10-31 creó 37 tareas en una lista llamada `Employment Workshop`, separada de las listas personales. Esa lista se puede borrar entera sin afectar a nada más.

### Sincronizar

```powershell
python scripts/agenda.py google
```

Empuja a Google los cambios de la base: crea las tareas nuevas, actualiza título, notas y fecha de las que cambiaron, y marca como completadas las que ya están hechas. Es idempotente: ejecutarlo dos veces seguidas no cambia nada.

Para ver qué haría sin escribir:

```powershell
python scripts/agenda.py google --dry-run
```

La primera vez enlaza las tareas de Google con las de la base por título y guarda el identificador en la columna `google_id`. Esa columna se añade sola si no existe. La correspondencia queda en `docs/privado/agenda/google.json`, que guarda la cuenta, el nombre de la lista y su identificador.

Opciones: `--email` para elegir cuenta si hay varias autorizadas, `--list` para usar otra lista, `--dry-run` para simular.

### Qué no hace

- No lee cambios desde Google. Si se marca una tarea como hecha en el móvil, la base no se entera y la siguiente sincronización la devuelve a pendiente. Por eso la regla es que Google nunca se edita a mano.
- No borra en Google las tareas eliminadas de la base. Quedan huérfanas hasta que se limpien a mano.
- No copia recurrencias, por la limitación de Google Tasks.

### De dónde salen las credenciales

De `~/.google_workspace_mcp/credentials/<cuenta>.json`, el fichero que deja el MCP al autorizar. El comando lo lee, pide un token nuevo a Google y llama a la API de Tasks con la biblioteca estándar: no necesita `google-auth` ni ningún paquete adicional.

### Límite del token

Mientras el proyecto de Google Cloud siga en estado de prueba, la autorización caduca a los siete días. Cuando eso pase, el comando falla con un mensaje claro y hay que volver a autorizar desde opencode. Publicar la aplicación lo evita, pero exige página de inicio, política de privacidad y términos en un dominio autorizado.

## Reglas de convivencia

- La base manda sobre el estado: si una tarea está hecha, está hecha aunque el markdown de origen siga hablando de ella.
- `hoy.md` y `semana.md` son vistas: se regeneran y se sobrescriben. No se editan a mano.
- `seed.json` solo se aplica al crear la base o al ejecutar `seed`; no actualiza tareas existentes.
- Una tarea es una acción concreta, no un proyecto. Los proyectos viven en `docs/privado/plan-estudios-2026.md`.
- El plan de estudios y el plan de LinkedIn siguen siendo la explicación; la agenda es la ejecución.

## Copia de seguridad

La base es un solo fichero. Copia `docs/privado/agenda/agenda.db` a otra carpeta o a un disco externo. `seed.json` permite reconstruir la carga inicial, pero no las tareas añadidas ni lo ya marcado.

## Problemas frecuentes

- **`python` no se reconoce:** usa `py scripts/agenda.py`. En este equipo Python 3.14.7 está en el PATH, pero una sesión abierta antes de instalarlo puede no verlo.
- **Acentos raros en la consola:** ejecuta en Windows Terminal o cambia a UTF-8 con `chcp 65001`.
- **El calendario no refleja los cambios:** vuelve a ejecutar `ics` e importa el fichero. La importación no se actualiza sola.
- **Eventos duplicados:** borra el calendario `Agenda EW 2026` y vuelve a importar el `.ics` actualizado.
- **Una tarea no aparece:** comprueba la fecha con `python scripts/agenda.py hoy --date 2026-11-04`; si no tiene fecha, está en el backlog.

## Siguiente fase

La interfaz React queda para después de cerrar D2 y D9, según la decisión D12 del plan. Reutilizará el mismo esquema y añadirá una API local; la base y el `.ics` no cambian.
