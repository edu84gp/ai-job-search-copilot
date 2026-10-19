# Plan Employment Workshop 2026

## ToDo general por fases

Leyenda de estado: pendiente, en curso, completada.

- [x] Fase 0: Base consolidada. Agentes cv-optimizer, interview-coach y tracker-doc optimizados con permission, temperature y rúbricas.
- [x] Fase 1: Estructura base del repositorio. Crear directorios docs, docs-ejercicios, docs-apuntes, cv, portfolio y templates. Crear README.md y CHANGELOG-progreso.md.
- [x] Fase 2: Higiene de MCPs existentes. Validar servidores github, filesystem y memory en opencode.json y .opencode/mcp.json. Sustituir token de ejemplo por variable de entorno. Documentar uso en docs/referencia-agentes-mcps.md.
- [x] Fase 3: Agente linkedin-optimizer. Crear .opencode/agents/linkedin-optimizer.md con análisis de titular, extracto y experiencia.
- [x] Fase 4: Agente github-portfolio-reviewer. Crear agente para revisión de README de repositorios, fijados y descripción de proyectos.
- [x] Fase 5: Agente ats-checker. Crear agente de verificación ATS con checklist de formato, palabras clave y legibilidad automática.
- [x] Fase 6: Agente cover-letter-drafter. Crear agente para borradores de carta de presentación alineada a oferta.
- [x] Fase 7: Agente job-search-strategist. Crear agente para estrategia semanal de búsqueda, filtrado de ofertas y priorización.
- [x] Fase 8: Agente application-tracker. Crear agente para registro de candidaturas con tabla de estado y seguimiento.
- [x] Fase 9: Agente behavioral-star-coach. Crear agente específico STAR separado de interview-coach para historias conductuales.
- [x] Fase 10: Agente live-coding-coach. Crear agente para simulacros de live-coding con protocolo sin solución directa.
- [x] Fase 11: Agente networking-outreach. Crear agente para mensajes de networking y seguimiento de contactos.
- [x] Fase 12: Agente personal-brand-builder. Crear agente para plan de contenido técnico y marca personal.
- [x] Fase 13: Agente salary-negotiator. Crear agente para preparación de negociación salarial y contraofertas.
- [x] Fase 14: Agente course-exercise-solver. Crear agente transversal para guiar ejercicios de Employment Workshop 2026 sin entregar solución directa.
- [x] Fase 15: MCP fetch y context7. Instalar y configurar servidores fetch y context7 para consulta de ofertas y documentación oficial.
- [x] Fase 16: MCP sequential-thinking. Instalar y configurar servidor sequential-thinking para análisis complejo de decisiones.
- [x] Fase 17: MCP playwright. Instalar y configurar servidor playwright para verificación visual del portfolio.
- [x] Fase 18: MCP sqlite y drive. Instalar sqlite como fuente unica del historial de candidaturas y evaluar notion o google-drive para respaldo.
- [x] Fase 19: Commands opencode. Crear comandos cv-review, linkedin-review, interview-technical, interview-behavioral, interview-live-coding y log-progress. Migrar las directrices globales a AGENTS.md.
- [x] Fase 20: Skills y memory-bank. Crear skills reutilizables y estructura docs/memoria para continuidad entre sesiones.
- [x] Fase 21: Visibilidad GitHub. Optimizar README para reclutadores, configurar GitHub Actions de despliegue, Projects Kanban y linter markdown.
- [x] Fase 22: Validación final. Ejecutar revisión cruzada de agentes, permisos y documentación. Cerrar CHANGELOG-progreso.md.

## Objetivo

Centralizar los ejercicios del curso pregrabado Employment Workshop 2026 y la documentación del proceso de inserción laboral en el repositorio `ai-job-search-copilot` para evidenciar el progreso técnico ante reclutadores.

## Estado de resolución

- Fase 0 completada: inventario y optimización de agentes existentes.
- Fase 1 completada: estructura base docs, cv, portfolio, templates, README.md y CHANGELOG-progreso.md.
- Fase 2 completada: higiene MCPs con opencode.json canónico, variable de entorno y documentación de uso.
- Fase 3 completada: agente linkedin-optimizer con análisis de titular, extracto y experiencia.
- Fase 4 completada: agente github-portfolio-reviewer genérico con MCP github vivo y protocolo de repo privado.
- Fase 5 completada: agente ats-checker como puerta previa a cv-optimizer con score y veredicto.
- Fase 6 completada: agente cover-letter-drafter con redacción en idioma de oferta y guardado en cv/cartas/.
- Fase 7 completada: agente job-search-strategist con match variable y plan semanal en docs/candidaturas/.
- Fase 8 completada: agente application-tracker con tabla Markdown en docs/candidaturas/ y estados detallados.
- Fase 9 completada: agente behavioral-star-coach con banco amplio y rúbrica de 0 a 10.
- Fase 10 completada: agente live-coding-coach con stack del bootcamp y protocolo por pasos.
- Fase 11 completada: agente networking-outreach con LinkedIn y email y registro en docs/networking/.
- Fase 12 completada: agente personal-brand-builder con estrategia, calendario y borradores en docs/marca-personal/.
- Fase 13 completada: agente salary-negotiator con paquete completo y registro en docs/negociacion/.
- Fase 14 completada: agente course-exercise-solver socrático transversal con índice en docs/ejercicios/.
- Fase 15 completada: MCPs fetch con uvx oficial y context7 remoto con clave, acotados por permisos a agentes de código e investigación.
- Fase 16 completada: MCP sequential-thinking acotado por permisos a agentes de decisión y análisis y a los primarios build y plan.
- Fase 17 completada: MCP playwright en modo headless con chromium, acotado por permisos a github-portfolio-reviewer, build y plan.
- Fase 18 completada: MCP sqlite como fuente única de candidaturas con la tabla Markdown regenerada desde la base, acotado por permisos a application-tracker, job-search-strategist, build y plan.
- Evaluación pendiente anotada: respaldo externo de candidaturas con Notion o Google Drive, sin implementar por ahora. Notion es la opción de menor fricción (solo token) y Google Drive exige OAuth con proyecto en Google Cloud. Detalle en docs/referencia-agentes-mcps.md.
- Fase 19 completada: 6 comandos en .opencode/commands/. cv-review encadena ats-checker y cv-optimizer con confirmación, log-progress registra avance con tracker-doc y actualiza CHANGELOG con confirmación de fase, y hay un comando por coach para entrevista técnica, conductual y live-coding.
- Migradas las directrices globales de .opencode/rules.md a AGENTS.md en la raíz, el archivo que opencode carga automáticamente. Descartado rules.md porque no se estaba cargando.
- Fase 20 completada: memoria del proyecto con Memory MCP en docs/memoria/memoria.local.json, ficheros versionados estado-actual.md y decisiones.md, 3 skills (flujo-candidatura, apunte-ejercicio y memoria-sesion) y comando log-progress ampliado con la memoria.
- Fase 21 completada: repositorio público en GitHub con gh CLI autenticado, README bilingüe orientado a reclutadores, workflow de calidad (markdownlint y lychee) en verde, Pages desplegado en pokedex_web y el-juego-de-la-vida y Kanban público de candidaturas con campo Pipeline en Projects.
- Fase 22 completada: auditoría de los 15 agentes, los 8 MCPs, los 6 comandos y las 3 skills con handshakes funcionales, coherencia documental y seguridad del repo público (sin secretos). Corregidos interview-coach (webfetch deny) y .gitignore (.playwright-mcp), añadido templates/README.md, pase de github-portfolio-reviewer y correcciones en los repos de proyectos (licencias MIT, topics, tildes y CTA de pokedex_web). Plan cerrado: 22 de 22 fases.
- El avance se marca en los checkboxes del ToDo y se detalla en CHANGELOG-progreso.md. El detalle técnico vive en docs/referencia-agentes-mcps.md.

## Documentación técnica

- Referencia de agentes y MCPs: `docs/referencia-agentes-mcps.md`
- Directrices globales: `AGENTS.md`
