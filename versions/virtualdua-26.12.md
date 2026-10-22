# Ficha de versión

> Fuente: paquete `entrada/virtualdua-26.12/` (datos.json + landings HTML en `build/`: `novedades.html` y una por novedad) y mensaje de Adrián del 22/10/2026 (sin webinar; lanzamiento el 5/11/2026).

- División: Virtual DUA (doc)
- Versión: 26.12 (doc)
- Fecha de lanzamiento: 2026-11-05 (Adrián). Ojo: el datos.json pone `month_year: "Octubre 2026"` y ese texto puede aparecer en las landings; hay que corregirlo a noviembre o quitarlo antes de publicarlas.
- Fecha prevista de la siguiente versión: `[DATO]` (no aparece en el material)
- ¿Hay webinar?: no (Adrián)
  - Fecha y hora del webinar: no aplica
  - Landing de invitación (URL): no aplica
  - Enlace de la sala (URL): no aplica
- Landing de la versión (URL): `[URL: landing general de novedades 26.12]`. Existe como HTML (`build/novedades.html`), sin URL pública.
- Landings por novedad (URL): `[URL: ...]` para las cuatro. Existen como HTML (`build/26-12-*.html`), sin URL pública.
- Histórico de novedades (doc): `https://visualtrans.com/productos/empuries/novedades/`. Apunta a la ruta de **Empuries**, no de Virtual DUA (la página dice «Virtual DUA y Empuries»). Confirmar si es la URL correcta o si existe una de Virtual DUA.
- Contacto que figura en las landings (doc): soporte@visualtrans.com
- Lista(s) de destino en HubSpot: `[DATO]` (lo decide Adrián)
- Exclusiones: `[DATO]` (lo decide Adrián)
- Vídeos: ninguno en el material (doc). `[DATO: vídeo de cada novedad]`
- Idea central (doc): «Menos pasos manuales, más control en cada expediente.» Entradilla: «Virtual DUA lee tus facturas con IA, te trae el ARC de EMCS a la pantalla y simplifica el pago de tributos y los justificativos.»

## Novedades
Ordenadas por potencial de email.

### Novedad 1. Principal (doc: `rol: principal`)
- Título: Carga facturas y packing lists en el DUA sin teclear (doc; módulo interno «Digitalización con IA · vExtract»)
- Qué hace: Virtual DUA lee con IA la factura comercial y el packing list, cruza cada línea de uno con la del otro y monta los datos de cabecera y las partidas del DUA, sea un DUA nuevo o uno ya existente. Agrupa las partidas por código de mercancía y origen, y el usuario revisa y valida. Los PDF se arrastran o se suben desde Outlook sin descargar el adjunto, y si se suben varios se consolidan en un único DUA. (doc)
- Problema que resuelve / beneficio: elimina copiar a mano número y fecha de factura, importes, contenedor, bultos y pesos, y agrupar partidas con calculadora. Es lo que más tiempo consume y donde se cuelan errores de transcripción. «Si el expediente tiene 13 líneas o 60, tu esfuerzo es el mismo: revisar el resultado.» Funciona con distintos formatos de factura sin configurar plantillas previas. Avisa si la factura ya está en otro expediente. (doc) Única cifra del material: el ejemplo ilustrativo «13 líneas → 10 partidas» (doc, es un ejemplo, no un dato de ahorro). Cifra de ahorro: `[DATO: tiempo ahorrado por expediente]`
- A quién afecta: todos los usuarios que tramitan DUAs a partir de facturas y packing lists, sobre todo tramitadores y operaciones y quien trabaja con muchos proveedores (doc: sección «Para quién»). Horizontal dentro de la base (deducido).
- Potencial de email: alto (horizontal, muy visual y demostrable en vídeo: PDF → partidas)
- Vídeo (URL y duración): `[DATO]`
- Producto de otra división que encaja para cross-selling: no evidente. vForwarding tiene una función parecida de digitalización con IA, pero es para transitarios y no es un cross-sell claro (deducido). Por regla actual, cross-selling «todo a todos».
- Notas para el redactor:
  - Es un **borrador** que el usuario revisa: «La responsabilidad sobre la declaración sigue siendo tuya». No prometer que el DUA se hace solo ni que no hay errores. Lo que no viene en el documento (incoterm, bultos) queda vacío: «no se inventa». (doc)
  - Ubicación: botón **DUAS PDF**; tres opciones: actualizar datos, actualizar partidas, añadir partidas. (doc)
  - Activación (doc): «se activa con la actualización de versión», pero el CTA de la landing es «Escríbenos para probarlo» (mailto a soporte con asunto «Quiero probar vExtract en Virtual DUA») y dice «lo ponemos en marcha». **Ambiguo**: ¿está incluido para todos sin coste o requiere alta, activación por soporte o contratación? No prometer «incluido» ni «gratis» hasta confirmarlo.
  - El nombre interno «vExtract» sí aparece de cara al cliente en la landing (en negrita); se puede usar como nombre de marca, pero el título debe ir en beneficio.

### Novedad 2
- Título: Justificativos de varios DUAs a la vez (doc)
- Qué hace: los documentos justificativos posteriores al levante se crean en bloque desde el planificador: buscas los DUAs pendientes, los seleccionas y pulsas «Crear justificativo». Se crean con la factura comercial (N380), sin indicarla partida a partida. Se marca «acorde» o «a regularizar» en el primer DUA y el programa pregunta si se aplica a todos. (doc)
- Problema que resuelve / beneficio: antes era DUA a DUA y partida a partida; con cientos de DUAs pendientes era «inabarcable». Ahora, «en unos pocos clics». (doc) Cifra de ahorro: `[DATO: tiempo ahorrado por lote]`. La única cifra del material es técnica: la AEAT admite hasta 999 MRN a la vez (doc).
- A quién afecta: segmento: tramitadores de importación con DUAs pendientes de justificativo posterior al levante, sobre todo los que acumulan volumen (deducido).
- Potencial de email: medio (nicho, pero muy alto valor para quien lo sufre; demostrable en vídeo)
- Vídeo (URL y duración): `[DATO]`
- Producto de otra división que encaja para cross-selling: no evidente.
- Notas para el redactor:
  - Recomendación de producto: lotes pequeños divididos por fecha; con demasiados MRN de golpe la respuesta de la AEAT puede tardar mucho. No vender «999 de golpe». (doc)
  - El DUA de importación no se modifica; el cambio está solo en el planificador. (doc)
  - Los documentos del justificativo se definen en un parámetro (separados por comas). (doc) ¿Viene configurado o hay que configurarlo? `[DATO]`

### Novedad 3
- Título: Un método de pago para cada tributo (doc)
- Qué hace: el método de pago deja de ser único para todo el DUA. Puedes elegir uno por tributo, por ejemplo garantía del cliente para el arancel y el antidumping y pago previo para el IVA, y el H1 envía cada tributo a la aduana con el suyo. (doc)
- Problema que resuelve / beneficio: antes se aplicaba a todos el método de la cabecera y la garantía podía no llegar a la aduana; ahora ningún tributo sale sin garantizar. Evita un error, no ahorra tiempo. (doc)
- A quién afecta: segmento: tramitadores de importación que combinan garantía y pago previo en un mismo DUA (doc: «Para quién»). Afecta al H1 (importación).
- Potencial de email: medio (nicho; ángulo de «error que evita»; poco vistoso en vídeo)
- Vídeo (URL y duración): `[DATO]`
- Producto de otra división que encaja para cross-selling: no evidente.
- Notas para el redactor: no prometer nada sobre la aceptación por la aduana más allá de «el H1 envía cada tributo con su método». No hay cifras.

### Novedad 4
- Título: El ARC de EMCS, sin salir de Virtual DUA (doc)
- Qué hace: al recibir la aceptación de un envío EMCS, la propia ventana de envío ofrece descargar el CSV del e-DA o imprimirlo. Es el mismo documento que ofrece la AEAT, obtenido a partir del ARC, no un impreso de Virtual DUA. (doc)
- Problema que resuelve / beneficio: evita salir del programa y entrar en la Sede Electrónica de la AEAT en cada envío para descargarlo. (doc) Sin cifra.
- A quién afecta: segmento: usuarios del módulo EMCS (impuestos especiales), envíos internos e intracomunitarios (doc + deducido).
- Potencial de email: bajo-medio (nicho y mejora de un clic; mejor como bloque dentro de otro correo o en el de «ya disponible» que como píldora propia, salvo para la base EMCS)
- Vídeo (URL y duración): `[DATO]`
- Producto de otra división que encaja para cross-selling: no evidente.
- Notas para el redactor: si el documento no está aceptado, no cambia nada (sigue la impresión por programa). Funciona igual que en Exportación cuando se recibe el circuito del DUA. (doc)

## Descartado para email
- Nada descartado: las cuatro novedades tienen impacto para el usuario. El material no incluye correcciones de errores ni cambios internos.

## Avisos
- Fecha del material: `month_year: "Octubre 2026"` frente a un lanzamiento el 5/11/2026. Revisar las landings antes de publicarlas.
- URL del histórico en la ruta de Empuries (`/productos/empuries/novedades/`). No usarla en los correos de Virtual DUA sin confirmarlo.
- Landings sin publicar: ningún correo puede enlazar a ellas hasta tener la URL. Quedan como `[URL: ...]`.
- vExtract: activación o condiciones comerciales ambiguas (ver Novedad 1). No prometer «incluido» ni «sin coste».
- Justificativos: no animar a enviar lotes grandes (recomendación de lotes pequeños por fecha).
- Sin cambios normativos con fecha obligatoria en esta versión.
