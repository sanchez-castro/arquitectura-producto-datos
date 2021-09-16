# Temario Arquitectura de Producto de Datos | ITAM  | 2021

Esta clase tiene como objetivo brindar una introducción a la ingeniería de datos e ingeniería de aprenizaje de máquina para científicos de datos tomando en cuenta las últimas practicas y tecnologías mayormente adoptadas y validadas por las empresas tecnológicas más maduras del mundo.

El objetivo es **(1)** dar una perspectiva holística del ecosistema de infrastructura de datos actualizada, **(2)** contextualizar el trabajo del científico de datos dentro de una organización y **(3)** desarrollar las habilidades necesarias para diseñar e implementar una infraestructura de datos escalabale para resolver un problema de negocio.

### Perspectiva holística del ecosistema de infrastructura de datos
Se estudirá el ciclo de ingeniería de datos a través del análisis "Arquitecturas Modernas de Infrastructura de Datos" planteado por Matt Bornstein, Martin Casado, y Jennifer Li en su artículo [*Emerging Architectures for Modern Data Infrastructure*](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/) enfatizando el nuevo paradigma de computo en la nube sin servidores (*serverless computing*) y el surgimiento de Servicios de Software (SaaS) auto-gestionables (self-managed) especializados en los componentes de una Arquitectura de Producto de Datos. 

### El rol del científico de datos dentro de una organización
Se contextualizará el trabajo del científico de datos dentro de una organización, donde la toma decisiones basada en evidencia es repsonsabilidad de un equipo (de datos) cuyos roles se han especializado en los últimos años para tener responsabilidades y habilidades más enfocadas y específicas dentro del ciclo de ingeniería de datos. 

### Trade-off entre agilidad de producción y deuda técnica
Se diseñará y desarrollará una arquitectura de producto de datos bajo el análisis del *trade-off* entre la agilidad de producción y la deuda técnica que suele incurrirse por la falta diseños robustos para la manutención y escalamiento de arquitecturas de productos de datos. Inspirado en el debate presentado en el artículo [*Hidden Technical Debt in Machine Learning Systems*](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) por investigadores del equipo de Google . 


### Temario
1. Innovación con datos
    1. Arquitecturas modernas de datos
        - Inteligencia de Datos/Descriptiva
        - Inteligencia Artificial/Predictiva
    2. Equipos modernos de Ciencia de Datos: ingeniero de datos, cientifico de datos, investigador de aprendizaje de máquina, inginiero de aprendizaje de máquina
    3. [Administración y ejecución de productos de datos](https://www.oreilly.com/radar/practical-skills-for-the-ai-product-manager/)
        - Planteamiento de projecto (project scoping)
        - Trade-off: Agilidad de producción y deuda técnica
    4. Repercusiones y responsabilidades éticas de un producto de datos. 
2. Infraestructura *severless* en la nube: Google Cloud Platform
3. Fuentes de datos: API como caso de uso
4. Ingeniería y Governanza de Datos: Gestión de Identidades y Accesos (IAM)
5. ETL vs ELT
6. Orquestador: Airflow
7. Almacenamiento (Data Lake): Google Cloud Storage
8. Almacén de Datos (Data Warehouse): BigQuery
9. Inteligencia de Datos: Looker
10. Maquinas Virtuales con aceleradores GPU/TPU
11. Modelación de Aprendizaje de Maquina en la nube: empaquetamiento de modelo (docker vs python-package)
12. Ingenieria de datos para grandes volumnes de datos: Apache Beam vs Spark vs Bigquery
13. MLOps (CI/CD)
14. Ingeniería de Aprendizaje de Máquina: Producción 
15. Monitorización


### Principios en la construcción de arquitecturas deproducto de datos 

1. **Choose good data over complex models**
2. **Don't fight your infrastructure**
    - Use managed services over custom tools 
3. **Storage is cheap; people are not**
    - Bring data into your DB/DW as raw as possible and transform with SQL/common tools
    - Choose ELT over ETL 
4. **Don't duplicate tools**
    - Choose flexible software over tools that support specific use cases
5. **Avoid bulky, legacy tech**
    - HDFS is no longer cutting edge
    - Build for the cloud; avoid on-prem
6. **Build, measure, learn**
    - Work quickly, iterate often 

### Recursos adicionales
1. [Machine Learning Design Patterns](https://www.oreilly.com/library/view/machine-learning-design/9781098115777/)
2. [Data Science on the Google Cloud Platform](https://www.oreilly.com/library/view/data-science-on/9781491974551/)
3. [Practical AI on the Google Cloud Platform](https://www.oreilly.com/library/view/practical-ai-on/9781492075806/)
4. [Google BigQuery: The Definitive Guide](https://www.oreilly.com/library/view/google-bigquery-the/9781492044451/)

### Instructores
**[Adrian Sanchez-Castro](https://www.linkedin.com/in/sanchez-castro/) & [Jake Klein](https://www.linkedin.com/in/jake-klein-180498b9/)**
