---
description: Abre una lección del Employment Workshop en el navegador y resume su contenido.
agent: build
subagent: false
---

Entrada: $ARGUMENTS

La entrada es el número de una lección, por ejemplo `4.4` o `10.2`.

Pasos:

1. Abre `https://www.neoland.online/products/employment-workshop-2026` con Playwright.
2. Localiza el enlace cuyo texto empiece por el número indicado. Si no aparece, navega a la categoría de la unidad y búscalo en la barra lateral.
3. Abre la lección y lee el contenido completo, incluidas las imágenes con texto.
4. Devuelve el título, el estado de la lección y un resumen de tres o cuatro líneas con las ideas principales.

No marques la lección como completada ni entregues actividades. Responde en español.
