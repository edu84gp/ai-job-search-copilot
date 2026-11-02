# Pack LinkedIn li-*: auditoría e instalación

## Objetivo

Verificar la seguridad del repositorio público `Jakeschincariol/linkedin-agent-skill`, instalar sus 11 skills en OpenCode y dejar el comando `/li-post` operativo con las adaptaciones necesarias para este proyecto.

## Conceptos clave

- **Skill**: carpeta con `SKILL.md` y recursos. OpenCode la descubre por el nombre del directorio y la carga con la herramienta `skill`.
- **Comando**: archivo en `.opencode/commands/` que se invoca con `/nombre`. Los skills no se exponen solos como comandos, así que se añadió un envoltorio por skill.
- **Humanizador**: dos scripts Python locales, `humanize.py` y `detect.py`, que limpian marcas tipográficas e invisibles y puntúan el texto con cinco heurísticas.
- **Perfil de voz**: `docs/privado/linkedin/voice.md`, fuera de git, con la voz, las posiciones y los límites de publicación.
- **Commit pin**: `add2c23882fe79180737d242ff80a5da205eda6a`, único commit de la versión 1.0 revisada.

## Enfoque planteado

### 1. Ficha del repositorio

| Campo | Valor |
| --- | --- |
| Repositorio | `Jakeschincariol/linkedin-agent-skill` |
| URL | https://github.com/Jakeschincariol/linkedin-agent-skill |
| Autor | Jake Schincariol |
| Licencia | MIT |
| Estrellas en la revisión | 2.618 |
| Commit revisado | `add2c23882fe79180737d242ff80a5da205eda6a` |
| Fecha del commit | 2026-09-07 |
| Etiquetas | Ninguna; se fija el commit |
| Contenido | 11 skills, 21 fórmulas de gancho, léxico de 113 términos, rúbrica de perfil de 100 puntos y plantilla de voz |
| Tamaño | 22 archivos, 98.302 bytes |

### 2. Auditoría de seguridad

| Vector | Resultado |
| --- | --- |
| Llamadas de red | Ninguna. Los scripts solo importan `argparse`, `json`, `os`, `re`, `sys`, `statistics` y `unicodedata`. |
| Ejecución de procesos | Ninguna. No hay `subprocess`, `os.system`, `popen`, `eval` ni `exec`. |
| Dependencias | Ninguna. No hay `package.json`, `requirements.txt` ni instaladores. |
| Binarios | Ninguno. Solo Markdown, JSON y Python de texto. |
| Secretos | Ninguno. No hay tokens, claves ni credenciales. |
| Escrituras | `humanize.py` solo escribe si se pasa `-o`; los skills escriben el perfil de voz, el plan y el registro en la carpeta privada del proyecto. |
| Publicación automática | Prohibida de forma explícita. El README y los 11 skills insisten en que la persona publica el texto. |
| Automatización de LinkedIn | Prohibida de forma explícita. No hay navegador, scraping ni llamadas a la API de LinkedIn. |
| Inyección de instrucciones | No se encontraron comentarios HTML, instrucciones para ignorar reglas, acceso a `.env`, `.ssh` ni exfiltración. |
| Reputación | Proyecto MIT de un autor identificado, con 2.618 estrellas. Un solo mantenedor y sin firmas: se fija el commit para que una actualización no cambie el contenido sin revisión. |

Riesgo residual: los skills son instrucciones que el agente sigue. La revisión cubre el contenido actual, no una versión futura. Cualquier actualización del repositorio exige repetir la auditoría y cambiar el pin.

### 3. Adaptaciones locales

| Cambio | Motivo |
| --- | --- |
| `~/.claude/linkedin/` pasa a `docs/privado/linkedin/` | El perfil de voz puede contener clientes, cifras y posiciones personales; `docs/privado/` ya está excluido de git. |
| `python3` pasa a `uv run --no-project python` | Windows no incluye `python3` y el proceso de OpenCode arrancó antes de instalar Python 3.14.7, así que heredó un PATH sin Python. `uv` fija Python 3.15 y evita depender del PATH o de paquetes globales. |
| Las referencias internas `/li-human`, `/li-post`, `/li-plan` y `/li-audit` pasan a nombrar el skill | El agente no puede invocar comandos de la TUI desde dentro de un skill; sí puede cargar otro skill con la herramienta `skill`. |
| `li-post/hooks.json` pasa a `../li-post/hooks.json` en los skills hermanos | La ruta relativa correcta desde `.opencode/skills/li-plan` o `li-repurpose` es la del directorio hermano. |
| Se añaden 11 comandos `li-*.md` | OpenCode no convierte skills en comandos; el pack se diseñó para Claude, donde cada skill se invoca como `/li-*`. |
| La plantilla de voz se traduce y se guarda en `docs/marca-personal/linkedin/voice-template.md` | Deja una plantilla pública sin datos personales; el archivo de trabajo se copia a la carpeta privada. |
| `li-post` registra el texto publicado, no el borrador, con imagen, enlace y panel | Los posts del 31 de octubre y del 2 de noviembre se editaron antes de publicar; el historial debe coincidir con lo que ve la audiencia. |

### 4. Instalación

- 11 skills en `.opencode/skills/li-*`: `li-audit`, `li-carousel`, `li-comment`, `li-dm`, `li-human`, `li-inbox`, `li-plan`, `li-post`, `li-profile`, `li-reply` y `li-repurpose`.
- 11 comandos en `.opencode/commands/li-*.md`, ejecutados por el agente `build` y en la sesión actual.
- Perfil de voz en `docs/privado/linkedin/voice.md`, construido el 2026-10-25 desde tres publicaciones propias.
- Plantilla pública en `docs/marca-personal/linkedin/voice-template.md`.

### 5. Verificación

- En la instalación del 2026-10-25, los tres JSON auxiliares parseaban: 21 ganchos, 81 palabras y 32 frases del léxico, 17 clases de caracteres invisibles, 11 sustituciones tipográficas, 11 señales estructurales y una rúbrica de 12 apartados.
- `humanize.py` y `detect.py` se ejecutan con `uv` y sin dependencias.
- Un texto de control en inglés pasó de 78,0 a 95,6 con veredicto PASS tras eliminar el BOM.
- En esa misma prueba, el borrador en español quedó en 1.102 caracteres, con 0 términos del léxico, 0 señales estructurales y 1 artefacto eliminado (BOM). El panel devolvió 57,2 REVIEW: SLOP y FINGERPRINT al 100, BURSTINESS en 89,3, SPECIFICITY en 57,2 y VOICE en 30,0, porque los pronombres y las contracciones que medía VOICE aún estaban calibrados para inglés.
- `humanize.py` reescribe los saltos de línea como CRLF, así que el fichero limpio mide 1.118 caracteres. El texto no cambia: solo el BOM desaparece y los finales de línea se normalizan.
- El skill `li-post` se cargó con la herramienta `skill`, leyó el perfil de voz, eligió tres ganchos y generó el borrador completo.

## Estado de resolución

- Instalado y verificado el 2026-10-25.
- `/li-post` operativo y con prueba de extremo a extremo.
- Perfil de voz definitivo desde el 2026-10-25: dos registros, aperturas, giro, cierres, posiciones, límites, pruebas y las tres muestras originales. La sección `Ruido de las muestras que no replico` separa la voz de las erratas.
- Los tres posts generados con `/li-post` se publicaron el 2026-10-27, el 2026-10-31 y el 2026-11-02, y quedaron registrados en `docs/privado/linkedin/log.md`; falta medir su rendimiento.
- Limitación conocida: el panel de cinco comprobaciones se calibró en castellano el 2026-10-31 y se recalibró el 2026-11-02 con las 36 publicaciones exportadas (16 PASS, 17 REVIEW y 3 FLAGGED). Ese día se añadió un suelo para los textos sin pronombres pero con verbos en primera persona, porque el castellano omite el sujeto. Sigue siendo una heurística local: PASS significa «parece tu voz», no «es indetectable».
- Mantenimiento: si se actualiza el repositorio, revisar el diff, repetir la auditoría y actualizar el commit pin de esta ficha.

## Uso

| Comando | Función |
| --- | --- |
| `/li-post` | Convierte una idea en un post con tres ganchos y un borrador humanizado. |
| `/li-human` | Limpia un borrador y lo puntúa con el panel local. |
| `/li-comment` | Redacta comentarios para publicaciones de otras personas. |
| `/li-reply` | Clasifica y responde a los comentarios de un post propio. |
| `/li-profile` | Puntúa el perfil sobre 100 y reescribe lo que pierde puntos. |
| `/li-plan` | Planifica la semana y guarda el plan en la carpeta privada. |
| `/li-carousel` | Convierte una idea secuencial en un carrusel. |
| `/li-repurpose` | Extrae una semana de posts de un vídeo, artículo o transcripción. |
| `/li-dm` | Redacta la nota de conexión y los seguimientos. |
| `/li-inbox` | Clasifica la bandeja y redacta solo las respuestas útiles. |
| `/li-audit` | Analiza el rendimiento de lo ya publicado. |

Ejemplo:

```text
/li-post he instalado un pack de 11 skills de LinkedIn tras auditar el código
```

El comando no publica. Devuelve el texto listo para copiar y espera confirmación antes de registrar nada en el historial.
