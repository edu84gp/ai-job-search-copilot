# Eduardo García Prieto — Junior Full-Stack + IA

![Calidad](https://github.com/edu84gp/ai-job-search-copilot/actions/workflows/quality.yml/badge.svg)
![Estado](https://img.shields.io/badge/estado-b%C3%BAsqueda%20activa-brightgreen)
![Employment Workshop 2026](https://img.shields.io/badge/Employment%20Workshop-2026-blue)

**Palencia, España · Remoto > híbrido > presencial · Disponibilidad inmediata**

📧 [edu84gp@gmail.com](mailto:edu84gp@gmail.com) · 💼 [LinkedIn](https://www.linkedin.com/in/edu84gp) · 💻 [GitHub](https://github.com/edu84gp)

[🇬🇧 Go to English version](#english-version)

## Perfil

Desarrollador Junior Full-Stack con enfoque en IA aplicada, recién graduado del bootcamp de desarrollo web y participante del programa Employment Workshop 2026. Como parte del programa construí un sistema completo de búsqueda de empleo asistido por IA sobre opencode: 15 subagentes especializados, 9 servidores MCP, 17 comandos y 14 skills con permisos acotados por agente. Este repositorio documenta ese sistema y todo el proceso con trazabilidad total.

Busco mi primera oportunidad como desarrollador Junior Full-Stack, con especial interés en equipos que apliquen IA al desarrollo de producto.

- **Aplicaciones web completas**: arquitectura cliente-servidor, comunicación en tiempo real con WebSockets y Socket.io, consumo de APIs REST e integración de IA con Ollama.
- **Automatización con IA**: diseño de agentes con permisos mínimos, integración de servidores MCP y orquestación de flujos de trabajo reproducibles.
- **Documentación técnica**: cada fase, ejercicio y decisión del proyecto queda registrada en `docs/` con formato normalizado.

## Stack técnico

| Área | Tecnologías |
| --- | --- |
| Frontend | HTML5, CSS3, JavaScript, React |
| Backend | Node.js, Express, Socket.io, WebSockets, APIs REST |
| Datos | SQL, SQLite |
| IA aplicada | Ollama, agentes con opencode, servidores MCP, prompt engineering |
| Herramientas | Git, GitHub, GitHub Actions, opencode |

## Proyectos destacados

| Proyecto | Descripción | Enlaces |
| --- | --- | --- |
| POKÉDEX WEB | Aplicación web que consume PokéAPI con paginación fluida, tarjetas interactivas y ficha detallada. | [Código](https://github.com/edu84gp/pokedex_web) · [Demo](https://edu84gp.github.io/pokedex_web/) |
| El juego de la vida | Simulador web del autómata celular de Conway: tablero vacío configurable de 1×1 a 99×99, edición de células, patrón inicial aleatorio, control de velocidad y evolución por generaciones. | [Código](https://github.com/edu84gp/el-juego-de-la-vida) · [Demo](https://edu84gp.github.io/el-juego-de-la-vida/) |
| WhatsChatGPT | Chatbot web en tiempo real con arquitectura cliente-servidor, WebSockets con Socket.io e IA local vía Ollama. Demo pendiente de despliegue: requiere un servidor con Ollama en ejecución. | [Código](https://github.com/edu84gp/WhatsChatGPT) |
| Aplika Jobs 🔒 | Conecta ofertas de empleo técnico con perfiles académicos: extrae el CV, busca ofertas relevantes, calcula el match con IA y genera CV optimizado ATS, carta y email adaptados. Proyecto en equipo con el código privado; la documentación técnica pública recoge la arquitectura, las decisiones y mi aportación. | [Caso de estudio](https://github.com/edu84gp/aplika-jobs-case-study) |

## Búsqueda de empleo asistida por IA

Employment Workshop 2026 es un programa de inserción laboral. Para seguirlo, construí sobre opencode un sistema que automatiza y documenta todo el proceso:

`Oferta → análisis de match → CV optimizado ATS → carta de presentación → registro de candidatura → preparación de entrevistas → negociación`

Cada etapa tiene agentes y comandos dedicados, con permisos mínimos y memoria persistente entre sesiones. Las evidencias quedan versionadas en el repositorio:

| Evidencia | Dónde |
| --- | --- |
| Plan por fases (22 fases) | [PLAN.md](PLAN.md) |
| Historial de progreso | [CHANGELOG-progreso.md](CHANGELOG-progreso.md) |
| Referencia de agentes, MCPs, comandos y skills | [docs/referencia-agentes-mcps.md](docs/referencia-agentes-mcps.md) |
| Guía de uso del sistema | [docs/guia-uso-ai-job-search-copilot.md](docs/guia-uso-ai-job-search-copilot.md) |
| Auditoría del pack LinkedIn `li-*` | [docs/marca-personal/linkedin-agent-skill.md](docs/marca-personal/linkedin-agent-skill.md) |
| Pipeline de candidaturas | [docs/candidaturas/tabla-candidaturas.md](docs/candidaturas/tabla-candidaturas.md) |
| Kanban del pipeline | [Project público](https://github.com/users/edu84gp/projects/3) |
| Memoria y decisiones del proyecto | [docs/memoria/](docs/memoria/) |
| Ejercicios y apuntes del programa | [docs/ejercicios/](docs/ejercicios/) · [docs/apuntes/](docs/apuntes/) |

## Cómo trabajo

- **Trazabilidad total**: cada avance se registra en el plan y el changelog; cada decisión técnica, con su alternativa descartada, en `docs/memoria/decisiones.md`.
- **Calidad automatizada**: GitHub Actions ejecuta en cada push el lint de Markdown y la verificación de enlaces, con configuración versionada en el repositorio.
- **IA con criterio**: los agentes tienen permisos mínimos por diseño (denegación global, habilitación por agente) y no entregan soluciones directas en los ejercicios del programa, solo guían el proceso.

## Cómo reproducirlo

Requisitos: opencode, Node.js con `npx`, Python con `uv` y Git. Para las tareas de GitHub, `gh` autenticado.

1. Clona el repositorio:

   ```powershell
   git clone https://github.com/edu84gp/ai-job-search-copilot.git
   cd ai-job-search-copilot
   ```

2. Define las claves en el entorno del sistema; OpenCode V2 no lee `.env`. `.env.example` sirve como lista de variables:

   ```powershell
   setx GITHUB_PERSONAL_ACCESS_TOKEN "tu_token"
   ```

   `GITHUB_PERSONAL_ACCESS_TOKEN` necesita los scopes `repo`, `project`, `workflow`, `gist` y `read:org`. `CONTEXT7_API_KEY` solo es necesario si usas el MCP context7. Abre una sesión nueva después de definirlas.

3. No hace falta configurar rutas: `scripts/memory-mcp.mjs` resuelve la ruta absoluta de `docs/memoria/memoria.local.json` desde la raíz del clon y arranca el Memory MCP con `MEMORY_FILE_PATH`.

4. Abre opencode en la carpeta del repositorio. La base SQLite y el grafo de memoria se crean al primer uso y están excluidos de git.

5. Comprueba que arrancan los 9 MCPs y que los 15 agentes están disponibles. La referencia técnica de cada servidor, permiso y agente está en [docs/referencia-agentes-mcps.md](docs/referencia-agentes-mcps.md).

<details>
<summary>Estructura del repositorio</summary>

- `PLAN.md`: plan general por fases.
- `CHANGELOG-progreso.md`: historial de progreso.
- `AGENTS.md`: directrices globales del proyecto.
- `docs/`: documentación, ejercicios, apuntes, candidaturas y memoria.
- `docs/referencia-agentes-mcps.md`: referencia técnica del ecosistema de IA.
- `cv/`: CV y cartas en local, fuera del repositorio público.
- `portfolio/`: evidencias de proyectos.
- `templates/`: plantillas `kebab-case`.
- `scripts/`: lanzadores de apoyo, como el del Memory MCP.
- `.opencode/`: agentes, comandos y skills.
- `.github/workflows/`: automatizaciones de calidad.

</details>

## Estado del proyecto

- 22 de 22 fases completadas.

---

<a id="english-version"></a>

# Eduardo García Prieto — Junior Full-Stack + AI

![Quality](https://github.com/edu84gp/ai-job-search-copilot/actions/workflows/quality.yml/badge.svg)
![Status](https://img.shields.io/badge/status-open%20to%20work-brightgreen)
![Employment Workshop 2026](https://img.shields.io/badge/Employment%20Workshop-2026-blue)

**Palencia, Spain · Remote > hybrid > on-site · Available immediately**

📧 [edu84gp@gmail.com](mailto:edu84gp@gmail.com) · 💼 [LinkedIn](https://www.linkedin.com/in/edu84gp) · 💻 [GitHub](https://github.com/edu84gp)

## Profile

Junior Full-Stack Developer focused on applied AI, recent web development bootcamp graduate and Employment Workshop 2026 participant. As part of the program I built a complete AI-assisted job search system on top of opencode: 15 specialized subagents, 8 MCP servers, 17 commands and 14 skills with per-agent scoped permissions. This repository documents that system and the whole process with full traceability.

I am looking for my first opportunity as a Junior Full-Stack Developer, especially in teams applying AI to product development.

- **Complete web applications**: client-server architecture, real-time communication with WebSockets and Socket.io, REST API consumption and AI integration with Ollama.
- **AI automation**: agent design with least-privilege permissions, MCP server integration and reproducible workflow orchestration.
- **Technical documentation**: every phase, exercise and decision of the project is recorded in `docs/` using a standardized format.

## Tech stack

| Area | Technologies |
| --- | --- |
| Frontend | HTML5, CSS3, JavaScript, React |
| Backend | Node.js, Express, Socket.io, WebSockets, REST APIs |
| Data | SQL, SQLite |
| Applied AI | Ollama, agents with opencode, MCP servers, prompt engineering |
| Tooling | Git, GitHub, GitHub Actions, opencode |

## Featured projects

| Project | Description | Links |
| --- | --- | --- |
| POKÉDEX WEB | Web application consuming PokéAPI with smooth pagination, interactive cards and detailed view. | [Code](https://github.com/edu84gp/pokedex_web) · [Demo](https://edu84gp.github.io/pokedex_web/) |
| Game of Life | Web simulator of Conway's cellular automaton: empty configurable 1×1 to 99×99 board, cell editing, random initial pattern, speed control and generation-by-generation evolution. | [Code](https://github.com/edu84gp/el-juego-de-la-vida) · [Demo](https://edu84gp.github.io/el-juego-de-la-vida/) |
| WhatsChatGPT | Real-time web chatbot with client-server architecture, WebSockets via Socket.io and local AI via Ollama. Demo pending deployment: requires a server with Ollama running. | [Code](https://github.com/edu84gp/WhatsChatGPT) |
| Aplika Jobs 🔒 | Matches tech job offers with student profiles: parses the CV, finds relevant offers, computes AI match and generates ATS-optimized CV, cover letter and tailored email. Team project with a private codebase; the public technical documentation covers architecture, decisions and my contribution. | [Case study](https://github.com/edu84gp/aplika-jobs-case-study) |

## AI-assisted job search

Employment Workshop 2026 is a job placement program. To follow it, I built a system on top of opencode that automates and documents the whole process:

`Offer → match analysis → ATS-optimized CV → cover letter → application tracking → interview preparation → negotiation`

Every stage has dedicated agents and commands, with least-privilege permissions and persistent memory across sessions. The evidence is versioned in the repository:

| Evidence | Where |
| --- | --- |
| Phased plan (22 phases) | [PLAN.md](PLAN.md) |
| Progress log | [CHANGELOG-progreso.md](CHANGELOG-progreso.md) |
| Agents, MCPs, commands and skills reference | [docs/referencia-agentes-mcps.md](docs/referencia-agentes-mcps.md) |
| System usage guide | [docs/guia-uso-ai-job-search-copilot.md](docs/guia-uso-ai-job-search-copilot.md) |
| LinkedIn `li-*` pack audit | [docs/marca-personal/linkedin-agent-skill.md](docs/marca-personal/linkedin-agent-skill.md) |
| Application pipeline | [docs/candidaturas/tabla-candidaturas.md](docs/candidaturas/tabla-candidaturas.md) |
| Pipeline Kanban | [Public project](https://github.com/users/edu84gp/projects/3) |
| Project memory and decisions | [docs/memoria/](docs/memoria/) |
| Program exercises and notes | [docs/ejercicios/](docs/ejercicios/) · [docs/apuntes/](docs/apuntes/) |

## How I work

- **Full traceability**: every milestone is logged in the plan and changelog; every technical decision, with its discarded alternative, in `docs/memoria/decisiones.md`.
- **Automated quality**: GitHub Actions runs Markdown lint and link checking on every push, with versioned configuration in the repository.
- **AI with judgment**: agents have least-privilege permissions by design (global deny, per-agent enable) and never hand out direct solutions in program exercises, they only guide the process.

## How to reproduce it

Requirements: opencode, Node.js with `npx`, Python with `uv` and Git. For GitHub tasks, authenticated `gh`.

1. Clone the repository:

   ```bash
   git clone https://github.com/edu84gp/ai-job-search-copilot.git
   cd ai-job-search-copilot
   ```

2. Define the keys in the system environment; OpenCode V2 does not read `.env`. `.env.example` lists the variables:

   ```bash
   export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
   ```

   `GITHUB_PERSONAL_ACCESS_TOKEN` needs the `repo`, `project`, `workflow`, `gist` and `read:org` scopes. `CONTEXT7_API_KEY` is only required if you use the context7 MCP. Start a new session after defining them.

3. No path configuration is needed: `scripts/memory-mcp.mjs` resolves the absolute path of `docs/memoria/memoria.local.json` from the clone root and starts the Memory MCP with `MEMORY_FILE_PATH`.

4. Open opencode in the repository folder. The SQLite database and the memory graph are created on first use and are excluded from git.

5. Check that the 9 MCPs start and the 15 agents are available. The technical reference for each server, permission and agent is in [docs/referencia-agentes-mcps.md](docs/referencia-agentes-mcps.md).

<details>
<summary>Repository structure</summary>

- `PLAN.md`: phased master plan.
- `CHANGELOG-progreso.md`: progress log.
- `AGENTS.md`: global project guidelines.
- `docs/`: documentation, exercises, notes, applications and memory.
- `docs/referencia-agentes-mcps.md`: technical reference of the AI ecosystem.
- `cv/`: CV and cover letters kept local, outside the public repository.
- `portfolio/`: project evidence.
- `templates/`: `kebab-case` templates.
- `scripts/`: supporting launchers, such as the Memory MCP one.
- `.opencode/`: agents, commands and skills.
- `.github/workflows/`: quality automations.

</details>

## Project status

- 22 of 22 phases completed.
