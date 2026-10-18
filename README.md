# Eduardo García Prieto — Junior Full-Stack + IA

![Calidad](https://github.com/edu84gp/job-support-portfolio/actions/workflows/quality.yml/badge.svg)
![Estado](https://img.shields.io/badge/estado-b%C3%BAsqueda%20activa-brightgreen)
![Employment Workshop 2026](https://img.shields.io/badge/Employment%20Workshop-2026-blue)

**Palencia, España · Remoto > híbrido > presencial · Disponibilidad inmediata**

📧 [edu84gp@gmail.com](mailto:edu84gp@gmail.com) · 💼 [LinkedIn](https://www.linkedin.com/in/edu84gp) · 💻 [GitHub](https://github.com/edu84gp)

[🇬🇧 Go to English version](#english-version)

## Perfil

Desarrollador Junior Full-Stack con enfoque en IA aplicada, recién graduado del bootcamp de desarrollo web y participante del programa Employment Workshop 2026. Como parte del programa construí un sistema completo de búsqueda de empleo asistido por IA sobre opencode: 15 subagentes especializados, 8 servidores MCP, 6 comandos y 3 skills con permisos acotados por agente. Este repositorio documenta ese sistema y todo el proceso con trazabilidad total.

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
| El juego de la vida | Autómata celular Turing-completo: simula cualquier Máquina de Turing a partir del estado inicial. | [Código](https://github.com/edu84gp/el-juego-de-la-vida) · [Demo](https://edu84gp.github.io/el-juego-de-la-vida/) |
| WhatsChatGPT | Chatbot web en tiempo real con arquitectura cliente-servidor, WebSockets con Socket.io e IA local vía Ollama. Demo pendiente de despliegue: requiere un servidor con Ollama en ejecución. | [Código](https://github.com/edu84gp/WhatsChatGPT) |
| Aplika Jobs 🔒 | Conecta ofertas de empleo técnico con perfiles académicos: extrae el CV, busca ofertas relevantes, calcula el match con IA y genera CV optimizado ATS, carta y email adaptados. Repositorio privado por explotación comercial; acceso bajo petición. | [Solicitar acceso](mailto:edu84gp@gmail.com?subject=Solicitud%20acceso%20Aplika%20Jobs) |

## Búsqueda de empleo asistida por IA

Employment Workshop 2026 es un programa de inserción laboral. Para seguirlo, construí sobre opencode un sistema que automatiza y documenta todo el proceso:

`Oferta → análisis de match → CV optimizado ATS → carta de presentación → registro de candidatura → preparación de entrevistas → negociación`

Cada etapa tiene agentes y comandos dedicados, con permisos mínimos y memoria persistente entre sesiones. Las evidencias quedan versionadas en el repositorio:

| Evidencia | Dónde |
| --- | --- |
| Plan por fases (22 fases) | [PLAN.md](PLAN.md) |
| Historial de progreso | [CHANGELOG-progreso.md](CHANGELOG-progreso.md) |
| Referencia de agentes, MCPs, comandos y skills | [docs/referencia-agentes-mcps.md](docs/referencia-agentes-mcps.md) |
| Pipeline de candidaturas | [docs/candidaturas/tabla-candidaturas.md](docs/candidaturas/tabla-candidaturas.md) |
| Kanban del pipeline | [Project público](https://github.com/users/edu84gp/projects/3) |
| Memoria y decisiones del proyecto | [docs/memoria/](docs/memoria/) |
| Ejercicios y apuntes del programa | [docs/ejercicios/](docs/ejercicios/) · [docs/apuntes/](docs/apuntes/) |

## Cómo trabajo

- **Trazabilidad total**: cada avance se registra en el plan y el changelog; cada decisión técnica, con su alternativa descartada, en `docs/memoria/decisiones.md`.
- **Calidad automatizada**: GitHub Actions ejecuta en cada push el lint de Markdown y la verificación de enlaces, con configuración versionada en el repositorio.
- **IA con criterio**: los agentes tienen permisos mínimos por diseño (denegación global, habilitación por agente) y no entregan soluciones directas en los ejercicios del programa, solo guían el proceso.

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
- `.opencode/`: agentes, comandos y skills.
- `.github/workflows/`: automatizaciones de calidad.

</details>

## Estado del proyecto

- 21 de 22 fases completadas; la fase 22 (validación final) está en curso.

---

<a id="english-version"></a>

# Eduardo García Prieto — Junior Full-Stack + AI

![Quality](https://github.com/edu84gp/job-support-portfolio/actions/workflows/quality.yml/badge.svg)
![Status](https://img.shields.io/badge/status-open%20to%20work-brightgreen)
![Employment Workshop 2026](https://img.shields.io/badge/Employment%20Workshop-2026-blue)

**Palencia, Spain · Remote > hybrid > on-site · Available immediately**

📧 [edu84gp@gmail.com](mailto:edu84gp@gmail.com) · 💼 [LinkedIn](https://www.linkedin.com/in/edu84gp) · 💻 [GitHub](https://github.com/edu84gp)

## Profile

Junior Full-Stack Developer focused on applied AI, recent web development bootcamp graduate and Employment Workshop 2026 participant. As part of the program I built a complete AI-assisted job search system on top of opencode: 15 specialized subagents, 8 MCP servers, 6 commands and 3 skills with per-agent scoped permissions. This repository documents that system and the whole process with full traceability.

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
| Game of Life | Turing-complete cellular automaton: simulates any Turing Machine from the initial state. | [Code](https://github.com/edu84gp/el-juego-de-la-vida) · [Demo](https://edu84gp.github.io/el-juego-de-la-vida/) |
| WhatsChatGPT | Real-time web chatbot with client-server architecture, WebSockets via Socket.io and local AI via Ollama. Demo pending deployment: requires a server with Ollama running. | [Code](https://github.com/edu84gp/WhatsChatGPT) |
| Aplika Jobs 🔒 | Matches tech job offers with student profiles: parses the CV, finds relevant offers, computes AI match and generates ATS-optimized CV, cover letter and tailored email. Private repository for commercial exploitation; access on request. | [Request access](mailto:edu84gp@gmail.com?subject=Aplika%20Jobs%20access%20request) |

## AI-assisted job search

Employment Workshop 2026 is a job placement program. To follow it, I built a system on top of opencode that automates and documents the whole process:

`Offer → match analysis → ATS-optimized CV → cover letter → application tracking → interview preparation → negotiation`

Every stage has dedicated agents and commands, with least-privilege permissions and persistent memory across sessions. The evidence is versioned in the repository:

| Evidence | Where |
| --- | --- |
| Phased plan (22 phases) | [PLAN.md](PLAN.md) |
| Progress log | [CHANGELOG-progreso.md](CHANGELOG-progreso.md) |
| Agents, MCPs, commands and skills reference | [docs/referencia-agentes-mcps.md](docs/referencia-agentes-mcps.md) |
| Application pipeline | [docs/candidaturas/tabla-candidaturas.md](docs/candidaturas/tabla-candidaturas.md) |
| Pipeline Kanban | [Public project](https://github.com/users/edu84gp/projects/3) |
| Project memory and decisions | [docs/memoria/](docs/memoria/) |
| Program exercises and notes | [docs/ejercicios/](docs/ejercicios/) · [docs/apuntes/](docs/apuntes/) |

## How I work

- **Full traceability**: every milestone is logged in the plan and changelog; every technical decision, with its discarded alternative, in `docs/memoria/decisiones.md`.
- **Automated quality**: GitHub Actions runs Markdown lint and link checking on every push, with versioned configuration in the repository.
- **AI with judgment**: agents have least-privilege permissions by design (global deny, per-agent enable) and never hand out direct solutions in program exercises, they only guide the process.

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
- `.opencode/`: agents, commands and skills.
- `.github/workflows/`: quality automations.

</details>

## Project status

- 21 of 22 phases completed; phase 22 (final validation) is in progress.
