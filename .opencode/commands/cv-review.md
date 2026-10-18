---
description: Audita el CV con ats-checker y, si procede y lo confirmas, encadena la revisión con cv-optimizer.
agent: build
subtask: false
---

Lanza el pipeline de revisión de CV en dos pasos con control humano entre ellos.

Entrada de la persona: $ARGUMENTS

Paso 1, obligatorio: invoca al subagente ats-checker mediante Task con subagent_type ats-checker sobre el CV indicado. Si la entrada no indica archivo, lista qué hay en cv/ y pregunta cuál auditar antes de invocar. Pide que devuelva veredicto, score desglosado, keywords faltantes y correcciones priorizadas.

Paso 2: presenta el veredicto tal cual, sin reescribirlo. Si el score es inferior a 80, explica en dos líneas que el siguiente paso es cv-optimizer y pregunta si continúa. Solo si confirma, invoca al subagente cv-optimizer con el mismo CV y las correcciones del informe ATS como contexto. Si el score es 80 o superior, informa de que no hace falta reescritura y ofrece revisar keywords solo si lo pide.

Reglas: verifica rutas antes de invocar y no inventes archivos. No encadenes el paso 2 sin confirmación explícita. Responde en español.
