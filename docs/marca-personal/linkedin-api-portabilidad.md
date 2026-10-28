# API de portabilidad de LinkedIn: lectura de perfil, red y publicaciones

## Objetivo

Dar acceso de solo lectura a los datos de LinkedIn mediante la API que LinkedIn publica para cumplir el Reglamento de Mercados Digitales, de modo que el contenido propio, la red de contactos y el historial de publicaciones estén en el repositorio y no dependan de copiar y pegar.

## Por qué esta vía y no otra

No existe un permiso de lectura en los productos autoservicio de LinkedIn: `Sign In with LinkedIn` solo entrega nombre, foto y correo, y `Share on LinkedIn` solo permite escribir. El acceso a datos personales está en los **productos regulatorios**, que exigen consentimiento explícito del miembro y son revocables.

La alternativa descartada es automatizar la sesión con Playwright. `linkedin.com` lo prohíbe en su `robots.txt` y el riesgo es una restricción de la cuenta con la que se busca empleo. La API no tiene ese riesgo: es la vía documentada, con Términos aceptados y token revocable.

## Alcance de la lectura

La API tiene dos endpoints y el cliente solo sabe llamar a esos dos, siempre con `GET`.

| Endpoint | Qué devuelve |
| --- | --- |
| `memberSnapshotData` | Fotografía completa por dominio, con histórico |
| `memberChangeLogs` | Eventos desde el consentimiento, ventana de 28 días |

Dominios descargados por defecto con `--core`: perfil, experiencia, formación, aptitudes, certificaciones, proyectos, cursos, idiomas, premios, publicaciones, voluntariado, recomendaciones, validaciones, contactos, invitaciones, publicaciones y reposteos propios, comentarios propios, reacciones propias, empresas y personas seguidas, empleos guardados y candidaturas.

`INBOX`, `SEARCHES`, `PREMIUM_NOTES` y `AD_TARGETING` existen pero no se descargan salvo petición explícita, por contener conversaciones privadas y datos de navegación.

## Lo que no trae

Ningún dominio contiene impresiones, alcance, visitas al perfil ni apariciones en búsquedas. Las métricas de rendimiento solo existen en la pantalla de Analítica de LinkedIn y se siguen copiando a mano. La API resuelve el archivo del contenido, no la medición.

Tampoco incluye los comentarios que otras personas dejan en las publicaciones propias. Comprobado el 2026-10-27 con dos fuentes independientes: el CSV `Comments.csv` y el dominio `ALL_COMMENTS` devuelven los mismos 38 comentarios, todos escritos por el miembro. Para leer un hilo de respuestas sigue haciendo falta copiarlo a mano.

## Alta en el portal

Esta parte la hace la persona, no el agente: implica iniciar sesión en LinkedIn y aceptar unos Términos en nombre propio.

1. Entrar en `developer.linkedin.com` y crear una aplicación.
2. Al asociar la página de empresa, elegir **Member Data Portability (Member) Default Company**. Crear una página nueva invalida la solicitud.
3. En la pestaña **Products**, solicitar **Member Data Portability API (Member)** y aceptar los Términos.
4. Si la pestaña **Auth** exige una URL de redirección, añadir `https://oauth.pstmn.io/v1/callback`, que es la que la propia documentación de LinkedIn propone para pruebas.
5. En **Docs and tools → OAuth Token Tools → Create token**, elegir la aplicación y el scope `r_dma_portability_self_serve`.
6. Autorizar en la pantalla de consentimiento y copiar el token junto con su tiempo de vida, que aparece en la misma página.

El token se pega en `.env` como `LINKEDIN_DMA_TOKEN=...`. OpenCode no lee `.env`, pero el cliente sí lo parsea, así que no hace falta exportar la variable al sistema.

## Uso del cliente

El cliente vive en `scripts/linkedin-portability.py` y no tiene dependencias: usa solo la biblioteca estándar de Python.

```
python scripts/linkedin-portability.py check
python scripts/linkedin-portability.py domains
python scripts/linkedin-portability.py snapshot --core
python scripts/linkedin-portability.py snapshot CONNECTIONS MEMBER_SHARE_INFO
python scripts/linkedin-portability.py changelog
python scripts/linkedin-portability.py describe
```

`check` confirma que el consentimiento está activo y muestra desde cuándo. `snapshot` descarga y pagina por dominio hasta agotar los resultados. `changelog` guarda el punto de control en `state.json` para no repetir eventos entre ejecuciones. `describe` resume lo descargado sin salir a la red.

Los datos quedan en `docs/privado/linkedin/api/`, que está fuera de git.

## Seguridad

- El cliente solo emite `GET`, valida que el host sea `api.linkedin.com` y comprueba el recurso contra una lista de tres permitidos. Cualquier otra cosa aborta antes de salir a la red.
- El token es una credencial bearer con acceso de lectura a la cuenta. Vive en `.env`, que está ignorado por git, y no se escribe en logs ni en los JSON descargados.
- El consentimiento se revoca desde el mismo portal, y el token deja de valer de inmediato.
- Si el token caduca, `check` devuelve 401 con la causa indicada.

## Estado

Cliente escrito y verificado en sus rutas locales el 2026-10-26: listado de dominios, resumen de datos y guardas de host y recurso.

Primera descarga autenticada el 2026-10-26 con consentimiento concedido a las 13:09 UTC. Los dominios aparecen de forma progresiva: `PROFILE`, `SKILLS` y `CONNECTIONS` llegaron en la primera pasada, mientras `MEMBER_SHARE_INFO`, `ALL_COMMENTS` y `POSITIONS` seguían en proceso. Un 404 con el mensaje `No data found for this domain and memberId` no significa error, sino que LinkedIn todavía no ha collacionado ese dominio; el cliente lo trata como pendiente y continúa con el resto en lugar de abortar.

Segunda pasada el 2026-10-27: `MEMBER_SHARE_INFO` devolvió 34 publicaciones y `ALL_COMMENTS` 38 comentarios, cifras idénticas a las del CSV de la exportación. `POSITIONS` seguía pendiente.

La paginación devuelve filas solapadas entre páginas: `ALL_COMMENTS` llegó con 75 filas en dos páginas, de las que 37 eran duplicados exactos. El cliente deduplica por fila completa antes de guardar y deja constancia en `rawRowCount` de cuántas llegaron sin depurar.

El changelog empieza a registrar eventos desde el momento del consentimiento, así que hasta que haya actividad nueva en la cuenta devuelve una lista vacía.
