# Estado actual del proyecto

## Foto

- Última actualización: 2026-10-24.
- Fase del plan: Fases 0 a 22 completadas; plan cerrado y validado. Fase 0 de identidad profesional cerrada el 2026-10-23 y ampliada el 2026-10-24 con el caso de estudio público de Aplika Jobs.
- Ecosistema: 15 agentes, 8 MCPs, 6 comandos y 3 skills.
- Repositorio: público en https://github.com/edu84gp/ai-job-search-copilot (renombrado desde job-support-portfolio el 2026-10-19) con CI de calidad (markdownlint y lychee) en verde.
- Kanban público del pipeline de candidaturas: https://github.com/users/edu84gp/projects/3 con campo Pipeline propio.
- Demos desplegadas en GitHub Pages: pokedex_web y el-juego-de-la-vida. WhatsChatGPT pendiente por requerir servidor con Ollama.
- Candidaturas: sin registros todavía. La tabla `candidaturas` se creará al primer registro con application-tracker.
- Memoria: grafo del Memory MCP sembrado el 2026-10-19 con los hitos de las fases 0 a 21 en formato JSON Lines y ampliado el 2026-10-20 con el plan y el CV (8 entidades y 11 relaciones), verificado contra el fichero.
- Post-plan: flecos del renombrado corregidos, guía de reproducción añadida al README en español e inglés y repo insignia fijado en el perfil de GitHub.
- Plan privado de estudios: `docs/privado/plan-estudios-2026.md`, excluido del repo público con `docs/privado/` en `.gitignore`; fija 4 h/día, fases hasta el 2026-12-14, 3 candidaturas semanales y pausa de DevOps.
- CV base ATS: `cv/cv-base-2026-10.md`, `.docx` y `.pdf` (privado), de una página, una columna, sin tablas, cuadros de texto, imágenes ni foto; PDF textual verificado y revisión ATS con correcciones aplicadas. El 2026-10-21 se ajustó a 11 pt, se añadió el nivel de inglés B1 (EF SET, 2026) y se enlazó al certificado https://cert.efset.org/es/dTcq2Q en DOCX, PDF y Markdown.
- Plan del perfil de GitHub: `docs/privado/plan-perfil-github.md` ajustado el 2026-10-21; `edu84gp/edu84gp` contendrá solo `README.md`, el borrador vivirá en `docs/privado/readme-perfil-github.md` y no se creará un repositorio local.
- Perfil de GitHub: `edu84gp/edu84gp` público con únicamente `README.md` desde el 2026-10-22; el README se renderiza en `https://github.com/edu84gp` y el borrador editable sigue en `docs/privado/readme-perfil-github.md`.
- LinkedIn: perfil completo el 2026-10-23. `Acerca de` publicado; titular Junior Full-Stack; URL `https://www.linkedin.com/in/edu84gp/`; Open to Work activo; 4 proyectos (AI Job Search Copilot, Aplika Jobs, Pokédex Web y WhatsChatGPT); 28 aptitudes; 3 publicaciones en Destacado; certificación EF SET única; idioma inglés B1 (`Competencia básica limitada`); banner propio; Educación, Aptitudes, Proyectos, Licencias e Idiomas visibles en el perfil principal. GitHub: bio, ubicación y website ya configurados; 3 repos fijados el 2026-10-24 en este orden (ai-job-search-copilot, aplika-jobs-case-study y pokedex_web); el-juego-de-la-vida se retiró de los fijados.
- Caso de estudio de Aplika Jobs: publicado el 2026-10-24 en https://github.com/edu84gp/aplika-jobs-case-study (público, rama `main`, commit inicial `a2d7fcb`). Contiene README, `LICENSE` restrictiva, `NOTICE.md`, arquitectura, decisiones, cuatro fragmentos y dos capturas de la superficie pública. CI `Calidad` en verde (run `39918208136`). Descripción, homepage `https://aplika-jobs.vercel.app` y topics `ai`, `case-study`, `full-stack`, `nodejs`, `postgresql`, `prisma`, `react`, `typescript`. El código sigue privado en `edu84gp/Aplika-Jobs` y no se enlaza.
- Enlaces al caso de estudio: README del perfil `edu84gp/edu84gp` actualizado (commit `348d808`); proyecto Aplika Jobs de LinkedIn (`1704320950`) con la URL al final de la descripción; CV base con el enlace `Caso de estudio` en la ficha de Aplika Jobs, regenerado en DOCX y PDF con Word COM y verificado en una página.
- Publicación de LinkedIn: el multimedia del proyecto no admite la vista previa de GitHub y bloquea `Guardar`; la URL queda como texto plano en la descripción y no se añadió a Destacados. En la sesión del 2026-10-24 la sección Destacados del perfil no renderiza el bloque de añadir enlace (errores de la interfaz), así que el enlace clicable sigue pendiente.

## Siguiente paso

- Retomar los flecos técnicos de `el-juego-de-la-vida` (tablero inicial, orden de limpieza, Enter, intervalo y accesibilidad), el favicon de `pokedex_web` y la corrección del overclaim `Turing-completo` en el README de `ai-job-search-copilot`.

## Bloqueos

- Ninguno. El grafo del Memory MCP quedó sembrado tras corregir MEMORY_FILE_PATH a ruta absoluta (el servidor resuelve las relativas contra la caché de npx) y reescribir el fichero en formato JSON Lines (el servidor v2.0.0 carga un registro JSON por línea).

## Pendientes anotados

- LinkedIn: mantener actualizado el perfil; no hay sección Experiencia porque los proyectos viven en `Proyectos`. Valorar añadir RAG y Groq/OpenAI si se refuerza el relato de IA.
- Inglés: certificado EF SET B1 (2026) incorporado al CV y a LinkedIn (https://cert.efset.org/es/dTcq2Q); mantener la rutina y valorar el objetivo B2.
- Evidencia real pendiente de avance del curso: apuntes y ejercicios en docs/apuntes y docs/ejercicios, y vídeo corto del sistema y del Kanban.
- Vista Board del Project agrupada por Pipeline, con una candidatura anonimizada de ejemplo; aplazada por decisión del 2026-10-19.
- README de el-juego-de-la-vida reescrito y verificado; quedan correcciones de código y demo (tablero inicial vacío, overclaim `Turing-completo`, limpiar antes de generar, Enter que recarga, intervalo al regenerar y accesibilidad) y favicon ausente en pokedex_web.
- Caso de estudio público de Aplika Jobs: publicado y enlazado desde README de perfil, CV y proyecto de LinkedIn. Queda pendiente fijarlo en GitHub y revisar la presentación de la URL en LinkedIn.
- Acceso al repositorio privado de Aplika: no prometer solo lectura mientras sea un repositorio privado de cuenta personal; GitHub solo permite escritura a colaboradores. Alternativa recomendada: caso de estudio público.
- Evaluación de respaldo externo de candidaturas con Notion o Google Drive, sin implementar. Notion es la opción de menor fricción.
- Demo de WhatsChatGPT sin desplegar: necesita un servidor con Ollama en ejecución.
- English coach: MVP acordado, pendiente de construir después de la Unidad 5 y de las primeras candidaturas.
