(satre_principles)=

# Principios arquitectónicos

Los principios arquitectónicos influyen y orientan la forma en que se diseña y se implementa un TRE alineado con SATRE. 
Constituyen un conjunto de consideraciones rectoras que se sitúan por encima de cualquier requisito arquitectónico específico y pueden aplicarse a toda la arquitectura.

Constan de las siguientes partes: 
:Declaración: Una única oración que resume el principio. 
:Fundamento: Justificación de por qué este principio es importante para la especificación.
:Implicaciones: Aspectos que deben considerarse o acciones que deben llevarse a cabo para aplicar este principio.

(principle_usability)=

## Principio 1 - Usabilidad

### Declaración

Una instancia de TRE que funcione para todos los usuarios minimiza las barreras de uso y proporciona un entorno de análisis productivo y accesible para la investigación.

### Fundamento

Con frecuencia existe una disyuntiva entre un mayor nivel de seguridad operativa y la usabilidad de un TRE. Para mantener la productividad, un TRE debe equilibrar estos dos objetivos contrapuestos. El diseño y la configuración de un TRE deben permitir que todas las personas involucradas puedan cumplir eficazmente sus roles.

### Implicaciones

- El diseño y la implementación robustos de un TRE deben partir de la comprensión de las diversas expectativas, necesidades, competencias existentes, preferencias y responsabilidades de los usuarios.
- El diseño, la configuración y las pruebas de los TRE deben reconocer la diversidad de perfiles de usuario. Por ejemplo, no todos los usuarios son investigadores ni todos los investigadores son usuarios finales. Otros usuarios incluyen operadores de TRE, responsables de gobernanza de la información y desarrolladores o constructores de TRE.
- Debido a la diversidad de necesidades, es poco probable que una instancia concreta de TRE se ajuste perfectamente a todos los usuarios.
- Un TRE excesivamente restrictivo en cuanto a herramientas y software puede volverse inutilizable para usuarios con trayectorias y competencias diversas.
- Los entornos de trabajo pueden diferir de forma significativa de las configuraciones preferidas por los usuarios. Esto tiene implicaciones de diseño y de recursos para el apoyo a nuevos usuarios, por lo que deben considerarse el tiempo y los recursos necesarios para facilitar su adaptación a instancias de TRE nuevas o poco familiares.
- La mejora de la experiencia del usuario requiere tiempo y recursos, e implica compromisos entre invertir en estándares más sólidos, mejorar el diseño funcional, fortalecer la cultura de trabajo y organizacional, reforzar las competencias de los usuarios mediante formación y facilitar el acceso a apoyo a nivel institucional. Estos compromisos deben abordarse a nivel organizacional. Los equipos pueden considerar la asignación de personal dedicado específicamente a estas cuestiones, por ejemplo mediante funciones de gestión de producto o de prestación de servicios.


(principle_maintaining_trust)=

## Principio 2 - Mantenimiento de la confianza pública

### Declaración

Los TRE que alojan datos públicos deben construir y mantener la confianza de los titulares de los datos y de cualquier otra persona, grupo, comunidad u organización afectada, mediante la protección de la privacidad, la seguridad de los datos y la transparencia en sus actividades.

### Fundamento

Para garantizar el apoyo público continuo al uso de datos y de TRE para fines de investigación, resulta esencial mantener la confianza en la forma en que los TRE almacenan y utilizan los datos, así como mitigar posibles preocupaciones. Esto incluye la confianza de las personas cuyos datos se conservan, de quienes se ven afectados por la investigación realizada y de los proveedores comerciales de datos.

En el caso de los datos del sector público, los procesos de participación pública han mostrado que existe apoyo al uso de TRE regulados y éticos orientados al beneficio público, siempre que se cumplan condiciones relativas a la seguridad y la transparencia. La consulta a las partes afectadas, incluida la ciudadanía, contribuye a garantizar que los TRE se utilicen con fines positivos, pertinentes y acordados. La transparencia respecto de los datos alojados y de los proyectos u organizaciones que acceden a ellos también contribuye a mantener la confianza.

### Implicaciones

- La máxima transparencia posible es un elemento clave para generar confianza. Los TRE que alojan datos públicos deben aplicar prácticas de transparencia. Por ejemplo, deben estar disponibles públicamente la acreditación por parte de un organismo externo, la adhesión a un marco de diseño específico (como el marco _Five Safes_) y la información sobre los proyectos u organizaciones que acceden a los datos. Esta información debe proporcionarse de manera accesible.
- Además de la transparencia, la participación activa del público en la supervisión de los TRE y de sus procesos es fundamental para la rendición de cuentas. La participación y el involucramiento del público requieren tiempo y recursos. Los TRE que alojan datos públicos deben considerar la asignación específica de personal y presupuesto para actividades de participación pública.
- Cuando se haya consultado a las partes afectadas, los TRE deben ser auditables por dichas partes e incorporarlas en los procesos de toma de decisiones. Esto puede incluir la provisión de documentación y recursos educativos dirigidos a públicos diversos.
- El acceso a datos del sector público debe ser revisado por un panel independiente que incluya, cuando sea posible, a miembros del público, y debe regirse por mecanismos de gobernanza acordados que garanticen el beneficio público de los proyectos y aporten claridad respecto de cualquier acceso de carácter comercial.


(principle_observability)=

## Principio 3 - Observabilidad

### Declaración

Los procesos iniciados por personas y los procesos automatizados que generan cambios dentro del TRE deben ser observables.

### Fundamento

La observabilidad de sistemas y procesos es fundamental para comprender si las políticas y los controles funcionan conforme a lo previsto.

Asimismo, permite a los operadores mejorar continuamente sus sistemas y procesos, medir su eficacia e identificar las causas de incidentes. Los datos generados también pueden ponerse a disposición de otras partes, como auditores, titulares de los datos y proveedores de datos, como parte de los procesos de aseguramiento.

Este principio se aplica tanto a los sistemas técnicos como a las políticas y los procesos.

### Implicaciones

- Para comprender lo que ocurre dentro del TRE, tanto los procesos automatizados como los iniciados por personas deben generar datos suficientes, por ejemplo mediante registros de auditoría. Los datos generados deben ajustarse a estándares de procedencia y transparencia que permitan la trazabilidad de auditoría.
- Pueden requerirse distintos niveles de observabilidad según el tipo de usuario. Los datos recopilados con fines de observabilidad deben responder a las necesidades de quienes los utilizarán y limitarse al mínimo necesario.
- Al implementar el principio de observabilidad, deben considerarse posibles implicaciones éticas y de confidencialidad.


(principle_standardisation)=

## Principio 4 - Estandarización

### Declaración

Los TRE deben adherirse, siempre que sea posible, a estándares o patrones ampliamente reconocidos.

### Fundamento

La estandarización facilita el diseño, la operación, el uso y la comprensión de los TRE, y reduce la duplicación de esfuerzos. Asimismo, contribuye a que los TRE sean más fáciles de usar, desplegar y auditar.

Los TRE deben construirse de forma que no restrinjan ni impidan la interoperabilidad cuando esta pueda ser deseable en el futuro, identificando y evitando o eliminando barreras a dicha interoperabilidad.

La estandarización también está vinculada al principio de confianza pública, ya que un enfoque estandarizado facilita que las partes afectadas comprendan cómo se utilizarán sus datos dentro de los TRE.

### Implicaciones

- Debido a la definición amplia de los [TREs](https://glossary.uktre.org/en/latest/#term-trusted-research-environment--tre-), tactualmente no existen estándares técnicos ni de gobernanza de la información específicos para estos entornos.
  Por ello, la especificación SATRE se ha diseñado para ayudar a {ref}`desarrolladores y operadores<infrastructure_roles>` con distintos requisitos técnicos y normativos a considerar sus opciones.
- Los {ref}`desarrolladores y operadores<infrastructure_roles>` de TRE deben estar preparados para identificar los estándares técnicos pertinentes hacia los cuales orientar el desarrollo o mantenimiento de sus TRE.
- Los estándares a los que un TRE puede adherirse pueden abarcar requisitos técnicos, operativos y de gobernanza.
- Los {ref}`desarrolladores y operadores<infrastructure_roles>` deben garantizar que, cuando se propongan cumplir múltiples estándares, dichos estándares sean coherentes entre sí, de modo que no existan contradicciones entre los requisitos.

Pueden existir razones válidas por las cuales un TRE concreto no disponga de una o más de las capacidades descritas en esta especificación; no obstante, la mayoría de los TRE deberían aspirar a cumplirlas a largo plazo.
