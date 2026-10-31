---
description: Marca como hecha una tarea o recurrencia de la agenda.
agent: build
subagent: false
---

Entrada: $ARGUMENTS

Valida que la entrada sea un id numérico (`12`), una recurrencia (`r3`) o una recurrencia con fecha (`r3 --date 2026-10-30`). Si no encaja, no ejecutes nada y pide el id.

Ejecuta `python scripts/agenda.py done <entrada>`.

Después ejecuta `python scripts/agenda.py hoy` y muestra solo las tareas que quedan.

Si la tarea cerrada tiene una referencia D1-D12, A1-A6 o de fase, propone ejecutar `/log-progress` sin lanzarlo.

Responde en español.
