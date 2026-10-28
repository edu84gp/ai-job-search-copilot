---
description: Limpia un borrador de marcas de IA y lo puntúa con el panel de cinco comprobaciones.
agent: build
subagent: false
---

Usa la herramienta skill con el id `li-human` y sigue sus instrucciones.

Entrada de la persona: $ARGUMENTS

Contexto local:

- Ejecuta los dos scripts desde la raíz del repositorio con `uv run --no-project python .opencode/skills/li-human/humanize.py` y `detect.py`.
- Muestra el texto limpio y la puntuación, nunca la puntuación sola.
- No afirmes que el texto es indetectable: son heurísticas locales.
