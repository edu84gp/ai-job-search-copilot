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
