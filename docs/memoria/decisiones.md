# Registro de decisiones

Cada decisión se anota con fecha, decisión tomada, motivo y alternativas descartadas.

## 2026-11-02 - Tres hashtags, emojis con tope y VOICE para el sujeto implícito

- Decisión: fijar tres hashtags como máximo; permitir de dos a cuatro emojis en un post normal y hasta seis en uno narrativo con estados o listas; y añadir a `detect.py` un suelo de 1,0 marcadores cuando no hay pronombres pero sí verbos en primera persona.
- Motivo: `voice.md` permitía de tres a cinco hashtags mientras `li-post` y `plan.md` ya fijaban tres. El post del sábado usó seis emojis y el perfil solo permitía dos en un post personal. Además, `VOICE` bajaba a 65 en textos castellanos sin «yo» aunque tuvieran verbos en primera persona: el post del sábado tenía 2,5 verbos por 100 palabras y ningún pronombre.
- Alternativas descartadas: mantener tres a cinco hashtags y relajar `li-post` (más ruido y tres reglas distintas); prohibir los emojis o dejarlos a criterio (el perfil real los usa); contar solo pronombres (penaliza el sujeto implícito); añadir clíticos como `me` y `nos` (insuficiente: el post del sábado seguía por debajo del umbral); bajar el umbral de 1,6 a 0,4 (maquilla el cero y penaliza menos los textos impersonales).
- Consecuencia: `voice.md` queda con tres hashtags y los topes nuevos; `li-post` genera emojis en cada borrador. El panel pasa de 14 PASS, 19 REVIEW y 3 FLAGGED a 16 PASS, 17 REVIEW y 3 FLAGGED. El post del sábado sube de 80,3 a 89,4 PASS y el del lunes se mantiene en 100 PASS. Los controles de relleno y LLM típico siguen FLAGGED (35,2 y 22,7).
- Verificación: `py_compile` sin errores; 36 publicaciones puntuadas; los dos posts nuevos medidos; `markdownlint-cli2` sin incidencias.

## 2026-11-02 - El log guarda la versión publicada, no el borrador

- Decisión: `li-post` registra en `log.md` el texto publicado, con fecha, gancho, primera línea, longitud, imagen, enlace y panel del humanizador. Si la persona edita el borrador antes de publicar, se guarda la versión final.
- Motivo: los posts del 2026-10-31 y del 2026-11-02 se editaron antes de publicar. Guardar el borrador habría dejado un historial que no coincide con lo que ve la audiencia y habría roto la comparación de `li-audit`.
- Alternativas descartadas: guardar solo fecha, gancho y primera línea (no permite auditar voz, longitud ni cierre); guardar el borrador y un diff (más mantenimiento para una sola persona); no registrar los posts ya publicados (pierde la serie y la hipótesis).
- Consecuencia: `log.md` tiene tres fichas completas. La imagen queda como «adjunta» mientras no se registre el nombre del archivo.

## 2026-11-02 - Calibración de `li-human` con las 36 publicaciones reales

- Decisión: recalibrar `detect.py` y `slop.json` con el corpus completo de LinkedIn, 36 publicaciones exportadas el 2026-10-31, en lugar de las cuatro muestras iniciales. Umbrales nuevos: BURSTINESS 0,45/0,11, SPECIFICITY 5,4/1,35 y pronombres 1,6/0,4. Se retira la estructura `triada` y se ajustan las dos reglas que chocaban con el perfil de voz: un emoji suelto deja de puntuar y solo se marca el que se repite dos veces seguidas; la pared de hashtags empieza en 6 como red de seguridad, por encima del límite de tres.
- Motivo: los umbrales anteriores se habían fijado con tres muestras y un borrador, y dejaban en REVIEW textos que el perfil considera normales. `triada` marcaba listas técnicas legítimas («subprocess, eval y exec.», «Angular, React y Redux.»), la regla del emoji castigaba un único 🚀 y la de hashtags marcaba el límite que el perfil permite. La distribución real del corpus (mediana de BURSTINESS 0,45; p25 de SPECIFICITY 5,4; mediana de pronombres 1,6) sitúa los umbrales en la voz publicada.
- Alternativas descartadas: mantener los umbrales de cuatro muestras, que dejaban en REVIEW textos que el perfil considera normales y seguían marcando `triada`, emojis sueltos y cinco hashtags; bajarlos más para que todo pase, que dejaría el control de relleno en FLAGGED pero perdería la señal; crear perfiles por idioma o por registro, más código y mantenimiento para una sola persona; excluir los posts cortos del corpus, que son 13 de 36 y sesgarían la mediana hacia los textos largos.
- Consecuencia: el panel da 14 PASS, 19 REVIEW y 3 FLAGGED sobre 36 publicaciones. Trece de los 19 REVIEW tienen menos de 25 palabras y el panel no puede juzgarlos; los otros seis son textos de una a tres frases. Los tres FLAGGED son el post del 2026-10-14, por 40 espacios duros y 3 rayas largas del pegado; el del 2026-09-20, un enlace a un curso con «Microsoft» al inicio y sin cifras; y el del 2026-08-04, una actualización de una frase con nombres técnicos que la regex de nombres propios no reconoce. Los dos últimos son falsos positivos conocidos de textos cortos.
- Verificación: `py_compile` sin errores; 36 posts puntuados; controles de relleno y LLM típico FLAGGED (19,2 y 35,2); `markdownlint-cli2` sin incidencias.

## 2026-11-02 - La unidad 4 se trabaja sobre el CV ATS existente

- Decisión: usar `cv/cv-base-2026-10.md`, el `.docx`, el `.pdf` y `ats-checker` como base para la unidad 4; las actividades se resuelven como revisión y adaptación por oferta.
- Motivo: el CV ya está en una página, una columna, sin tablas, con PDF textual verificado y revisión ATS; además hay una versión adaptada a IGNIS. Rehacerlo duplicaría trabajo y rompería la trazabilidad.
- Alternativas descartadas: crear un CV nuevo para el curso; usar una plantilla de Canva con columnas o iconos; y mantener dos CV distintos, uno para el curso y otro para las candidaturas.
- Consecuencia: la unidad 4 se usa como checklist y no como reconstrucción. Si alguna lección pide un formato distinto, se compara con el CV actual antes de cambiar nada.

## 2026-11-02 - Cierre de octubre: el sistema está montado, falta volumen

- Decisión: cerrar octubre con una candidatura, una entrevista real y tres publicaciones; mantener en noviembre tres candidaturas por semana, 12-15 horas de curso, tres publicaciones de LinkedIn, tres sesiones de inglés, tres contactos de networking y una práctica de entrevista semanal.
- Motivo: la revisión mensual confirma que la infraestructura (plan de 22 fases, CV ATS, LinkedIn, caso de estudio, agenda y registro de candidaturas) está terminada, pero el volumen de candidaturas y las horas de curso quedaron por debajo del plan. El registro diario de la agenda no se usó.
- Alternativas descartadas: subir el número de candidaturas antes de tener respuesta de IGNIS; compensar las horas de curso en un solo día; y abrir un frente nuevo (Aplika Copilot o DevOps) antes de estabilizar el ritmo de noviembre.
- Consecuencia: la revisión mensual vive en `docs/privado/revisiones/2026-10-revision-mensual.md` y la tarea 4 de la agenda queda cerrada. La siguiente revisión mensual se fija el 2026-11-30; el objetivo SMART no cambia.

## 2026-11-02 - Ajustes de la revisión semanal 3.7: registro diario, tres publicaciones y tres candidaturas

- Decisión: mantener tres candidaturas por semana; bajar LinkedIn a tres publicaciones semanales (martes, jueves y viernes); registrar los bloques diarios de la agenda al final de cada día; no recuperar la publicación del miércoles 28 de octubre; y cerrar la revisión mensual de octubre el 2 o 3 de noviembre.
- Motivo: la semana del 26 de octubre al 1 de noviembre cerró con 1 de 3 candidaturas, 3 de 4 publicaciones, 4 horas de curso frente a las 12-15 previstas, 4 sesiones de inglés frente a 3 y 1 contacto de networking. El registro diario no se usó, así que las horas y las sesiones se reconstruyeron de memoria. La entrevista de Neoland se hizo y la primera candidatura está en seguimiento.
- Alternativas descartadas: mantener cuatro publicaciones semanales, que no se cumplieron; subir a cuatro candidaturas, que no cabe en la capacidad actual; compensar las horas de curso en un solo día, que rompe el día mínimo; y contar la entrevista de Neoland como práctica de entrevista, porque no cubre el circuito de una entrevista de oferta.
- Consecuencia: la revisión del viernes 6 de noviembre comprobará el registro diario. Si falla, se baja LinkedIn a dos publicaciones y se mantiene el resto. La revisión mensual de octubre se traslada al 2 o 3 de noviembre y el objetivo SMART no cambia.

## 2026-11-01 - El trabajo diario pasa a la rama `dev`

- Decisión: `main` queda como rama estable y el trabajo diario se hace en `dev`, que se creó ese día desde `main` y ya tiene upstream en `origin`. Los cambios llegan a `main` por fusión o pull request, no por commit directo.
- Motivo: el CI `Calidad` solo se dispara en `push` a `main` y en `pull_request`. Trabajar en `dev` permite agrupar varios commits y verlos pasar juntos antes de que toquen la rama publicada, sin dejar `main` a medias entre dos sesiones.
- Alternativas descartadas: seguir en `main` con commits directos (cada push publica el estado intermedio y el CI solo avisa después); una rama por tema (más limpio, pero el repositorio es de una sola persona y añade ceremonia sin beneficio mientras el trabajo sea secuencial); trabajar en `dev` sin publicarla (se pierde la copia remota y la posibilidad de abrir PR desde el móvil).
- Consecuencia: los `push` a `dev` no ejecutan el CI, así que la comprobación de calidad llega al abrir el pull request o al fusionar en `main`. Si una sesión se queda a medias, `dev` puede estar roja sin que nadie lo note.

## 2026-10-31 - Detector li-human bilingüe y calibrado con la voz propia

- Decisión: adaptar `detect.py` y `slop.json` al castellano. Regex Unicode para palabras y nombres propios, pronombres españoles en lugar de contracciones inglesas, umbrales calibrados con las 36 publicaciones descargadas de la API de portabilidad, 57 palabras y 51 frases nuevas en el léxico, 13 estructuras españolas y una puerta de PASS que ignora los checks que no pueden juzgar textos cortos.
- Motivo: el panel era monolingüe en las dos direcciones. VOICE valía siempre 30 porque buscaba contracciones con apóstrofo y pronombres ingleses, y con ese 30 el máximo aritmético del panel era 63,6: ningún texto español podía llegar a PASS. A la vez, SLOP devolvía 100 siempre porque el léxico era inglés, así que un texto de relleno pasaba sin un solo aviso.
- Alternativas descartadas: dejar el detector en inglés y usarlo solo como lista de comprobación (el veredicto seguía mintiendo en ambos sentidos); bajar la puerta de 55 a 50 (maquilla el resultado sin arreglar la métrica); parchear solo las expresiones regulares (deja el léxico y las estructuras sin tocar); sacar un `profiles/es.json` con perfiles por idioma (más limpio a largo plazo, pero cuesta más código ahora y solo hay dos idiomas).
- Consecuencia: PASS significa «se parece a cómo escribes tú», no «es indetectable». El código de salida solo falla con FLAGGED y `--strict` recupera el comportamiento antiguo para hooks. El léxico se edita a mano y puede marcar palabras técnicas legítimas como `robusto`, `roadmap` o `networking`.
- Verificación: 36 publicaciones medidas; 10 son juzgables con el panel completo y 7 pasan, 2 quedan en REVIEW (una por SPECIFICITY baja y otra por cuatro emojis) y 1 en FLAGGED por 3 em dashes y 40 espacios duros pegados de un documento. Las cuatro muestras de referencia pasan (91,5 / 74,5 / 76,2 / 83,5); el post de Story #3 saca 81,8 con 0 avisos estructurales; los controles de relleno y de LLM típico quedan FLAGGED (15,9 y 32,7); un texto con cuatro estructuras españolas recibe los cuatro avisos; `humanize.py` devuelve el post idéntico carácter a carácter.

## 2026-10-31 - Objetivo SMART de búsqueda: contrato antes del 2027-03-31, sin filtros de empresa

- Decisión: fijar como objetivo el contrato como desarrollador full-stack junior antes del 2027-03-31, con tres candidaturas registradas por semana hasta el 2026-12-31, y descartar las otras dos formulaciones del ejercicio 3.3: la de esfuerzo puro y la que añadía filtros de empresa y el B2 previo a marzo.
- Motivo: la versión de esfuerzo mide actividad y no resultado, así que se puede cumplir sin acercarse al puesto; la versión con filtros convierte el inglés en un requisito previo y deja de enviar candidaturas mientras se prepara, cuando el inglés se estudia en paralelo. El rango de 20 a 200 empleados procedía del perfil de empresa objetivo y no se entiende fuera del registro interno.
- Alternativas descartadas: mantener el rango de 20 a 200 empleados en el enunciado, que no aporta nada al lector y no cambia la conducta semanal; exigir el B2 antes de marzo, que retrasa el objetivo sin mejorar la candidatura; y quedarse solo con la métrica de candidaturas, que no tiene fecha de resultado.
- Consecuencia: el filtro de empresa sigue vigente como criterio de prospección en la decisión del 2026-10-29, pero no forma parte del objetivo; el objetivo se evalúa con el contrato y se corrige con indicadores tempranos (entrevistas, pruebas en el repositorio, explicar un proyecto sin IA).
- Verificación: ejercicio enviado el 2026-10-31 y registrado en `docs/ejercicios/tema-3-3-objetivo-smart.md`.

## 2026-10-30 - Agenda diaria sobre SQLite privada, sin app externa

- Decisión: convertir el plan en una agenda operativa con `docs/privado/agenda/agenda.db` como fuente única, `scripts/agenda.py` como CLI sin dependencias, los comandos `/hoy` y `/hecho`, y un `.ics` importable en Google Calendar, Outlook o Apple Calendar. La interfaz React se pospone hasta cerrar D2 y D9.
- Motivo: el «qué tocar hoy» estaba repartido entre `PLAN.md`, el plan de estudios, el plan de LinkedIn, el calendario de contenido, `estado-actual.md` y la base de candidaturas. Ninguna vista era diaria y marcar un checkbox en un markdown no cambiaba el estado en ningún sitio.
- Alternativas descartadas: Obsidian con el plugin Tasks (añade una app y un plugin, y el móvil exige sincronización de pago); Todoist o Google Tasks (notificaciones nativas, pero dos fuentes de verdad y sincronización frágil); GitHub Projects en un repo privado (saca datos personales del repositorio y no avisa en el móvil); construir la app React ahora (contradice la regla D12 de no abrir proyectos hasta cerrar D2 y D9).
- Consecuencia: la base y las vistas viven en `docs/privado/`, ignorado por git; `estado-actual.md` incorpora un bloque generado entre marcadores; el plan de estudios y el plan de LinkedIn siguen explicando el porqué y la agenda manda sobre el estado.
- Excepción de nomenclatura: `/hoy` y `/hecho` van en español por ser de uso diario; el resto de comandos sigue en inglés kebab-case.
- Verificación: `init` crea 36 tareas y 5 recurrencias; `hoy` muestra la carga del día; `done` persiste y retira la tarea de la vista; `ics` genera 33 eventos con `UID` estable, horas flotantes y avisos solo en tareas con hora.

## 2026-10-29 - Los registros del curso no se publican en el repositorio

- Decisión: excluir `docs/ejercicios/` del repositorio público salvo el índice vacío, con las reglas `docs/ejercicios/*` y `!docs/ejercicios/indice-ejercicios.md` en `.gitignore`.
- Motivo: los apuntes y los entregables del Employment Workshop contienen el DAFO con doce debilidades propias, el autodiagnóstico de competencias, la lista de empresas a evitar y dos direcciones de correo. Publicarlos entrega a cualquier reclutador argumentos en contra del candidato y expone datos de contacto.
- Alternativas descartadas: publicarlos íntegros, que perjudica la candidatura; sanearlos hasta dejar solo lo positivo, que convierte el apunte en marketing y le quita su función de trabajo real; y borrarlos, que pierde el seguimiento del curso.
- Consecuencia: el índice público `docs/ejercicios/indice-ejercicios.md` se mantiene como plantilla sin filas y la memoria del proyecto queda como única referencia pública al avance del curso.

## 2026-10-29 - Entregables del curso en primera persona y sin restringir el sector

- Decisión: redactar los entregables del Employment Workshop en primera persona y en lenguaje llano, sin identificadores de commit, acrónimos de arquitectura, nombres de bibliotecas ni referencias a códigos internos del repositorio; y presentar los sectores de experiencia previa como punto de partida y no como límite del puesto al que se aspira.
- Motivo: la primera versión del DAFO del ejercicio 2.5 usaba vocabulario interno que un evaluador externo no entiende y que delataba que el texto no lo había escrito la persona. Además, fijar logística, hostelería, producción y gestión ecuestre en la dirección profesional convertía una ventaja de acceso en una restricción del puesto.
- Alternativas descartadas: mantener los códigos internos con un glosario al pie, que sigue sin sonar propio; eliminar la mención a los sectores, que pierde una ventaja real; y dejar el documento como borrador interno sin entregar, que incumple la actividad.
- Consecuencia aceptada: el entregable y el registro interno del 2.3 ya no coinciden palabra por palabra. La correspondencia se mantiene por código en `docs/ejercicios/tema-2-5-actividades-practicas.md`.
- Verificación: la lección 2.5 quedó entregada y completada en la plataforma el 2026-10-29, con el progreso del 11 % al 12 %.

## 2026-10-29 - Dirección profesional fijada por el ejercicio 2.2: full-stack junior con IA

- Decisión: fijar como dirección el puesto de Desarrollador Full-Stack Junior con orientación a automatización e IA, en software para pymes de logística, hostelería, producción y gestión ecuestre, con HR-tech y empleo como alternativa, y en pymes de software o consultoras medianas de 20 a 200 personas con producto propio e infraestructura propia.
- Motivo: de las seis intersecciones del Ikigai, la de vocación y profesión es la única con demanda demostrada, porque 5 de 5 ofertas de la muestra son de desarrollo; la de profesión y misión es la ventaja diferencial por el acceso de primera mano a cuatro sectores de baja digitalización; la de pasión y profesión, agentes e infraestructura, no aparece en la muestra y queda como diferenciador de entrevista y dirección a dos o tres años.
- Alternativas descartadas: AI Engineer, que no es el título que contrata junior en la muestra; DevOps o SRE, con 0 de 5; arquitecto, porque aún no se implementa lo que se diseña; y el posicionamiento como especialista en automatización con IA, porque ninguna oferta menciona agentes y reduciría el embudo.
- Verificación: registro completo en `docs/ejercicios/tema-2-2-ikigai-y-dafo.md`, validado el 2026-10-29. La muestra es de cinco ofertas, una de ellas salida de Aplika con un 70 % de match, y queda pendiente ampliarla a 25 antes de dar la dirección sectorial por cerrada.

## 2026-10-28 - El PDF se audita con un script determinista, no con código del agente

- Decisión: retirar al subagente `ats-checker` el acceso a Code Mode, a la lectura directa de PDF y a las herramientas del servidor `filesystem`, y darle una única vía para el PDF: `python scripts/verify-cv-pdf.py <pdf> --md <markdown> --json`.
- Motivo: el agente intentaba extraer el texto del PDF a mano, sin bibliotecas, y escribía decodificadores DEFLATE en JavaScript dentro de Code Mode. La llamada no terminaba nunca y bloqueaba la sesión durante horas; ocurrió dos veces el mismo día. La extracción de PDF es un problema resuelto que no debe improvisar un modelo.
- Alternativas descartadas: seguir confiando en el prompt y pedirle que no lo hiciera, que ya falló dos veces; instalar una biblioteca de PDF externa, que añade una dependencia y no impide que el agente vuelva a escribir código; dejar el agente sin acceso al PDF, que elimina la verificación mecánica del bloque de parseo.
- Verificación: el script tarda unos 150 ms, decodifica las cadenas CID con los mapas `ToUnicode`, conserva los acentos y devuelve las mismas 512 palabras que el Markdown. El agente corregido terminó la auditoría en segundos.

## 2026-10-28 - Primera candidatura real: IGNIS y ángulo electrotécnico

- Decisión: adaptar el CV a la oferta de IGNIS, Junior Fullstack Developer (GdD), enviarla el 2026-10-28 y registrarla en SQLite como aplicada, con el eje de la formación electrotécnica y las prácticas en Telefónica y Enerpal, sin incluir Python, y ofrecer disponibilidad de traslado a Madrid y contrato de prácticas gestionado por Neoland.
- Motivo: la oferta pide formación afín, APIs y PostgreSQL, y valora el conocimiento del sector energético y la gestión de la demanda. El perfil acredita el título, las prácticas y el stack full-stack, pero no Python; el ángulo diferencial es el dominio eléctrico, no competir por una palabra clave que no se puede defender en entrevista.
- Alternativas descartadas: incluir Python como «en aprendizaje» sin evidencia, ocultar la brecha en la carta, limitar la candidatura a remoto y no mencionar la vía de prácticas.
- Verificación: CV de una página y 500 palabras, PDF textual, carta de 237 palabras, auditoría ATS manual (el subagente `ats-checker` se quedó colgado y se descartó); oferta resumida en `docs/candidaturas/ofertas/ignis-junior-fullstack-gdd-2026-10.md`, análisis privado en `docs/privado/candidaturas/` y candidatura registrada en SQLite como aplicada con seguimiento el 2026-11-04.

## 2026-10-26 - Aplika Copilot: módulo premium como opción principal

- Decisión: evaluar la integración de `ai-job-search-copilot` en Aplika como módulo premium centrado en el seguimiento posterior a la candidatura, con la aplicación independiente como alternativa y el caso de estudio como respaldo. No se implementa nada hasta validar al compañero, 5-10 usuarios beta y tres candidaturas reales.
- Motivo: Aplika cubre la parte inicial (perfil, ofertas, matching, CV y carta); el copilot cubre la parte posterior (seguimiento, entrevistas, LinkedIn, networking, negociación y memoria). El módulo reutiliza autenticación, PostgreSQL/Prisma, IA y `Application`, y evita duplicar el núcleo.
- Alternativas descartadas: aplicación independiente como opción principal (duplica autenticación, infraestructura y soporte, y carece de distribución), API híbrida con dos frontends (complejidad prematura), widget embebido (deuda técnica), escritorio o CLI (poca distribución) y runtime de OpenCode en el navegador (riesgo de seguridad y 4-8 semanas).
- Hallazgos del esquema real de Aplika: `ApplicationStatus` no incluye `REJECTED` ni `WITHDRAWN`, y `Application.jobOfferId` es obligatorio, lo que impide registrar candidaturas externas sin una `JobOffer`. El MVP requiere migración, estados de cierre y campos de candidatura externa.
- Documentos: `docs/privado/aplika-copilot-posibilidades.md` y `docs/privado/aplika-copilot-propuesta-companero.md`, verificados con `markdownlint-cli2`.
- Estado: pendiente la conversación con el compañero; la prioridad inmediata sigue siendo la primera candidatura real del 2026-10-27.

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
- Sustituida el mismo día por el lanzador `scripts/memory-mcp.mjs`: OpenCode V2 no carga `.env`, así que `{env:MEMORY_FILE_PATH}` se resolvía como cadena vacía y el servidor escribía en la caché de npx. Detalle en la entrada siguiente.

## 2026-10-24 - Lanzar el Memory MCP con la ruta resuelta

- Decisión: arrancar `@modelcontextprotocol/server-memory` mediante `scripts/memory-mcp.mjs`, que calcula la ruta absoluta de `docs/memoria/memoria.local.json` desde la raíz del repositorio y la exporta en `MEMORY_FILE_PATH`; retirar la clave de `.env` y `.env.example`.
- Motivo: OpenCode V2 no carga `.env` en el entorno de los MCPs. El token de GitHub funcionaba porque está definido como variable de usuario de Windows, pero `MEMORY_FILE_PATH` llegaba vacía y el grafo se escribía en `dist/memory.jsonl` de la caché de npx.
- Alternativas descartadas: variable de entorno del sistema (depende de cada equipo y obliga a reiniciar el servicio), `{file:...}` con un fichero de ruta (falla en silencio si falta o termina en salto de línea) y una ruta absoluta versionada (expone el entorno local).
- Verificación: tras recargar la configuración, `read_graph` devuelve 11 entidades y 17 relaciones desde `docs/memoria/memoria.local.json`; una observación de prueba escrita con `add_observations` persiste en el fichero del repositorio.

## 2026-10-24 - Capturas del panel con datos ficticios y sin JSearch

- Decisión: completar la vista del producto del caso de estudio con tres capturas del panel (lista, detalle y flujo de matching) tomadas en tema oscuro con una cuenta ficticia, y mantener la landing existente con un aviso sobre logotipos de terceros y métricas de producto.
- Motivo: la demo no ofrece tema claro ni estado de progreso del matching; las ofertas se crearon manualmente para evitar datos de terceros de JSearch y el umbral se bajó al 60 % para que las ofertas de 68 % siguieran visibles.
- Alternativas descartadas: forzar un tema claro inexistente, usar ofertas reales de JSearch, inventar un estado de progreso y publicar `login.png` (484,8 KiB) en lugar de las capturas del panel.
- Verificación: commits `635dd23` y `2bc67f0`, CI `Calidad` en verde (runs `40128199801` y `40128521622`), imágenes de 1440×900 sin metadatos, README y NOTICE con datos ficticios y descargos.

## 2026-10-25 - Cierre del caso de estudio: landing fuera y lectura rápida

- Decisión: retirar `landing-hero.png` y `login.png` del repositorio público, dejar tres capturas del panel, añadir un TL;DR de 56 palabras y un bloque `Stack principal` / `También he trabajado con`, y corregir el README para describir el modo demostración del panel.
- Motivo: la landing mostraba marcas de terceros y cifras de marketing (95 %, 98 % y €85k) que el descargo no eliminaba; el panel es la evidencia relevante para la aportación backend. El README completo tarda 5,5-6,8 minutos, así que el criterio de lectura se ajusta a la lectura rápida del TL;DR. La demo abre el panel sin login con datos ficticios y el README afirmaba lo contrario.
- Alternativas descartadas: mantener la landing con descargo (no cumple el checklist de métricas), recapturar un hero limpio (más trabajo y menos relevante), recortar el README a 700 palabras (pierde detalle técnico) y cambiar la demo para exigir login (mayor riesgo).
- Verificación: commits `d7b25da` y `9dd8156`; CI `Calidad` en verde en el HEAD (run `40137561987`); el commit intermedio `d7b25da` falló porque el README aún referenciaba las imágenes borradas. Plan privado: 87/93; las 6 restantes son la Fase 8 continua.

## 2026-10-25 - Pack LinkedIn auditado e instalado con adaptaciones locales

- Decisión: instalar los 11 skills y 11 comandos del repositorio `Jakeschincariol/linkedin-agent-skill` (MIT, commit `add2c23882fe79180737d242ff80a5da205eda6a`) tras auditar su contenido, con el perfil de voz, el plan y el historial en `docs/privado/linkedin/` y los scripts ejecutados con `uv run --no-project python`.
- Motivo: el pack cubre la escritura y la planificación de LinkedIn con 21 fórmulas de gancho y un humanizador local, sin publicar ni automatizar la cuenta. La auditoría no encontró red, ejecución de procesos, dependencias, binarios, secretos ni exfiltración; las únicas escrituras son locales y el README prohíbe la publicación automática.
- Alternativas descartadas: instalar el pack global en `~/.claude/skills/` (mezcla con otros proyectos y rutas fuera del repositorio), mantener las rutas `~/.claude/linkedin/` (saca datos personales del control del proyecto), ejecutar con `python3` (Windows no lo incluye y el PATH heredado de esta sesión no resuelve `python`), copiar solo `li-post` (rompe la dependencia con `li-human` y el resto del pack) y confiar en la invocación automática de skills sin comandos (OpenCode no los expone como `/li-*`).
- Verificación: los tres JSON parsean; `humanize.py` y `detect.py` funcionan con `uv`; un texto de control en inglés pasa de 78,0 a 95,6 PASS; el borrador español de prueba queda en 1.102 caracteres y 57,2 REVIEW por la comprobación VOICE calibrada para inglés; `/li-post` carga el skill, lee el perfil de voz y entrega tres ganchos y un borrador humanizado. Detalle en `docs/marca-personal/linkedin-agent-skill.md`.

## 2026-10-25 - Perfil de voz construido desde tres publicaciones reales

- Decisión: sustituir el perfil provisional de `docs/privado/linkedin/voice.md` por uno construido desde tres publicaciones propias, con dos registros (hito personal en primera del singular y anuncio de equipo en primera del plural), aperturas, giro, cierres y una sección de patrones que no se replican.
- Motivo: el borrador anterior inventaba rasgos (decía que no se usaban emojis y listaba un léxico que no aparece en las muestras). Las tres publicaciones reales muestran emoji, puntuación expresiva, vocabulario coloquial de España y un cierre con pregunta en todos los casos; el perfil tiene que describir eso, no lo que el repositorio sugiere.
- Alternativas descartadas: rellenar solo las casillas de la plantilla (pierde ritmo, aperturas y cierres), copiar las muestras sin filtro (arrastra erratas como `Aplica Jobs`, `developper` y los hashtags dentro de la frase) y normalizar las muestras (borra la evidencia que permite imitar el ritmo).
- Verificación: las tres muestras se guardan íntegras en bloques `text`; la sección de ruido documenta los siete patrones detectados; el fichero pasa `markdownlint-cli2` sin incidencias y está excluido de git por `docs/privado/`.

## 2026-10-25 - Python 3.14.7: no reinstalar y corregir la premisa del PATH

- Decisión: no instalar una segunda versión de Python. El equipo ya tiene Python 3.14.7 con pip 26.2.1, el lanzador `py` y el componente Add to Path; el problema era que el proceso de OpenCode arrancó antes de la instalación y heredó un PATH sin las entradas nuevas.
- Motivo: reinstalar habría duplicado intérpretes y abierto un conflicto de PATH. Con el PATH actualizado, `python --version`, `pip --version` y `py --version` responden, y `detect.py` devuelve el mismo 57,2 que con `uv`.
- Alternativas descartadas: instalar Python 3.13 desde winget (duplica sin aportar), crear un alias `python3.exe` en la carpeta de Python (Windows no lo necesita y se pierde en la próxima actualización) y cambiar los comandos del pack a `python` (pierde la reproducibilidad entre equipos).
- Verificación: el PATH de usuario contiene `Python314`, `Python314\Scripts` y `Launcher` antes de `WindowsApps`. Tras reiniciar el equipo, `python --version` devuelve 3.14.7 desde la ruta real, `pip` 26.2.1 y `py` 3.14.7; `detect.py` ejecutado con el intérprete del sistema devuelve el mismo 57,2 que con `uv`. `uv` sigue siendo el ejecutor canónico del pack porque fija Python 3.15 y evita paquetes globales.

## 2026-10-25 - Plan semanal de LinkedIn sin automatizar la cuenta

- Decisión: generar el plan semanal en `docs/privado/linkedin/plan.md` con cuatro publicaciones del 27 al 30 de octubre y diez cuentas de interacción, sin abrir LinkedIn con Playwright ni automatizar la sesión.
- Motivo: la lista se puede construir con cuentas públicas y con las ofertas reales de la semana; automatizar la sesión es el comportamiento que el propio pack advierte y puede restringir la cuenta. El coste de un bloqueo supera el beneficio de diez nombres elegidos a ciegas.
- Alternativas descartadas: usar Playwright con la sesión de LinkedIn (riesgo de restricción y contradice la auditoría del pack), inventar nombres de reclutadores (rompe la regla de no fabricar) y dejar la lista vacía (el plan dejaría de ser operativo).
- Verificación: `plan.md` pasa `markdownlint-cli2`; las cuentas de alcance y pares son verificables; los dos huecos de contratación se llenan con la primera oferta registrada; las cuatro filas están en el calendario público.

## 2026-10-26 - Plan de estudios enlazado con el plan de LinkedIn

- Decisión: añadir al plan de estudios una columna diaria de LinkedIn en la semana tipo, dos métricas semanales (comentarios y publicaciones) y una rutina diaria con la semana en curso; mantener `docs/privado/linkedin/plan.md` como fuente operativa y enlazar ambos documentos en los dos sentidos.
- Motivo: el plan de estudios repartía el tiempo en «Búsqueda, portfolio y LinkedIn/GitHub» sin decir qué tocaba en LinkedIn, y el plan semanal vivía en otro fichero, así que la acción del día no era visible al abrir el plan de estudios.
- Alternativas descartadas: copiar el plan semanal completo en el plan de estudios (duplica contenido y se desincroniza), mover el plan de LinkedIn al plan de estudios (pierde el detalle de ganchos y cuentas de interacción) y dejar solo un enlace sin vista diaria (no resuelve la consulta de qué hacer hoy).
- Cambio asociado: se sustituye «un post cada una o dos semanas» por la cadencia que fije el plan semanal, porque contradecía las cuatro publicaciones del 27 al 30 de octubre.
- Correcciones de coherencia: se elimina la entrada de Experiencia en §8, porque la decisión del 2026-10-23 dejó los proyectos en `Proyectos`, y se sustituye la lista de Destacados por las tres publicaciones reales, sin `english-coach` porque aún no existe.
- Verificación: las tablas mantienen el número de columnas y pasan `markdownlint-cli2`; `plan.md` enlaza de vuelta al plan de estudios; la tabla de la semana en curso se actualiza al regenerar `plan.md` con `li-plan`.

## 2026-10-26 - Guía de uso operativa del sistema

- Decisión: crear `docs/guia-uso-ai-job-search-copilot.md` con el modelo de cinco capas, comprobaciones de entorno, formas de invocación, rutina diaria, pipeline de candidatura, flujos de estudio, entrevistas, LinkedIn y memoria, privacidad, solución de problemas y chuleta; enlazarla desde `README.md` en español e inglés y desde `AGENTS.md`.
- Motivo: `docs/referencia-agentes-mcps.md` es una referencia técnica densa, no un manual de arranque; faltaba un documento que explicara el orden de uso y qué pieza tocar en cada momento.
- Alternativas descartadas: ampliar la referencia técnica (mezcla manual y referencia), crear un README aparte (duplica el existente) y dejar las instrucciones solo en la conversación (no persisten).
- Redacción: delegada en `tracker-doc`, con revisión posterior de dos imprecisiones de OpenCode V2: el cambio de agente es `Ctrl+X A` o `Shift+Tab`, no `/agents`, y el CLI de npm no es requisito porque en este equipo el shim no encuentra el binario de plataforma.
- Verificación: `markdownlint-cli2` sin incidencias en la guía, `README.md` y `AGENTS.md`; enlaces locales a la guía comprobados; recuento contrastado de 15 agentes, 9 MCPs, 17 comandos y 14 skills.

## 2026-10-26 - microsoft-learn como MCP remoto sin credenciales

- Decisión: añadir el servidor MCP `microsoft-learn` en modo remoto contra `https://learn.microsoft.com/api/mcp`, sin clave ni cabeceras, denegado globalmente y habilitado solo en los agentes `build` y `plan`.
- Motivo: la documentación de las APIs de LinkedIn vive en `learn.microsoft.com`, que permite el acceso automatizado, mientras que `linkedin.com` lo prohíbe expresamente en su `robots.txt`. Es la única vía limpia para comprobar scopes, versiones de endpoint y productos regulatorios antes de escribir código.
- Alternativas descartadas: extraer la documentación con Playwright desde `linkedin.com` (bloqueado y con riesgo de restricción), depender de `context7` para documentación de LinkedIn (no la indexa) y pegar los fragmentos a mano en el chat (no verificable ni repetible).
- Verificación: handshake correcto con respuesta 200 en `text/event-stream`, servidor `Microsoft Learn MCP Server` 1.0.0 sobre protocolo `2025-06-18`, tres herramientas listadas y una búsqueda real devolviendo resultados. `opencode.json` y `.opencode/mcp.json` mantienen el mismo inventario.

## 2026-10-26 - Lectura de LinkedIn por la API DMA, no por automatización

- Decisión: leer el perfil, la red y las publicaciones propias con la API de portabilidad de LinkedIn (`Member Data Portability (Member)`), mediante un cliente local de solo lectura en `scripts/linkedin-portability.py`, con token personal guardado en `.env`.
- Motivo: es la vía que LinkedIn documenta para extraer datos con consentimiento revocable y no entraña riesgo de restricción. Automatizar la sesión con Playwright sigue prohibido por `robots.txt` y por el propio interés de la cuenta con la que se busca empleo. El export por CSV sigue disponible como respaldo, pero la API entrega JSON por dominio, más dominios y eventos de los últimos 28 días.
- Alternativas descartadas: export manual mensual como única vía (sin changelog ni consulta por dominio), automatización del navegador (riesgo de bloqueo) y renunciar al acceso (deja sin base el historial de `li-audit`).
- Limitación aceptada: ningún dominio incluye impresiones ni alcance, así que las métricas de rendimiento se siguen copiando a mano. Queda por confirmar si `ALL_COMMENTS` incluye comentarios ajenos en publicaciones propias.
- Verificación: listado de dominios, resumen de datos y guardas de host y recurso probadas en local; el cliente rechaza un host ajeno y un recurso no permitido antes de salir a la red. La primera llamada autenticada queda pendiente del alta en el portal.

## 2026-10-27 - Publicar solo cifras que el lector pueda verificar

- Decisión: retirar del post del martes la cifra «87 de 93» que figuraba en el plan y sustituirla por tres datos contables del repositorio público: cuatro fragmentos, tres capturas y un NOTICE.
- Motivo: la rúbrica de 93 casillas es interna del taller y no aparece en el repositorio, así que nadie que lea el post puede comprobarla. Un número autoconcedido y no verificable es el riesgo que el propio plan advertía y contradice la regla del perfil de voz: no afirmar resultados que no se puedan demostrar con un enlace, una captura o un dato del repositorio.
- Alternativas descartadas: publicar el 87/93 como «mi rúbrica interna» (sigue sin poder comprobarse), publicar el número sin contexto (parece un farol) y suprimir toda cifra (deja el post sin prueba, que es su único valor).
- Verificación: el repositorio público tiene exactamente cuatro ficheros en `docs/fragmentos/`, tres en `docs/capturas/` y un `NOTICE.md`, comprobado contra el árbol de GitHub antes de escribir el post.
