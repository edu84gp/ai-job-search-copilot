# Guía de uso de `ai-job-search-copilot`

## Objetivo

Explicar cómo se usa el repositorio `ai-job-search-copilot` durante el Employment Workshop 2026: qué piezas lo componen, cómo se invoca cada una, qué orden sigue una candidatura y cómo se cierra una sesión sin perder trazabilidad.

Esta guía es operativa. El detalle técnico de cada agente, MCP, comando y skill vive en `docs/referencia-agentes-mcps.md`; el plan por fases, en `PLAN.md`. Algunas rutas citadas viven en `docs/privado/` y no se publican en GitHub; se incluyen como referencia interna para quien ejecuta el sistema.

Al terminar la lectura, una persona que abra el repositorio por primera vez debe poder:

- Reconocer las cinco capas del sistema y la función de cada una.
- Comprobar que el entorno está completo antes de trabajar.
- Elegir entre lenguaje natural, comando o subagente según la tarea.
- Ejecutar el pipeline de candidatura en el orden correcto.
- Registrar apuntes, ejercicios, entrevistas y avances sin duplicar información.
- Saber qué se publica y qué queda fuera de git.

## Conceptos clave

### Modelo mental de cinco capas

El sistema se lee de arriba abajo: las directrices fijan el comportamiento, los agentes ejecutan, los comandos ordenan secuencias, los skills aportan procedimiento y los MCPs conectan herramientas externas.

| Capa | Dónde vive | Qué aporta | Cuándo se toca |
| --- | --- | --- | --- |
| Directrices | `AGENTS.md` | Rol, idioma, método, formato y memoria | Al cambiar una regla global |
| Agentes | `.opencode/agents/` | Especialistas con permisos y contrato de salida | Al crear o ajustar un especialista |
| Comandos | `.opencode/commands/` | Secuencias repetibles con agente fijado | Al estabilizar un flujo |
| Skills | `.opencode/skills/` | Procedimiento y convenciones por tarea | Al documentar cómo se hace algo |
| MCPs | `opencode.json` | Herramientas externas acotadas por permisos | Al conectar un servicio |

**Directrices.** `AGENTS.md` es el archivo de directrices que el agente primario carga al iniciar la sesión. Fija el rol de tutor técnico, el español como idioma único, la prohibición de dar soluciones directas sin petición explícita, el formato de los bloques de código, la organización de `docs/` y el ciclo de memoria. Si una regla global cambia, se cambia ahí y no en cada agente.

**Agentes.** Los 15 subagentes de `.opencode/agents/` son especialistas. Cada archivo combina frontmatter con `description`, `mode`, `temperature` y `permission`, y un cuerpo que actúa como system prompt. Los de solo lectura auditan; los de escritura guardan en una carpeta acotada. Se ejecutan en sesiones hijas y devuelven un informe con contrato de salida.

**Comandos.** Los 17 comandos de `.opencode/commands/` son plantillas con frontmatter. `description` los hace visibles, `agent` decide quién los ejecuta y `subtask: false` o `subagent: false` mantiene la conversación en la sesión actual para permitir preguntas por turno. Se invocan con `/nombre` y reciben argumentos con `$ARGUMENTS`.

**Skills.** Los 14 skills de `.opencode/skills/<id>/SKILL.md` aportan procedimiento, convenciones y, en algunos casos, scripts auxiliares. Se cargan solos cuando la descripción encaja con la tarea; también se pueden forzar mencionando su id con `@`. No conceden permisos: solo dicen cómo hacer algo.

**MCPs.** Los 9 servidores de `opencode.json` exponen herramientas con el nombre del servidor como prefijo (`github_*`, `sqlite_*`, `fetch_*`). La política del proyecto deniega globalmente los MCPs sensibles (`context7`, `fetch`, `microsoft-learn`, `sequential-thinking`, `playwright` y `sqlite`) y los habilita solo en los agentes que los necesitan. Los secretos llegan por variables de entorno, nunca escritos en el repositorio.

### Agente, comando y skill

| Pieza | Responde a | Se invoca con | Fija permisos | Ejemplo |
| --- | --- | --- | --- | --- |
| Agente | Quién ejecuta el trabajo | Delegación desde el primario; `Ctrl+X A` o `Shift+Tab` cambia el agente de la sesión | Sí | `ats-checker` |
| Comando | Qué secuencia se ejecuta | `/nombre` | Hereda los del agente que declara | `/cv-review` |
| Skill | Cómo se hace este tipo de tarea | Carga automática o `@id` | No | `flujo-candidatura` |

Un agente se puede usar sin comando; un comando siempre se ejecuta dentro de un agente. La diferencia práctica está en el alcance: `ats-checker` audita un CV y devuelve un veredicto, mientras que `/cv-review` encadena esa auditoría con `cv-optimizer` y coloca una confirmación humana entre ambos pasos. El comando no añade capacidades: añade orden.

Un skill es una instrucción reutilizable, con sus scripts y referencias, que el agente carga cuando la tarea encaja con su descripción. No ejecuta nada por sí solo ni concede permisos: aporta el procedimiento.

### Qué aporta cada MCP

| MCP | Aporta | Requisito |
| --- | --- | --- |
| `github` | Consulta repositorios, ramas, issues y pull requests | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| `filesystem` | Lectura y listado dentro del repositorio | Ninguno |
| `memory` | Grafo de entidades, observaciones y relaciones entre sesiones | `scripts/memory-mcp.mjs` |
| `fetch` | Descarga una URL y la convierte en Markdown o texto | `uv` con `uvx` |
| `context7` | Documentación oficial y versionada de librerías | `CONTEXT7_API_KEY` si se usa |
| `microsoft-learn` | Documentación de Microsoft, Azure y API de LinkedIn | Ninguno |
| `sequential-thinking` | Razonamiento paso a paso en decisiones con varios factores | Ninguno |
| `playwright` | Navegación headless y capturas para verificar demos | Ninguno |
| `sqlite` | Consulta y escritura de la base de candidaturas | `uv` con `uvx` y el pin `mcp<2` |

El detalle de permisos por agente y de cada herramienta está en `docs/referencia-agentes-mcps.md`. En la práctica, un agente solo ve las herramientas que tiene habilitadas: si una tarea requiere `sqlite` y el agente no lo tiene, la petición debe pasar por `application-tracker` o `job-search-strategist`.

### Los 15 agentes y cuándo usarlos

| Agente | Cuándo usarlo |
| --- | --- |
| `cv-optimizer` | Cuando el CV ya pasa el filtro ATS y toca alinear contenido y palabras clave con una oferta. |
| `interview-coach` | Cuando hay que ensayar una entrevista técnica o conductual con preguntas y evaluación por turno. |
| `tracker-doc` | Cuando hay que convertir apuntes en un documento de `docs/` con la plantilla obligatoria. |
| `linkedin-optimizer` | Cuando hay que auditar titular, extracto y experiencia del perfil de LinkedIn. |
| `github-portfolio-reviewer` | Cuando hay que revisar repositorios, README, topics y fijados del portfolio. |
| `ats-checker` | Antes de reescribir el CV: dictamina parseo, keywords y legibilidad con score. |
| `cover-letter-drafter` | Cuando hay una oferta concreta y hace falta una carta en su idioma. |
| `application-tracker` | Cuando una candidatura se registra o cambia de estado. |
| `behavioral-star-coach` | Cuando faltan historias STAR con métrica o hay que practicarlas. |
| `job-search-strategist` | Cuando hay una lista de ofertas y hace falta priorizar la semana. |
| `live-coding-coach` | Cuando toca ensayar código en vivo sin recibir la solución. |
| `networking-outreach` | Cuando hay que escribir a un reclutador o referido y dejar registro del contacto. |
| `personal-brand-builder` | Cuando hace falta un calendario y borradores de contenido técnico. |
| `salary-negotiator` | Cuando hay una oferta económica y hay que preparar límites, guion y email. |
| `course-exercise-solver` | Cuando hay un ejercicio del taller que comprender antes de resolver. |

## Enfoque planteado

### Antes de empezar

El sistema no instala nada por sí solo. Antes de la primera sesión conviene comprobar que las piezas externas existen y que el repositorio se abre desde su raíz.

| Pieza | Para qué | Comprobación |
| --- | --- | --- |
| `opencode` | Ejecuta agentes, comandos y MCPs | La TUI abre en la raíz del repositorio |
| Node.js con `npx` | Lanza `github`, `filesystem`, `sequential-thinking` y `playwright` | `node --version` y `npx --version` |
| `uv` con `uvx` | Lanza `fetch` y `sqlite`, y ejecuta los scripts del pack `li-*` | `uv --version` y `uvx --version` |
| `gh` | Autentica GitHub para push, workflows y Projects | `gh --version` y `gh auth status` |
| `git` | Clona el repositorio y versiona los cambios | `git --version` |
| Variables de entorno | Tokens de GitHub y context7 | Definidas en el sistema |
| Repositorio clonado | Rutas relativas y lanzador de memoria | `opencode` abierto en la raíz |

```powershell
node --version
npx --version
uv --version
uvx --version
gh --version
gh auth status
git --version
```

Cada línea comprueba una dependencia. Las comprobaciones propias de OpenCode se hacen dentro de la TUI: `/mcps` lista los servidores y `Ctrl+X A` abre la lista de agentes. Si el CLI de `opencode` está instalado y sano, `opencode mcp list` y `opencode debug agents` dan la misma información desde la terminal.

| Recurso | Cantidad | Dónde se verifica |
| --- | --- | --- |
| Agentes | 15 | `.opencode/agents/` |
| MCPs | 9 | `opencode.json` y `/mcps` |
| Comandos | 17 | `.opencode/commands/` |
| Skills | 14 | `.opencode/skills/` |

`Ctrl+X A` abre la lista de agentes y `Shift+Tab` rota al siguiente; los subagentes no se seleccionan ahí, se lanzan por delegación. La disponibilidad se contrasta con el contenido de `.opencode/agents/` y con una prueba de delegación real sobre un agente de solo lectura.

Las claves se definen en el entorno del sistema. OpenCode V2 no lee `.env`, así que el archivo `.env.example` sirve como lista de variables, no como fuente de carga.

```powershell
setx GITHUB_PERSONAL_ACCESS_TOKEN "tu_token"
setx CONTEXT7_API_KEY "tu_clave"
```

`GITHUB_PERSONAL_ACCESS_TOKEN` necesita los scopes `repo`, `project`, `workflow`, `gist` y `read:org`. `CONTEXT7_API_KEY` solo es necesaria si se usa el MCP `context7`. `MEMORY_FILE_PATH` no se define a mano: `scripts/memory-mcp.mjs` calcula la ruta absoluta del grafo. Después de `setx`, hay que abrir una terminal nueva para que la sesión herede las variables.

### Cómo se habla al sistema

Hay tres formas de pedir trabajo (lenguaje natural, comando y subagente) y un ajuste de sesión: cambiar de agente primario. Cuanto más específica es la petición, menos margen de interpretación tiene el agente.

| Registro | Cómo se escribe | Cuándo conviene | Ejemplo |
| --- | --- | --- | --- |
| Lenguaje natural | Frase directa al agente primario | Cuando no hay comando o el flujo debe adaptarse | "Analiza el CV de `cv/` contra esta oferta y dime los gaps." |
| Comando | `/nombre` con argumentos | Cuando el flujo ya está definido | `/cv-review` con el CV y la oferta |
| Subagente | Nombrar el especialista en la petición | Cuando se quiere un informe concreto sin pipeline | "Que lo audite `ats-checker` antes de tocar el CV." |
| Agente primario | `Ctrl+X A` o `Shift+Tab` | Cuando toda la conversación debe llevarla un especialista | Elegir `plan` para diseñar sin editar |

El agente primario por defecto es `build`. Lee `AGENTS.md`, decide si delega y conserva el hilo de la conversación. Nombrar un subagente orienta la delegación, pero no le concede permisos que no tenga: si se pide una escritura a un agente de solo lectura, la rechazará.

Los comandos que declaran `subtask: false` o `subagent: false` se quedan en la sesión actual. Esa es la razón de que `/interview-technical` pueda hacer una pregunta y esperar la respuesta, en lugar de cerrar la subtarea en un turno. Los skills se cargan solos cuando la descripción encaja; para forzar uno, se menciona su id con `@`, por ejemplo `@li-post`.

```text
/cv-review revisa el CV de cv/ contra esta oferta de Full-Stack Junior
```

El texto anterior es un comando completo: `/cv-review` es el nombre y el resto llega como `$ARGUMENTS`. Si el comando no encuentra el archivo, lista `cv/` y pregunta antes de invocar; no inventa rutas.

### Rutina diaria

La sesión empieza leyendo `docs/memoria/estado-actual.md` y consultando `docs/memoria/decisiones.md`. Es una regla de `AGENTS.md`, no una sugerencia: evita repetir trabajo y contradecir decisiones previas.

| Bloque | Qué se hace | Pieza | Evidencia |
| --- | --- | --- | --- |
| Curso | Entender y resolver el ejercicio del día | `course-exercise-solver` y `tracker-doc` | `docs/ejercicios/` y su índice |
| Búsqueda | Revisar ofertas, priorizar y preparar CV y carta | `job-search-strategist`, `/cv-review`, `cover-letter-drafter` | `docs/candidaturas/` y `cv/cartas/` |
| LinkedIn | Planificar, escribir y revisar contenido | `/li-plan`, `/li-post`, `/li-human` | `docs/privado/linkedin/` |
| Inglés | Practicar y registrar el avance | Sin agente dedicado | `docs/apuntes/` |
| Cierre | Registrar el avance y actualizar la memoria | `/log-progress` | `CHANGELOG-progreso.md` y `docs/memoria/` |

No hay agente de inglés. El MVP del English coach está acordado pero pendiente de construir, así que la práctica se registra como apunte y no se pide a un agente que simule uno que no existe. El plan privado de estudios, en `docs/privado/plan-estudios-2026.md`, fija la carga diaria y el objetivo semanal.

Cierre de sesión:

1. Reunir lo hecho: ejercicios, candidaturas, mensajes y decisiones.
2. Ejecutar `/log-progress` con un resumen en una frase.
3. Comprobar que el apunte está en `docs/apuntes/`, la memoria actualizada y el CHANGELOG con la entrada.
4. Confirmar solo si el avance cierra una fase; en ese caso, `/log-progress` marca el checkbox de `PLAN.md`.
5. Si hubo una decisión, verificar que está en `decisiones.md` y en el grafo del Memory MCP.

```text
/log-progress hoy cerré el módulo de hooks de React y actualicé el CV base
```

### Pipeline de candidatura en seis etapas

El skill `flujo-candidatura` se carga solo cuando la petición encaja y recuerda el orden. Las etapas no se saltan: la revisión de CV va antes del registro y la carta se escribe antes de registrar.

| Etapa | Acción | Pieza exacta | Dónde queda |
| --- | --- | --- | --- |
| 1. Priorizar | Filtrar ofertas por match y objetivo semanal | `job-search-strategist` | `docs/candidaturas/plan-semanal-AAAA-MM-DD.md` |
| 2. Revisar CV | Auditar ATS y, si procede, reescribir | `/cv-review` | Informe en la conversación; CV en `cv/` |
| 3. Carta | Redactar en el idioma de la oferta | `cover-letter-drafter` | `cv/cartas/carta-empresa-rol-fecha.md` |
| 4. Registrar | Guardar la candidatura y regenerar la tabla | `application-tracker` | `docs/candidaturas/candidaturas.db` y `tabla-candidaturas.md` |
| 5. Contactar | Escribir a reclutador o referido | `networking-outreach` | `docs/networking/contactos-networking.md` |
| 6. Negociar | Preparar límites, guion y email | `salary-negotiator` | `docs/negociacion/` |

Reglas del pipeline:

- `/cv-review` presenta el veredicto de `ats-checker` sin reescribirlo. Con score inferior a 80 pregunta antes de lanzar `cv-optimizer`; con 80 o más informa de que no hace falta reescritura.
- Los estados válidos son `aplicada`, `en-seguimiento`, `entrevista-tecnica`, `entrevista-final`, `oferta`, `descartada` y `archivada`.
- La base SQLite es la fuente única; `tabla-candidaturas.md` es una vista que se regenera desde ella y no se edita a mano.
- No se avanza de estado sin evidencia. Tampoco se inventan enlaces ni rutas: se verifican antes de registrar.
- Al acordar condiciones, `salary-negotiator` deriva a `application-tracker` para actualizar el estado.

### Flujo de apuntes y ejercicios

1. Llevar el enunciado y el intento propio. `course-exercise-solver` no aporta pistas sin intento.
2. El agente reformula el enunciado, identifica conceptos y escala la ayuda en cuatro niveles: pregunta socrática, pista, esquema o pseudocódigo, y solución completa solo bajo petición explícita.
3. Al cerrar, actualiza `docs/ejercicios/indice-ejercicios.md` con el enlace al registro.
4. `tracker-doc` redacta el archivo con las cuatro secciones obligatorias y nombre en `kebab-case`.
5. El skill `apunte-ejercicio` fija la estructura y recuerda el reparto de agentes.
6. Si la práctica es de código en vivo, conduce `live-coding-coach`; si es de entrevista, los coaches correspondientes.

| Tipo | Dónde | Quién escribe |
| --- | --- | --- |
| Apunte de estudio | `docs/apuntes/` | `tracker-doc` |
| Registro de ejercicio | `docs/ejercicios/` | `tracker-doc`, con índice de `course-exercise-solver` |
| Práctica de live-coding | `docs/ejercicios/` | `live-coding-coach` deriva a `tracker-doc` |
| Banco de historias STAR | `docs/apuntes/` | `behavioral-star-coach` deriva a `tracker-doc` |

Las cuatro secciones son `Objetivo`, `Conceptos clave`, `Enfoque planteado` y `Estado de resolución`. No se incluye la solución completa salvo petición explícita y no se escriben comentarios dentro de los bloques de código.

### Flujo de entrevistas

| Modalidad | Comando | Agente | Qué produce |
| --- | --- | --- | --- |
| Técnica | `/interview-technical` | `interview-coach` | Preguntas por turno, evaluación por criterios y errores por categoría |
| Conductual | `/interview-behavioral` | `behavioral-star-coach` | Historias STAR, nota de 0 a 10 y huecos del banco |
| Live-coding | `/interview-live-coding` | `live-coding-coach` | Enunciado, pistas, nota de 0 a 10 y errores por categoría |

1. Aportar rol, stack, nivel y, si existe, la oferta como contexto.
2. Responder una pregunta por turno, sin pedir la solución.
3. Al cierre, leer la evaluación y elegir dos errores para la siguiente sesión.
4. Guardar el resumen con `tracker-doc` en `docs/apuntes/` o `docs/ejercicios/`.
5. En la entrevista técnica, dos notas altas seguidas suben la dificultad; dos bajas la reducen con una pista.

### Flujo de LinkedIn con el pack `li-*`

El pack aporta 11 comandos y 11 skills. Escriben, puntúan y planifican, pero no publican ni automatizan la cuenta: el texto se copia a LinkedIn a mano.

| Necesidad | Comando | Skill | Salida |
| --- | --- | --- | --- |
| Planificar la semana | `/li-plan` | `li-plan` | Plan en `docs/privado/linkedin/plan.md` |
| Escribir un post | `/li-post` | `li-post` | Tres ganchos, borrador y bloque para copiar |
| Limpiar marcas de IA | `/li-human` | `li-human` | Texto revisado y puntuación |
| Comentar | `/li-comment` | `li-comment` | Comentarios por publicación |
| Responder comentarios | `/li-reply` | `li-reply` | Respuestas priorizadas |
| Revisar el perfil | `/li-profile` | `li-profile` | Puntuación sobre 100 y reescritura |
| Preparar un carrusel | `/li-carousel` | `li-carousel` | Guion por diapositivas |
| Reaprovechar contenido | `/li-repurpose` | `li-repurpose` | Semana de posts desde un activo largo |
| Escribir un DM | `/li-dm` | `li-dm` | Nota de conexión y seguimientos |
| Ordenar la bandeja | `/li-inbox` | `li-inbox` | Clasificación y respuestas útiles |
| Auditar lo publicado | `/li-audit` | `li-audit` | Qué funcionó y qué conviene parar |

Reglas del pack:

- `/li-post` necesita el perfil de voz en `docs/privado/linkedin/voice.md`. Si no existe, pide tres publicaciones propias antes de escribir.
- El panel de `li-human` está calibrado para inglés. En español se usa como lista de comprobación, no como veredicto.
- El perfil se revisa con `/linkedin-review` y `linkedin-optimizer`, que no navega LinkedIn: trabaja con el texto pegado.
- La estrategia y el calendario de contenido son de `personal-brand-builder`, con borradores en `docs/marca-personal/borradores/`.
- Los contactos y seguimientos son de `networking-outreach`, con registro en `docs/networking/contactos-networking.md`.
- Para consultar la documentación de la API de LinkedIn se usa `microsoft-learn`, porque `linkedin.com` bloquea el acceso automatizado.
- La auditoría y las adaptaciones del pack están en `docs/marca-personal/linkedin-agent-skill.md`.

### Flujo de documentación y memoria

`/log-progress` integra el cierre completo. No es un simple apunte: actualiza la memoria, el changelog y, solo con confirmación, el plan.

| Paso | Acción | Archivo |
| --- | --- | --- |
| 1 | Redactar el apunte con `tracker-doc` | `docs/apuntes/` |
| 2 | Actualizar la foto, el siguiente paso y los bloqueos | `docs/memoria/estado-actual.md` |
| 3 | Registrar la decisión con fecha, motivo y alternativa descartada | `docs/memoria/decisiones.md` |
| 4 | Ampliar el grafo con `create_entities` o `add_observations` | Memory MCP |
| 5 | Añadir la entrada cronológica | `CHANGELOG-progreso.md` |
| 6 | Marcar la fase, solo con confirmación | `PLAN.md` |

| Archivo | Función | Se actualiza |
| --- | --- | --- |
| `docs/memoria/estado-actual.md` | Foto, fase, siguiente paso y bloqueos | Al cerrar un hito |
| `docs/memoria/decisiones.md` | Decisión, motivo y alternativas | Al tomar una decisión |
| `docs/memoria/memoria.local.json` | Grafo en formato JSON Lines | Con las herramientas del Memory MCP |
| `CHANGELOG-progreso.md` | Cronología del avance | En cada cierre |

La memoria es foto y motivo; el CHANGELOG es cronología. No se duplica el mismo contenido en ambos. `estado-actual.md` se mantiene corto: si crece, se resume y el detalle pasa al grafo.

`memoria.local.json` se escribe con un objeto JSON por línea. Si se edita a mano, hay que conservar ese formato: el servidor carga línea a línea e ignora las ilegibles. El archivo está excluido de git, así que su respaldo es manual.

### Privacidad y límites

| Ruta | Qué contiene | Regla |
| --- | --- | --- |
| `docs/privado/` | Perfil de voz, planes personales y notas internas | Excluido de git; no se enlaza desde documentos públicos |
| `cv/` | CV y cartas | Excluido salvo `cv/README.md`; las cartas viven en `cv/cartas/` |
| `.env` | Claves de los MCPs | Excluido; nunca se pega su contenido en un prompt ni en `docs/` |
| `docs/candidaturas/candidaturas.db` | Historial de candidaturas | Excluido; la vista pública es `tabla-candidaturas.md` |
| `docs/networking/contactos-networking.md` | Contactos y seguimientos | Excluido |
| `docs/negociacion/registro-negociaciones.md` | Negociaciones | Excluido |
| `docs/memoria/*.local.json` | Grafo de memoria | Excluido; respaldo manual |

Límites de LinkedIn:

- El sistema no publica, no comenta y no envía mensajes por la cuenta. El pack `li-*` entrega texto para copiar.
- No se automatiza la navegación ni el scraping. `linkedin.com` bloquea el acceso automatizado en su `robots.txt`; por eso `.lycheeignore` excluye LinkedIn y por eso `fetch` o `playwright` fallan contra esas URLs.
- El cliente `scripts/linkedin-portability.py` es de solo lectura y trabaja con la API DMA, con consentimiento. No publica ni modifica el perfil.
- Para documentación de la API se consulta `microsoft-learn`, que publica las páginas de LinkedIn.

Regla de oro: si un dato no debe aparecer en GitHub, no debe aparecer en un prompt que escriba en `docs/`. Los tokens, los correos y los datos de terceros se quedan fuera.

### Solución de problemas

| Síntoma | Causa | Solución |
| --- | --- | --- |
| Un script falla porque no encuentra `python` o `python3` | El intérprete no está en el PATH | Ejecutar con `uv run --no-project python`; el pack `li-*` ya lo hace |
| El grafo de memoria aparece vacío o las escrituras fallan con `ENOENT` | Una ruta relativa se resuelve contra la caché de `npx` | Arrancar `memory` con `scripts/memory-mcp.mjs`; no fijar `MEMORY_FILE_PATH` a mano |
| `sqlite` cae con `MCP error -32000: Connection closed` | El SDK 2.x retiró `Server.list_resources` | Mantener `--with "mcp<2"` en el comando de `sqlite` |
| `github` o `context7` no autentican aunque `.env` tenga las claves | OpenCode V2 no carga `.env` | Definir las variables en el sistema, abrir una terminal nueva y reiniciar la sesión |
| `fetch` o `playwright` fallan contra `linkedin.com` | LinkedIn bloquea el acceso automatizado | No insistir; usar `microsoft-learn` o pegar el contenido |
| `opencode --help` falla con «no es una aplicación válida para esta plataforma» | El shim de npm no encuentra el binario de la plataforma | Usar la TUI que ya está abierta; si hace falta el CLI, reinstalar `@opencode/cli` con el instalador oficial |
| Un MCP no aparece o está caído | Comando, credencial o servidor mal configurado | `opencode mcp list`, `/mcps`, revisar el comando y ejecutar `/reload` |

El diagnóstico general empieza por `/mcps`; si el CLI funciona, `opencode mcp list` da el mismo estado desde la terminal. Si el servidor arranca pero la herramienta no está disponible para un agente, el problema es de permisos: en los MCPs con denegación global, la herramienta solo se habilita en los agentes que la declaran.

### Chuleta final

#### Comandos

| Comando | Para qué | Ejecuta |
| --- | --- | --- |
| `/cv-review` | Audita el CV y, con confirmación, lo revisa | `build`, con `ats-checker` y `cv-optimizer` |
| `/linkedin-review` | Informe del perfil con gaps y checklist | `linkedin-optimizer` |
| `/interview-technical` | Simulacro técnico pregunta a pregunta | `interview-coach` |
| `/interview-behavioral` | Práctica STAR con evaluación | `behavioral-star-coach` |
| `/interview-live-coding` | Live-coding por pasos con pistas limitadas | `live-coding-coach` |
| `/log-progress` | Apunte, memoria, CHANGELOG y fase opcional | `build` |
| `/li-post` | Post desde una idea, con ganchos y humanización | `build` y skill `li-post` |
| `/li-human` | Limpia marcas de IA y puntúa el texto | `build` y skill `li-human` |
| `/li-comment` | Comentarios para publicaciones ajenas | `build` y skill `li-comment` |
| `/li-reply` | Respuestas a comentarios propios | `build` y skill `li-reply` |
| `/li-profile` | Puntuación y reescritura del perfil | `build` y skill `li-profile` |
| `/li-plan` | Plan semanal de contenido | `build` y skill `li-plan` |
| `/li-carousel` | Carrusel por diapositivas | `build` y skill `li-carousel` |
| `/li-repurpose` | Posts desde un activo largo | `build` y skill `li-repurpose` |
| `/li-dm` | Nota de conexión y seguimientos | `build` y skill `li-dm` |
| `/li-inbox` | Clasificación de la bandeja | `build` y skill `li-inbox` |
| `/li-audit` | Auditoría de lo publicado | `build` y skill `li-audit` |

#### Agentes

| Agente | Cómo pedirlo |
| --- | --- |
| `cv-optimizer` | "Analiza el CV de `cv/` contra esta oferta y dime fortalezas y gaps." |
| `interview-coach` | "Simula una entrevista técnica junior de React y Node, una pregunta por turno." |
| `tracker-doc` | "Documenta este avance en `docs/apuntes/` con la plantilla obligatoria." |
| `linkedin-optimizer` | "Revisa mi titular, extracto y dos experiencias contra esta oferta." |
| `github-portfolio-reviewer` | "Revisa mis repositorios fijados y propón mejoras de README y topics." |
| `ats-checker` | "Pasa el CV por ATS contra esta oferta y dame veredicto con score." |
| `cover-letter-drafter` | "Redacta la carta para esta oferta y guárdala en `cv/cartas/`." |
| `application-tracker` | "Registra esta candidatura con su oferta, carta y CV." |
| `behavioral-star-coach` | "Construye mi banco STAR y practica una historia por turno." |
| `job-search-strategist` | "Prioriza estas ofertas con umbral 75 y genera el plan semanal." |
| `live-coding-coach` | "Simula un live-coding de JavaScript asíncrono en 30 minutos." |
| `networking-outreach` | "Escribe un primer mensaje a una reclutadora y regístralo." |
| `personal-brand-builder` | "Propón tres piezas semanales desde mis proyectos con métrica." |
| `salary-negotiator` | "Prepara la negociación con mínimo, objetivo y este rango." |
| `course-exercise-solver` | "Ayúdame con este ejercicio; mi intento es este." |

### Errores que no se deben cometer

- Registrar candidaturas a mano en `tabla-candidaturas.md` en lugar de usar `application-tracker`.
- Reescribir el CV sin pasar antes por `ats-checker`.
- Avanzar el estado de una candidatura sin evidencia.
- Publicar o automatizar acciones en LinkedIn.
- Pegar tokens, correos o datos de terceros en un prompt o en un documento.
- Versionar `cv/`, `docs/privado/`, `.env` o la base SQLite.
- Editar `memoria.local.json` sin mantener el formato JSON Lines.
- Cerrar el día con avances sin ejecutar `/log-progress`.
- Contradecir `docs/memoria/decisiones.md` sin haberlo leído.
- Pedir la solución completa de un ejercicio como primera opción.
- Inventar rutas, agentes o comandos que no existen en el repositorio.
- Incluir comentarios dentro de un bloque de código.

## Estado de resolución

- Fecha de creación: 2026-10-26.
- Recuento verificado contra el repositorio: 15 agentes, 9 MCPs, 17 comandos y 14 skills.
- Fuentes del recuento: `.opencode/agents/`, `opencode.json`, `.opencode/commands/` y `.opencode/skills/`.
- Verificación de formato: `npx markdownlint-cli2 "docs/guia-uso-ai-job-search-copilot.md"` ejecutado el 2026-10-26 sin incidencias.
- Mantenimiento: actualizar esta guía cuando cambie el número de agentes, MCPs, comandos o skills; el detalle técnico se mantiene en `docs/referencia-agentes-mcps.md`.
