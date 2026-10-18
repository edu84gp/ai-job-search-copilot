---
description: Registra el avance del día con tracker-doc, actualiza memoria, CHANGELOG y ofrece cerrar fases en PLAN.
agent: build
subtask: false
---

Registra el avance indicado con trazabilidad completa.

Entrada de la persona: $ARGUMENTS

Paso 1: invoca al subagente tracker-doc mediante Task con subagent_type tracker-doc, pasando el avance indicado, para que redacte el apunte en docs/apuntes/ y devuelva la ruta guardada.

Paso 2: actualiza docs/memoria/estado-actual.md con la nueva foto, el siguiente paso y los bloqueos. Si hubo una decisión relevante, añádela a docs/memoria/decisiones.md con fecha, decisión, motivo y alternativas descartadas, y amplía el grafo del Memory MCP con create_entities o add_observations.

Paso 3: añade una entrada al final de CHANGELOG-progreso.md, en el estilo existente, con la fecha de hoy y el avance resumido en dos a cuatro puntos.

Paso 4: si el avance cierra una fase del plan, pregunta antes de marcar el checkbox correspondiente en PLAN.md y actualizar la línea de estado de resolución. Sin confirmación, no toques PLAN.md.

Cierra con un resumen de dos líneas y las rutas modificadas. Responde en español.
