# Temario Arquitectura de Producto de Datos | ITAM  | 2021

### Aproximación de la materia
Esta clase tiene como objetivo brindar una introducción a la ingeniería de datos e ingeniería de aprenizaje de máquina para científicos de datos tomando en cuenta las últimas practicas y tecnologías mayormente adoptadas y validadas por las empresas tecnológicas más maduras del mundo.

Busca dar a los estudiantes un perspectiva holística del ecosistema de infrastrucutura de datos planteado planteado por Matt Bornstein, Martin Casado, y Jennifer Li en su artículo [*Emerging Architectures for Modern Data Infrastructure*](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/) enfatizando el nuevo paradigma de computo en la nube sin servidores (*serverless computing*). 

Además es imperativo contextualizar el trabajo del científico de datos dentro de una organización donde la toma decisiones basada en evidencia es repsonsabilidad de un equipo (de datos) donde los roles de sus integrantes se han especializado en los últimos años para tener cada día responsabilidades y habilidades más especializadas que no solo son responsabilidades del científico de datos. 

Por último, como lo plantea el artículo [*Hidden Technical Debt in Machine Learning Systems*](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf), se busca posicionar el reto de mantener y escalar una arquitectura de producto de datos de aprendizaje de máquina con base en el *trade-off* entre la agilidad de producción y la deuda tecnica que suele incurrirse por la falta diseños robustos en arquitecturas de productos de datos.


### Temario
1. Introducción a la arquitectura de producto de datos
2. Innovación con datos
    1. Planteamiento de projecto (project scoping)
    2. Equipos modernos de Ciencia de Datos: ingeniero de datos, cientifico de datos, investigador de aprendizaje de máquina, inginiero de aprendizaje de máquina
    3. [Administración y ejecución de productos de datos](https://www.oreilly.com/radar/practical-skills-for-the-ai-product-manager/)
3. [Arquitecturas modernas de datos]
    1. Inteligencia de Datos/Descriptiva
    2. Inteligencia Artificial/Predictiva
4. Infraestructura *severless* en la nube: Google Cloud Platform
5. Fuentes de datos: API como caso de uso
6. Ingeniería de Datos
7. Governanza de Datos: Gestión de Identidades y Accesos (IAM)
8. ETL vs ELT
9. Orquestador: Airflow
10. Almacenamiento (Data Lake): Google Cloud Storage
11. Almacén de Datos (Data Warehouse): BigQuery
12. Inteligencia de Datos: Looker
13. Maquinas Virtuales con aceleradores GPU/TPU
14. Modelación de Aprendizaje de Maquina en la nube: empaquetamiento de modelo (docker vs python-package)
15. Ingenieria de datos para grandes volumnes de datos: Apache Beam vs Spark vs Bigquery
16. MLOps (CI/CD)
17. Ingeniería de Aprendizaje de Máquina: Producción 
18. Monitorización


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
