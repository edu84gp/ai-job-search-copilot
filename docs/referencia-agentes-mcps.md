# Referencia de agentes, MCPs, comandos y skills

## Objetivo

Centralizar la documentación técnica de los subagentes de opencode, de los servidores MCP, de los comandos y de los skills del proyecto para evitar que `PLAN.md` crezca con detalle operativo.

## Conceptos clave

- Subagentes definidos en `.opencode/agents/` con campo `permission` y `temperature`.
- Servidores MCP definidos en `opencode.json` canónico y `.opencode/mcp.json` legacy.
- Comandos definidos en `.opencode/commands/` con `description` y `agent`.
- Skills definidos en `.opencode/skills/<nombre>/SKILL.md` y cargados según la tarea.
- Convención `kebab-case` para archivos en `docs/`.

## Enfoque planteado

1. Mantener `PLAN.md` solo como plan de aplicación con el ToDo por fases.
2. Mantener este archivo como referencia viva de qué hace cada agente, cada MCP, cada comando y cada skill, para qué sirve y cómo usarlo.
3. Actualizar este archivo en cada fase que cree o modifique un agente, un MCP, un comando o un skill.

## Estado de resolución

- Referencia creada con 15 agentes, 8 MCPs, 6 comandos y 3 skills.
- Pendiente de ampliación en la Fase 21 según ToDo en `PLAN.md`.

---

## Agentes

### 1. cv-optimizer

**Qué hace:**

Analiza currículums, perfiles profesionales y descripciones de puestos de trabajo. Identifica fortalezas, áreas de mejora, uso de palabras clave técnicas y formato parseable por ATS. Verifica que las tecnologías mencionadas estén respaldadas por proyectos o logros concretos. Propone mejoras de redacción con estructura Acción más Tecnología más Resultado con métrica. Formula preguntas específicas cuando falta información clave. No infiere experiencia no declarada.

**Para qué sirve:**

Optimizar el currículum para superar filtros ATS y alinearse con los requerimientos del mercado técnico en desarrollo de software e inteligencia artificial. No redacta el currículum final de forma automática. Orienta y evalúa.

**Cómo usar:**

Se invoca como subagente de solo lectura. Requiere como entrada la ruta del currículum y, de forma opcional, la descripción de la oferta objetivo. Si no hay oferta, evalúa contra perfil Junior Full-Stack con fundamentos de IA.

Ejemplo de uso en opencode:

```text
Analiza docs/cv/cv-eduardo.pdf contra esta oferta de Full-Stack Junior y dime fortalezas y gaps de palabras clave.
```

Invocación programática mediante Task:

```text
subagent_type: cv-optimizer
prompt: Analizar el archivo indicado y devolver retroalimentación estructurada sin modificar archivos.
```

Configuración aplicada en `.opencode/agents/cv-optimizer.md`:

```text
mode: subagent
temperature: 0.1
color: info
permission:
  edit: deny
  bash: deny
  webfetch: deny
```

Salida obligatoria: Fortalezas, Gaps críticos, Palabras clave faltantes, Propuestas de reformulación, Preguntas para completar, Puntuación por criterio de 1 a 5.

### 2. interview-coach

**Qué hace:**

Simula entrevistas técnicas y conductuales para perfiles Full-Stack e Inteligencia Artificial. Solicita rol objetivo, stack y nivel antes de iniciar. Realiza una sola pregunta por turno y espera respuesta. Evalúa cada respuesta por precisión del concepto, terminología técnica y completitud con escala de 1 a 5. Si la respuesta es incompleta, realiza pregunta de seguimiento sin entregar la solución directa. Alterna teoría, diseño de sistemas y preguntas conductuales STAR. Ajusta la dificultad según desempeño.

**Para qué sirve:**

Preparar entrevistas reales, medir claridad técnica y capacidad de resolución de problemas, entrenar comunicación profesional bajo exigencia constructiva.

**Cómo usar:**

Se invoca como subagente interactivo en sesión. El usuario debe indicar rol objetivo, stack y nivel antes de iniciar.

Ejemplo de uso en opencode:

```text
Inicia simulacro para puesto Full-Stack Junior con stack React Node. Alterna una pregunta técnica y una conductual STAR. Una pregunta por turno.
```

Invocación programática mediante Task:

```text
subagent_type: interview-coach
prompt: Iniciar simulación de entrevista técnica y conductual con evaluación por turnos.
```

Configuración aplicada en `.opencode/agents/interview-coach.md`:

```text
mode: subagent
temperature: 0.3
color: warning
permission:
  edit: deny
  bash: deny
```

Regla de adaptación: dos evaluaciones consecutivas iguales o superiores a 4 aumentan dificultad. Dos evaluaciones iguales o inferiores a 2 reducen dificultad con pista socrática. No escribe archivos. Deriva a tracker-doc si se pide guardar resumen.

### 3. tracker-doc

**Qué hace:**

Organiza, redacta y estructura notas de estudio, guías técnicas y registros de avance en archivos Markdown dentro de `docs/`. Gestiona tres tipos: ejercicio, apunte y registro de progreso. Verifica existencia de directorio y archivo antes de escribir. Aplica encabezados, listas y bloques de código explicados. Registra con las cuatro secciones obligatorias: Objetivo, Conceptos clave, Enfoque planteado y Estado de resolución. Aplica convención `kebab-case` en nombres de archivo.

**Para qué sirve:**

Mantener documentación trazable del taller de empleo, normalizar apuntes de Employment Workshop 2026 y generar evidencia pública de progreso para GitHub y reclutadores.

**Cómo usar:**

Se invoca como subagente con permiso de escritura. Requiere tipo de contenido, título, apuntes en bruto y estado actual.

Ejemplo de uso en opencode:

```text
Documenta el ejercicio 01 de análisis CV en docs/ejercicios/ejercicio-01-analisis-cv.md con las cuatro secciones obligatorias.
```

Invocación programática mediante Task:

```text
subagent_type: tracker-doc
prompt: Crear o actualizar archivo en docs/ siguiendo estructura y convención kebab-case.
```

Configuración aplicada en `.opencode/agents/tracker-doc.md`:

```text
mode: subagent
temperature: 0.1
color: success
permission:
  edit: allow
  bash: deny
  webfetch: deny
```

Al finalizar devuelve ruta del archivo y lista de cumplimiento de formato. Referencia a `PLAN.md` cuando forma parte del seguimiento.

### 4. linkedin-optimizer

**Qué hace:**

Analiza titular, extracto y experiencia de LinkedIn. Verifica titular con rol, stack y propuesta de valor en un máximo de 220 caracteres. Verifica extracto en primera persona con stack, proyectos con métrica y llamada a contacto en un máximo de 2600 caracteres. Verifica cada experiencia con estructura Acción más Tecnología más Resultado con métrica y coherencia con CV y GitHub. No infiere experiencia no declarada.

**Para qué sirve:**

Optimizar el perfil de LinkedIn para perfil Junior Full-Stack con IA, mejorar descubrimiento por reclutadores y mantener coherencia entre LinkedIn, CV y GitHub. No reescribe el perfil de forma automática. Orienta y evalúa.

**Cómo usar:**

Se invoca como subagente de solo lectura. Requiere texto del titular actual, extracto actual y dos experiencias recientes. De forma opcional recibe oferta objetivo y enlaces a GitHub y portfolio. Si no hay oferta, evalúa contra perfil Junior Full-Stack con fundamentos de IA.

Ejemplo de uso en opencode:

```text
Revisa mi titular, extracto y dos experiencias de LinkedIn contra esta oferta Full-Stack Junior y dime gaps por sección.
```

Invocación programática mediante Task:

```text
subagent_type: linkedin-optimizer
prompt: Analizar titular, extracto y experiencia indicados y devolver informe por secciones sin modificar archivos.
```

Configuración aplicada en `.opencode/agents/linkedin-optimizer.md`:

```text
mode: subagent
temperature: 0.1
color: info
permission:
  edit: deny
  bash: deny
  webfetch: deny
```

Salida obligatoria: Fortalezas, Gaps críticos por sección titular extracto y experiencia, Palabras clave faltantes, Propuestas de reformulación por sección, Preguntas para completar, Puntuación por criterio de 1 a 5.

### 5. github-portfolio-reviewer

**Qué hace:**

Revisa cualquier repositorio vía MCP github en vivo. Consulta README, descripción corta, topics, campo about con demo, licencia y estado de fijado cuando la herramienta lo expone. Revisa README por bloques título, pitch, stack, demo, instalación, capturas y contacto. Revisa estrategia de fijados con un máximo de 6. Aplica protocolo de repo privado sin eludir controles. No infiere contenido no observado.

**Para qué sirve:**

Elevar el portfolio GitHub a estándar contratable, mejorar descubribilidad por topics y demo, mantener coherencia entre CV LinkedIn y GitHub, y tratar Aplika Jobs privado como case study público sin exponer propiedad intelectual. No edita repositorios. Orienta y evalúa.

**Cómo usar:**

Se invoca como subagente de solo lectura con permiso explícito para herramientas `github_*`. Requiere identificador propietario más repositorio o URL. Acepta uno o varios repos por sesión. De forma opcional recibe CV y LinkedIn para coherencia e indicación de público o privado.

Ejemplo de uso en opencode:

```text
Revisa vía MCP github edu84gp/pokedex_web y edu84gp/WhatsChatGPT con revisión completa y recomendación de fijados.
```

Invocación programática mediante Task:

```text
subagent_type: github-portfolio-reviewer
prompt: Revisar repos indicados vía MCP github y devolver informe por repositorio sin modificar archivos.
```

Configuración aplicada en `.opencode/agents/github-portfolio-reviewer.md`:

```text
mode: subagent
temperature: 0.1
color: accent
permission:
  edit: deny
  bash: deny
  github_*: allow
  webfetch: deny
  sequential-thinking_*: allow
  playwright_*: allow
```

Salida obligatoria por repositorio: Fortalezas, Gaps por bloque README descripción topics demo licencia y fijado, Propuestas de reescritura, Recomendación de fijados, Bloque de caso privado cuando aplique, Preguntas para completar, Puntuación por criterio de 1 a 5.

### 6. ats-checker

**Qué hace:**

Audita CV en PDF y Markdown como puerta técnica previa a cv-optimizer. Lee el archivo real en `cv/` para verificar existencia y contenido extraíble. Verifica parseo ATS con una sola columna y sin tablas ni imágenes con información. Verifica cobertura de keywords contra la oferta con coincidencia exacta y variantes. Verifica legibilidad con longitud y bullets con métrica. Calcula score de 0 a 100 y emite veredicto.

**Para qué sirve:**

Detectar bloqueos automáticos antes de la reescritura estratégica, priorizar correcciones por impacto en parseo y decidir derivación a cv-optimizer. No reescribe el CV. Audita y dictamina.

**Cómo usar:**

Se invoca como subagente de solo lectura con inspección local vía lectura y listado, sin bash. Requiere ruta del PDF o Markdown en `cv/`. Acepta ambos para comparar coherencia. Recibe oferta objetivo cuando exista. Si no hay oferta, evalúa contra Junior Full-Stack con IA.

Ejemplo de uso en opencode:

```text
Pasa ats-checker a cv/cv-eduardo.pdf contra esta oferta Full-Stack Junior y dame veredicto con checklist.
```

Invocación programática mediante Task:

```text
subagent_type: ats-checker
prompt: Auditar el CV indicado en PDF y Markdown y devolver veredicto con score sin modificar archivos.
```

Configuración aplicada en `.opencode/agents/ats-checker.md`:

```text
mode: subagent
temperature: 0.1
color: error
permission:
  edit: deny
  bash: deny
  webfetch: deny
```

Ponderación fija: parseo 35, keywords 35, legibilidad 20, coherencia PDF Markdown 10. Umbrales: APTO con 80 o más, CORREGIR de 60 a 79, NO APTO por debajo de 60.

Salida obligatoria: Veredicto y score con desglose, Checklist por bloque, Keywords faltantes, Correcciones priorizadas, Siguiente paso con derivación a cv-optimizer cuando el score sea inferior a 80.

### 7. cover-letter-drafter

**Qué hace:**

Redacta carta de presentación alineada a oferta y la guarda en `cv/cartas/` con convención kebab-case. Detecta el idioma de la oferta entre español e inglés y redacta la carta en ese idioma. Mapea tres requisitos nucleares contra CV y proyectos con evidencia. No inventa experiencia ni métricas.

**Para qué sirve:**

Producir cartas personalizadas por empresa y rol con límite de 250 palabras, declarar gaps sin maquillar y dejar trazabilidad de cada candidatura en `cv/cartas/`.

**Cómo usar:**

Se invoca como subagente con permiso de escritura limitado por prompt a `cv/cartas/`. Requiere texto de la oferta, CV base en `cv/` y dos proyectos con métrica. Verifica existencia de la carpeta y de carta previa para la misma empresa y rol antes de escribir.

Ejemplo de uso en opencode:

```text
Redacta carta para esta oferta Full-Stack Junior en Acme con mi CV de cv/ y guarda en cv/cartas/.
```

Invocación programática mediante Task:

```text
subagent_type: cover-letter-drafter
prompt: Redactar carta alineada a la oferta indicada y guardar en cv/cartas sin modificar otros directorios.
```

Configuración aplicada en `.opencode/agents/cover-letter-drafter.md`:

```text
mode: subagent
temperature: 0.3
color: primary
permission:
  edit: allow
  bash: deny
  webfetch: deny
```

Estructura fija: apertura con rol y motivación, encaje con dos pruebas con métrica, cierre con disponibilidad y contacto. Nombre de archivo `carta-empresa-rol-fecha.md`.

Salida obligatoria: Ruta del archivo guardado, Mapeo de requisitos contra evidencia, Gaps declarados, Preguntas para completar.

### 8. application-tracker

**Qué hace:**

Registra candidaturas en la base SQLite `docs/candidaturas/candidaturas.db` como fuente única de verdad y regenera la vista `docs/candidaturas/tabla-candidaturas.md` desde la base. Inserta filas nuevas sin alterar el historial y actualiza Estado, Contacto y Próximo paso. Enlaza Oferta, Carta en `cv/cartas/` y CV en `cv/` con rutas verificadas. Alerta de seguimientos vencidos.

**Para qué sirve:**

Mantener trazabilidad de cada candidatura con estado detallado y evidencias enlazadas, evitar duplicados y priorizar próximos pasos. La base permite consultas e histórico y la tabla Markdown queda como vista legible y versionada.

**Cómo usar:**

Se invoca como subagente con permiso de escritura limitado por prompt a `docs/candidaturas/` y acceso al MCP sqlite. Requiere empresa, rol, fecha y enlace a oferta. Recibe carta, CV, contacto y estado para actualización.

Ejemplo de uso en opencode:

```text
Registra candidatura en Acme Full-Stack Junior aplicada hoy con oferta, carta de cv/cartas y CV de cv/.
```

Invocación programática mediante Task:

```text
subagent_type: application-tracker
prompt: Registrar o actualizar candidatura en la base SQLite y regenerar la tabla Markdown en docs/candidaturas/ sin borrar historial.
```

Configuración aplicada en `.opencode/agents/application-tracker.md`:

```text
mode: subagent
temperature: 0.1
color: secondary
permission:
  edit: allow
  bash: deny
  webfetch: deny
  sqlite_*: allow
```

Estados válidos: aplicada, en-seguimiento, entrevista-tecnica, entrevista-final, oferta, descartada, archivada.

Salida obligatoria: Ruta de la base y de la tabla regenerada, Fila añadida o modificada con identificador, Alertas de seguimiento, Preguntas para completar.

### 9. behavioral-star-coach

**Qué hace:**

Construye banco de historias STAR amplio y practica solo conductual. Convierte anécdotas en estructura Situación más Tarea más Acción más Resultado con métrica. Cubre equipo, conflicto, error, aprendizaje bajo presión, iniciativa, liderazgo y logro. Formula una pregunta por turno y evalúa con escala de 0 a 10. Complementa a interview-coach sin duplicar teoría ni sistemas.

**Para qué sirve:**

Disponer de banco reutilizable de 90 a 120 segundos por historia, forzar especificidad con métrica y separar acción propia de acción del equipo.

**Cómo usar:**

Se invoca como subagente sin escritura. Requiere anécdotas en bruto, rol objetivo y banco existente cuando haya. Si se pide guardar, deriva a tracker-doc en `docs/apuntes/`.

Ejemplo de uso en opencode:

```text
Construye mi banco STAR amplio desde mis proyectos y practica una historia por turno con nota.
```

Invocación programática mediante Task:

```text
subagent_type: behavioral-star-coach
prompt: Construir banco STAR y evaluar historias sin modificar archivos.
```

Configuración aplicada en `.opencode/agents/behavioral-star-coach.md`:

```text
mode: subagent
temperature: 0.3
color: '#AB47BC'
permission:
  edit: deny
  bash: deny
  webfetch: deny
```

Criterios de 0 a 10: especificidad, acción propia verificable, métrica, aprendizaje y concisión. Exige métrica antes de validar historia.

Salida obligatoria: Banco en tabla con estado valida o en curso, Evaluación con nota global, Propuestas de refuerzo, Orden de derivación a tracker-doc.

### 10. job-search-strategist

**Qué hace:**

Prioriza ofertas de LinkedIn e InfoJobs con match variable de 0 a 100 y genera plan semanal guardado en `docs/candidaturas/plan-semanal-AAAA-MM-DD.md`. Consulta la base SQLite de candidaturas para no repetir registros. Pregunta umbral mínimo y objetivo semanal antes de priorizar. Clasifica en aplicar ahora, en seguimiento y descartar con motivo. Deriva el top a application-tracker y propone cartas a cover-letter-drafter.

**Para qué sirve:**

Convertir volumen de ofertas en foco ejecutable diario de lunes a viernes con trazabilidad por archivo semanal y conexión con registro y cartas.

**Cómo usar:**

Se invoca como subagente con permiso de escritura limitado por prompt a `docs/candidaturas/` y acceso al MCP sqlite en consulta. Requiere lista de ofertas, perfil base en `cv/`, umbral y objetivo. Sin umbral usa 70 y sin objetivo usa 10 tras confirmación.

Ejemplo de uso en opencode:

```text
Filtra estas 15 ofertas de LinkedIn e InfoJobs con umbral 75 y objetivo 8 y genera plan semanal.
```

Invocación programática mediante Task:

```text
subagent_type: job-search-strategist
prompt: Priorizar ofertas indicadas y guardar plan semanal sin tocar la tabla de candidaturas.
```

Configuración aplicada en `.opencode/agents/job-search-strategist.md`:

```text
mode: subagent
temperature: 0.2
color: '#26A69A'
permission:
  edit: allow
  bash: deny
  webfetch: deny
  fetch_*: allow
  sequential-thinking_*: allow
  sqlite_*: allow
```

Ponderación fija: stack 40, experiencia exigible 25, modalidad y ubicación 20, calidad de oferta 15.

Salida obligatoria: Tabla priorizada, Plan diario, Archivo guardado, Orden de derivación, Preguntas para completar.

### 11. live-coding-coach

**Qué hace:**

Simula live-coding por pasos con el stack del bootcamp: HTML CSS con responsive y BEM, JavaScript con DOM y asincronía, POO SOLID y MVC, Node Express con API REST, MongoDB con CRUD Prisma y Supabase, WebSockets con Socket.io, React con Redux y nociones de IA con RAG y MCP. Conduce con enunciado más restricciones, piensa en voz alta y un máximo de tres pistas sin desvelar la solución.

**Para qué sirve:**

Entrenar prueba técnica en vivo con comunicación, plan y código funcional sin recibir la solución directa.

**Cómo usar:**

Se invoca como subagente sin escritura. Requiere bloque objetivo, nivel Junior y tiempo disponible. Sin bloque propone secuencia desde fundamentos.

Ejemplo de uso en opencode:

```text
Simula live-coding de JavaScript asíncrono con 30 minutos por pasos y sin darme la solución.
```

Invocación programática mediante Task:

```text
subagent_type: live-coding-coach
prompt: Conducir simulacro de live-coding por pasos sin modificar archivos.
```

Configuración aplicada en `.opencode/agents/live-coding-coach.md`:

```text
mode: subagent
temperature: 0.4
color: '#EF6C00'
permission:
  edit: deny
  bash: deny
  webfetch: deny
```

Evaluación de 0 a 10: comprensión, plan en voz alta, código funcional, complejidad, comunicación y errores con casos borde. Deriva guardado a tracker-doc en `docs/ejercicios/`.

Salida obligatoria: Enunciado, Pistas dadas, Evaluación con nota global, Errores a reforzar, Orden de derivación.

### 12. networking-outreach

**Qué hace:**

Redacta mensajes de networking en LinkedIn y email para 7 escenarios: primer contacto con reclutador, solicitud de referido, vacante concreta, contacto tras evento, seguimiento tras 5 a 7 días de silencio, agradecimiento tras entrevista y reconexión. Ajusta longitud por canal con nota de conexión de 300 caracteres y email de 120 palabras. Registra contactos en `docs/networking/contactos-networking.md` sin duplicados.

**Para qué sirve:**

Abrir conversaciones reales con reclutadores y empleados con mensajes personalizados y trazables, evitar duplicados y controlar tiempos de seguimiento.

**Cómo usar:**

Se invoca como subagente con permiso de escritura limitado por prompt a `docs/networking/`. Requiere nombre, empresa, cargo, canal y contexto. Recibe oferta cuando aplique y mensaje previo con días transcurridos para seguimiento.

Ejemplo de uso en opencode:

```text
Redacta primer mensaje LinkedIn a una reclutadora de Acme para la vacante Full-Stack Junior y regístrala.
```

Invocación programática mediante Task:

```text
subagent_type: networking-outreach
prompt: Redactar mensaje para el contacto indicado y registrar en docs/networking sin modificar otros directorios.
```

Configuración aplicada en `.opencode/agents/networking-outreach.md`:

```text
mode: subagent
temperature: 0.3
color: '#5C6BC0'
permission:
  edit: allow
  bash: deny
  webfetch: deny
```

Estructura fija de mensaje: motivo específico, valor con prueba con métrica y petición única. Estados de contacto: contactado, respondido, referido, reunion-agendada, sin-respuesta, descartado. Deriva a application-tracker cuando derive en candidatura.

Salida obligatoria: Borrador listo con canal y longitud, Variante corta, Fila de tabla actualizada, Alertas de seguimiento, Orden de derivación, Preguntas para completar.

### 13. personal-brand-builder

**Qué hace:**

Crea estrategia, calendario y borradores de contenido técnico en LinkedIn y GitHub. Cubre cuatro pilares: aprendizaje del bootcamp y Employment Workshop 2026, proyectos con métrica, IA aplicada y agentes en opencode, y búsqueda de empleo en abierto. Redacta en español y guarda borradores en `docs/marca-personal/borradores/`. Propone canales futuros como blog dev.to, X y YouTube sin activarlos.

**Para qué sirve:**

Sostener una presencia técnica constante de 2 a 3 piezas por semana que posicione el perfil Junior Full-Stack con IA ante reclutadores y comunidad, con contenido verificable y sin grandilocuencia.

**Cómo usar:**

Se invoca como subagente con permiso de escritura limitado por prompt a `docs/marca-personal/`. Requiere objetivo de posicionamiento, público meta, proyectos y aprendizajes con métricas. Verifica calendario existente antes de añadir.

Ejemplo de uso en opencode:

```text
Genera estrategia y 3 piezas semanales para LinkedIn y GitHub desde mis proyectos con métrica.
```

Invocación programática mediante Task:

```text
subagent_type: personal-brand-builder
prompt: Crear calendario y borradores en docs/marca-personal sin publicar en redes.
```

Configuración aplicada en `.opencode/agents/personal-brand-builder.md`:

```text
mode: subagent
temperature: 0.4
color: '#C2185B'
permission:
  edit: allow
  bash: deny
  webfetch: deny
```

Estados de pieza: idea, borrador, revisado, publicado. LinkedIn con máximo 1300 caracteres y GitHub con README o descripción concisa. Idioma español único hasta ampliar.

Salida obligatoria: Estrategia breve, Calendario actualizado, Borradores con ruta, Alertas de piezas sin métrica, Orden de derivación a github-portfolio-reviewer, Preguntas para completar.

### 14. salary-negotiator

**Qué hace:**

Prepara la negociación del paquete completo: salario base, modalidad, formación, bonos, equipo, fecha de inicio y revisión a 6 y 12 meses. Cubre 5 escenarios: primera oferta, contraoferta, subida tras prueba, dos ofertas a la vez y expectativa en criba. Fija mínimo, objetivo y BATNA antes de redactar. Genera guion de llamada, borrador de email y tabla de límites. Contrasta la oferta frente a rangos de mercado aportados o vía MCP de búsqueda cuando exista.

**Para qué sirve:**

Negociar con método y sin improvisar, proteger tu mínimo, priorizar beneficios cuando el salario está fijo y registrar el historial por oferta.

**Cómo usar:**

Se invoca como subagente con permiso de escritura limitado por prompt a `docs/negociacion/`. Requiere oferta, mínimo, objetivo y rangos de mercado. Sin mínimo o BATNA no redacta y pregunta.

Ejemplo de uso en opencode:

```text
Prepara la negociación de la oferta de Acme con mínimo 22000, objetivo 26000 y este rango de mercado.
```

Invocación programática mediante Task:

```text
subagent_type: salary-negotiator
prompt: Preparar guion email y tabla de limites y guardar en docs/negociacion sin modificar otros directorios.
```

Configuración aplicada en `.opencode/agents/salary-negotiator.md`:

```text
mode: subagent
temperature: 0.2
color: '#546E7A'
permission:
  edit: allow
  bash: deny
  webfetch: deny
```

Reglas clave: nunca dar la primera cifra, anclar con rango y justificación, priorizar el paquete completo y no aceptar en la misma llamada. Estados: oferta-recibida, preparando, negociando, contraofertado, acordada, rechazada. Deriva a application-tracker al pasar a oferta o acordada.

Salida obligatoria: Tabla de límites, Guion por fases, Borrador de email, Registro actualizado, Alertas de datos faltantes, Orden de derivación, Preguntas para completar.

### 15. course-exercise-solver

**Qué hace:**

Tutor socrático transversal para los ejercicios del Employment Workshop 2026. Reformula el enunciado, identifica conceptos clave y guía con preguntas antes que con respuestas. Cubre cualquier tipo de ejercicio, de código, análisis, CV, entrevistas, networking o documentos. Deriva al agente experto cuando el tema es específico. Escala la ayuda en cuatro niveles y solo da solución completa si se pide de forma explícita, conforme a `AGENTS.md`. Mantiene el índice en `docs/ejercicios/indice-ejercicios.md` y pasa el registro individual a tracker-doc.

**Para qué sirve:**

Comprender y resolver los ejercicios del curso con método, fomentar el aprendizaje real y mantener un índice con enlaces que evidencia avance y cobertura del temario.

**Cómo usar:**

Se invoca como subagente con permiso de escritura limitado por prompt a `docs/ejercicios/`. Requiere el enunciado y, si existe, el intento de la persona. Sin intento no aporta pistas.

Ejemplo de uso en opencode:

```text
Ayúdame con este ejercicio del módulo de async en JavaScript. Mi intento es este.
```

Invocación programática mediante Task:

```text
subagent_type: course-exercise-solver
prompt: Guiar el ejercicio socraticamente, actualizar el indice y derivar el registro a tracker-doc.
```

Configuración aplicada en `.opencode/agents/course-exercise-solver.md`:

```text
mode: subagent
temperature: 0.3
color: '#795548'
permission:
  edit: allow
  bash: deny
  webfetch: deny
```

Escala de ayuda: pregunta socrática, pista, esquema o pseudocódigo, y solución completa solo bajo petición explícita. Derivaciones: cv-optimizer, live-coding-coach, interview-coach, behavioral-star-coach, cover-letter-drafter, job-search-strategist, linkedin-optimizer, github-portfolio-reviewer, networking-outreach y salary-negotiator. Único archivo propio: `docs/ejercicios/indice-ejercicios.md`.

Salida obligatoria: Enunciado reformulado, Conceptos clave, Preguntas o nivel de ayuda, Enfoque planteado, Agente experto a derivar, Orden de derivación a tracker-doc, Índice actualizado, Preguntas para completar.

---

## MCPs

Configuración canónica en `opencode.json` con formato `type local`, `command` como arreglo y `environment` con sustitución `{env:VARIABLE}`. Archivo legacy `.opencode/mcp.json` higienizado sin token hardcodeado.

Los tools de un MCP se registran en opencode con el nombre del servidor como prefijo. Por eso los permisos por agente usan el patrón `servidor_*`, por ejemplo `github_*`, `context7_*` o `fetch_*`.

Protección aplicada: `.gitignore` con entradas `.env` y `node_modules/`. Plantilla `.env.example` con claves vacías para `GITHUB_PERSONAL_ACCESS_TOKEN` y `CONTEXT7_API_KEY`.

Política de acceso MCP: `context7_*`, `fetch_*`, `sequential-thinking_*`, `playwright_*` y `sqlite_*` están denegados a nivel global en `opencode.json` y habilitados solo en los agentes que los usan, mediante el bloque `permission` de cada agente. Al poner el permiso en `deny`, la herramienta queda deshabilitada y no consume contexto en el resto de agentes. Los agentes primarios `build` y `plan` también los tienen habilitados en `opencode.json` para poder invocarlos directamente sin delegar. El MCP sqlite además queda acotado a `application-tracker` y `job-search-strategist` por contener datos de candidaturas.

### 1. github

**Qué hace:**

Opera con `@modelcontextprotocol/server-github`. Expone herramientas para consultar repositorios, ramas, issues y pull requests del usuario autenticado.

**Para qué sirve:**

Evidenciar progreso en GitHub, revisar repositorios del portfolio y preparar pushes de documentación sin salir de opencode.

**Cómo usar:**

Requiere variable `GITHUB_PERSONAL_ACCESS_TOKEN` definida en entorno o archivo `.env` no versionado. Procedimiento: copiar `.env.example` a `.env`, definir el token con alcance mínimo de lectura y exportar la variable antes de iniciar opencode. No versionar el archivo `.env`. Si el servidor no responde, verificar que el paquete se ejecuta con `npx -y` y que la variable está exportada.

### 2. filesystem

**Qué hace:**

Opera con `@modelcontextprotocol/server-filesystem` con raíz `.`. Expone lectura y listado controlado dentro del proyecto.

**Para qué sirve:**

Permitir a cv-optimizer, interview-coach, tracker-doc, linkedin-optimizer, github-portfolio-reviewer y ats-checker leer `docs/`, `cv/` y `PLAN.md` sin acceso fuera del repositorio.

**Cómo usar:**

No requiere secreto. Está habilitado por defecto en `opencode.json`. Invocado automáticamente por los subagentes para leer y listar. Si se amplía la raíz fuera de `.`, actualizar `opencode.json` y documentar el motivo en este archivo.

### 3. memory

**Qué hace:**

Opera con `@modelcontextprotocol/server-memory`. Almacena entidades, observaciones y relaciones entre sesiones. Desde la Fase 20 persiste en `docs/memoria/memoria.local.json` mediante la variable `MEMORY_FILE_PATH`, en lugar de la ruta por defecto dentro de la caché de npx. La ruta debe ser absoluta: el proceso del servidor trabaja con su propio directorio de trabajo (la caché de npx), así que una ruta relativa resuelve contra esa caché y falla con ENOENT. El fichero se escribe en formato JSON Lines, con un registro JSON completo por línea (entidad o relación); al editarlo a mano hay que mantener ese formato porque el servidor lo carga línea a línea y cualquier línea ilegible se ignora conservándola en el siguiente guardado.

**Para qué sirve:**

Mantener continuidad entre sesiones del taller: decisiones tomadas, estado de fases y preferencias del usuario. Complementa a los ficheros versionados `docs/memoria/estado-actual.md` y `docs/memoria/decisiones.md`, que dan la vista legible.

**Cómo usar:**

No requiere secreto. El agente primario lo utiliza para recordar contexto. Uso recomendado: guardar hito al completar cada fase con fecha, archivos creados y siguiente paso. Si el grafo crece, podar observaciones obsoletas para controlar el contexto. El fichero local está excluido de git por `.gitignore` con el patrón `docs/memoria/*.local.json`; para respaldarlo, copiarlo junto al resto de `docs/memoria/`.

### 4. fetch

**Qué hace:**

Opera con `mcp-server-fetch`, el servidor oficial de modelcontextprotocol para descarga web. Expone una herramienta `fetch` que recupera una URL y devuelve su contenido en markdown, texto o html, con control de longitud máxima y de redirecciones. Se ejecuta con `uvx mcp-server-fetch` sobre Python gestionado por `uv`.

**Para qué sirve:**

Permitir a los agentes de investigación consultar ofertas de empleo, páginas de empresa y documentación web dentro de su propio razonamiento, encadenando varias peticiones y controlando el formato. Complementa a la herramienta `webfetch` integrada de opencode.

**Cómo usar:**

Requiere `uv` instalado con su binario `uvx` en el PATH. En Windows se instala con `winget install --id astral-sh.uv -e`. El paquete `mcp-server-fetch` se descarga automáticamente en el primer arranque. La primera vez descarga un Python gestionado, por lo que el primer inicio puede tardar más. No requiere secreto. Habilitado por defecto en `opencode.json`. Uso en agentes permitidos: job-search-strategist, salary-negotiator, cv-optimizer y ats-checker, mediante `fetch_*: allow`.

### 5. context7

**Qué hace:**

Opera como servidor MCP remoto en `https://mcp.context7.com/mcp`. Expone herramientas para resolver el identificador de una librería y recuperar su documentación oficial actualizada. Admite una clave de API en la cabecera `CONTEXT7_API_KEY` para elevar los límites de uso.

**Para qué sirve:**

Dar a los agentes de código documentación oficial y versionada de librerías y frameworks sin depender del conocimiento del modelo, reduciendo respuestas desactualizadas.

**Cómo usar:**

Requiere la variable de entorno `CONTEXT7_API_KEY` definida en `.env` no versionado o exportada antes de iniciar opencode. Obtener la clave en context7.com con una cuenta gratuita. En los prompts, basta con añadir `use context7` o referir el servidor por su nombre. Habilitado por defecto en `opencode.json`. Uso en agentes permitidos: course-exercise-solver, live-coding-coach e interview-coach, mediante `context7_*: allow`. Si el servidor no responde, verificar la clave y la conectividad a mcp.context7.com.

### 6. sequential-thinking

**Qué hace:**

Opera con `@modelcontextprotocol/server-sequential-thinking`. Expone una herramienta que permite al modelo registrar y revisar cadenas de razonamiento paso a paso, con posibilidad de corregir y ramificar el pensamiento antes de concluir. Se ejecuta con `npx -y @modelcontextprotocol/server-sequential-thinking`.

**Para qué sirve:**

Estructurar análisis de decisiones con múltiples factores y compensaciones antes de responder, útil en negociación, priorización de ofertas, resolución de ejercicios y revisión de portfolio. Mejora la trazabilidad del razonamiento en tareas complejas.

**Cómo usar:**

No requiere secreto. Habilitado por defecto en `opencode.json`. Uso en agentes permitidos: salary-negotiator, job-search-strategist, course-exercise-solver y github-portfolio-reviewer, además de los primarios build y plan, mediante `sequential-thinking_*: allow`. Conviene no abusar de esta herramienta, ya que añade contexto; reservarla para decisiones con varios factores.

### 7. playwright

**Qué hace:**

Opera con `@playwright/mcp`, el servidor de automatización de navegador de Microsoft. Expone herramientas para navegar, inspeccionar el DOM, hacer clics, rellenar formularios y tomar capturas de pantalla. Se ejecuta con `npx -y @playwright/mcp --headless`, en modo sin ventana y con el chromium por defecto.

**Para qué sirve:**

Verificar visualmente el portfolio y las demos desplegadas: comprobar que las páginas cargan, revisar layouts y capturar pantallas para validar el resultado antes de enseñarlo a reclutadores.

**Cómo usar:**

No requiere secreto. Los navegadores de Playwright ya están instalados en la caché del sistema, por lo que no descarga binarios. La opción `--browser` acepta chrome, firefox, webkit o msedge; al omitirla se usa el chromium por defecto. A diferencia de otros MCPs, playwright expone muchas herramientas, así que su permiso `playwright_*` se deniega globalmente y solo se habilita en github-portfolio-reviewer, build y plan. Si un sitio bloquea la automatización, revisar `--user-agent` o `--ignore-https-errors`.

### 8. sqlite

**Qué hace:**

Opera con `mcp-server-sqlite` en local vía uvx. Expone herramientas para consultar y modificar una base de datos SQLite: listar tablas, leer el esquema, ejecutar consultas de lectura y de escritura. Se ejecuta con `uvx --with "mcp<2" mcp-server-sqlite --db-path docs/candidaturas/candidaturas.db`, creando la base si no existe.

**Para qué sirve:**

Guardar el historial de candidaturas como fuente única de verdad, permitiendo consultas e informes que la tabla Markdown no ofrece. La tabla `docs/candidaturas/tabla-candidaturas.md` se regenera desde la base como vista legible y versionada. La base queda fuera de git por contener datos personales.

**Cómo usar:**

No requiere secreto. Habilitado por defecto en `opencode.json`. Debe estar en `deny` global por contener datos sensibles y habilitarse por agente. Uso en agentes permitidos: application-tracker, job-search-strategist y los primarios build y plan, mediante `sqlite_*: allow`. El esquema de la tabla `candidaturas` lo define application-tracker y se crea al primer uso con `CREATE TABLE IF NOT EXISTS`.

El pin `--with "mcp<2"` es necesario: el servidor oficial usa la API `Server.list_resources`, retirada en el SDK 2.x. Sin el pin, uvx resuelve el SDK nuevo y el servidor arranca y cae con error `AttributeError: 'Server' object has no attribute 'list_resources'`, que opencode muestra como `MCP error -32000: Connection closed`. Con el pin responde al handshake y expone read_query, write_query, create_table, list_tables, describe_table y append_insight.

### Respaldo externo pendiente de evaluación: Notion y Google Drive

**Qué hace:**

Notion dispone de MCP oficial con `@notionhq/notion-mcp-server` y Google Drive con `@modelcontextprotocol/server-gdrive`. Permitirían respaldar o sincronizar las candidaturas fuera del repositorio.

**Para qué sirve:**

Tener una copia externa del historial de candidaturas y acceder a ella desde otros dispositivos.

**Cómo usar:**

No implementado en la Fase 18. Evaluación pendiente: Notion es la vía de menor fricción porque solo requiere crear una integración y aportar un `NOTION_TOKEN`; Google Drive exige crear un proyecto en Google Cloud y credenciales OAuth, con más montaje. Ambas opciones suman herramientas al contexto, por lo que se añadirán solo si se decide respaldar fuera del repositorio.

---

## Comandos

Los comandos viven en `.opencode/commands/` con nombres en inglés kebab-case, coherentes con los nombres de los agentes, y se invocan en la TUI con `/nombre`. El campo `agent` decide quién los ejecuta y `subtask: false` evita que se conviertan en subtareas de un solo turno, permitiendo conversación interactiva.

### 1. cv-review

Pipeline de revisión de CV en dos pasos con control humano. Lanza ats-checker y presenta el veredicto con score y correcciones; si el score es inferior a 80, pregunta antes de lanzar cv-optimizer con el informe ATS como contexto. Ejecutado por `build`.

Uso: `/cv-review cv/cv-eduardo.pdf contra esta oferta ...`

### 2. linkedin-review

Análisis del perfil de LinkedIn con informe, gaps por bloque y checklist de acciones. Lo ejecuta directamente el agente `linkedin-optimizer`, que no navega LinkedIn y trabaja con lo que se le pegue.

Uso: `/linkedin-review` y a continuación pegar titular, extracto y experiencias.

### 3. interview-technical

Simulacro de entrevista técnica de Junior Full-Stack con IA, pregunta a pregunta y una sola por turno, con informe final y rúbrica de 0 a 10. Lo ejecuta el agente `interview-coach`.

Uso: `/interview-technical nivel junior stack React y Node dificultad media`

### 4. interview-behavioral

Práctica conductual con respuestas STAR, una historia por turno, rúbrica de 0 a 10 y huecos del banco al cierre. Lo ejecuta el agente `behavioral-star-coach`.

Uso: `/interview-behavioral para esta oferta ...`

### 5. interview-live-coding

Simulacro de live-coding por pasos con el stack del bootcamp y máximo tres pistas sin desvelar la solución, con errores por categoría al final. Lo ejecuta el agente `live-coding-coach`.

Uso: `/interview-live-coding React con estado y petición a API`

### 6. log-progress

Registro de avance con trazabilidad completa: apunte en `docs/apuntes/` delegado a tracker-doc, entrada en `CHANGELOG-progreso.md` y, solo con confirmación, checkbox de fase y estado en `PLAN.md`. Ejecutado por `build`.

Uso: `/log-progress hoy terminé el módulo de hooks de React`

Si un comando con `agent` apuntando a un subagente no mantiene la conversación interactiva en la sesión, la alternativa es convertir ese agente a `mode: all` y cambiar de agente con Tab antes de conversar.

---

## Skills

Los skills viven en `.opencode/skills/<nombre>/SKILL.md` y se cargan solos cuando la tarea encaja con su descripción. Se eligieron tres para no duplicar lo que ya cubren los agentes y `AGENTS.md`.

### 1. flujo-candidatura

Pipeline de candidatura en seis etapas con el agente que interviene en cada una: priorización con job-search-strategist, revisión de CV con `/cv-review`, carta con cover-letter-drafter, registro con application-tracker, contacto con networking-outreach y negociación con salary-negotiator. Incluye los estados válidos y las reglas de no inventar rutas ni avanzar de estado sin evidencia.

### 2. apunte-ejercicio

Estructura obligatoria de apuntes y registros de ejercicios: Objetivo, Conceptos clave, Enfoque planteado y Estado de resolución. Recuerda las convenciones de kebab-case, el índice en `docs/ejercicios/indice-ejercicios.md` y el reparto de agentes entre course-exercise-solver, tracker-doc y los coaches.

### 3. memoria-sesion

Ciclo de memoria entre sesiones: al retomar trabajo, leer `docs/memoria/estado-actual.md` y consultar `docs/memoria/decisiones.md` antes de contradecir decisiones previas; al cerrar hito, actualizar ambos, ampliar el grafo del Memory MCP y usar `/log-progress` para el registro completo.

### Memoria del proyecto

La carpeta `docs/memoria/` contiene la vista versionada del proyecto:

- `estado-actual.md`: foto viva con la última actualización, la fase, el siguiente paso y los bloqueos.
- `decisiones.md`: registro de decisiones con fecha, decisión, motivo y alternativas descartadas.
- `memoria.local.json`: grafo del Memory MCP en formato JSON Lines, excluido de git.

El detalle de cada decisión también se refleja en el grafo del Memory MCP, que los agentes pueden consultar con read_graph o search_nodes.

---

## Visibilidad en GitHub

El repositorio es público en https://github.com/edu84gp/ai-job-search-copilot. El `.gitignore` excluye los datos sensibles: `cv/*` salvo su README, `docs/networking/contactos-networking.md`, `docs/negociacion/registro-negociaciones.md`, `docs/memoria/*.local.json`, `docs/candidaturas/*.db` y `.env`. La tabla `docs/candidaturas/tabla-candidaturas.md` sí se publica como evidencia del proceso.

**Calidad con GitHub Actions:** `.github/workflows/quality.yml` se ejecuta en cada push a main, en pull requests y manualmente. Dos trabajos: lint de Markdown con `DavidAnson/markdownlint-cli2-action` sobre `**/*.md` y verificación de enlaces con `lycheeverse/lychee-action`. La configuración del lint vive en `.markdownlint-cli2.jsonc`, que desactiva MD013, MD025, MD033, MD034, MD036 y MD040 por el estilo del proyecto (tablas largas, HTML embebido, URLs visibles) e ignora `node_modules/` y los prompts de `.opencode/agents` y `.opencode/commands` por no ser documentos. `.lycheeignore` excluye LinkedIn (bloquea automatización) y el endpoint MCP de context7 (solo acepta POST).

**GitHub Pages en los proyectos:** cada repo estático tiene su propio `.github/workflows/deploy-pages.yml` con `actions/checkout@v6`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3` y `actions/deploy-pages@v5`. Pages se activó vía API REST con `build_type=workflow`. Demos: https://edu84gp.github.io/pokedex_web/ y https://edu84gp.github.io/el-juego-de-la-vida/. WhatsChatGPT no se despliega porque necesita servidor con Ollama.

**Kanban de candidaturas:** Project v2 público en https://github.com/users/edu84gp/projects/3 con el campo propio `Pipeline` (Aplicada, En seguimiento, Entrevista tecnica, Entrevista final, Oferta, Descartada) y vinculado al repositorio.

**gh CLI:** instalado con winget (GitHub.cli 2.102.0) y autenticado con el PAT de `.env` mediante `gh auth login --with-token`. Scopes del token: gist, project, read:org, repo y workflow, suficientes para push, workflows y Projects.

## Cambios aplicados en optimización

- Eliminado bloque deprecado `tools: read_file, list_dir, write_file` en cv-optimizer, interview-coach y tracker-doc.
- Añadido bloque `permission` con control `edit`, `bash` y `webfetch` en los 15 agentes. github-portfolio-reviewer añade `github_*: allow` para consulta viva vía MCP github. cover-letter-drafter, job-search-strategist, application-tracker, networking-outreach, personal-brand-builder, salary-negotiator, course-exercise-solver y tracker-doc usan `edit: allow` limitado por prompt a `cv/cartas/`, `docs/candidaturas/`, `docs/networking/`, `docs/marca-personal/`, `docs/negociacion/`, `docs/ejercicios/` y `docs/`.
- Añadidos `temperature` y `color` diferenciados: 0.1 para análisis y documentación determinista, 0.3 para entrevista con variabilidad controlada.
- Reescritas las descripciones con criterio de uso para mejorar la autodelegación del agente primario.
- Añadidos contratos de entrada, rúbricas de 1 a 5 y reglas anti-especulación.
- Añadido protocolo de inicio y adaptación de dificultad en interview-coach.
- Añadida verificación previa y plantilla obligatoria en tracker-doc.
- Creado linkedin-optimizer en Fase 3 con el mismo estándar.
- Creado github-portfolio-reviewer en Fase 4 como agente genérico con revisión completa y protocolo de repo privado tipo Aplika Jobs.
- Creado ats-checker en Fase 5 como puerta previa a cv-optimizer con score 0 a 100 y veredicto APTO CORREGIR NO APTO.
- Creado cover-letter-drafter en Fase 6 con redacción en idioma de oferta y guardado en cv/cartas/.
- Creado application-tracker en Fase 8 con tabla Markdown en docs/candidaturas/ y estados detallados.
- Creado behavioral-star-coach en Fase 9 con banco amplio y rúbrica de 0 a 10.
- Creado job-search-strategist en Fase 7 con match variable y plan semanal en docs/candidaturas/.
- Creado live-coding-coach en Fase 10 con stack del bootcamp y protocolo por pasos sin solución directa.
- Creado networking-outreach en Fase 11 con LinkedIn y email, 7 escenarios y registro en docs/networking/.
- Creado personal-brand-builder en Fase 12 con estrategia calendario y borradores en docs/marca-personal/.
- Creado salary-negotiator en Fase 13 con paquete completo, 5 escenarios y registro en docs/negociacion/.
- Creado course-exercise-solver en Fase 14 con guía socrática transversal, índice en docs/ejercicios/ y derivaciones a expertos.
- Añadidos MCPs fetch y context7 en Fase 15. fetch oficial vía uvx en local y context7 remoto con clave. Permisos `context7_*` y `fetch_*` denegados globalmente y habilitados por agente: context7 en course-exercise-solver, live-coding-coach e interview-coach; fetch en job-search-strategist, salary-negotiator, cv-optimizer y ats-checker. El agente primario build queda habilitado para ambos. Añadida `CONTEXT7_API_KEY` a .env.example y .env.
- Añadido MCP sequential-thinking en Fase 16. Permiso `sequential-thinking_*` denegado globalmente y habilitado en salary-negotiator, job-search-strategist, course-exercise-solver y github-portfolio-reviewer, además de los primarios build y plan.
- Añadido MCP playwright en Fase 17 en modo headless con el chromium ya instalado. Permiso `playwright_*` denegado globalmente y habilitado en github-portfolio-reviewer, build y plan.
- Añadido MCP sqlite en Fase 18 con `mcp-server-sqlite` vía uvx. La base `docs/candidaturas/candidaturas.db` pasa a ser la fuente única de candidaturas y la tabla Markdown se regenera desde ella. Base fuera de git por contener datos personales. Permiso `sqlite_*` denegado globalmente y habilitado en application-tracker, job-search-strategist, build y plan. Actualizado application-tracker al flujo SQLite y job-search-strategist a la consulta de la base. Documentada la evaluación de respaldo externo con Notion y Google Drive, sin implementar.
- Corregido el MCP sqlite en Fase 18: el servidor oficial chocaba con el SDK 2.x del protocolo y caía con `Connection closed`. Se fija el SDK con `--with "mcp<2"` y se verifica el handshake y el listado de herramientas contra una base temporal.
- Creados 6 comandos en Fase 19 dentro de `.opencode/commands/`: cv-review y log-progress ejecutados por build, linkedin-review, interview-technical, interview-behavioral e interview-live-coding ejecutados por su agente especialista con `subtask: false` para permitir interacción.
- Migradas las directrices globales en Fase 19 de `.opencode/rules.md` a `AGENTS.md` en la raíz, el archivo que opencode carga automáticamente. El anterior rules.md no se estaba cargando porque no figuraba en `instructions` de `opencode.json`. Actualizadas las referencias en PLAN, referencia técnica y course-exercise-solver.
- Creada la memoria del proyecto en Fase 20: Memory MCP con `MEMORY_FILE_PATH` en `docs/memoria/memoria.local.json` fuera de git, más `docs/memoria/estado-actual.md` y `docs/memoria/decisiones.md` versionados. AGENTS.md indica leerlos al iniciar sesión y actualizarlos al cerrar hitos.
- Creados 3 skills en Fase 20 dentro de `.opencode/skills/`: flujo-candidatura, apunte-ejercicio y memoria-sesion. Se descartaron skills de convenciones y de revisión de portfolio por solapar con AGENTS.md y con github-portfolio-reviewer.
- Ampliado el comando log-progress en Fase 20 para actualizar la memoria del proyecto antes del CHANGELOG.
- Publicado el repositorio en Fase 21 tras autenticar gh CLI con el PAT existente. `.gitignore` ampliado para excluir CV, contactos, negociaciones y base de datos; la tabla de candidaturas se publica.
- Reescrito el README en Fase 21 en bilingüe orientado a reclutadores: badges, stack, proyectos con demos, pipeline de candidatura y tabla de evidencias con el Kanban.
- Añadido en Fase 21 el workflow `Calidad` con markdownlint-cli2 y lychee, más `.markdownlint-cli2.jsonc` y `.lycheeignore`. Corregidos separadores de tablas, MD037 en CHANGELOG y creado `docs/apuntes/README.md` para que las carpetas vacías existan en git.
- Añadido en Fase 21 `deploy-pages.yml` a pokedex_web y el-juego-de-la-vida, activado Pages por API con build_type workflow y configuradas descripciones y homepage de ambos repos.
- Creado en Fase 21 el Project público de candidaturas (#3) con campo Pipeline propio y vinculado al repositorio.
- Corregido el Memory MCP tras la Fase 21: `MEMORY_FILE_PATH` pasa a ruta absoluta porque el servidor resuelve las relativas contra la caché de npx y las escrituras fallaban con ENOENT.
- Sembrado tras la Fase 21 el grafo del Memory MCP con los hitos de las fases 0 a 21: 5 entidades y 5 relaciones. El servidor v2.0.0 usa formato JSON Lines, así que la siembra manual como objeto JSON único cargaba vacía; verificado arrancando el servidor contra el fichero.
- Cerrada la Fase 22 con la auditoría final: permisos y frontmatter de los 15 agentes, handshakes de los 8 MCPs, comandos, skills, coherencia documental y seguridad del repo (sin secretos, .env ignorado). Corregidos interview-coach (`webfetch: deny`) y `.playwright-mcp/` en .gitignore. Pase de github-portfolio-reviewer y correcciones en los repos de proyectos: licencias MIT, topics, tildes y CTA de pokedex_web.
- Renombrado el repositorio de job-support-portfolio a ai-job-search-copilot el 2026-10-19 por orientación a reclutadores; GitHub mantiene el redirect 301 de la URL antigua y se actualizaron badges, referencias de documentación y `MEMORY_FILE_PATH` con la carpeta local renombrada a juego.

## Referencias técnicas

- Definiciones de agentes: `.opencode/agents/cv-optimizer.md`, `.opencode/agents/interview-coach.md`, `.opencode/agents/tracker-doc.md`, `.opencode/agents/linkedin-optimizer.md`, `.opencode/agents/github-portfolio-reviewer.md`, `.opencode/agents/ats-checker.md`, `.opencode/agents/cover-letter-drafter.md`, `.opencode/agents/application-tracker.md`, `.opencode/agents/behavioral-star-coach.md`, `.opencode/agents/job-search-strategist.md`, `.opencode/agents/live-coding-coach.md`, `.opencode/agents/networking-outreach.md`, `.opencode/agents/personal-brand-builder.md`, `.opencode/agents/salary-negotiator.md`, `.opencode/agents/course-exercise-solver.md`
- Comandos: `.opencode/commands/cv-review.md`, `.opencode/commands/linkedin-review.md`, `.opencode/commands/interview-technical.md`, `.opencode/commands/interview-behavioral.md`, `.opencode/commands/interview-live-coding.md`, `.opencode/commands/log-progress.md`
- Skills: `.opencode/skills/flujo-candidatura/SKILL.md`, `.opencode/skills/apunte-ejercicio/SKILL.md`, `.opencode/skills/memoria-sesion/SKILL.md`
- Memoria: `docs/memoria/estado-actual.md`, `docs/memoria/decisiones.md` y `docs/memoria/memoria.local.json` fuera de git
- Directrices globales: `AGENTS.md`
- MCPs: `opencode.json` canónico y `.opencode/mcp.json` legacy. Claves en `.env` no versionado y `.env.example` como plantilla: `GITHUB_PERSONAL_ACCESS_TOKEN` y `CONTEXT7_API_KEY`.
- Calidad: `.github/workflows/quality.yml`, `.markdownlint-cli2.jsonc` y `.lycheeignore`
- Despliegue: `.github/workflows/deploy-pages.yml` en los repos pokedex_web y el-juego-de-la-vida
- Visibilidad: repositorio en https://github.com/edu84gp/ai-job-search-copilot y Kanban en https://github.com/users/edu84gp/projects/3
- Plan de aplicación: `PLAN.md`
