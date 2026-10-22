# Playbook – Correos de novedades de versión

Fuente: auditoría de HubSpot del 21/10/2026 (envíos de oct 2025 a oct 2026, métricas sin bots). Contraste adicional: exportes de Drive de Adrián (770 correos y 5.000 formularios de ene. 2022 a oct. 2025, sin filtro de bots confirmado), analizados en `outputs/vforwarding-26.3/analisis-drive.md`. El analista actualiza este archivo; solo entran aprendizajes de confianza media o alta.

## Baseline por tipo de correo
| Tipo | División / ejemplo | CTR | CTOR |
|---|---|---|---|
| Lanzamiento «ya disponible» | Suite 26.07 (#1) | 3,1% | 12,7% |
| Lanzamiento «ya disponible» | Suite 25.16 | 2,9% | 13,5% |
| Notas de versión | Virtual DUA (nov 25 – jun 26) | 6–23% | 21–54% |
| Notas de versión | Empuries (feb 26) | 8,9% | 27,9% |
| Invitaciones webinar | vForwarding 26.1 (#1) | 7,0% (3,78% sobre elegibles, 80 clics) | 27,6% |
| Invitaciones webinar | vForwarding 26.2 (#1–#4) | 0,9–2,4% (#1: 1,64% sobre elegibles, 29 clics) | 4,6–11,7% |
| Recordatorios webinar | vForwarding 26.2 (#5–#7) | 0,75–1,4% | 4,8–8,6% |
| «En directo» (sala) | vForwarding 26.2 / 26.1 | 3,5% / 6,5% (sobre elegibles: 3,11% / 1,58%; 73 / 47 clics) | 18,6% / 18,1% |
| Grabación no asistentes | vForwarding 26.2 | 2,9% | 16,9% |
| Post-webinar clientes | vForwarding 26.1 | 11,2% (3,30% sobre elegibles, 72 clics) | 28,3% |
| Píldora semanal | vForwarding 26.1 (media de 8) | ~1,5% | 7–12% |
| Píldora semanal | Suite 26.07 (4 novedades) | 1,4–4,7% | 6,6–19,5% |
| Refuerzo con vídeo | Suite 25.16 (vNotify, Air tracking, H1) | 3,6–10,5% | 14–28% |
| Cross-selling comercial | Virtual DUA → Vinculador | 0,3–1,6% | 1,5–7,7% |

Asistencia al webinar de vForwarding 26.2: 72 asistentes, ~3,5% de la base.
Media del portal: CTR ~1,5% y CTOR ~8%.

**Cómo leer el baseline (21/10/2026, `analisis-profundo.md`):** hasta junio de 2026 HubSpot dejaba sin enviar al 30–50% de los contactos (los poco activos) y desde julio solo al 1%. Las cifras de 26.1 y anteriores están infladas. Se informa siempre de tres cifras: CTR sobre entregados, **CTR sobre elegibles** (entregados + no enviados) y **clics únicos absolutos**. El «7,0% lanzamiento» de 26.1 era una invitación mal clasificada.

## Reglas (confianza alta)
1. **Relevancia antes que novedad.** En Suite 26.07, la novedad horizontal (copiar y pegar documentos) logró un 4,7% de CTR frente al 1,4–1,65% de las de nicho (RORO, PUE agroalimentario), enviadas a la misma base de unos 5.500 contactos. Cada novedad se segmenta por audiencia.
2. **Beneficio concreto y vídeo antes que intriga.** Los asuntos con cifra o resultado concreto («H1 un 40% más rápido», «mira cómo funciona») alcanzan un CTOR del 20–28%; las preguntas-gancho («¿Tus márgenes son reales?», «Tienes un nuevo compañero») se quedan en el 7–8%.
3. **Formato utilitario en bases de usuarios.** En Virtual DUA y Empuries, «Nueva versión disponible» logra un CTR del 11–23% frente al 0,3–1,6% del cross-selling comercial.
4. *(Pasa a «En observación»: la comparación de 26.2 fue la invitación #1 frente a la #3, confundida con la posición.)* **Las invitaciones informativas ganan a las de intriga:** «La versión 26.2 llega el 30 de junio» (2,4%) frente a «Esto es lo que verás» (0,9%).
   *Revisión del 21/10/2026 (exporte de Drive 2022–2025, `outputs/vforwarding-26.3/analisis-drive.md`): confianza rebajada a **media** hasta comprobar en HubSpot qué posición ocupó cada asunto en 26.2. La regla 7 muestra que la primera invitación gana siempre; en 25.2, la informativa con fecha y BI (posición 2) sacó un 0,97% frente al 5,50% de la de intriga (posición 1). Solo vale comparar asuntos dentro del mismo envío (A/B).*
5. **La grabación rinde casi como el directo** (2,9% frente a 3,5% de CTR). Es un activo que hay que explotar.
   *Refuerzo del 21/10/2026 (exporte de Drive): en 4 de 5 parejas de 2023–2025 la grabación rindió entre el 76% y el 139% del directo (formación vForwarding 2023, AES 2023, Verifactu 2025, Ley Antifraude 2025); la excepción es vForwarding 25.2 (56%).*
6. **Las listas manuales o importadas son un riesgo:** tuvieron entre un 13% y un 31% de rebotes duros, y en junio de 2026 la salud del portal cayó de 84 a 55 por esa causa. Verifactu (noviembre de 2025) tuvo un 22% de rebotes duros.
7. **La primera invitación de una secuencia es siempre la que más CTR saca; las siguientes caen, sea cual sea el asunto.** Fuente: exporte de Drive 2022–2025 (`outputs/vforwarding-26.3/analisis-drive.md`, apartado 2.1). Ocurre en 8 de 8 secuencias (vForwarding 24.1, 24.2, 25.01, 25.2 y 2023; webinars de Aduanas 2024, consignaciones 2024 y Verifactu 2025). Por ejemplo, 25.01: 2,97% → 2,41% → 1,99% → 1,38%. Consecuencia: los asuntos se comparan solo con A/B dentro del mismo envío, nunca entre invitaciones de distinta posición.

9. **El botón entrega algo; nunca pide contacto comercial.** Con un recurso que se usa en el momento (vídeo, guía, FAQ, grabación, landing con las novedades), la mediana de CTR es del 1,97% (85 correos); con «Me interesa», «Quiero activarlo», «Agendar llamada» o /contactar, del 0,67% (37). Mismo tema, distinto botón: Digitalizaciones 3,03% como píldora con vídeo frente a 0,06% como campaña comercial; DeCA, FAQ 4,09% frente a post-DeCA 0,02%. Fuente: `analisis-profundo.md`, punto 2.
10. **El asunto nombra el entregable.** «Documentación para el uso del Sistema de Importación H1.» (19,0%), «Lo prometido: grabación + vídeos del webinar» (14,3%), «sRMT 2.0: manual y vídeo para trabajar con la nueva versión» (4,03%). Fuera la pregunta de alarma o reproche («¿Te adaptas o te toca pedir favores?», 0,20%). *Confianza media: el top está sesgado por una lista de ~730 usuarios de Suite.*

## Reglas (confianza media)
11. **El clic en el correo de sala es el proxy de asistencia** (26.2: 73 clics, 72 asistentes). Los registros están en Vidiv, no en HubSpot.
8. **Los registros al webinar se concentran en el día de la primera invitación y en las últimas 48 horas (víspera y día).** Fuente: formularios del exporte de Drive (`analisis-drive.md`, apartado 2.2). vForwarding 25.2: 29% el día 1 y 39% los dos últimos días (110 registros externos); 24.2: 38% los dos últimos días (123); webinar de factura electrónica 2025: 22% y 35% (345). Las invitaciones del medio aportan poco (25.2, invitación 2: 4%). El recordatorio de la víspera y el correo del día se evalúan también por registros, no solo por CTR.

## En observación (confianza baja)
- Personalizar el asunto con el nombre no muestra una mejora clara.
- En las píldoras de vForwarding 26.1, HubSpot excluyó casi tantos contactos como los entregados. Hay que averiguar si son contactos no comerciales o poco activos.
- *(Exporte de Drive 2022–2025, 21/10/2026; detalle en `outputs/vforwarding-26.3/analisis-drive.md`.)*
  - Los asuntos con pregunta tienen menos CTR (mediana del 1,88% frente al 2,53%, 30 frente a 364 correos), pero el mismo CTOR (9,5%): la pregunta resta aperturas, no clics. Es mezcla de tipos de correo.
  - «Asistente IA» es un gancho flojo: Aduania 4,13% frente al 7,07% de vExtract con la misma base de Suite; en 26.1, 1,23%. Un envío por división.
  - BI como protagonista de una invitación rinde poco: 25.2, 0,97% (posición 2); nurturing de BI, 1,12–1,37%, en el tercio inferior.
  - Día y hora: no se ve efecto que se distinga del tipo de correo; el martes no sale mejor que el lunes. «Martes a jueves a las 10:00» es una convención, no una regla con datos.
  - Emojis en el asunto: sin diferencia (2,40% frente a 2,54% de mediana).
  - Cross-selling: genérico 0,4–0,9% (workflows «Transitarios S/Solución»); con beneficio concreto y gratis (Aduania), 4,76% sobre 1.743. Pocos casos.
  - Los webinars normativos (Aduanas, Verifactu) traen más registros en absoluto (345–671 únicos), pero sobre bases de 7.000–8.000; el de novedades de vForwarding 25.2 registra ~11–13% de su base, con un 1% de correos personales.

## Lagunas de medición
- Los enlaces no llevan UTM: hoy no se pueden medir las visitas a vídeo ni el cross-selling. Se corrige a partir de la primera versión del agente.
- No hay correos de The Wall localizados en HubSpot: pendiente de confirmar con qué nombre aparecen.
- En un A/B de invitación, si A y B llevan el mismo `utm_content`, los registros no se pueden atribuir a cada variante. Hay que añadir la variante (`invitacion-01-landing-a` / `-b`) o un campo oculto en el formulario.
- El exporte de campañas de HubSpot (informe de rendimiento de todas las campañas) calcula la tasa de clics sobre enviados, no consta que filtre bots y tiene un 8% de envíos grandes con 0 clics (avisos sin enlace o sin medir). No se mezcla con el baseline sin bots.

## Objetivos para la primera versión gestionada por el agente
- Píldoras semanales: CTR ≥ 3% y CTOR ≥ 20%.
- Invitaciones: CTR medio ≥ 2,5% y asistencia ≥ 6%.
- Rebotes duros < 0,5% en todos los envíos.
- 100% de los enlaces con UTM.

## Defectos que no pueden repetirse (lectura de cuerpos, 21/10/2026)
- «Hola,  .» con el token de nombre vacío (9 correos) y asuntos que empiezan por «  ,»: si se usa el nombre, siempre con valor por defecto.
- Nombres internos «(Clon)» o «Nuevo correo».
- La encuesta de baja está desactivada: activarla para saber por qué se va la gente.
