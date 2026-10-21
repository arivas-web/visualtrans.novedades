# Agente de Novedades de Versión – Visual Trans

Agente de Claude Code que genera las secuencias de email de las nuevas versiones de **Virtual DUA, Empuries, vForwarding, Suite y The Wall**, basándose en los datos reales de HubSpot y aprendiendo de cada envío.

## Cómo se usa
1. Abre el repositorio con Claude Code.
2. Pásale el documento de la versión: déjalo en `entrada/` o pega el texto en el chat.
3. El agente extrae la información, te pide los datos que falten y te entrega los correos en texto plano, cada uno con su fecha de envío.
4. Revisas los correos y das feedback. Después, el agente maqueta cada correo en HTML y crea el Google Doc final.
5. Con tu OK explícito, monta los correos en HubSpot como borradores. Tú los programas y los envías.
6. 48 horas después de cada envío, el agente mide los resultados, decide qué variante gana y mejora los siguientes correos: cada uno parte del mejor resultado conocido y prueba una cosa nueva.

## Estructura
```
CLAUDE.md                  Agente principal (coordinador y reglas)
.claude/agents/
  extractor.md             Documento → ficha de versión
  analista.md              Baseline, objetivos y aprendizaje tras cada envío
  planificador.md          Calendario de la secuencia
  redactor.md              Redacción de los correos
  revisor.md               Control de calidad y entregabilidad
  maquetador.md            HTML optimizado para conversión a partir de la plantilla
  optimizador.md           Bucle de mejora continua: mide, decide los A/B y mejora el siguiente correo
  publicador.md            Montaje de borradores en HubSpot (solo con OK)
knowledge/
  playbook.md              Baseline y reglas basadas en datos (lo actualiza el analista)
  marca.md                 Look and feel del email y guía de marca
  plantilla-email.html     Plantilla HTML de los correos
  experimentos.md          Experimentos A/B abiertos y cerrados, campeón vigente y cola de hipótesis
scripts/
  ab_test.py               Decisión estadística de los A/B con los envíos acumulados
versions/
  _plantilla-ficha.md      Estructura de la ficha de versión
entrada/                   Documentos originales (excluidos de git)
outputs/                   Borradores y resultados (excluidos de git)
```

## Requisitos
- Claude Code con los conectores de **HubSpot** y **Google Drive** configurados.

## Reglas clave
- Nunca envía ni programa nada: envía y programa Adrián. En HubSpot solo lee datos y, con OK, crea borradores.
- Todos los enlaces llevan UTM: `utm_source=hubspot&utm_medium=email&utm_campaign={division}-{version}&utm_content={tipo}-{n}-{enlace}`.
- Una novedad por correo, segmentada según a quién afecta.
