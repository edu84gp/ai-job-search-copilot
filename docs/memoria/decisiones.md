# Registro de decisiones

Cada decisión se anota con fecha, decisión tomada, motivo y alternativas descartadas.

## 2026-10-15 - Nombres de agentes en inglés y documentación en español

- Decisión: agentes en inglés kebab-case (cv-optimizer, application-tracker) y documentación en español.
- Motivo: los nombres técnicos en inglés son estándar en el ecosistema y la documentación en español favorece la lectura propia.
- Descartado: nombres de agentes en español.

## 2026-10-16 - MCPs con deny global y allow por agente

- Decisión: los MCPs de valor añadido quedan en `deny` global y se habilitan por agente con el bloque `permission`.
- Motivo: ahorro de contexto y mínimo privilegio. El permiso en `deny` deshabilita la herramienta en el resto de agentes.
- Descartado: allow global para todos los MCPs.

## 2026-10-16 - SQLite como fuente única de candidaturas

- Decisión: base SQLite en `docs/candidaturas/candidaturas.db` como fuente única, con la tabla Markdown regenerada desde ella.
- Motivo: consultas e histórico sin duplicar escritura manual y con la vista pública intacta.
- Descartado: mantener el Markdown como fuente principal.

## 2026-10-17 - Directrices globales en AGENTS.md

- Decisión: mover `.opencode/rules.md` a `AGENTS.md` en la raíz.
- Motivo: opencode solo carga automáticamente `AGENTS.md` o lo listado en `instructions`; `rules.md` no se estaba aplicando.
- Descartado: conectar `rules.md` mediante `instructions`.

## 2026-10-17 - Comandos en inglés y uno por coach de entrevista

- Decisión: 6 comandos en inglés kebab-case, tres de ellos de entrevista separados por coach.
- Motivo: coherencia con los nombres de los agentes y acceso directo a cada tipo de práctica.
- Descartado: mezcla de inglés y español del plan original, y un único comando de entrevista con argumento.

## 2026-10-17 - Memoria con MCP y resumen versionado

- Decisión: Memory MCP apuntando a `docs/memoria/memoria.local.json` más `docs/memoria/estado-actual.md` y `docs/memoria/decisiones.md` versionados.
- Motivo: el grafo da consultas rápidas a los agentes y el markdown da visibilidad en el repositorio y portabilidad.
- Descartado: solo markdown o solo MCP.

## 2026-10-17 - Skills acotados a tres flujos

- Decisión: crear los skills flujo-candidatura, apunte-ejercicio y memoria-sesion.
- Motivo: cubren los tres flujos repetitivos reales sin duplicar lo que ya hacen los agentes o `AGENTS.md`.
- Descartado: skills de convenciones y de revisión de portfolio por solapar con `AGENTS.md` y github-portfolio-reviewer.

## 2026-10-18 - Repositorio público con exclusiones de privacidad

- Decisión: publicar `ai-job-search-copilot` (entonces job-support-portfolio) como repo público excluyendo `cv/*` (salvo su README), `docs/networking/contactos-networking.md`, `docs/negociacion/registro-negociaciones.md`, `docs/memoria/*.local.json`, `docs/candidaturas/*.db` y `.env`; la tabla de candidaturas sí se publica como evidencia.
- Motivo: el repositorio funciona como portfolio ante reclutadores y a la vez protege datos personales y contactos.
- Descartado: repositorio privado (pierde su función de portfolio) y publicación sin exclusiones.

## 2026-10-18 - Calidad automatizada con markdownlint y lychee

- Decisión: workflow `Calidad` en `.github/workflows/quality.yml` con lint de Markdown (markdownlint-cli2) y verificación de enlaces (lychee) en push, pull request y manual.
- Motivo: la documentación es el producto del repositorio; el CI evita enlaces roto y formato inconsistente sin depender de revisión manual.
- Descartado: lint solo en local y pre-commit hooks (el repo no es un paquete Node).

## 2026-10-18 - Pages por workflow en cada proyecto estático

- Decisión: añadir `deploy-pages.yml` a pokedex_web y el-juego-de-la-vida y activar Pages por API con `build_type=workflow`; WhatsChatGPT queda documentado como pendiente por requerir servidor con Ollama.
- Motivo: despliegue reproducible y versionado por repo, sin ramas fantasma.
- Descartado: publicar desde rama `gh-pages` y un Pages único con submódulos.

## 2026-10-18 - Kanban en Projects v2 con campo Pipeline propio

- Decisión: Project público con campo single-select `Pipeline` (Aplicada, En seguimiento, Entrevista tecnica, Entrevista final, Oferta, Descartada) además del Status por defecto, vinculado al repositorio.
- Motivo: el campo propio refleja el pipeline real de candidaturas y se crea por gh CLI; las opciones del Status por defecto requieren GraphQL para editarse.
- Descartado: reutilizar Status por defecto con opciones genéricas.

## 2026-10-19 - Licencia MIT única en los tres repositorios públicos

- Decisión: licencia MIT en ai-job-search-copilot, pokedex_web y el-juego-de-la-vida.
- Motivo: una única licencia permisiva y conocida por reclutadores; MIT es válida tanto para código como para la documentación técnica del repositorio principal.
- Descartado: CC BY 4.0 solo para la documentación del repo principal por añadir complejidad sin beneficio claro.

## 2026-10-19 - Renombrado del repositorio a ai-job-search-copilot

- Decisión: renombrar job-support-portfolio a ai-job-search-copilot en GitHub y renombrar la carpeta local a ai-job-search-copilot, actualizando MEMORY_FILE_PATH.
- Motivo: el nombre anterior era genérico y ambiguo ("job-support" se lee como soporte técnico); el nuevo comunica de un vistazo IA y búsqueda de empleo en la lista de repositorios fijados, que es lo primero que ve un reclutador.
- Descartado: mantener job-support-portfolio, ai-job-search-system (sobrio pero menos memorable), ai-career-copilot (más vago) y ai-job-search-agents (menos claro para perfiles no técnicos). GitHub mantiene redirect 301 de la URL antigua.

## 2026-10-20 - Prioridad al Employment Workshop y pausa de DevOps

- Decisión: pausar el Máster DevOps & Cloud y dedicar 2 h 30 min diarias al Employment Workshop, 1 h a búsqueda y portfolio y 30 min a inglés, con un total medio de 4 h/día.
- Motivo: el curso es la vía principal de inserción, el máster no caduca y compaginarlo ahora elevaría el riesgo de sobrecarga.
- Descartado: iniciar DevOps en paralelo, ampliar a 5-6 h/día y sustituir horas de curso por cursos técnicos.

## 2026-10-20 - CV ATS de una página y perfiles en español

- Decisión: usar un CV base de una página, una columna y sin elementos gráficos; mantener GitHub y LinkedIn en español y construir english-coach después de la base de CV, GitHub y LinkedIn.
- Motivo: el CV debe superar filtros ATS y el mercado español es el más accesible con el nivel actual de inglés; el proyecto de inglés aporta más valor cuando la base profesional ya está lista.
- Descartado: CV de tres páginas con columnas, publicar los perfiles en inglés ahora y empezar english-coach antes de las candidaturas.

## 2026-10-21 - Inglés B1 acreditado con EF SET

- Decisión: reflejar el nivel B1 de EF SET en el CV y en los perfiles profesionales.
- Motivo: sustituye la autoevaluación por una certificación verificable y evita afirmaciones no respaldadas.
- Descartado: mantener "Inglés intermedio" sin certificación.

## 2026-10-21 - Repositorio de perfil mínimo, sin repo local

- Decisión: el repositorio `edu84gp/edu84gp` contendrá únicamente `README.md`; el borrador editable vivirá en `docs/privado/readme-perfil-github.md` y se publicará directamente en GitHub sin crear un repositorio local.
- Motivo: evita un repositorio anidado dentro de `ai-job-search-copilot`, mantiene la fuente privada y reduce el mantenimiento a un solo archivo.
- Descartado: crear una carpeta local `edu84gp` con `git init`, `.gitignore`, `AGENTS.md` y `assets/`, y publicar un CV PDF o código en el repo de perfil.

## 2026-10-22 - Caso de estudio público de Aplika y límite de acceso read-only

- Decisión: publicar `aplika-jobs-case-study` como repositorio público con documentación, capturas y fragmentos seleccionados; mantener `Aplika-Jobs` privado y no prometer acceso de solo lectura a ese repositorio privado.
- Motivo: GitHub solo permite conceder escritura a colaboradores en repositorios privados de cuentas personales; el caso de estudio demuestra la aportación sin exponer el código ni obligar a transferir el repositorio.
- Alternativas descartadas: añadir colaboradores con escritura, transferir el repositorio a una organización solo para asignar lectura y publicar el código completo.
- Plan: `docs/privado/plan-caso-estudio-aplika.md`.

## 2026-10-23 - LinkedIn completo con banner propio y certificación única

- Decisión: cerrar LinkedIn con 4 proyectos, 28 aptitudes, 3 publicaciones en Destacado, una única certificación EF SET, inglés B1 como `Competencia básica limitada`, Open to Work y un banner propio; mantener los enlaces de GitHub fuera de Destacados por el fallo de vista previa y usar publicaciones.
- Motivo: el perfil queda coherente con el CV y el README, evita duplicados y keywords sin respaldo, y el banner genera una portada profesional sin depender de una imagen externa.
- Alternativas descartadas: mantener el banner por defecto, etiquetar el B1 como `Competencia profesional completa`, dejar dos certificaciones EF SET duplicadas y forzar el enlace de GitHub en Destacados con la vista previa rota.

## 2026-10-24 - Caso de estudio público, licencia restrictiva y CV regenerado con Word

- Decisión: publicar `aplika-jobs-case-study` como repositorio independiente con `LICENSE` restrictiva y `NOTICE.md` que separa la documentación de la titularidad compartida del producto; enlazarlo desde el README del perfil, el CV y la descripción del proyecto en LinkedIn.
- Motivo: demuestra la aportación real sin exponer código, secretos ni datos, y deja claro que el producto es de autoría compartida.
- Alternativas descartadas: enlazar el repositorio privado, usar licencia permisiva sobre documentación de un producto compartido y esperar a tener toolchain de Markdown a PDF.
- Regeneración del CV: ante la ausencia de pandoc, xelatex, Python y LibreOffice, se editó el DOCX con automatización de Word (`Word.Application` COM) y se exportó el PDF; verificado en una página, con el enlace `Caso de estudio` sustituyendo al de la empresa.
- LinkedIn: la vista previa de enlaces de GitHub falla en el multimedia del proyecto y bloquea el guardado, así que la URL se mantiene como texto en la descripción.
- Fijados de GitHub: el 2026-10-24 se fijó `aplika-jobs-case-study` y se retiró `el-juego-de-la-vida`; el orden final es `ai-job-search-copilot`, `aplika-jobs-case-study` y `pokedex_web`. No existe mutación pública de GraphQL ni endpoint REST para los fijados: hay que hacerlo desde la UI con sesión iniciada.

## 2026-10-24 - Correcciones del Juego de la Vida y patrón aleatorio

- Decisión: completar las correcciones de `el-juego-de-la-vida` con tablero inicial vacío, patrón aleatorio de entre el 10 % y el 50 %, generación solo por clic, intervalo único, controles con estado y anuncios accesibles.
- Motivo: Enter regeneraba el tablero y borraba el patrón dibujado, no había protección frente a intervalos duplicados y la accesibilidad del formulario y del estado era incompleta.
- Alternativas descartadas: conservar Enter como atajo de generación (destruía el patrón), mantener `type="submit"` con validación adicional (seguía exponiendo el borrado accidental), añadir dependencias o bundler (el despliegue publica archivos estáticos) y generar el patrón aleatorio automáticamente al cargar (el tablero debe arrancar vacío). Para el patrón aleatorio se descartó sortear la densidad y dejar cada célula al azar porque el total podía salirse del 10–50 %; se fija un número exacto de celdas vivas y se colocan en posiciones aleatorias.
- Verificación: Playwright en local y en la demo publicada (76 comprobaciones, 0 fallos), W3C sin errores, markdownlint sin incidencias y run de Pages `40100958847` en verde.

## 2026-10-24 - Archivar repositorios de bajo valor

- Decisión: archivar, sin borrar, `axios`, `WhatsChat`, `pokeapi` y `tarjeta_presentacion` con `gh repo archive`; mantener públicos `WhatsChatGPT`, `pokedex_web`, `el-juego-de-la-vida`, `aplika-jobs-case-study`, `ai-job-search-copilot` y `edu84gp`.
- Motivo: los cuatro son ejercicios de bajo valor para un reclutador y restaban foco a los tres fijados; no tenían estrellas ni forks y la operación es reversible con `gh repo unarchive`.
- Alternativas descartadas: borrarlos (pierde historial y no es reversible), hacerlos privados (sigue sin aportar al portfolio) y dejarlos públicos (ruido en el perfil).
- Verificación: `gh repo view --json isArchived` devuelve `true` en los cuatro el 2026-10-24. `tarjeta_presentacion` conserva su demo en Vercel, no referenciada desde el perfil ni el CV.

## 2026-10-24 - Externalizar MEMORY_FILE_PATH

- Decisión: sustituir la ruta absoluta de Windows en `opencode.json` por `{env:MEMORY_FILE_PATH}` y en `.opencode/mcp.json` por el marcador `USAR_VARIABLE_DE_ENTORNO_MEMORY_FILE_PATH`; documentar la variable en `.env.example` y cargarla desde `.env` no versionado.
- Motivo: el repositorio público no debe publicar rutas locales con el nombre de usuario; la ruta sigue siendo obligatoria y absoluta porque el servidor de memoria resuelve las relativas contra la caché de npx.
- Alternativas descartadas: mantener la ruta absoluta versionada (expone el entorno local), usar una ruta relativa (falla con ENOENT) y hardcodear la ruta en el marcador legacy (vuelve a exponerla).
- Verificación: los dos JSON son válidos; la búsqueda de rutas locales de Windows en archivos versionados no devuelve resultados; una instancia aislada del servidor con `MEMORY_FILE_PATH` lee 11 entidades y 17 relaciones. La sesión de opencode requiere reinicio para cargar la variable.
