# CHANGELOG de progreso

Historial de fases del plan definido en `PLAN.md`.

## 2026-11-06 - Segundo título superior en el CV y post de presentación listo

- Añadido a Formación el título de **Técnico Superior Deportivo en Equitación (2008)**, que solo estaba en el CV original. El CV queda con los dos grados superiores y sigue en una página; DOCX y PDF regenerados.
- Añadido a Educación de LinkedIn el mismo título, en el **Centro Ecuestre de Castilla y León** (Segovia), con solo el año 2008 porque no se recuerda la fecha de inicio. La sección queda con cuatro entradas y los dos grados superiores visibles.
- Redactado el post de presentación del examen 7.5 a partir del pitch de la 6.3, con el gancho de los tres oficios. La versión final la escribió la persona y se cerró en 1.148 caracteres, 92,9 PASS en `li-human`.
- El CV y el post dicen lo mismo sobre la formación: dos grados superiores, uno de ellos Deporte Ecuestre.
- **Publicado el post de presentación del examen 7.5** (2026-11-06, 1.123 caracteres, 92,9 PASS) en `https://www.linkedin.com/feed/update/urn:li:activity:7524393292369702912/`, con el primer comentario de portfolio y GitHub. Registrado en `docs/privado/linkedin/log.md`.
- Detectado al terminar la publicación que el titular del perfil había quedado como «Instalador electrotécnico en prácticas en Enerpal». Restaurado a «Junior Full-Stack Developer | React · Node.js · PostgreSQL | IA aplicada | Remoto/híbrido» y verificado en el perfil público.

## 2026-11-05 - Prácticas de 2006 en Telefónica y Enerpal

- Añadidas a LinkedIn las dos prácticas FCT del ciclo superior de Instalaciones Electrotécnicas, en el tercer trimestre del segundo curso: Telefónica de marzo a abril y Enerpal de mayo a junio de 2006, con 190 horas cada una. Se corrigieron las fechas para que no se solapen: la persona estuvo mes y medio en cada empresa, primero en Telefónica y después en Enerpal.
- El CV ya incluía el bloque «Prácticas de instalación electrotécnica — Telefónica y Enerpal (2006)»; se regeneraron DOCX y PDF y se verificó que sigue en una página.
- Se eliminaron dos entradas duplicadas creadas en paralelo durante la misma sesión. La sección de experiencia queda con ocho entradas: seis de la vida laboral, Paher y las dos prácticas.
- Yeguada Tierra Íbera (2005-2014) se descarta: el trabajo era del hermano, sin contrato y solo como colaboración. Solo aparece en el CV original sin optimizar; no está en el CV actual ni en LinkedIn.

## 2026-11-04 - Unidad 7: perfil de LinkedIn con experiencia real

- La 7.2 se aplicó sobre el perfil: titular «Junior Full-Stack Developer | React · Node.js · PostgreSQL | IA aplicada | Remoto/híbrido», extracto nuevo en cuatro párrafos con portfolio, GitHub y enlaces (94,3 PASS en `li-human`) y aptitudes destacadas JavaScript, Node.js y React.js.
- Se creó la sección Experiencia con seis entradas y las fechas de la vida laboral: VIÑA MAGNA SL, con Vinoteca CopaBoca en la descripción (ago. 2025 – jul. 2026); Cerealto, con el contrato a través de Randstad ETT (sept. 2022 – jul. 2025); Transportes y Mudanzas Buj, S.L. (mar. 2021 – ago. 2022); Logística de Transportes Raptor, S.L.U. (oct. 2020 – ene. 2021); Almacén de Recambios Paher, S.A. como prácticas no remuneradas (2022); e Hípica Paraíso (sept. 1998 – oct. 2020).
- Criterios: la razón social se usa cuando es quien contrata y el nombre comercial se explica en la descripción; la hípica va como una sola entrada porque los cinco cambios de situación contractual fueron el mismo puesto; Paher se publica sin mes porque no se conoce.
- Gráfica Impresiones se eliminó de LinkedIn y del CV: era una colaboración con un amigo que no llegó a cuajar. El DOCX se regeneró con `scripts/build-cv-docx.py` y el PDF con Chrome headless, porque Word COM se cuelga al exportar; queda en una página, con texto extraíble y sin la palabra «Gráfica».
- Hípica Paraíso no tiene página de empresa en LinkedIn: `/company/39804018/` corresponde a VIÑA MAGNA SL, así que la entrada queda como organización de texto libre.
- Corregida la ficha del Copilot en Proyectos: pasa de 8 MCP, 6 comandos y 3 skills a 10 servidores MCP, 20 comandos y 14 skills. El extracto ya decía 10 MCP. Se dejaron de seguir los cuatro juegos de LinkedIn (Queens, Tango, Mini Sudoku y Patches) que aparecían como empresas seguidas en Intereses.
- Pendiente para cerrar la 7.5: pedir recomendaciones, publicar el post de presentación y enviar cinco mensajes de conexión. La publicación del 2026-11-02 menciona 19 comandos; se deja tal cual porque ya está publicada.

## 2026-11-04 - Portfolio: fase 1 publicada y tarjeta social validada

- La fase 1 se publicó en https://edu84gp.github.io/ con HTML, CSS y JavaScript sin build: cabecera fija, tema de tres estados, ajustes responsive y cuatro fichas de proyecto.
- Lighthouse en vivo: 100 en rendimiento, accesibilidad, buenas prácticas, SEO y navegación agéntica, en móvil y escritorio; LCP 1,1 s y 0,4 s; CLS 0; TBT 0 ms. HTML, CSS, JavaScript, tarjeta, robots y sitemap responden 200; `README.md`, `docs/` y `_working/` responden 404 por `_config.yml`.
- Post Inspector de LinkedIn: título, descripción, imagen y URL canónica correctos. Author y Publish date quedan vacíos por ser un sitio y no un artículo.
- La tarjeta social se simplificó a `og-image-2026-11.png` (33 KB) para que el rol y el stack se lean a tamaño de feed. El nombre versionado invalida la caché de LinkedIn, que seguía sirviendo la imagen anterior, y el re-scrape ya muestra la tarjeta nueva.
- Se añadieron `og:image:type` y `twitter:image:alt`. Los validadores de X y Facebook exigen sesión; se comprobó que `Twitterbot`, `facebookexternalhit` y `LinkedInBot` reciben las nueve etiquetas sociales y la imagen como `image/png`.
- El trabajo técnico del 5.7 queda cerrado; la entrega del examen en la plataforma corresponde a la persona.

## 2026-11-02 - Portfolio: fase 0 cerrada y repositorio publicado

- Fase 0 del portfolio ejecutada con el material de origen: cuatro fichas de proyecto, enlaces comprobados, sistema visual y capturas. La carpeta de trabajo es `C:\Users\edu_g\portfolio`, fuera del repositorio del copilot.
- Repositorio público creado en https://github.com/edu84gp/edu84gp.github.io con `main` como rama por defecto y tres commits. GitHub Pages se activó solo desde `main` y la raíz, con HTTPS forzado.
- Decisiones: cuatro proyectos (Aplika, Copilot, Pokédex y El Juego de la Vida), tema automático claro y oscuro sin selector, acento azul `#2563eb` y `#60a5fa`, sin PDF del CV y foto de LinkedIn recortada a 120 px.
- Aplika se representa con el panel del caso de estudio y datos ficticios, no con la landing. Copilot se representa con un diagrama SVG, no con una captura de terminal.
- GitHub no permite despublicar un sitio de usuario. Hasta la fase 1, la raíz publica el `README.md` y `docs/` se sirve en crudo; se deja así por decisión de la persona.
- Estructura del repositorio: `assets/img/` con las imágenes que se publicarán, `docs/` con la documentación interna y `_working/` excluida por `.gitignore`.

## 2026-11-02 - Lección 4.7: perfil reescrito y CV validado con Jobscan

- La 4.7 pedía dos cosas: un perfil profesional de 3–4 líneas y dos escaneos del CV con Jobscan. El texto entregado responde quién soy, herramientas, problema que resuelvo y empleo buscado, y coincide con el apartado «Perfil» del CV.
- Primer escaneo contra Miravila Projects (Alcúdia): 78 %. Faltaba el título exacto «Full Stack» y WordPress en habilidades. Se cambió el titular a «Desarrollador Full Stack Junior», se reescribió el perfil y se añadió WordPress (Divi), los tres respaldados por la experiencia en Gráfica Impresiones. Segundo escaneo: 87 % y un aviso menos de hard skills.
- Segundo escaneo contra Verdnatura Levante (Algemesí): 73 %. Los huecos son Vue, Docker, Kubernetes, Linux, MySQL y Java; ninguno tiene evidencia, así que no se añaden y quedan anotados como formación pendiente.
- Descartados los avisos de Jobscan que no aplican a un CV español: encabezados «Education» y «Work History» y fechas MM/AAAA. El CV usa «Formación» y «Experiencia profesional» y rangos de año porque no se conocen los meses exactos.
- CV regenerado en DOCX y PDF, una página y veredicto APTO con `scripts/verify-cv-pdf.py`. Examen entregado y lección completada; el registro está en `docs/ejercicios/tema-4-7-actividades-practicas.md`.
- Leída la 4.8, conclusión de la unidad: el CV debe ser legible por ATS, relevante y medible, y debe demostrar adecuación al puesto con evidencia. Cierra la unidad 4.

## 2026-11-02 - Perfil cerrado y `main` sincronizado con `dev`

- El Juego de la Vida queda fijado como quinto repositorio del perfil, junto a AI Job Search Copilot, el caso de estudio de Aplika, Pokédex Web y WhatsChatGPT. Los fijados ya cubren el trabajo seleccionado del README.
- `main` recibe el fast-forward de `dev` hasta `3138553` con los diez commits acumulados: reescritura del CV, cierre de la unidad 3, unidad 4, agentes alineados, comando `/leccion` y memoria. La CI de calidad pasa en verde (run `41489110331`).
- `dev` se publica en `origin` para que la rama de trabajo y la estable queden alineadas. El README del repositorio insignia ya muestra 20 comandos, igual que el perfil y el CV.

## 2026-11-02 - Lección 4.6: CV, portfolio y LinkedIn alineados sin duplicarse

- La lección separa tres funciones: el CV supera el primer filtro, el portfolio demuestra cómo trabajas y LinkedIn construye reputación y exposición continua. Todos deben estar alineados, pero no duplicarse.
- Añadida esa distinción a `github-portfolio-reviewer` y `linkedin-optimizer`: si el README del perfil o el extracto replican el CV sección por sección, deben señalarlo y proponer un enfoque complementario.
- Corregida una incoherencia detectada por la propia lección: el README público de `edu84gp/edu84gp` seguía diciendo «15 agentes, 8 servidores MCP, 6 comandos y 3 skills» y fechaba la última actualización en octubre. Actualizado a 15 agentes, 10 MCPs, 20 comandos y 14 skills en el repositorio público (commit `6fa8c55`) y en el borrador `docs/privado/readme-perfil-github.md`.
- Observación pendiente: el README del perfil sigue el mismo orden y contenido que el CV. Con la distinción de la 4.6, parte de ese texto debería convertirse en evidencia de código y demo, no en una segunda copia del currículum.
- README del perfil reescrito el 2026-11-02 (commit `b42e173`): pasa de repetir el CV a organizarse por evidencia. Cuatro proyectos con su aportación concreta y enlaces, un bloque «Cómo trabajo» con prácticas verificables (documentación de decisiones, workflow de calidad, permisos de agentes y accesibilidad) y el stack en una tabla. Se añaden WhatsChatGPT y El Juego de la Vida, que no aparecían; Pokédex Web pasa a «Otros proyectos». El borrador `docs/privado/readme-perfil-github.md` queda sincronizado.
- Proyectos revisados en el perfil: los cuatro fijados son `ai-job-search-copilot`, `aplika-jobs-case-study`, `pokedex_web` y `WhatsChatGPT`. El Juego de la Vida no está fijado aunque ahora forma parte del trabajo seleccionado. Los repositorios de ejercicios (`axios`, `WhatsChat`, `pokeapi`, `tarjeta_presentacion`) siguen archivados y no se enlazan.

## 2026-11-02 - Lección 4.5: los cinco errores que bloquean un CV en ATS

- `ats-checker` añade dos comprobaciones que la lección 4.5 marca como bloqueantes y que solo estaban implícitas: el formato de entrega debe ser PDF textual o DOCX, nunca imagen o captura, y los encabezados deben ser estándar, sin títulos creativos. El orden de las reglas queda renumerado de 1 a 12.
- Revisado el CV base contra los cinco errores: una columna sin tablas, PDF textual verificado, encabezados tradicionales y versiones adaptadas por oferta. El único punto abierto sigue siendo la cobertura de palabras clave de cada anuncio.

## 2026-11-02 - Agentes alineados con la unidad 4 y comando `/leccion`

- `cv-optimizer` incorpora el vocabulario de referencia del sector de la lección 4.4 (Desarrollo Web e IA) como lista para detectar huecos, no para copiar, y tres reglas nuevas: extracción literal de las palabras clave de la oferta, colocación en experiencia o proyectos con un máximo de tres menciones, y prohibición de añadir tecnologías sin respaldo. Añade el bloque «Mapa de palabras clave» a la salida.
- `cv-optimizer` y `ats-checker` dejan de penalizar el orden de secciones: el ATS lee encabezados, no posiciones, y en perfiles junior con experiencia en otros sectores los proyectos antes de la experiencia se mantienen.
- `ats-checker` separa coincidencia exacta y variante, y penaliza el relleno: más de tres menciones, listas sin uso declarado y términos que solo viven en habilidades.
- Corregido el frontmatter de `ats-checker`: usaba la clave `permissions` con una estructura de `action`, `resource` y `effect` que no existe en el esquema actual. Pasa a `permission` con mapa de patrones, restringiendo `bash` al script de verificación y denegando PDF, edición y MCP. Hasta ahora el agente podía haberse ejecutado sin esas restricciones.
- Nuevo comando `/leccion <número>`: abre la lección, la resume y no la marca como completada. El ecosistema pasa a 15 agentes, 10 MCPs, 20 comandos y 14 skills; los recuentos se actualizaron en README, guía, referencia y CV base.

## 2026-11-02 - IGNIS descarta el proceso y se cierra la candidatura

- Correo de IGNIS el 2026-11-02: no continúan con el proceso de Junior Fullstack Developer (O&M). La candidatura pasa a `descartada` en `docs/candidaturas/candidaturas.db` con el próximo paso «Descartada por IGNIS. Proceso cerrado.», y `docs/candidaturas/tabla-candidaturas.md` se regeneró desde la base.
- Eliminado el CV adaptado `cv/cv-ignis-junior-fullstack-2026-10.md`, `.docx` y `.pdf`. Se conserva la carta en `cv/cartas/` como archivo de lo enviado.
- Eliminada la tarea de seguimiento del 2026-11-04 en la agenda y cerrada la tarea 33 del backlog, que pedía regenerar el CV con los recuentos antiguos. El hueco del 4 de noviembre queda libre para adelantar una candidatura.
- Corregido el dominio de la web de Los Robles: es `carnicerialosrobles.es`. El CV base incorpora que los dos sitios usan WordPress con el tema Divi.

## 2026-11-02 - Experiencia del CV reescrita con datos reales y una página conservada

- Reescrita la sección de experiencia de `cv/cv-base-2026-10.md` y de `cv/cv-ignis-junior-fullstack-2026-10.md` con los datos aportados por el usuario: equipo de 5 personas y catálogo de más de 300 referencias en CopaBoca; 6 a 10 rutas semanales como conductor de tráiler en Buj y Raptor; operación de extrusoras en Siro; prácticas de almacén en Paher con uso puntual de carretilla; dos webs corporativas sobre WordPress en Gráfica Impresiones; y unos 120 alumnos habituales con 4 personas de equipo, 5 en campamentos, en Hípica Paraíso.
- Eliminada la viñeta de habilidades blandas, que no aportaba evidencia, y añadida la viñeta que faltaba a la colaboración web, que era la única experiencia digital fuera de los proyectos.
- Unificados los recuentos del ecosistema en las dos versiones: 15 agentes, 10 MCPs, 19 comandos y 14 skills. El CV base decía 8 MCPs, 6 comandos y 3 skills; el de IGNIS, 9, 17 y 14.
- `scripts/build-cv-docx.py` pasa a 10,5 pt de cuerpo, encabezados de sección a 11,5 pt y espaciados más ajustados. DOCX y PDF regenerados con Word COM en una página y verificados con `scripts/verify-cv-pdf.py`: APTO en ambos, sin imágenes y con texto extraíble.

## 2026-11-02 - Unidad 3 cerrada: objetivo, plan y examen práctico

- Enviado el examen de la 3.9 con el objetivo SMART en el formato de la plataforma y una imagen del plan semanal del 2 al 8 de noviembre. El plan se generó desde la agenda real y se guardó en `docs/privado/agenda/plan-semanal-2026-11-02.png`; el registro está en `docs/ejercicios/tema-3-9-actividades-practicas.md`.
- Leída y marcada la 3.10, conclusión de la unidad. La unidad 3 queda cerrada con el 24 % del curso y las lecciones 3.1 a 3.10 completadas.
- La unidad 4 ya está accesible. La 4.1 es una introducción al CV como herramienta de marketing y filtro ATS; se trabajará sobre el CV ATS existente, no desde cero.

## 2026-11-02 - Revisión semanal 3.7 y cierre de la entrevista de Neoland

- La entrevista con Patricia (redes de Neoland) quedó marcada como realizada el 2026-10-31. Se actualizó la nota de la tarea 3, se regeneraron `hoy.md`, `semana.md`, `agenda.ics` y el bloque de agenda de `estado-actual.md`, y el calendario quedó con 33 eventos.
- Cerrada la revisión semanal 3.7 con los datos de la semana del 26 de octubre al 1 de noviembre: 1 candidatura, 1 entrevista real, 3 publicaciones de LinkedIn, 4 horas de curso, 4 sesiones de inglés y 1 contacto de networking. El registro está en `docs/ejercicios/tema-3-7-revision-semanal.md`.
- Ajustes aprobados: registrar los bloques diarios de la agenda, mantener tres candidaturas semanales y bajar LinkedIn a tres publicaciones. La revisión del viernes 6 de noviembre comprobará el registro diario.
- Añadida a `docs/privado/linkedin/log.md` la ficha del post Teach #5 The List Promise del 2026-10-30, con el texto íntegro y el enlace `urn:li:share:7521955995582021632`. La semana cerró con tres publicaciones: 27, 30 y 31 de octubre.
- La tarea 2 de la agenda, correspondiente a la Story #3, se cerró con fecha 2026-10-31 y ya no aparece en la vista del día.
- Cerrada la revisión mensual de octubre el 2026-11-02 en `docs/privado/revisiones/2026-10-revision-mensual.md`. El mes cierra con 22 de 22 fases del plan, 1 candidatura, 1 entrevista real, 3 publicaciones de LinkedIn y 1 contacto de networking; noviembre mantiene tres candidaturas semanales, 12-15 horas de curso, tres publicaciones y una práctica de entrevista por semana. La tarea 4 de la agenda queda marcada como hecha.
- Pendiente inmediato: continuar el Employment Workshop por la lección 3.8, errores comunes al fijar objetivos, y después la 3.9, actividades prácticas. Preparar la segunda candidatura para el 2026-11-03.

## 2026-10-30 - Agenda diaria con SQLite, ICS y comandos `/hoy` y `/hecho`

- Creada la base privada `docs/privado/agenda/agenda.db` con 36 tareas y 5 recurrencias: los plazos D1-D12 y A1-A6, los hitos de fase, las publicaciones de LinkedIn, la entrevista con Patricia del 31 de octubre, el seguimiento de IGNIS del 4 de noviembre y seis tareas de backlog.
- `scripts/agenda.py` usa solo la biblioteca estándar y expone `init`, `seed`, `sync`, `hoy`, `semana`, `done`, `skip`, `add`, `ics` y `memoria`. La tabla de recurrencias evita duplicar los bloques diarios; `recurrence_done` guarda los hábitos ya hechos.
- Genera `hoy.md`, `semana.md` y `agenda.ics` en la carpeta privada. El calendario incluye todas las tareas pendientes y las cinco recurrencias, con `UID` estable, horas flotantes y aviso de 15 minutos antes solo en las tareas con hora.
- Añadidos los comandos `/hoy` y `/hecho`, la guía `docs/agenda-diaria.md` y el bloque generado entre marcadores en `docs/memoria/estado-actual.md`. La interfaz React queda pospuesta hasta cerrar D2 y D9, según D12.

## 2026-10-28 - Reparación del bloqueo de ats-checker

- Causa del bloqueo: el agente no podía leer el PDF con la herramienta de lectura y se puso a extraer el texto a mano. Leyó el archivo en base64, descubrió que el entorno no tiene `DecompressionStream` y escribió un decodificador DEFLATE propio dentro de Code Mode. El bucle no tenía condición de salida y la llamada nunca devolvía, así que la sesión quedaba «en ejecución» durante horas. Ocurrió dos veces: 2 h 34 min el 2026-10-28 por la mañana y más de 5 h por la tarde.
- Creado `scripts/verify-cv-pdf.py`: verifica el PDF con la biblioteca estándar, decodifica las cadenas CID con los mapas `ToUnicode`, cuenta páginas, fuentes, imágenes y enlaces, conserva los acentos y compara el número de palabras con el Markdown. Tarda unos 150 ms.
- `.opencode/agents/ats-checker.md` migrado a permisos V2: denegación global, lectura y búsqueda permitidas, `shell` limitado al script, y denegados Code Mode, lectura directa de PDF y herramientas del servidor `filesystem`. Añadido `steps: 30` como tope de iteraciones.
- El primer informe del agente corregido señalaba un desfase de 120 palabras y dos fuentes sin `ToUnicode`. Era un artefacto del verificador: no decodificaba las cadenas hexadecimales y la consola de Windows rompía los acentos. Corregido: el PDF y el Markdown coinciden en 512 palabras y no hay códigos sin mapa.

## 2026-10-28 - Primera candidatura real enviada

- Enviada la candidatura a IGNIS (Junior Fullstack Developer, GdD), Madrid, con CV adaptado y carta de presentación.
- CV de una página y 500 palabras; carta de 237 palabras. Se incorporaron el título de Técnico Superior en Instalaciones Electrotécnicas MT/BT y las prácticas FCT de 2006 en Telefónica y Enerpal.
- Python no se incluye porque no se puede defender en entrevista; la carta declara la brecha de gestión de la demanda sin maquillarla.
- Registrada en SQLite (id 1) como aplicada, con seguimiento el 2026-11-04; `docs/candidaturas/tabla-candidaturas.md` regenerada.
- El subagente `ats-checker` se quedó colgado; la verificación ATS se hizo manualmente y se ajustó su definición para priorizar el Markdown sobre el PDF.

## 2026-10-27 - Primera publicación con el sistema completo

- Publicado el post del martes (Proof, gancho #11 Myth Bust) sobre el caso de estudio de Aplika Jobs, con `detalle-oferta.png` adjunta y el enlace en el primer comentario.
- Descartada la cifra «87 de 93» del plan: es la rúbrica interna del taller y no aparece en el repositorio público, así que el lector no puede verificarla. Sustituida por tres datos contables del repositorio: cuatro fragmentos, tres capturas y un NOTICE.
- Creado `docs/privado/linkedin/log.md` con la ficha del post, el texto íntegro, el comentario y la justificación de lo que se dejó fuera.
- El changelog de la API registró siete eventos en tiempo real durante la publicación, entre ellos `ugcPosts CREATE` y `socialActions/comments CREATE`, lo que confirma el archivado automático y permite obtener el URN de la publicación.
- Calendario público actualizado: la fila del 27 de octubre pasa a Publicado con el enlace.

## 2026-10-26 - Evaluación de Aplika Copilot

- Creados `docs/privado/aplika-copilot-posibilidades.md` y `docs/privado/aplika-copilot-propuesta-companero.md` con la evaluación de producto, arquitectura, modelo de datos, esfuerzo, costes, privacidad y propuesta al compañero.
- Recomendación: módulo premium dentro de Aplika centrado en el seguimiento posterior a la candidatura, con la app independiente como alternativa y el caso de estudio como respaldo. No se implementa hasta validar al compañero, 5-10 usuarios beta y tres candidaturas reales.
- Hallazgos del esquema real: `ApplicationStatus` no incluye `REJECTED` ni `WITHDRAWN`; `Application.jobOfferId` es obligatorio, lo que bloquea candidaturas externas. El MVP requiere migración y estados de cierre.
- Verificación: `markdownlint-cli2` sin incidencias en los dos documentos privados.

## 2026-10-26 - Guía de uso y cierre de la preparación de la Fase 1

- Creada `docs/guia-uso-ai-job-search-copilot.md` con `tracker-doc`: modelo de cinco capas, comprobaciones, rutina diaria, pipeline de candidatura, flujos de estudio, entrevistas, LinkedIn y memoria, privacidad, solución de problemas y chuleta. Enlazada desde `README.md` en español e inglés y desde `AGENTS.md`.
- Enlazado el plan de estudios con el plan de LinkedIn en ambos sentidos: columna diaria en la semana tipo, métricas de comentarios y publicaciones, rutina diaria y semana del 26 al 30 de octubre.
- Añadidos 11 topics a `WhatsChatGPT`: `ai`, `chatbot`, `express`, `full-stack`, `javascript`, `llm`, `nodejs`, `ollama`, `realtime`, `socket-io` y `websockets`. Cierra el ítem de Fase 1; el favicon de `pokedex_web` ya estaba desplegado.
- Verificación: `markdownlint-cli2` sin incidencias en los archivos públicos y en el plan privado; recuento de 15 agentes, 9 MCPs, 17 comandos y 14 skills.

## 2026-10-26 - Cliente de la API de portabilidad de LinkedIn

- Escrito `scripts/linkedin-portability.py`, cliente de solo lectura sobre la API DMA de LinkedIn, sin dependencias y con la biblioteca estándar de Python.
- Superficie mínima: dos endpoints de datos (`memberSnapshotData` y `memberChangeLogs`) y uno de control (`memberAuthorizations`), todos con `GET`. El cliente valida el host y el recurso contra una lista cerrada y aborta antes de la red si algo no coincide; verificado con dos intentos rechazados.
- Comandos: `check`, `domains`, `snapshot`, `changelog` y `describe`. El punto de control del changelog se guarda en `state.json` y los datos en `docs/privado/linkedin/api/`, fuera de git. `INBOX`, `SEARCHES`, `PREMIUM_NOTES` y `AD_TARGETING` quedan excluidos del conjunto por defecto.
- Documentado en `docs/marca-personal/linkedin-api-portabilidad.md` y añadido `LINKEDIN_DMA_TOKEN` a `.env.example`. Pendiente el alta en el portal y la primera descarga real.
- Alta completada el mismo día: consentimiento activo a las 13:09 UTC con el scope `DMA` y primera descarga correcta de `PROFILE`, `SKILLS` (28 aptitudes) y `CONNECTIONS` (43 contactos). Los dominios de publicaciones y comentarios seguían en proceso, porque LinkedIn los collaciona de forma progresiva.
- Corregido el tratamiento del 404 `No data found for this domain and memberId`: no es un fallo, es un dominio aún no procesado. El cliente lo marca como pendiente y sigue con los demás en lugar de abortar la tanda.
- Segunda tanda de la exportación recibida el 2026-10-27 en `docs/privado/linkedin/exportaciones/2026-10-26.2`: 38 ficheros, 323 filas normalizadas. Aporta `Shares` (34), `Comments` (38), `Reactions` (71), `InstantReposts` (5), `SearchQueries`, `Logins` y `Security Challenges`, estos últimos excluidos por ser privados.
- Escrito `scripts/linkedin-export-import.py`, que salta el bloque `Notes:` multilínea de los CSV, normaliza a JSON en `_normalizado/` y omite por defecto los ficheros sensibles.
- Cruce de fuentes: `MEMBER_SHARE_INFO` de la API y `Shares.csv` coinciden en 34; `ALL_COMMENTS` y `Comments.csv` coinciden en 38. Queda descartado que la API exponga comentarios ajenos, así que `li-reply` sigue necesitando el hilo pegado a mano.
- La paginación de `ALL_COMMENTS` devolvió 75 filas con 37 duplicados exactos entre páginas. El cliente ahora deduplica por fila completa antes de guardar.

## 2026-10-26 - MCP remoto microsoft-learn

- Añadido el servidor `microsoft-learn` en `opencode.json` con `type remote` y la URL `https://learn.microsoft.com/api/mcp`, sin autenticación ni clave, y replicado en el espejo `.opencode/mcp.json`.
- Verificado el handshake antes de documentarlo: responde 200 en `text/event-stream` con `Microsoft Learn MCP Server` 1.0.0 sobre protocolo `2025-06-18` y expone `microsoft_docs_search`, `microsoft_code_sample_search` y `microsoft_docs_fetch`.
- Motivo: la documentación de las APIs de LinkedIn se publica en `learn.microsoft.com`, que permite acceso automatizado, mientras que `linkedin.com` lo prohíbe en su `robots.txt`. Permite verificar scopes, endpoints y versiones sin abrir el navegador.
- Permiso `microsoft-learn_*` denegado globalmente y habilitado en los agentes primarios `build` y `plan`, igual que el resto de MCPs. Ecosistema actualizado a 9 MCPs.

## 2026-10-25 - Pack LinkedIn auditado e instalado

- Auditado `Jakeschincariol/linkedin-agent-skill` (MIT, commit `add2c23`, 2.618 estrellas): sin red, sin ejecución de procesos, sin dependencias, sin binarios, sin secretos y sin publicación automática.
- Instalados 11 skills `li-*` en `.opencode/skills/` y 11 comandos `li-*.md` en `.opencode/commands/`; OpenCode no convierte skills en comandos, así que cada uno tiene su envoltorio.
- Adaptaciones: `~/.claude/linkedin/` pasa a `docs/privado/linkedin/`, los scripts se ejecutan con `uv run --no-project python` porque Windows no incluye `python3` y el proceso heredó un PATH sin Python, y las referencias internas entre skills sustituyen a los comandos de la TUI.
- Verificado `/li-post` de extremo a extremo: tres ganchos, borrador de 1.102 caracteres y humanizador local. El panel está calibrado para inglés: el control inglés llega a 95,6 PASS y el borrador español queda en 57,2 REVIEW por la señal VOICE.
- Documentación: `docs/marca-personal/linkedin-agent-skill.md`, `docs/referencia-agentes-mcps.md`, `docs/memoria/estado-actual.md` y `docs/memoria/decisiones.md`. Memory MCP actualizado a 12 entidades y 20 relaciones.

## 2026-10-25 - Perfil de voz de LinkedIn desde tres publicaciones

- Construido `docs/privado/linkedin/voice.md` desde el post de los dos meses, el avance del proyecto y el extractor de CV; sustituye al borrador provisional, que describía mal la voz (decía que no había emojis).
- El perfil recoge dos registros (hito personal y anuncio de equipo), tres aperturas, el giro, tres cierres, la estructura, las posiciones, los límites y las pruebas verificables.
- Las tres muestras se guardan íntegras en bloques `text` y una sección separa siete patrones que no se replican (`Aplica Jobs`, `developper`, hashtags dentro de la frase, puntuación acumulada).
- Verificado con `markdownlint-cli2` sin incidencias; el archivo sigue fuera de git por `docs/privado/`.

## 2026-10-25 - Python ya instalado: se corrige la premisa del PATH

- Python 3.14.7 con pip 26.2.1, el lanzador `py` y el componente Add to Path está instalado hoy; no se reinstala para no duplicar intérpretes.
- Los procesos abiertos antes de la instalación heredaron un PATH sin las entradas nuevas, así que `python` no resolvía en la sesión. Tras reiniciar el equipo, `python` y `py` resuelven al intérprete real y `detect.py` devuelve el mismo 57,2 que con `uv`.
- Los scripts del pack siguen con `uv run --no-project python` por reproducibilidad y aislamiento, no porque falte el intérprete. Documentación corregida en la ficha del pack, decisiones y estado.

## 2026-10-25 - Plan semanal de LinkedIn del 26 al 30 de octubre

- Generado `docs/privado/linkedin/plan.md` con cuatro publicaciones: prueba del caso de estudio (martes), opinión sobre las skills como código (miércoles), siete comprobaciones de auditoría (jueves) e historia del commit en rojo (viernes).
- Interacción: cinco cuentas de alcance (NEOLAND, midudev, Brais Moure, Carlos Azaustre y Spain AI), tres pares (Roberto Antonio López, Fernando Martinez y un junior de otro bootcamp de Neoland) y dos de contratación (Neoland Empleo y el reclutador de la primera oferta real). La promoción fue de dos personas, así que el tercer par sale de la comunidad del centro, no de la clase.
- No se abre LinkedIn con Playwright: automatizar la sesión es el comportamiento que el pack desaconseja y puede restringir la cuenta. Los dos huecos de contratación se llenan con ofertas reales.
- Calendario público actualizado con las cuatro filas de la semana en `docs/marca-personal/calendario-contenido.md`. Nada programado ni publicado.

## 2026-10-24 - Descripción y topics de el-juego-de-la-vida

- Descripción vigente: simulador del autómata celular de Conway (B3/S23) con tablero vacío configurable, edición de células, patrón aleatorio del 10 % al 50 % y velocidad ajustable; HTML, CSS y JavaScript sin dependencias.
- Topics verificados: `cellular-automata`, `conway`, `css`, `frontend`, `game-of-life`, `github-pages`, `html`, `javascript`, `accessibility` y `vanilla-javascript`. No hay topic `canvas` porque el render usa DOM.
- Demo con HTTP 200 y README remoto idéntico al local (blob `1379062f`). El plan del perfil queda con un único pendiente externo: la revisión del bootcamp.

## 2026-10-24 - Memory MCP con ruta resuelta por lanzador

- Añadido `scripts/memory-mcp.mjs`, que calcula la ruta absoluta de `docs/memoria/memoria.local.json` desde la raíz del repositorio y arranca `@modelcontextprotocol/server-memory` con `MEMORY_FILE_PATH`.
- `opencode.json` y `.opencode/mcp.json` invocan el lanzador; retirada la clave `MEMORY_FILE_PATH` de `.env` y `.env.example` porque OpenCode V2 no carga `.env`.
- Verificado en la sesión: `read_graph` devuelve 11 entidades y 17 relaciones y una escritura persiste en el grafo del repositorio.

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
- Solución: ruta absoluta del proyecto a `docs/memoria/memoria.local.json` (carpeta local renombrada el 2026-10-19) en opencode.json y en .opencode/mcp.json, y exclusión docs/memoria/*.lock en .gitignore.
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
- Carpeta local renombrada a `ai-job-search-copilot` con MEMORY_FILE_PATH actualizado en opencode.json y .opencode/mcp.json; el grafo de memoria renombra la entidad y mantiene sus relaciones.

## 2026-10-19 - Flecos del renombrado y guía de reproducción

- Corregidas las dos referencias que aún indicaban que la carpeta local se había renombrado "a juego" en docs/referencia-agentes-mcps.md y docs/memoria/decisiones.md.
- Verificado que ai-job-search-copilot ya figura fijado en el perfil de GitHub junto a pokedex_web y el-juego-de-la-vida; retirado de pendientes.
- Añadida al README la guía "Cómo reproducirlo" en español e inglés: requisitos, clonado, .env, ajuste portable de MEMORY_FILE_PATH, creación de la base y del grafo al primer uso y verificación de MCPs y agentes.
- Actualizada docs/memoria/estado-actual.md: pendientes reducidos a evidencia real, vista Board aplazada, README del juego, favicon, caso Aplika, respaldo externo y demo de WhatsChatGPT.

## 2026-10-20 - Plan privado y CV base ATS

- Creado `docs/privado/plan-estudios-2026.md` con el reparto de 4 h/día, fases hasta el 2026-12-14, mapa del Employment Workshop, métricas semanales, plan de inglés y criterios de reinicio de DevOps.
- Añadido `docs/privado/` a `.gitignore`; el plan y el CV no se publican.
- Generado `cv/cv-base-2026-10.md`, `.docx` y `.pdf`: una página, una columna, sin tablas, cuadros de texto, imágenes ni foto; PDF textual de una página verificado con pypdf.
- Revisión del agente `ats-checker`: APTO CON CORRECCIONES; aplicados encabezados estándar, contacto etiquetado, cronología, atribución de Aplika como proyecto en equipo y aclaración de la aportación full-stack.
- Actualizados `docs/memoria/estado-actual.md`, `decisiones.md` y el grafo del Memory MCP con el plan, el CV y las decisiones del 2026-10-20.

## 2026-10-24 - Caso de estudio público de Aplika Jobs

- Publicado https://github.com/edu84gp/aplika-jobs-case-study: README, LICENSE restrictiva, NOTICE.md, arquitectura, decisiones, cuatro fragmentos y dos capturas de la superficie pública; CI Calidad en verde (run 39918208136).
- Enlazado desde el README del perfil edu84gp/edu84gp, el CV base (DOCX y PDF regenerados con Word COM, una página) y la descripción del proyecto Aplika Jobs en LinkedIn.
- Fijados de GitHub: añadido aplika-jobs-case-study y retirado el-juego-de-la-vida; orden final ai-job-search-copilot, aplika-jobs-case-study y pokedex_web.
- Playwright pasa a modo con ventana en opencode.json y .opencode/mcp.json para poder autenticar en la UI; los fijados no se pueden cambiar por REST ni por GraphQL público.
- Limpiados .tmp/aplika-jobs-case-study y las capturas temporales de la raíz tras verificar el push (commit 124f7ed).
- Actualizados docs/memoria/estado-actual.md, decisiones.md y el grafo del Memory MCP.

## 2026-10-24 - Correcciones de README y favicon

- README principal: sustituido el overclaim `Turing-completo` del juego de la vida por las funciones reales del simulador y cambiado el enlace de acceso bajo petición de Aplika Jobs por el caso de estudio público, en español e inglés.
- pokedex_web: añadido `assets/favicon.svg`, enlazado en `index.html` y documentado en el árbol de archivos del README; verificado en la demo desplegada.
- CI en verde en ambos repositorios (runs 40091315369 y 40091295134).

## 2026-10-24 - Cierre del plan del perfil de GitHub

- Archivados sin borrar `axios`, `WhatsChat`, `pokeapi` y `tarjeta_presentacion` (`isArchived: true`); el perfil queda con seis repositorios públicos no archivados.
- Externalizado `MEMORY_FILE_PATH`: `{env:MEMORY_FILE_PATH}` en `opencode.json`, marcador `USAR_VARIABLE_DE_ENTORNO_MEMORY_FILE_PATH` en `.opencode/mcp.json`, plantilla en `.env.example` y ruta real solo en `.env`. Sin rutas locales de Windows en archivos versionados.
- README del perfil: aportación personal en Aplika (API REST con Express y TypeScript, Prisma/PostgreSQL/Supabase, motor de búsqueda y matching, CV ATS, carta y email) y motivo `código privado` unificado; publicado en `7f957b3`.
- Plan `docs/privado/plan-perfil-github.md` reconciliado: 87 casillas cumplidas, evidencia de cierre y dos pendientes externos (revisión del bootcamp y descripción de `el-juego-de-la-vida`).
- Revisión visual con Playwright en 390×844 y 1440×900, tema claro y oscuro: sin scroll horizontal, sin cortes y 21 enlaces visibles.
- Memoria, decisiones y CHANGELOG actualizados; markdownlint sin incidencias y CI verificado en verde tras el push.
