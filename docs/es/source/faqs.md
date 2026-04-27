(faqs)=

# Preguntas frecuentes

- {ref}`what_tre`
- {ref}`why_satre`
- {ref}`how_developed`
- {ref}`who_developed`
- {ref}`is_standard`
- {ref}`is_everything`
- {ref}`developer_gain`
- {ref}`operator_gain`
- {ref}`how_build`
- {ref}`set_in_stone`
- {ref}`other_tre_types`
- {ref}`support_federation`

(what_tre)=

## ¿Qué es un TRE?

TRE significa _Trusted Research Environment_ (Entorno de investigación confiable). La definición más sencilla suele ser la de _cualquier_ entorno informático configurado para la investigación con datos sensibles, que cuenta con controles de seguridad integrados y funciones de gestión del acceso de los usuarios. La definición de TRE relevante para SATRE abarca el conjunto de procesos de gobernanza de la información y gestión de datos, junto con la tecnología informática utilizada para apoyar la investigación con datos sensibles; entendiéndose por datos sensibles, en términos generales, cualquier dato respecto del cual puedan existir consideraciones relacionadas con el control de la divulgación, por cualquier motivo.
Se reconoce que en el Reino Unido se han utilizado en la bibliografía otros términos, como _Secure Data Environment_ (entorno seguro de datos) o _Data Safe Haven_ (refugio seguro de datos), para referirse a la computación con datos sensibles, y que estos sistemas pueden recibir otras denominaciones en otros contextos geográficos. Para más información sobre los TRE, puede consultarse el sitio web de What is a TRE [la comunidad TRE de Reino Unido](https://www.uktre.org/en/latest/).

(why_satre)=

## ¿Por qué se necesita una arquitectura estándar para los TRE?

Se han adoptado diversos enfoques para la construcción de infraestructuras informáticas y para el diseño de procesos y políticas destinados a la investigación con datos sensibles. simismo, existen distintos estándares o marcos que pueden aplicarse a los TRE, como [ISO27001](https://www.iso.org/standard/27001) o [5 Safes](https://blog.ons.gov.uk/2017/01/27/the-five-safes-data-privacy-at-ons/)(marco de los cinco principios de seguridad). 

Sin embargo, estos no proporcionan orientaciones prescriptivas sobre cómo los TRE deben cumplir dichos marcos o alcanzar una acreditación. En este contexto, SATRE tiene como objetivo identificar los elementos comunes y compilar un recurso de referencia del que puedan beneficiarse {ref}`operadores, constructores y desarrolladores<infrastructure_roles>` de TRE. Para más información, véase {ref}`what_is_satre`.

(how_developed)=

## ¿Cómo se ha desarrollado la especificación SATRE y por qué?

Véase la información disponible en la página principal de {ref}`esta documentación<satre_why>`.

(who_developed)=

## ¿Quién ha desarrollado la especificación SATRE?

Puede consultarse la página de {ref}`colaboradores`.

(is_standard)=

## ¿Es SATRE una norma técnica ISO?

No.
La especificación SATRE tiene como finalidad proporcionar una guía práctica para {ref}`operadores, constructores y desarrolladores <infrastructure_roles>` de TRE. Puede utilizarse para orientar el proceso de desarrollo de nuevos TRE o para evaluar TRE existentes y determinar cómo podrían mejorarse. La evaluación de un TRE mediante la especificación SATRE puede ayudar a identificar qué normas técnicas (por ejemplo, ISO 27001) ya se cumplen y cuáles podrían ser deseables como objetivo de cumplimiento.

(is_everything)=

## ¿Proporciona SATRE todo lo necesario para construir un TRE?

No.
La especificación SATRE define un conjunto de {ref}`roles <satre_roles>` de las partes interesadas y capacidades funcionales para los TRE, determinados conforme a sus {ref}`principios arquitectónicos <satre_principles>`. No prescribe qué tecnologías específicas deben o deberían utilizarse para construir un TRE.

(developer_gain)=

## ¿Qué obtienen los {ref}`constructores o desarrolladores <infrastructure_roles>` de TRE al leer la especificación SATRE?

Al revisar la especificación SATRE, los desarrolladores a quienes su institución ha encomendado el diseño o la construcción de un TRE para proyectos con datos sensibles pueden evitar reinventar la rueda. La especificación no impone respuestas a las decisiones tecnológicas o normativas concretas que deben adoptarse al desarrollar un TRE, pero sí proporciona una guía para reflexionar sobre qué decisiones deben tomarse y qué  {ref}`capacidades <satre_pillars>` debe tener el TRE.

(operator_gain)=

## ¿Qué obtienen los {ref}`operadores <infrastructure_roles>` de TRE al evaluar su TRE con SATRE?

Véase: {ref}`why_evaluate`

(how_build)=

## ¿Cómo se diseña, implementa y opera un TRE conforme a SATRE?

Se anima a los {ref}`operadores y constructores <infrastructure_roles>` e TRE a evaluar públicamente sus TRE con respecto a la especificación SATRE; véase {ref}`evaluación`. Los {ref}`desarrolladores <infrastructure_roles>` de TRE pueden utilizar la especificación y las evaluaciones publicadas como punto de partida. 

Algunos TRE evaluados, como _[Data Safe Haven](https://data-safe-haven.readthedocs.io/en/latest/)_ del Alan Turing Institute y _[TREEHOOSE](https://github.com/HicResearch/TREEHOOSE/)_ del Health Informatics Centre de University of Dundee, se despliegan mediante infraestructura como código (infrastructure-as-code) de código abierto y pueden ser implementados por otras instituciones.

(set_in_stone)=

## ¿La especificación SATRE es inmutable?

En absoluto. Se reconoce que los TRE varían considerablemente en su arquitectura de diseño, en los fines para los que se crean, en los tipos de investigación que apoyan y en los datos que gestionan.
Se ha procurado elaborar una especificación con un conjunto de capacidades lo más ampliamente útil posible, reconociendo al mismo tiempo estos distintos enfoques. 
No se habrá cubierto todo y, si SATRE resulta valiosa pero se considera que falta algún elemento, se invita a {ref}`contribuir <contributing>`. 
Asimismo, las buenas prácticas en la provisión de TRE pueden evolucionar con el tiempo a medida que cambian las tecnologías y la normativa. 
Se espera que la especificación SATRE se mantenga en el futuro y se adapte a estos cambios cuando corresponda.

(other_tre_types)=

## Mi TRE está diseñado para datos que no requieren este nivel de protección. ¿Debería seguir SATRE de todos modos?

Sí. 
Actualmente, la especificación SATRE incluye un conjunto de capacidades marcadas como Obligatorias, que se consideran esenciales para que un sistema pueda definirse como TRE, así como numerosas capacidades Recomendadas y Opcionales. Es probable que algunas de las capacidades no obligatorias no sean necesarias en TRE que alojan datos que no requieren todas las protecciones posibles, y que existan compensaciones entre accesibilidad y seguridad que dependan de los datos que aloja el TRE. Una futura versión de la especificación podría incluir el concepto de diferentes arquetipos de TRE o niveles de sensibilidad de los datos, con requisitos diferenciados para cada uno.

(support_federation)=

## ¿Describe SATRE enfoques para la federación de TRE o la interoperabilidad entre TRE?

No. No obstante, se prevé que SATRE pueda constituir la base para futuros estándares y orientaciones sobre federación, interoperabilidad y trabajos relacionados.
