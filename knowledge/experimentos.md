# Experimentos – bucle de mejora continua

Registro vivo de los test A/B. Lo mantiene el subagente `optimizador` después de cada envío. El `redactor` lo lee antes de escribir o reescribir cualquier correo: la **variante A es siempre el campeón vigente** y la **B, el retador** del experimento abierto.

## Reglas del bucle
1. **Una sola variable por experimento** (asunto, preheader, CTA, primera línea, bloque de cross-selling…). Si cambian dos cosas a la vez, no se sabe cuál ha funcionado.
2. **Campeón frente a retador.** La A es lo mejor que conocemos; la B, una alternativa con una hipótesis concreta.
3. **Se acumulan envíos** del mismo experimento hasta decidir, siempre comparando de igual a igual (mismo tipo de correo y audiencia parecida).
4. **Decisión con `scripts/ab_test.py`** sobre los datos acumulados (mínimo 300 entregados por variante):
   - Probabilidad de que B sea mejor ≥ 95% y mejora ≥ 10% relativa → **gana B**: pasa a campeón.
   - Probabilidad ≤ 5% → **gana A**: se descarta el retador.
   - Entre 80% y 95% (o entre 5% y 20%) → **tendencia**: se repite el mismo par.
   - Sin decisión tras 4 envíos → **empate**: se cierra sin cambio y se prueba otra cosa.
5. **Métrica:** CTR por clics únicos sin bots; registros en las invitaciones y en los correos de webinar. El CTOR acompaña, no decide.
6. **El ganador sube al playbook** solo si la decisión es «gana» (confianza alta). Las tendencias van a «En observación».
7. **Vigilancia del campeón:** si el campeón cae por debajo de su media durante 3 envíos seguidos, se reabre el experimento.
8. **Frenos:** si un envío supera un 0,3% de bajas o un 0,5% de rebotes duros, se para el experimento y se avisa a Adrián antes de seguir.
9. **Nunca** se tocan las reglas fijas de la secuencia ni se inventan datos para un retador, y nada se envía ni se programa: el bucle propone y Adrián aprueba, programa y envía.

## Experimentos abiertos
| ID | Variable | Campeón (A) | Retador (B) | Tipo de correo | Envíos | A entreg./conv. | B entreg./conv. | P(B mejor) | Estado |
|---|---|---|---|---|---|---|---|---|---|
| E01 | Asunto de invitación | Fecha y hora + novedad protagonista | Fecha y hora + «todas las novedades» | invitacion (métrica: registros) | 0 | — | — | — | Abierto (vForwarding 26.3 #01–#04, que no se envía; DeiWorld #01–#03) |
| E03 | Cuerpo de píldora | Narrativo estándar (60–120 palabras) | Corto (≤ 60 palabras): problema en una frase, resultado y botón | novedad (métrica: CTR por clics únicos) | 0 | — | — | — | Abierto (DeiWorld #07–#14) |
| E02 | Asunto de píldora | Resultado concreto + «mira cómo funciona» | Pregunta-gancho | novedad | 0 | — | — | — | Abierto (vForwarding 26.3 #10 en adelante) |

## Plan registrado antes de enviar: DeiWorld, webinar del 5/11/2026
Se escribe antes del primer envío y no se cambia después de ver datos.
- **Base:** unos 75 contactos (lista de Adrián). Reparto 50/50 sobre toda la lista en cada envío, **sin ganador automático** (la fase de prueba serían ~15 personas). HubSpot reasigna en cada envío.
- **E01 (#01, #02 y #03):** solo cambia el asunto. Métrica que decide: clics únicos a la landing; los registros por variante (UTM `-a`/`-b`) acompañan, porque se esperan unos 9. El #04 no entra: su asunto ya es «las cuatro novedades».
- **E03 (#07 a #14):** solo cambia el cuerpo. Asunto, preheader, botón, vídeo y P. D. idénticos en A y B. Métrica que decide: CTR por clics únicos; los clics al vídeo acompañan.
- **Excepción a la regla 4:** con 37 entregados por variante y envío, el mínimo de 300 por variante solo se alcanza con 8 envíos. E03 se evalúa con `--max-envios 8`; E01 nunca llegará al mínimo y se registra como tendencia, como mucho.
- **Qué puede detectar (simulación, 22/10/2026):** con 8 envíos sumados, si B dobla el CTR de A (6% → 12%), se declara ganador un 81% de las veces; si lo mejora un 50% (6% → 9%), solo un 41%. Es optimista: las 75 personas se repiten en cada envío. Diferencias pequeñas no se verán.
- **Limpieza:** clics sin bots, descontando contactos internos.
- **Observación O01 · P. D. (no es A/B):** Adrián limita la P. D. a uno o dos correos «para ver cómo funciona» (23/10/2026). Va en el #01 (invitación) y el #07 (novedad), igual en A y B, con un enlace propio al mismo destino que el botón: `invitacion-01-landing-pd-a` / `-pd-b` y `novedad-01-video-pd`. Al sacar métricas, el `optimizador` informa de: clics del enlace de la P. D. sobre el total de clics del correo, y cuántos clicadores únicos **solo** hicieron clic en la P. D. (los que el correo habría perdido sin ella). Conclusión orientativa: si aporta menos del 5% de los clicadores únicos, la P. D. no se usa por defecto; si aporta un 15% o más, pasa a la cola de hipótesis como A/B en una base grande (hipótesis 7). Con esta base, es una lectura, no una regla.
- **Uso para los siguientes eventos:** lo que gane con confianza alta pasa al playbook; lo demás, a «En observación», a la espera de repetir el mismo par en una base mayor.

## Cola de hipótesis (siguiente retador cuando se cierre un experimento)
Ordenadas por impacto esperado según el playbook. El `optimizador` coge la primera que aplique al tipo de correo.
1. Cross-selling con beneficio concreto frente a genérico (necesita el beneficio de cada producto).
2. CTA con duración del vídeo («Ver cómo funciona (2 min)») frente a sin duración.
3. Primera línea con el problema frente a primera línea con el resultado.
4. Asunto con cifra frente a asunto con resultado sin cifra (cuando producto dé cifras).
5. Preheader que completa el asunto frente a preheader con el dato de fricción (duración, «sin registro»).
6. Correo corto (≤ 60 palabras) frente a correo estándar (60–120 palabras).
7. P. D. con segundo enlace frente a sin P. D.

## Experimentos cerrados
| ID | Variable | Ganador | Mejora | P(B mejor) | Envíos | Fecha | Pasa al playbook |
|---|---|---|---|---|---|---|---|
