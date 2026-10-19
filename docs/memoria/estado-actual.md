# Estado actual del proyecto

## Foto

- Última actualización: 2026-10-19.
- Fase del plan: Fase 21 completada (Fases 0 a 21 cerradas; Fase 22 pendiente).
- Ecosistema: 15 agentes, 8 MCPs, 6 comandos y 3 skills.
- Repositorio: público en https://github.com/edu84gp/job-support-portfolio con CI de calidad (markdownlint y lychee) en verde.
- Kanban público del pipeline de candidaturas: https://github.com/users/edu84gp/projects/3 con campo Pipeline propio.
- Demos desplegadas en GitHub Pages: pokedex_web y el-juego-de-la-vida. WhatsChatGPT pendiente por requerir servidor con Ollama.
- Candidaturas: sin registros todavía. La tabla `candidaturas` se creará al primer registro con application-tracker.
- Memoria: grafo del Memory MCP sembrado el 2026-10-19 con los hitos de las fases 0 a 21 en formato JSON Lines (5 entidades y 5 relaciones), verificado contra el fichero.

## Siguiente paso

- Fase 22: validación final con revisión cruzada de agentes, permisos y documentación, y cierre de CHANGELOG-progreso.md.

## Bloqueos

- Ninguno. El grafo del Memory MCP quedó sembrado tras corregir MEMORY_FILE_PATH a ruta absoluta (el servidor resuelve las relativas contra la caché de npx) y reescribir el fichero en formato JSON Lines (el servidor v2.0.0 carga un registro JSON por línea).

## Pendientes anotados

- Evaluación de respaldo externo de candidaturas con Notion o Google Drive, sin implementar. Notion es la opción de menor fricción.
- Demo de WhatsChatGPT sin desplegar: necesita un servidor con Ollama en ejecución.
