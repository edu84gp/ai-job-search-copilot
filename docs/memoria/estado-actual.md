# Estado actual del proyecto

## Foto

- Última actualización: 2026-10-25.
- Fase del plan: Fases 0 a 22 completadas; plan cerrado y validado. Fase 0 de identidad profesional cerrada el 2026-10-23 y ampliada el 2026-10-24 con el caso de estudio público de Aplika Jobs, cerrado en contenido el 2026-10-25 (87/93; las 6 restantes son la Fase 8 de mantenimiento continuo).
- Ecosistema: 15 agentes, 8 MCPs, 6 comandos y 3 skills.
- Repositorio: público en https://github.com/edu84gp/ai-job-search-copilot (renombrado desde job-support-portfolio el 2026-10-19) con CI de calidad (markdownlint y lychee) en verde.
- Kanban público del pipeline de candidaturas: https://github.com/users/edu84gp/projects/3 con campo Pipeline propio.
- Demos desplegadas en GitHub Pages: pokedex_web y el-juego-de-la-vida. WhatsChatGPT pendiente por requerir servidor con Ollama.
- Juego de la vida: correcciones completadas y demo verificada el 2026-10-24 (tablero inicial vacío, patrón aleatorio entre el 10 % y el 50 %, Enter sin borrar el patrón, intervalo único, controles coherentes, anuncios accesibles y README alineado). Run de Pages en verde: https://github.com/edu84gp/el-juego-de-la-vida/actions/runs/40100958847.
- Candidaturas: sin registros todavía. La tabla `candidaturas` se creará al primer registro con application-tracker.
- Memoria: grafo del Memory MCP en formato JSON Lines con 11 entidades y 17 relaciones (verificado el 2026-10-24); `scripts/memory-mcp.mjs` resuelve la ruta absoluta del grafo y arranca el servidor con `MEMORY_FILE_PATH`.
- Post-plan: flecos del renombrado corregidos, guía de reproducción añadida al README en español e inglés y repo insignia fijado en el perfil de GitHub.
- Plan privado de estudios: `docs/privado/plan-estudios-2026.md`, excluido del repo público con `docs/privado/` en `.gitignore`; fija 4 h/día, fases hasta el 2026-12-14, 3 candidaturas semanales y pausa de DevOps.
- CV base ATS: `cv/cv-base-2026-10.md`, `.docx` y `.pdf` (privado), de una página, una columna, sin tablas, cuadros de texto, imágenes ni foto; PDF textual verificado y revisión ATS con correcciones aplicadas. El 2026-10-21 se ajustó a 11 pt, se añadió el nivel de inglés B1 (EF SET, 2026) y se enlazó al certificado https://cert.efset.org/es/dTcq2Q en DOCX, PDF y Markdown.
- Plan del perfil de GitHub: `docs/privado/plan-perfil-github.md` cerrado el 2026-10-24 con 87 casillas cumplidas y un pendiente externo (revisión por una persona del bootcamp). `edu84gp/edu84gp` contiene solo `README.md`, el borrador vive en `docs/privado/readme-perfil-github.md` y no se creó un repositorio local.
- Perfil de GitHub: `edu84gp/edu84gp` público con únicamente `README.md` desde el 2026-10-22; el README se renderiza en `https://github.com/edu84gp` y el borrador editable sigue en `docs/privado/readme-perfil-github.md`. El 2026-10-24 se publicó la aportación personal en Aplika y se unificó el motivo `código privado` (commit `7f957b3`); revisión visual en 390×844 y 1440×900, tema claro y oscuro, sin scroll horizontal ni cortes.
- LinkedIn: perfil completo el 2026-10-23. `Acerca de` publicado; titular Junior Full-Stack; URL `https://www.linkedin.com/in/edu84gp/`; Open to Work activo; 4 proyectos (AI Job Search Copilot, Aplika Jobs, Pokédex Web y WhatsChatGPT); 28 aptitudes; 3 publicaciones en Destacado; certificación EF SET única; idioma inglés B1 (`Competencia básica limitada`); banner propio; Educación, Aptitudes, Proyectos, Licencias e Idiomas visibles en el perfil principal. GitHub: bio, ubicación y website ya configurados; 3 repos fijados el 2026-10-24 en este orden (ai-job-search-copilot, aplika-jobs-case-study y pokedex_web); el-juego-de-la-vida se retiró de los fijados.
- Caso de estudio de Aplika Jobs: publicado el 2026-10-24 y cerrado en contenido el 2026-10-25 en https://github.com/edu84gp/aplika-jobs-case-study (público, rama `main`, commits `d7b25da` y `9dd8156`; HEAD `9dd8156`). Contiene README con TL;DR, `LICENSE` restrictiva, `NOTICE.md`, arquitectura, decisiones, cuatro fragmentos y tres capturas del panel (lista, detalle y flujo) con datos ficticios. La landing y `login.png` se retiraron del repositorio público. CI `Calidad` en verde en el HEAD (run `40137561987`); el commit intermedio `d7b25da` falló porque el README aún referenciaba las imágenes borradas. Plan privado: 87/93 casillas; las 6 restantes son la Fase 8 de mantenimiento continuo. Descripción, homepage `https://aplika-jobs.vercel.app` y topics `ai`, `case-study`, `full-stack`, `nodejs`, `postgresql`, `prisma`, `react`, `typescript`. El código sigue privado en `edu84gp/Aplika-Jobs` y no se enlaza.
- Enlaces al caso de estudio: README del perfil `edu84gp/edu84gp` actualizado (commit `348d808`); proyecto Aplika Jobs de LinkedIn (`1704320950`) con la URL al final de la descripción; CV base con el enlace `Caso de estudio` en la ficha de Aplika Jobs, regenerado en DOCX y PDF con Word COM y verificado en una página.
- Publicación de LinkedIn: el multimedia del proyecto no admite la vista previa de GitHub y bloquea `Guardar`; la URL queda como texto plano en la descripción y no se añadió a Destacados. En la sesión del 2026-10-24 la sección Destacados del perfil no renderiza el bloque de añadir enlace (errores de la interfaz), así que el enlace clicable sigue pendiente.
- Repositorios de proyectos: `pokedex_web` con favicon SVG en `assets/favicon.svg`, enlazado en el HTML y desplegado (2026-10-24); el README principal ya no afirma que el juego sea Turing-completo y enlaza el caso de estudio de Aplika en la tabla de proyectos.
- Repositorios de bajo valor: `axios`, `WhatsChat`, `pokeapi` y `tarjeta_presentacion` archivados el 2026-10-24 (`isArchived: true`), sin borrar historial. `WhatsChatGPT`, `pokedex_web`, `el-juego-de-la-vida`, `aplika-jobs-case-study`, `ai-job-search-copilot` y `edu84gp` siguen públicos.

## Siguiente paso

- Iniciar la primera candidatura real a partir del 2026-10-27 con `flujo-candidatura` y `application-tracker`. El caso de estudio queda cerrado en contenido; solo mantiene la Fase 8 de mantenimiento continuo (primera revisión el 2026-12-25) y la revisión externa del plan del perfil por una persona del bootcamp.

## Bloqueos

- Ninguno funcional. El Memory MCP lee y escribe el grafo del repositorio mediante `scripts/memory-mcp.mjs` desde el 2026-10-24.

## Pendientes anotados

- Plan del perfil de GitHub: pendiente externo la revisión por una persona del bootcamp. La descripción y los topics de `el-juego-de-la-vida` se revisaron el 2026-10-24 (sin topic `canvas`, con `vanilla-javascript` y `accessibility`); el resto del plan quedó cerrado.
- LinkedIn: mantener actualizado el perfil; no hay sección Experiencia porque los proyectos viven en `Proyectos`. Valorar añadir RAG y Groq/OpenAI si se refuerza el relato de IA.
- Inglés: certificado EF SET B1 (2026) incorporado al CV y a LinkedIn (https://cert.efset.org/es/dTcq2Q); mantener la rutina y valorar el objetivo B2.
- Evidencia real pendiente de avance del curso: apuntes y ejercicios en docs/apuntes y docs/ejercicios, y vídeo corto del sistema y del Kanban.
- Vista Board del Project agrupada por Pipeline, con una candidatura anonimizada de ejemplo; aplazada por decisión del 2026-10-19.
- el-juego-de-la-vida: correcciones de código, accesibilidad y README completadas, demo verificada y descripción y topics revisados el 2026-10-24; no quedan pendientes funcionales del plan. El overclaim `Turing-completo` del README principal se sustituyó el 2026-10-24 por las funciones reales del simulador y el favicon de pokedex_web está publicado y enlazado.
- Caso de estudio público de Aplika Jobs: cerrado en contenido el 2026-10-25. Plan privado 87/93; las 6 restantes son la Fase 8 de mantenimiento continuo. La landing con métricas y marcas y `login.png` se retiraron del repositorio; quedan tres capturas del panel. Pendientes vivos: cuenta ficticia de la demo sin eliminar (no se conserva la contraseña), inconsistencia «El candidato»/«Candidata Demo» documentada como limitación y vista previa de la URL en LinkedIn (la plataforma bloquea el guardado).
- Acceso al repositorio privado de Aplika: no prometer solo lectura mientras sea un repositorio privado de cuenta personal; GitHub solo permite escritura a colaboradores. Alternativa recomendada: caso de estudio público.
- Evaluación de respaldo externo de candidaturas con Notion o Google Drive, sin implementar. Notion es la opción de menor fricción.
- Demo de WhatsChatGPT sin desplegar: necesita un servidor con Ollama en ejecución.
- English coach: MVP acordado, pendiente de construir después de la Unidad 5 y de las primeras candidaturas.
