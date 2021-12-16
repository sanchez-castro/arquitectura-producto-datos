# Temario Arquitectura de Producto de Datos | ITAM  | Primavera 2022

Esta clase tiene como objetivo brindar una introducción a la ingeniería de datos e ingeniería de aprendizaje de máquina para científicos de datos tomando en cuenta las últimas prácticas y tecnologías mayormente adoptadas y validadas por las empresas tecnológicas más maduras del mundo.

## Aproximación de la materia
El objetivo es **(1)** dar una perspectiva holística del [ecosistema de infrastructura de datos actualizada](https://mattturck.com/data2021/), **(2)** contextualizar el trabajo del científico de datos dentro de una organización y **(3)** desarrollar las habilidades necesarias para diseñar e implementar una infraestructura de datos escalabale para resolver un problema de negocio con base en los pilares anteriormente mencionados.

### 1) Perspectiva holística del ecosistema de infrastructura de datos
Se estudiará el ciclo de ingeniería de datos a través del análisis "Arquitecturas Modernas de Infraestructura de Datos" planteado por Matt Bornstein, Martin Casado, y Jennifer Li en su artículo [*Emerging Architectures for Modern Data Infrastructure*](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/) enfatizando el nuevo paradigma de cómputo en la nube sin servidores (*serverless computing*) y el surgimiento de Servicios de Software (SaaS) auto-gestionables (managed services) especializados en sistemas de análisis de datos y de operación de aprendizaje de máquina.

### 2) El rol del científico de datos dentro de una organización
Se contextualizará el trabajo del científico de datos dentro de una organización, donde la toma decisiones, basada en evidencia, es la tarea principal de un equipo (de datos) cuyos roles se han especializado en los últimos años para tener responsabilidades y habilidades más enfocadas y específicas dentro del ciclo de ingeniería de datos. 

### 3) Trade-off entre agilidad de producción y deuda técnica
Se diseñará y desarrollará una arquitectura de producto de datos bajo el análisis del *trade-off* entre la agilidad de producción y la deuda técnica que suele incurrirse por la falta diseños robustos para la manutención y escalamiento de arquitecturas de productos de datos. Inspirado en el debate presentado en el artículo [*Hidden Technical Debt in Machine Learning Systems*](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) por investigadores del equipo de Google . 

---
## Formato de enseñanza
#### Horario
Martes y Jueves 7.30-9.00 AM 

Las clase tendrán un enfoque de ***learning by doing***:
* La clase será impartida durante dos sesiones de 1.5 horas por clase con un break de 5-7 minutos. 
* La primera sesión de la semana estará enfocada a teoría, discusión en clase y, dependiendo de la clase, se trabajarán algunos ejercicios básicos de programación. 
* La segunda sesión de la semana estará enfocada a aplicar los conceptos aprendidos en la sesión anterior en un ambiente real en la nube. Se trabajará en un ejemplo *end-to-end* durante la clase para que los alumnos puedan replicarlo en su proyecto final que deberán de ir completando en el transcurso del semestre. 

#### Formato
La clase tendrá como objetivo la implementación de un proyecto de "principio a fin" de una arquitectura de producto de datos en la nube a través de ***checkpoints*** de avance durante el transcurso del semestre.

Se formarán equipos de 4 personas que se organizarán durante el primer día de clase de manera aleatoria, pero tomando en cuenta la experiencia y la educación previa de los estudiantes. La idea es tener grupos mixtos de disciplinas y experiencias para reflejar y emular la manera en cómo un científico de datos trabaja en el mundo real laboral. 


#### Checkpoints
Habrán 6 ***checkpoints*** que trendrán que ser reflejados en un repositorio de github. 

1. Definición de projecto en la nube y ambiente de repositorio
2. Configuración de DAG y puesta en marcha
3. Extracción y Carga de datos provenientes de API
4. Transformación y analítica de datos descriptiva
5. Feature Engineering y modelado en la nube
6. Producción y monitorización

#### Evaluación
* Cada checkpoint contruibirá a un punto de la calificación total. Entre ellos podrán sumar un total de 6 de los diez puntos de calificación.
* Los 4 puntos restantes serán ponderados a través de una presentación final.  

\**Cada checkpoint y la presentación final serán calculados por rúbricas disponibles a los estudiantes.



---
## Notas de Clase
Las notas de clase estarán disponibles en la plataforma [Notion](https://www.notion.so/product) disponible en la siguiente liga: [Notion: Arquitectura de Producto de Datos ](https://www.notion.so/Arquitectura-de-Producto-de-Datos-86e9cc35860f48d1baf0e2feb8962441). 

## Temario
1. Innovación con datos
    1. Misión de la organización y problema de negocio
        - Andrew Ng: [Forget about building an AI-first business. Start with a mission](https://www.technologyreview.com/2021/03/26/1021258/ai-pioneer-andrew-ng-machine-learning-business/)
        - Cassie Kozyrkov: [Decision intelligence: Why do business fail at Machine Learning?](https://www.youtube.com/watch?v=dRJGyhS6gA0)
        - Lutz Finer: What is the objective function you are trying to optimze with ML?**
        - Ines Montani: [How to Translate Problems into Solutions: Applied NLP](https://explosion.ai/blog/applied-nlp-thinking)
    2. Píramide de necesidades de ciencia de datos 
    3. Arquitecturas modernas de datos
        - Inteligencia de Datos/Descriptiva
        - Inteligencia Artificial/Predictiva
    4. Equipos modernos de Ciencia de Datos: ingeniero de datos, científico de datos, investigador de aprendizaje de máquina, ingeniero de aprendizaje de máquina, manager de producto AI/ML
    5. [Administración y ejecución de productos de datos](https://www.oreilly.com/radar/practical-skills-for-the-ai-product-manager/)
        - Planteamiento de projecto (project scoping)
        - Trade-off: Agilidad de producción y deuda técnica
    6. Repercusiones y responsabilidades éticas de un producto de datos. 
    7. Buenas prácticas de programación: documentación (GitHub is King), programación modular y cultura de trabajo.
2. Infraestructura de datos en la nube: almacén de objetos, máquinas virtuales, almacén de datos.
    - AWS, GCP, Azure, Databricks y otras "ML platforms"
    - Aproximación de ciencia de datos en la nube: Data warehouse vs Data lakes
    - Hadoop vs Serverless
    - Terraform
    - Governanza de Datos: Gestión de Identidades y Accesos (IAM)

>Checkpoint 1

3. ETL vs ELT
4. Orquestador: Airflow vs Kubeflow vs Cloud Pipelines (AI Pipelines)

>Checkpoint 2

5. Fuentes de datos: API como caso de uso
6. Almacenamiento (Data Lake): Google Cloud Storage
7. Ingeniería de datos para grandes volúmenes de datos: Apache Beam vs Spark vs Bigquery
8. Almacén de Datos (Data Warehouse): BigQuery

>Checkpoint 3

9. Inteligencia de Datos: Looker

>Checkpoint 4

10. Máquinas Virtuales con aceleradores GPU/TPU
11. Modelación de Aprendizaje de Máquina en la nube:
    - AutmoML como baseline
    - Notebooks vs Py-Script: Sagemaker vs Vertex AI
    - Empaquetamiento de modelo (Docker vs "Python-package")
12. MLOps (CI/CD)

>Checkpoint 5

13. Ingeniería de Aprendizaje de Máquina: Producción 
14. Monitorización

>Checkpoint 6


## Principios en la construcción de arquitecturas deproducto de datos 

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

## Recursos adicionales

#### Libros
1. [Data Pipelines Pocket Reference](https://www.oreilly.com/library/view/data-pipelines-pocket/9781492087823/)
2. [Machine Learning Design Patterns](https://www.oreilly.com/library/view/machine-learning-design/9781098115777/)
3. [SQL Pocket Guide](https://www.oreilly.com/library/view/sql-pocket-guide/9781492090397/)
4. [Data Science at the Command Line](https://datascienceatthecommandline.com/2e/index.html)
5. [Data Science on the Google Cloud Platform](https://www.oreilly.com/library/view/data-science-on/9781491974551/)
6. [Practical AI on the Google Cloud Platform](https://www.oreilly.com/library/view/practical-ai-on/9781492075806/)
7. [Google BigQuery: The Definitive Guide](https://www.oreilly.com/library/view/google-bigquery-the/9781492044451/)

#### Web
1. https://technically.dev
2. https://www.kaggle.com/learn
3. https://missing.csail.mit.edu/


## Instructores
La clase será impartida por **[Adrian Sanchez-Castro](https://www.linkedin.com/in/sanchez-castro/)** científico de datos de Walmart y **[Jake Klein](https://www.linkedin.com/in/jake-klein-180498b9/)** ingeniero de datos de Walmart. 

## Organizaciones invitadas a dar *Perspectivas* sobre productos de datos
- Google
- Twitter
- New York Times
- Amazon
- Walmart
- Nike

## Revisión y retroalimentación
- Memo González - Ingeniero de Aprendizaje de Maquina - Google
- Anders Christiansen - VP de Ciencia de Datos - Kavak
- Alejandra Garay - Ingeniera de Datos Lead - Cinépolis
- Gustavo Salaiz - Director de Datos - Albo
- Gerardo Mathus - Director de Ingeniería - Nextia
- Esteban Wasson - Manager de Producto - CoverWallet - Profesor Data Visualization and Analytics - Yeshiva University
- Santiago Battezzati - Científico de datos - OPI
