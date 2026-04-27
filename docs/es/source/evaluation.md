(evaluation)=

# Evaluación del TRE conforme a SATRE

Esta sección detalla el método para evaluar un TRE con respecto a la especificación SATRE.

## ¿Quién debería evaluar un TRE conforme a SATRE?

Esta sección está dirigida a {ref}`operadores <infrastructure_roles>` y {ref}`responsables de gobernanza de la información <governance_roles>` de TRE en instituciones que alojan proyectos de investigación con datos sensibles. Los ejemplos de evaluaciones proporcionados también pueden ser útiles para {ref}`desarrolladores <infrastructure_roles>` de TRE que deseen revisar implementaciones existentes, así como la propia especificación.


(why_evaluate)=

## ¿Por qué debería evaluar el TRE de mi institución?

La especificación SATRE se ha elaborado a partir del conocimiento acumulado sobre la provisión exitosa de TRE en diversas instituciones. Esto incluye procedimientos de gobernanza de la información, tecnología informática, gestión de datos y otras capacidades.

Al puntuar el TRE de la institución con respecto a la especificación, utilizando el método que se describe a continuación, es posible:

1. Identificar omisiones técnicas en el diseño del TRE que podrían dar lugar a divulgaciones no intencionadas de datos sensibles o a accesos inapropiados por parte de los usuarios.
2. Identificar procedimientos operativos que podrían mejorarse en el TRE y cómo mejorarlos, lo que también permitirá minimizar riesgos y garantizar el funcionamiento fluido de los proyectos de investigación basados en TRE.
3. Elaborar una lista de capacidades que el TRE no posee (o que podrían mejorarse). Por ejemplo, podría citar la especificación SATRE como evidencia para justificar la asignación de recursos (computacionales o humanos) por parte de la institución.

:::{note}
SATRE no es una norma técnica para la cual pueda obtenerse una acreditación formal. Para más información, véase: {ref}`is_standard`
:::

## Evaluaciones disponibles públicamente

Actualmente se encuentran disponibles en el [sitio de la comunidad SATRE UKTRE](https://satre.uktre.org/en/)ejemplos de evaluaciones de TRE del Reino Unido. 
Estos ejemplos muestran cómo distintas instituciones han evaluado sus TRE con respecto a la especificación SATRE y pueden servir de guía para el proceso de evaluación propio.

Se anima a las organizaciones a compartir sus evaluaciones en beneficio de la comunidad y como contribución a la transparencia. Al hacer públicas las evaluaciones, se puede mejorar colectivamente la provisión de TRE en todo el sector y aprender de las experiencias y enfoques de otras instituciones.

(scoring_method)=

## Método

Debería asignarse una puntuación al TRE con respecto a cada declaración de la especificación SATRE utilizando el siguiente sistema de puntuación:

:0 - No cumplido: El TRE no cumple este requisito (si el requisito es **Obligatorio**, esto significa que el TRE no es conforme con SATRE).
:1 - Suficiente: El TRE cumple este requisito, pero existe un margen sustancial de mejora.
:2 - Satisfactorio: El TRE cumple este requisito, aunque todavía puede existir margen de mejora.
:N/A: No aplicable: La declaración no es relevante para un TRE. Puede aplicarse a declaraciones de tipo **Recomendado** u **Opcional**, así como a un número muy limitado de declaraciones de tipo **Obligatorio\***.

Una puntuación de **1** o superior significa que el requisito se ha cumplido. De forma opcional, es posible utilizar las puntuaciones **1** y **2** para indicar posibles áreas de mejora en el TRE.

Una evaluación puede limitarse a asignar puntuaciones a cada declaración para el TRE. No obstante, se recomienda una evaluación más detallada, que incluya una puntuación, una justificación y, cuando corresponda, sugerencias de mejora.

Las evaluaciones de ejemplo son detalladas e incluyen tanto el texto de apoyo como las puntuaciones.

### Combinación de puntuaciones

Las puntuaciones de cada declaración pueden combinarse fácilmente a nivel de capacidad, pilar o global. 
Si todas las declaraciones de tipo **Obligatorio** de una capacidad se cumplen, ya sea con puntuación **1** o **2**, la capacidad se considera cumplida. 
Si todas las capacidades de un pilar se consideran cumplidas, el pilar se considera cumplido. Si todos los pilares se consideran cumplidos, la especificación SATRE se considera cumplida.

(evaluate_spreadsheet)=

## Hoja de cálculo de evaluación

Puede utilizarse la siguiente [hoja de cálculo](satre.xlsx)como plantilla para la evaluación: