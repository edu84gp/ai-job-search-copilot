---
description: Convierte una idea secuencial en un carrusel de LinkedIn con texto y PDF.
agent: build
subagent: false
---

Usa la herramienta skill con el id `li-carousel` y sigue sus instrucciones.

Entrada de la persona: $ARGUMENTS

Contexto local:

- Si la idea no tiene secuencia, dilo y deriva al skill `li-post`.
- Entrega primero el texto diapositiva a diapositiva y el post que lo acompaña; pasa ambos por `li-human`.
- Construye el PDF solo con aprobación explícita y no lo subas a LinkedIn.
