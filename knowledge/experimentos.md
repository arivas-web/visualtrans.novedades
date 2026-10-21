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
| E01 | Asunto de invitación | Fecha y hora + novedad protagonista | Fecha y hora + «todas las novedades» | invitacion (métrica: registros) | 0 | — | — | — | Abierto (vForwarding 26.3 #01–#04) |
| E02 | Asunto de píldora | Resultado concreto + «mira cómo funciona» | Pregunta-gancho | novedad | 0 | — | — | — | Abierto (vForwarding 26.3 #10 en adelante) |

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
