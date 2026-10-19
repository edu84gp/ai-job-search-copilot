# Estado actual del proyecto

## Foto

- Última actualización: 2026-10-19.
- Fase del plan: Fases 0 a 22 completadas; plan cerrado y validado.
- Ecosistema: 15 agentes, 8 MCPs, 6 comandos y 3 skills.
- Repositorio: público en https://github.com/edu84gp/ai-job-search-copilot (renombrado desde job-support-portfolio el 2026-10-19) con CI de calidad (markdownlint y lychee) en verde.
- Kanban público del pipeline de candidaturas: https://github.com/users/edu84gp/projects/3 con campo Pipeline propio.
- Demos desplegadas en GitHub Pages: pokedex_web y el-juego-de-la-vida. WhatsChatGPT pendiente por requerir servidor con Ollama.
- Candidaturas: sin registros todavía. La tabla `candidaturas` se creará al primer registro con application-tracker.
- Memoria: grafo del Memory MCP sembrado el 2026-10-19 con los hitos de las fases 0 a 21 en formato JSON Lines (5 entidades y 5 relaciones), verificado contra el fichero.

## Siguiente paso

- Plan completado. Siguiente hito operativo: registrar la primera candidatura real con application-tracker y mantener la memoria al día.

## Bloqueos

- Ninguno. El grafo del Memory MCP quedó sembrado tras corregir MEMORY_FILE_PATH a ruta absoluta (el servidor resuelve las relativas contra la caché de npx) y reescribir el fichero en formato JSON Lines (el servidor v2.0.0 carga un registro JSON por línea).

## Pendientes anotados

- Fijar ai-job-search-copilot en el perfil de GitHub: manual en el navegador (Customize your pins), pendiente tras la auditoría.
- Guía "Cómo reproducirlo" en el README del sistema: la ruta absoluta de MEMORY_FILE_PATH no es portable a otro equipo.
- Evidencia real pendiente de avance del curso: apuntes y ejercicios en docs/apuntes y docs/ejercicios, y vídeo corto del sistema y del Kanban.
- Vista Board del Project agrupada por Pipeline, con una candidatura anonimizada de ejemplo.
- README de el-juego-de-la-vida por reescribir como README de proyecto y favicon ausente en pokedex_web.
- Caso de estudio público de Aplika Jobs sin exponer propiedad intelectual.
- Evaluación de respaldo externo de candidaturas con Notion o Google Drive, sin implementar. Notion es la opción de menor fricción.
- Demo de WhatsChatGPT sin desplegar: necesita un servidor con Ollama en ejecución.
