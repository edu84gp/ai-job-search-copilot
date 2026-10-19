# CHANGELOG de progreso

Historial de fases del plan definido en `PLAN.md`.

## 2026-10-15 - Fase 0 completada

- Inventario de agentes existentes: cv-optimizer, interview-coach y tracker-doc.
- Optimización de frontmatter con migration de campo deprecado tools a permission.
- Asignación de temperature y color diferenciados.
- Definición de rúbricas, contratos de entrada y reglas anti-especulación.

## 2026-10-15 - Fase 1 completada

- Creación de directorios docs, docs-ejercicios, docs-apuntes, cv, portfolio y templates.
- Creación de README.md con descripción, estructura y uso.
- Creación de este archivo CHANGELOG-progreso.md para trazabilidad.

## 2026-10-15 - README v2 orientado a reclutadores

- Sustitución de README interno por formato personal y profesional bilingüe ES/EN.
- Inclusión de titular Full-Stack Junior IA, disponibilidad remota prioritaria y datos de contacto.
- Inclusión de tabla de 4 proyectos con descripción ES/EN y enlaces a GitHub.

## 2026-10-15 - README v3 ES/EN separado y Aplika Jobs privado

- Separación en dos bloques: español arriba con enlace a versión inglesa abajo.
- Marcado de Aplika Jobs como repositorio privado por explotación comercial.
- Sustitución de enlace directo por solicitud de acceso vía email en ES y EN.

## 2026-10-15 - Fase 2 completada

- Creación de opencode.json canónico con MCPs github, filesystem y memory en formato type local y command como arreglo.
- Higienización de .opencode/mcp.json con eliminación de token TU_TOKEN_DE_GITHUB.
- Creación de .gitignore con protección de .env y .env.example con variable GITHUB_PERSONAL_ACCESS_TOKEN.
- Documentación de uso de cada MCP en PLAN.md.

## 2026-10-15 - Fase 3 completada

- Creación de .opencode/agents/linkedin-optimizer.md con análisis de titular, extracto y experiencia.
- Configuración con temperature 0.1, permission edit deny y rúbrica 1 a 5.
- Actualización de PLAN.md y referencias técnicas.

## 2026-10-15 - Reestructuración PLAN y referencia técnica

- Creación de docs/referencia-agentes-mcps.md con documentación completa de 4 agentes y 3 MCPs.
- Inclusión de linkedin-optimizer faltante con qué hace, para qué sirve y cómo usar.
- Adelgazamiento de PLAN.md solo a ToDo, Objetivo, Estado y enlace a referencia.
- Formato elegido md en docs por ser versionable, compatible con GitHub y editable por tracker-doc.

## 2026-10-15 - Fase 4 completada

- Creación de .opencode/agents/github-portfolio-reviewer.md como agente genérico con MCP github vivo.
- Revisión completa de README, descripción, topics, demo, licencia y fijados con rúbrica 1 a 5.
- Protocolo de repo privado tipo Aplika Jobs con case study sin exponer propiedad intelectual.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-15 - Fase 5 completada

- Creación de .opencode/agents/ats-checker.md como puerta previa a cv-optimizer para PDF y Markdown en cv.
- Inspección local vía lectura sin bash, ponderación parseo 35 keywords 35 legibilidad 20 coherencia 10.
- Veredicto APTO CORREGIR NO APTO con derivación a cv-optimizer cuando el score sea inferior a 80.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-15 - Fase 6 completada

- Creación de .opencode/agents/cover-letter-drafter.md con redacción en idioma de oferta y guardado en cv/cartas/.
- Creación de carpeta cv/cartas/ para trazabilidad de candidaturas.
- Estructura de 4 bloques con límite de 250 palabras y prohibición de inventar experiencia.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-15 - Fase 8 completada

- Creación de .opencode/agents/application-tracker.md con tabla Markdown y estados detallados.
- Creación de docs/candidaturas/tabla-candidaturas.md con columnas Fecha Empresa Rol Estado Oferta Carta CV Contacto y Próximo paso.
- Enlaces verificados a oferta carta y CV sin inventar rutas, actualización sin borrar historial.
- Fase 7 queda pendiente a petición del usuario.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-15 - Fase 9 completada

- Creación de .opencode/agents/behavioral-star-coach.md con banco amplio de 7 bloques y rúbrica de 0 a 10.
- Complemento sin duplicado de interview-coach, guardado derivado a tracker-doc.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 7 completada

- Creación de .opencode/agents/job-search-strategist.md con match variable y plan semanal en docs/candidaturas/.
- Ponderación stack 40 experiencia 25 modalidad 20 calidad 15, canales LinkedIn e InfoJobs.
- Derivación a application-tracker y cover-letter-drafter sin tocar la tabla.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 10 completada

- Creación de .opencode/agents/live-coding-coach.md con stack del bootcamp y protocolo por pasos.
- Bloques HTML CSS JS React Node Express MongoDB WebSockets y nociones RAG MCP.
- Tres pistas socráticas sin solución, rúbrica de 0 a 10 y guardado derivado a tracker-doc.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 11 completada

- Creación de .opencode/agents/networking-outreach.md con LinkedIn y email y 7 escenarios.
- Creación de docs/networking/contactos-networking.md con tabla de contactos y estados.
- Estructura de mensaje en motivo valor y petición única, sin duplicados y con alertas de seguimiento.
- Derivación a application-tracker y cover-letter-drafter cuando aplique.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 12 completada

- Creación de .opencode/agents/personal-brand-builder.md con estrategia, calendario y borradores.
- Creación de docs/marca-personal/calendario-contenido.md y carpeta borradores/.
- Canales LinkedIn y GitHub con ampliación futura, idioma español único, cadencia de 2 a 3 piezas por semana.
- Cuatro pilares de contenido y prohibición de inventar métricas.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 13 completada

- Creación de .opencode/agents/salary-negotiator.md con paquete completo, 5 escenarios y tabla de limites.
- Creación de docs/negociacion/registro-negociaciones.md y carpeta ofertas/.
- Regla clave de no dar la primera cifra, anclar con rango y no aceptar en la misma llamada.
- Rangos aportados ahora y vía MCP de búsqueda cuando exista, derivación a application-tracker.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 14 completada

- Creación de .opencode/agents/course-exercise-solver.md socrático transversal con 4 niveles de ayuda.
- Creación de docs/ejercicios/indice-ejercicios.md con tabla de seguimiento y estados.
- Derivación a agentes expertos y registro individual delegado a tracker-doc.
- Solución completa solo bajo petición explícita conforme a rules.md.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 15 completada

- Instalación de uv 0.13.1 con winget y configuración del MCP fetch oficial con uvx mcp-server-fetch.
- Configuración del MCP context7 remoto en https://mcp.context7.com/mcp con cabecera CONTEXT7_API_KEY.
- Añadidos fetch y context7 a opencode.json canónico y por paridad a .opencode/mcp.json legacy.
- Permisos `context7_*` y `fetch_*` denegados globalmente y habilitados por agente: context7 en course-exercise-solver, live-coding-coach e interview-coach; fetch en job-search-strategist, salary-negotiator, cv-optimizer y ats-checker.
- Añadida CONTEXT7_API_KEY a .env.example y creado .env no versionado para claves.
- Habilitados context7 y fetch en el agente primario build y en plan.
- Verificado context7 con clave real frente a clave falsa y fetch con descarga real.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 16 completada

- Configuración del MCP sequential-thinking con npx @modelcontextprotocol/server-sequential-thinking.
- Añadido a opencode.json canónico y por paridad a .opencode/mcp.json legacy.
- Permiso sequential-thinking_* denegado globalmente y habilitado en salary-negotiator, job-search-strategist, course-exercise-solver y github-portfolio-reviewer, además de los primarios build y plan.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 17 completada

- Configuración del MCP playwright con npx @playwright/mcp en modo headless usando el chromium ya instalado.
- Añadido a opencode.json canónico y por paridad a .opencode/mcp.json legacy.
- Permiso playwright_* denegado globalmente para ahorrar contexto y habilitado en github-portfolio-reviewer, build y plan.
- Verificado el arranque del servidor y las opciones disponibles con --help.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-16 - Fase 18 completada

- Configuración del MCP sqlite con uvx mcp-server-sqlite sobre docs/candidaturas/candidaturas.db.
- Añadido a opencode.json canónico y por paridad a .opencode/mcp.json legacy.
- Base SQLite como fuente única de candidaturas y tabla Markdown regenerada desde la base.
- Base fuera de git mediante docs/candidaturas/*.db por contener datos personales.
- Permiso sqlite_* denegado globalmente y habilitado en application-tracker, job-search-strategist, build y plan.
- Actualizado application-tracker al flujo SQLite con esquema de la tabla candidaturas y regeneración de la vista Markdown.
- Actualizado job-search-strategist para consultar la base y no repetir candidaturas.
- Evaluación de respaldo externo documentada con Notion y Google Drive, sin implementar.
- Documentación en docs/referencia-agentes-mcps.md y actualización de PLAN.md.

## 2026-10-17 - Corrección del MCP sqlite

- Detectado tras el reinicio que el servidor sqlite caía con MCP error -32000 Connection closed.
- Causa: el servidor oficial usaba Server.list_resources, retirada en el SDK 2.x resuelto por uvx.
- Solución: pin del SDK con uvx --with "mcp<2" en opencode.json y en .opencode/mcp.json.
- Verificado el handshake JSON-RPC y el listado de herramientas contra una base temporal y confirmado sqlite connected en opencode mcp list.

## 2026-10-17 - Fase 19 completada

- Creación de la carpeta .opencode/commands/ con 6 comandos en inglés kebab-case: cv-review, linkedin-review, interview-technical, interview-behavioral, interview-live-coding y log-progress.
- cv-review encadena ats-checker y cv-optimizer en dos pasos con confirmación entre ellos, ejecutado por build.
- Los tres comandos de entrevista se ejecutan directamente con su coach (subtask false) para permitir conversación interactiva.
- log-progress delega el apunte en tracker-doc, añade entrada al CHANGELOG y solo toca PLAN.md con confirmación de la persona.
- Migración de directrices globales de .opencode/rules.md a AGENTS.md en la raíz: opencode solo carga AGENTS.md o lo listado en instructions de opencode.json, así que rules.md no se estaba aplicando.
- Actualizadas las referencias a rules.md en PLAN.md, docs/referencia-agentes-mcps.md y course-exercise-solver.
- Añadida a docs/referencia-agentes-mcps.md la sección de comandos y actualizado el recuento a 15 agentes, 8 MCPs y 6 comandos.

## 2026-10-17 - Fase 20 completada

- Fijado el Memory MCP en docs/memoria/memoria.local.json mediante MEMORY_FILE_PATH, fuera de git y antes en la caché de npx.
- Creación de docs/memoria/ con estado-actual.md (foto viva) y decisiones.md (registro de decisiones con motivo y alternativas descartadas).
- Creación de 3 skills en .opencode/skills/: flujo-candidatura, apunte-ejercicio y memoria-sesion.
- AGENTS.md incorpora la sección de memoria: leer estado-actual y decisiones al iniciar sesión y actualizarlos al cerrar hitos.
- Ampliado el comando log-progress para actualizar la memoria del proyecto antes del CHANGELOG.
- Actualizada docs/referencia-agentes-mcps.md con la sección de skills, la memoria del proyecto y el recuento a 15 agentes, 8 MCPs, 6 comandos y 3 skills.
- Pendiente tras el reinicio: el grafo de memoria arranca vacío en la nueva ruta y se puede sembrar con los hitos de las fases anteriores.

## 2026-10-18 - Fase 21 completada

- Instalado gh CLI 2.102.0 con winget y autenticado con `gh auth login --with-token` usando el PAT de .env; scopes confirmados: gist, project, read:org, repo y workflow.
- Creado el repositorio público edu84gp/ai-job-search-copilot (entonces job-support-portfolio) con push inicial de 43 ficheros y topics orientados a reclutadores.
- Ampliado .gitignore para el repo público: cv/* salvo su README, contactos de networking, registro de negociaciones, base SQLite y .env fuera; la tabla de candidaturas se publica como evidencia.
- README reescrito en bilingüe orientado a reclutadores: badges de calidad y estado, stack, proyectos con demos, pipeline de candidatura y tabla de evidencias.
- Creado .github/workflows/quality.yml con lint de Markdown (markdownlint-cli2, globs `**/*.md`) y verificación de enlaces (lychee); workflow en verde tras corregir separadores de tablas y MD037.
- Configuración del lint en .markdownlint-cli2.jsonc con reglas desactivadas por estilo del proyecto y exclusiones de node_modules y prompts de .opencode; .lycheeignore excluye LinkedIn y el endpoint MCP de context7.
- Añadido .github/workflows/deploy-pages.yml a pokedex_web y el-juego-de-la-vida con checkout@v6, configure-pages@v5, upload-pages-artifact@v3 y deploy-pages@v5; Pages activado vía API con build_type workflow y demos respondiendo 200.
- Configuradas descripciones y homepage de ambos repos de proyectos con las URLs de las demos.
- Creado el Project público "Candidaturas Employment Workshop 2026" (#3) con campo Pipeline (Aplicada, En seguimiento, Entrevista tecnica, Entrevista final, Oferta, Descartada) y vinculado al repositorio.
- Creado docs/apuntes/README.md para que la carpeta exista en el repo y los enlaces relativos resuelvan.
- Documentación en docs/referencia-agentes-mcps.md, actualización de PLAN.md y de docs/memoria/.

## 2026-10-18 - Corrección del Memory MCP

- Detectado al sembrar el grafo que una ruta relativa en MEMORY_FILE_PATH falla con ENOENT: el servidor del MCP resuelve la ruta contra su propio directorio de trabajo, la caché de npx.
- Solución: ruta absoluta C:\Users\edu_g\ai-job-search-copilot\docs\memoria\memoria.local.json (carpeta local renombrada el 2026-10-19) en opencode.json y en .opencode/mcp.json, y exclusión docs/memoria/*.lock en .gitignore.
- Pendiente tras reiniciar opencode: sembrar el grafo con los hitos de las fases 0 a 21.

## 2026-10-19 - Grafo de memoria sembrado

- Sembrado el grafo del Memory MCP con los hitos de las fases 0 a 21: 5 entidades (Employment Workshop 2026, ai-job-search-copilot, Ecosistema IA opencode, Kanban candidaturas y Fase 21 visibilidad GitHub) y 5 relaciones.
- Detectada una segunda causa raíz: el servidor v2.0.0 carga el fichero en formato JSON Lines, con un registro JSON completo por línea; la siembra previa como objeto JSON único se ignoraba y el grafo arrancaba vacío. Reescrito el fichero con 10 líneas válidas.
- Terminados los procesos server-memory huérfanos con el entorno antiguo que impedían la recarga tras los reinicios; el servidor se validó arrancándolo contra el fichero y carga las 5 entidades y 5 relaciones.

## 2026-10-19 - Fase 22 completada: validación final

- Auditoría completa del ecosistema: frontmatter y permisos de los 15 agentes conformes a la matriz documentada, handshakes funcionales de los 8 MCPs, 6 comandos y 3 skills verificados, recuentos y URLs coherentes y CI en verde.
- Correcciones durante la auditoría: interview-coach sin `webfetch: deny` (única desviación del estándar de los 15 agentes) y `.playwright-mcp/` añadido a .gitignore por los artefactos del MCP playwright.
- Pase del agente github-portfolio-reviewer sobre el estado público: veredicto apto con reservas (3.0/5). Hallazgos principales: repo insignia sin fijar, falta guía de reproducción y evidencia real, CTA roto en pokedex_web, README de el-juego-de-la-vida mejorable, 0 topics en los proyectos y sin LICENSE.
- Correcciones aplicadas en GitHub: LICENSE MIT en los tres repositorios, topics en pokedex_web y el-juego-de-la-vida, descripciones con tildes y CTA y URL de clon corregidos en pokedex_web.
- Creado templates/README.md para que la carpeta mencionada en el README exista en el repositorio público.
- Plan cerrado: 22 de 22 fases. Pendientes anotados en estado-actual.md: fijar repo insignia, guía de reproducción, evidencia real, vista Board, README del juego, favicon y caso Aplika.

## 2026-10-19 - Renombrado a ai-job-search-copilot

- Renombrado el repositorio en GitHub de job-support-portfolio a ai-job-search-copilot con `gh repo rename`; la URL antigua redirige con 301 y el remoto local queda actualizado.
- Actualizadas las referencias en README (badges), PLAN, estado-actual, referencia técnica, decisiones y entradas históricas del CHANGELOG; nueva decisión con motivo y alternativas descartadas.
- Carpeta local renombrada a C:\Users\edu_g\ai-job-search-copilot con MEMORY_FILE_PATH actualizado en opencode.json y .opencode/mcp.json; el grafo de memoria renombra la entidad y mantiene sus relaciones.
