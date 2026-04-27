(satre_roles)=

# Roles

Un TRE conforme a la especificación SATRE debe ofrecer una experiencia similar, en términos generales, a las partes interesadas que operan en cada uno de los roles definidos a continuación. 
No existe necesariamente una correspondencia uno a uno entre roles y personas. Una misma persona puede desempeñar múltiples roles.

(project_roles)=

## Roles del proyecto

Roles correspondientes a los usuarios finales del TRE que realizan investigación o análisis de datos dentro del TRE, así como a otras personas involucradas en la gestión de dicha investigación.

```{list-table}
:header-rows: 1
:name: tab-tre-role-project

* - Nombre del rol
  - Descripción del rol
* - Consumidor de datos (Data Consumer)
  - Término general que designa a cualquier persona a la que se le conceda acceso a datos a través de un TRE.
* - Analista de datos (Data Analyst)
  - Término específico para las personas a las que se les concede acceso a datos a través de un TRE con el objetivo de realizar análisis o llevar a cabo investigación utilizando dichos datos.
    Pueden tratarse de programadores y científicos de datos, pero también de científicos de otros ámbitos en los que la experiencia avanzada en computación es menos habitual.
    Los analistas que trabajan con TRE que cumplen el estándar SATRE deben contar con una experiencia de usuario en términos generales similar, al menos cuando el tipo de analista sea comparable (por ejemplo, científicos de datos).
    Esto incluye tanto la experiencia de uso de las propias plataformas como la documentación asociada.
* - Responsable del proyecto (Project Manager)
  - Persona encargada de coordinar a los demás roles durante la duración de un proyecto específico que utiliza un TRE.
    Véase {ref}`project_management`.
* - Equipo del proyecto (Project Team)
  - Hace referencia al conjunto de analistas de datos y responsables de proyecto que trabajan en un proyecto específico que utiliza un TRE.

```

(data_roles)=

## Roles de gestión de datos

Roles correspondientes a las personas responsables de gestionar los datos y las bases de datos utilizadas en un TRE.

```{list-table}
:header-rows: 1
:name: tab-tre-role-data

* - Nombre del rol
  - Descripción del rol
* - Responsable de datos (Data Steward)
  - Personas que garantizan que los datos dentro de un TRE se mantengan y procesen de forma útil para los {ref}`analistas de datos (project_roles)` <project_roles>`, incluida la provisión de extractos de datos.
    También pueden denominarse Data Wranglers (especialistas en preparación de datos), Data Engineers (ingenieros de datos) o Data Cleaners (especialistas en depuración de datos).
* - Administrador de bases de datos (Database Administrator)
  - Personas responsables de la gestión de cualquier base de datos incluida en el TRE.
    Cuando una base de datos es utilizada por múltiples proyectos, este rol incluye la gestión de la segregación de usuarios y de bases de datos correspondientes a distintos proyectos.
    Véase {ref}`advanced_CCC`.
* - Propietario del activo de información (Information Asset Owner)
  - Término general para los custodios o propietarios de conjuntos de datos, proyectos u otros activos de información dentro de un TRE.
    Por ejemplo, el propietario de un conjunto de datos que haya coordinado con un {ref}`operador del TRE (infrastructure_roles)<infrastructure_roles>` {ref}`el ingreso seguro de datos (data_lifecycle_management)<data_lifecyle_management>` en el TRE.
* - Revisor de salidas (Output Checker)
  - Personas responsables de evaluar el riesgo de divulgación de las salidas de un proyecto antes de su egreso, como parte del proceso de control de divulgación.
    Véase {ref}`output_management`.
```

(infrastructure_roles)=

## Roles de gestión de infraestructura

Profesionales de TI e ingenieros de software responsables del desarrollo, despliegue y gestión de instancias de TRE conformes a la especificación SATRE.

```{list-table}
:header-rows: 1
:name: tab-tre-role-administrator

* - Nombre del rol
  - Descripción del rol
* - Operador (Operator)
  - Personas responsables de la gestión de la infraestructura de TI del TRE y de los procesos generales documentados a lo largo de la especificación SATRE.
    Entre sus funciones se incluyen, por ejemplo, la gestión del ingreso y egreso de datos y la administración del acceso de los usuarios.
    Se espera que los operadores del TRE tengan acceso a documentación relativa a todos los procesos que deban ejecutar, elaborada por ellos mismos o por los desarrolladores del TRE, o en colaboración con estos últimos.
    Dicha documentación debe ser exhaustiva e incluir procedimientos de resolución de problemas (véase {ref}`knowledge_management`).
* - Desarrollador (Developer)
  - Personas responsables de construir la infraestructura de software que puede utilizarse    como TRE.
    Pueden ser ingenieros de software de investigación, cuyo trabajo consiste en aplicar prácticas profesionales de ingeniería de software a desafíos propios de la investigación científica.
    Alternativamente, pueden ser desarrolladores contratados para construir un TRE para una institución o proyecto específico.
    Los desarrolladores de TRE incluyen tanto a quienes crean plataformas a medida para requisitos específicos de un proyecto o conjunto de datos, como a quienes desarrollan soluciones generalizables para la provisión de TRE que pueden configurarse según el contexto de investigación.

* - Constructor (Builder)
  - Personas responsables de llevar a cabo el {ref}`infrastructure_deployment_process`.
    Este rol puede ser asumido tanto por operadores del TRE como por desarrolladores del TRE.
```

(governance_roles)=

## Roles de gobernanza

Roles encargados de sostener la gobernanza de los TRE.
Estas responsabilidades suelen implicar el establecimiento de políticas y procedimientos para garantizar el uso responsable de los datos, proteger la privacidad y la confidencialidad de los participantes en la investigación y promover la transparencia y la rendición de cuentas en las actividades de investigación.

```{list-table}
:header-rows: 1
:name: tab-tre-role-governance

* - Nombre del rol
  - Descripción del rol
* - Responsable de gobernanza de la información (Information Governance Manager)
  - Personas responsables de redactar y/o compilar los procedimientos operativos y las políticas adecuadas para el TRE.
* - Responsable de calidad (Quality Manager)
  - Personas responsables de garantizar que el TRE funcione correctamente y que todos los procedimientos y políticas sean seguidos por los demás roles y resulten eficaces.
    Véase {ref}`quality_management`.
* - Alta dirección (Top Management)
  - Personas que dirigen y controlan una organización en el nivel más alto.
    Esta definición procede de la norma ISO 9000:2015 y, en este contexto, se refiere al responsable de gobernanza de mayor nivel que asume la propiedad de los riesgos asociados a la investigación en TRE, puede tomar decisiones y asignar recursos.
    Véase {ref}`risk_ownership_process`.
* - Responsable de protección de datos (Data Protection Manager)
  - Personas responsables de la {ref}`protección de datos <data_protection>` en la organización que aloja el TRE.
* - Auditor
  - Término general del ámbito de TI que designa a las personas que evalúan los sistemas de TI de una organización para determinar si cumplen con requisitos normativos de carácter tecnológico o de ciberseguridad.
    En el caso de los TRE, esto puede incluir requisitos relacionados con el tratamiento de datos sensibles y los controles de seguridad de la información.
    Los auditores pueden ser internos o externos, por ejemplo, personal de una empresa consultora.

```

(public_roles)=

## Roles públicos

Roles relacionados con la participación de miembros del público en los TRE y en la investigación realizada a través de estos entornos.

```{list-table}
:header-rows: 1
:name: tab-tre-role-public

* - Nombre del rol
  - Descripción del rol
* - Panel ciudadano (Lay Panel)
  - Miembros del público encargados de la supervisión de decisiones operativas del TRE en representación de las partes afectadas por el uso de los datos.
* - Titular de los datos (Data Subject)
  - Personas identificables a partir de los datos utilizados para la investigación, por ejemplo, pacientes cuyos datos proceden de registros sanitarios.
```
