---
description: Puntúa un perfil de LinkedIn sobre 100 y reescribe lo que pierde puntos.
agent: build
subagent: false
---

Usa la herramienta skill con el id `li-profile` y sigue sus instrucciones.

Entrada de la persona: $ARGUMENTS

Contexto local:

- Lee `rubric.json` del propio skill para puntuar los doce apartados.
- Si faltan titular, extracto o experiencias, pídelos; no navegues LinkedIn ni inventes datos.
- Pasa las reescrituras por el skill `li-human` antes de entregarlas.
