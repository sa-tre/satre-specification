# Arquitectura estándar para entornos de investigación confiables (SATRE)

```{toctree}
:hidden:
:caption: Sobre SATRE

self
```

```{toctree}
:hidden:
:caption: Especificación

La especificación SATRE <specification.md>
Evaluación conforme a SATRE <evaluation.md>
Alineación de controles SATRE <alignment.md>
Glosario <https://glossary.uktre.org/en/stable/>
```

```{toctree}
:hidden:
:caption: Arquitectura

Visión general de la arquitectura <architecture.md>
principles.md
roles.md
Arquitectura de SATRE <https://satre-archimate.readthedocs.io/en/latest/?view=id-4349bc52159b48e9b785e9809a876c03>
```

```{toctree}
:hidden:
:caption: FAQs

faqs.md
```

(what_is_satre)=

## ¿Qué es SATRE?

SATRE (Standard Architecture for Trusted Research Environments [Arquitectura estándar para entornos de investigación confiables]) es la primera especificación abierta del Reino Unido, impulsada por la comunidad, para los Entornos de Investigación Confiables (TRE). SATRE se desarrolló mediante una amplia colaboración con más de 60 organizaciones y con una sólida base de participación pública.Proporciona un marco integral para el diseño, la operación y la evaluación de TRE en los ámbitos académico, sanitario, industrial y gubernamental.

Los TRE son entornos informáticos seguros diseñados específicamente para la investigación con datos sensibles o personales. Permiten a la comunidad investigadora acceder a los datos y analizarlos de forma segura, minimizando al mismo tiempo el riesgo de exposición o divulgación de los datos. SATRE aporta coherencia y buenas prácticas a la forma en que estos entornos se diseñan, operan y gobiernan.


SATRE se basa en cuatro  [principios rectores](principles.md): **Usabilidad, mantenimiento de la confianza pública, observabilidad y estandarización.** Estos principios garantizan que los TRE no solo sean seguros y conformes, sino también accesibles para la comunidad investigadora y dignos de confianza para el público.

### Introducción al proyecto SATRE

```{raw} html
<div style="max-width: 640px; margin: 20px auto;">
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe src="https://www.youtube-nocookie.com/embed/auExNHEGwcc"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
    </iframe>
  </div>
</div>
```

## Por qué SATRE es importante

Los datos personales y sensibles recopilados con fines operativos, comerciales o gubernamentales tienen un enorme valor para la investigación que beneficia a la sociedad. Sin embargo, el acceso a estos datos requiere marcos sólidos de seguridad, gobernanza y ética. En ausencia de estandarización, los TRE del Reino Unido se han desarrollado de forma independiente, lo que ha dado lugar a:

- Normas de gobernanza y enfoques de seguridad inconsistentes
- Dificultades para las personas investigadoras que trabajan en múltiples TRE
- Desafíos para los propietarios de los datos a la hora de comprender y confiar en el funcionamiento de los TRE
- Barreras para la colaboración y el intercambio de datos entre instituciones
- Duplicación de esfuerzos en el desarrollo de capacidades de los TRE

## La especificación SATRE

La [especificación SATRE](especificación.md) define 160 requisitos, organizados en capacidades que los TRE deben implementar para garantizar una investigación segura, protegida y eficaz con datos sensibles. Cada requisito se clasifica como Obligatorio u Opcional, lo que proporciona flexibilidad sin dejar de mantener estándares esenciales.

Los requisitos se estructuran en cuatro pilares interconectados.

### Los cuatro pilares de SATRE

**1. [Gobernanza de la información](specification.md#information-governance)**
Gestión de la calidad, gestión de riesgos, impartición de formación, acreditación de miembros y procedimientos de gobernanza que garantizan que los TRE operen de forma segura y ética..<br>
**2. [Tecnología de computación](specification.md#computing-technology-and-information-security)**
Experiencia de computación del usuario final, gestión de la infraestructura, seguridad de la información y gestión de la configuración para entornos seguros de análisis de datos. <br>
**3. [Gestión de datos](specification.md#data-management)**
Gestión del ciclo de vida de los datos, gestión de identidades y accesos, gestión de salidas, búsqueda y descubrimiento de información y capacidades de metadatos de investigación. <br>
**4. [Capacidades de apoyo](specification.md#supporting-capabilities)**
Gestión financiera, participación e involucramiento del público, gestión de proyectos, adquisiciones y otras funciones operativas esenciales.

## La Arquitectura SATRE

La [Arquitectura](architecture.md) proporciona una arquitectura integral de alto nivel para organizaciones de investigación que gestionan datos sensibles de forma segura. Las capacidades requeridas se documentan junto con los roles, procesos, datos y aplicaciones clave que permiten materializar dichas capacidades. Al proporcionar esta arquitectura, quienes diseñan e implementan TRE podrán identificar incorporaciones y cambios necesarios dentro de su organización para garantizar que la investigación con datos sensibles pueda realizarse de forma segura.

## La confianza pública como eje central

SATRE integra la participación y el involucramiento del público a lo largo de su desarrollo y dentro de la propia especificación. A través de talleres con miembros del público, se identificó que la ciberseguridad, la supervisión, la transparencia y la participación pública son esenciales para mantener la confianza en los TRE.

### La voz pública en acción

Dos miembros del público formaron parte del equipo central del proyecto SATRE desde el inicio, garantizando que las perspectivas públicas influyeran en todos los paquetes de trabajo. Los comentarios recibidos en los talleres públicos dieron lugar directamente a:

- La elevación de las declaraciones de Participación e involucramiento del público de Opcional a Obligatorio para los TRE que utilizan datos personales
- La inclusión de requisitos para que los TRE informen públicamente sobre incidentes y cuasi incidentes
- La incorporación de especificaciones detalladas sobre transparencia e información dirigida al público
- El fortalecimiento de los requisitos de supervisión y gobernanza

## Participar en SATRE

- [Contribuir en GitHub](https://github.com/sa-tre/satre-specification)
- [Unirse a la comunidad TRE del Reino Unido](https://www.uktre.org/)

## Versiones

```{list-table}
:widths: 12 18 70
:header-rows: 1

* - Versión
  - Fecha de publicación
  - Notas de la versión
* - [1.1.0](https://satre-archimate.readthedocs.io/en/v1.1.0/)
  - 2025-07-01
  - - Se añadió la gestión de salidas como capacidad, conforme a la especificación.
    - Se añadieron las declaraciones de la especificación como requisitos y se vincularon a las capacidades.
    - Se añadió, cuando fue posible, la URL de las declaraciones de la especificación en la documentación.
    - El pilar de Capacidades de apoyo se alineó con la especificación.
    - Se crearon vistas para todas las capacidades de apoyo.
    - Se añadieron todos los requisitos a las vistas.
* - 1.0.0
  - 2023-10-05
  -
```

## Publicaciones

- Ed Chalstrey, Jim Madge, James Robinson, Simon Li, Hari Sood, Arron Lacey, Matt Craddock, Tim Machin, Chris Cole, & Martin O'Reilly. (2025). sa-tre/satre-specification: Version 1.1.1 (v1.1.1). Zenodo. https://doi.org/10.5281/zenodo.17353472
- Simon, L. (2025, October 15). A standard architecture for TREs: why is it important in a federated world?. Health Data Research UK Conference 2025, Glasgow. Zenodo. https://doi.org/10.5281/zenodo.17305295
- Johnston, J., Sheane, S., Almond, E., Whiting, A., Higgins, D., Nadin, R., Hagen, J.-A., & Billins, T. (2025). SATRE Centric Control Alignment Table for Trusted Research Environments. TRE Community, Leeds. Zenodo. https://doi.org/10.5281/zenodo.16837077
- Machin, T., Chalstrey, E., Cole, C., Craddock, M., Hetherington, J., Li, S., Madge, J., O'Reilly, M., Robinson, J., Swanepoel, N., & Hari, S. (2023). A Standard Architecture for Trusted Research Environments (1.01). Zenodo. https://doi.org/10.5281/zenodo.10053383
- Katie Oldfield, Dr Christian Cole, Jillian Beggs, & Antony Chuter. (2023). SATRE Public Involvement and Engagement Final Report. Zenodo. https://doi.org/10.5281/zenodo.10084354
- Dr Christian Cole, Hari Sood, Dr Simon Li, Katie Oldfield, Matt Craddock, Nel Swanepoel, Professor Sonya Coleman, Dr Martin O'Reilly, Dr Dermot Kerr, Dr Cian O'Donovan, Professor James Hetherington, Dr Jim Madge, David Sarmiento-Perez, Ed Chalstrey, Dr James Robinson, Jillian Beggs, Tim Machin, & Antony Chuter. (2023). SATRE: Standardised Architecture for Trusted Research Environments. Zenodo. https://doi.org/10.5281/zenodo.10055345
- Li, S., Christian, C., O'Reilly, M., Jim, M., Craddock, M., Chalstrey, E., & Sarmiento-Perez, D. (2023, October 25). SATRE Evaluation workshop: Evaluating your TRE. Zenodo. https://doi.org/10.5281/zenodo.10040590
- Chalstrey, E., Cole, C., Coleman, S., Craddock, M., Hetherington, J., Kerr, D., Li, S., Madge, J., O'Donovan, C., Oldfield, K., O'Reilly, M., Sarmiento-Perez, D., Sood, H., & Swanepoel, N. (2023, April 18). SATRE – Standardised Architecture for Trusted Research Environments (Kick off). Zenodo. https://doi.org/10.5281/zenodo.7853186

## Agradecimientos

Se agradece el siguiente apoyo para este proyecto:

- UKRI a través del programa TREvolution, fase 2, de [DARE Phase 2](https://dareuk.org.uk/news-and-events/dare-uk-phase-2-is-underway-but-what-does-this-mean-for-everyone/)
- UKRI a través del programa de proyectos impulsores, fase 1, de ([SATRE](https://dareuk.org.uk/how-we-work/previous-activities/dare-uk-phase-1-driver-projects/satre-standardised-architecture-for-trusted-research-environments/))
