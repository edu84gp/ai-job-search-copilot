---
name: memoria-sesion
description: Ciclo de memoria del proyecto entre sesiones: consultar docs/memoria al retomar trabajo y actualizarla al cerrar hitos o tomar decisiones. Usar al empezar una sesión de continuidad o al cerrar una fase o avance relevante.
---

# Ciclo de memoria de sesión

## Al retomar trabajo

1. Lee `docs/memoria/estado-actual.md` para conocer la foto, el siguiente paso y los bloqueos.
2. Consulta `docs/memoria/decisiones.md` antes de proponer cambios que contradigan decisiones previas.
3. Para detalle, usa el Memory MCP (read_graph o search_nodes) sobre el grafo local de `docs/memoria/memoria.local.json`.

## Al cerrar un hito

1. Actualiza `docs/memoria/estado-actual.md`: última actualización, fase, siguiente paso y bloqueos.
2. Si hubo decisión relevante, añádela a `docs/memoria/decisiones.md` con fecha, decisión, motivo y alternativas descartadas.
3. Añade o amplía entidades en el Memory MCP con create_entities o add_observations.
4. Para el registro completo del avance, usa el comando `/log-progress`, que ya integra estos pasos.

## Reglas

- No duplicar el CHANGELOG: la memoria es foto y motivo, no cronología.
- Mantener `estado-actual.md` corto: si crece, resumir y mover el detalle al grafo.
