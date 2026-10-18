---
name: flujo-candidatura
description: Pipeline completo de una candidatura desde la oferta hasta el seguimiento, con el agente y el orden de pasos de cada etapa. Usar cuando se pida aplicar a una oferta, gestionar una candidatura de principio a fin o recordar el orden del proceso.
---

# Flujo de candidatura

Pipeline en seis etapas. Ejecutar las etapas en orden y no saltar la revisión de CV antes de registrar.

## Etapas

1. Filtrado y priorización: invoca a job-search-strategist con la lista de ofertas, umbral de match y objetivo semanal. El plan se guarda en `docs/candidaturas/`.
2. Revisión de CV: ejecuta `/cv-review` con el CV de `cv/` y la oferta, o invoca a ats-checker y después a cv-optimizer si el score es inferior a 80.
3. Carta: invoca a cover-letter-drafter con la oferta y el CV. Se guarda en `cv/cartas/` con nombre kebab-case.
4. Registro: invoca a application-tracker con empresa, rol, fecha, enlace, carta y CV. La base SQLite es la fuente y la tabla Markdown se regenera desde ella.
5. Contacto: si hay reclutador o referido, invoca a networking-outreach y registra el contacto en `docs/networking/`.
6. Negociación: cuando llegue una oferta, invoca a salary-negotiator. Nunca dar la primera cifra. Al acordar condiciones, actualiza el estado con application-tracker.

## Reglas

- Estados válidos de candidatura: aplicada, en-seguimiento, entrevista-tecnica, entrevista-final, oferta, descartada, archivada.
- No inventar enlaces ni rutas: verificar antes de registrar.
- No avanzar de estado sin evidencia aportada por la persona.
- Al cerrar el día con avances, sugiere `/log-progress`.
