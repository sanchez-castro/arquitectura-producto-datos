# Temario Arquitectura de Producto de Datos | ITAM  | Primavera 2022

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
    1. Píramide de necesidades de ciencia de datos 
    2. Arquitecturas modernas de datos
        - Inteligencia de Datos/Descriptiva
        - Inteligencia Artificial/Predictiva
    2. Equipos modernos de Ciencia de Datos: ingeniero de datos, cientifico de datos, investigador de aprendizaje de máquina, inginiero de aprendizaje de máquina, manager de producto AI/ML
    3. [Administración y ejecución de productos de datos](https://www.oreilly.com/radar/practical-skills-for-the-ai-product-manager/)
        - Planteamiento de projecto (project scoping)
        - Trade-off: Agilidad de producción y deuda técnica
    4. Repercusiones y responsabilidades éticas de un producto de datos. 
    5. Buenas practicas de programacion: documentación (GitHub is King), programación modular y cultura de trabajo
2. Infraestructura de datos en la nube: Google Cloud Platform
    - Data warehouse vs Data lakes
    - Hadoop to serverless
    - Terraform
    - Governanza de Datos: Gestión de Identidades y Accesos (IAM)
3. Fuentes de datos: API como caso de uso
4. ETL vs ELT
5. Orquestador: Airflow vs Kubeflow vs Cloud Pipelines (AI Pipelines) 
6. Almacenamiento (Data Lake): Google Cloud Storage
7. Ingenieria de datos para grandes volumnes de datos: Apache Beam vs Spark vs Bigquery
8. Almacén de Datos (Data Warehouse): BigQuery
9. Inteligencia de Datos: Looker
10. Maquinas Virtuales con aceleradores GPU/TPU
11. Modelación de Aprendizaje de Maquina en la nube:
    - AutmoML como baseline
    - Notebooks vs Py-Script: Sagemaker vs Vertex AI
    - Empaquetamiento de modelo (Docker vs "Python-package")
12. MLOps (CI/CD)
13. Ingeniería de Aprendizaje de Máquina: Producción 
14. Monitorización: 


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
    - Work quickly and iterate often 

### Recursos adicionales
1. [Machine Learning Design Patterns](https://www.oreilly.com/library/view/machine-learning-design/9781098115777/)
2. [Data Science on the Google Cloud Platform](https://www.oreilly.com/library/view/data-science-on/9781491974551/)
3. [Practical AI on the Google Cloud Platform](https://www.oreilly.com/library/view/practical-ai-on/9781492075806/)
4. [Google BigQuery: The Definitive Guide](https://www.oreilly.com/library/view/google-bigquery-the/9781492044451/)

### Instructores
**[Adrian Sanchez-Castro](https://www.linkedin.com/in/sanchez-castro/) & [Jake Klein](https://www.linkedin.com/in/jake-klein-180498b9/)**

### Organizaciones invitadas a dar *Perspectivas* sobre productos de datos
- Google Brain
- Twitter
- New York Times
- Amazon
- Walmart
- Nike
