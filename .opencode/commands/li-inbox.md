---
description: Clasifica la bandeja de LinkedIn y redacta solo las respuestas que merecen la pena.
agent: build
subagent: false
---

Usa la herramienta skill con el id `li-inbox` y sigue sus instrucciones.

Entrada de la persona: $ARGUMENTS

Contexto local:

- Si faltan los mensajes, pídelos; no inicies sesión ni leas la bandeja con automatización.
- Muestra primero los recuentos por LEAD, RECRUITER, PEER, ASK y SPAM.
- Pasa las respuestas por el skill `li-human`; la persona las envía.
