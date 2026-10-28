---
description: Escribe un post de LinkedIn desde una idea con 21 fórmulas de gancho y humanización.
agent: build
subagent: false
---

Usa la herramienta skill con el id `li-post` y sigue sus instrucciones.

Entrada de la persona: $ARGUMENTS

Contexto local:

- El perfil de voz y el historial viven en `docs/privado/linkedin/`. Si `voice.md` no existe, pide tres publicaciones propias antes de escribir.
- Ejecuta el humanizador con `uv run --no-project python .opencode/skills/li-human/humanize.py` y la puntuación con `detect.py`.
- No publiques en LinkedIn. Entrega tres ganchos, un borrador completo humanizado y el bloque listo para copiar; espera confirmación antes de registrar nada.
