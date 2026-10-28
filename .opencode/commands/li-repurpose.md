---
description: Extrae una semana de publicaciones de LinkedIn de un vídeo, artículo o transcripción.
agent: build
subagent: false
---

Usa la herramienta skill con el id `li-repurpose` y sigue sus instrucciones.

Entrada de la persona: $ARGUMENTS

Contexto local:

- Lee el material completo antes de extraer; si no llega a cuatro piezas, dilo.
- Asigna fórmulas de `../li-post/hooks.json` y redacta una publicación cada vez.
- Pasa cada borrador por los skills `li-post` y `li-human`; no publiques nada.
