# Arquitectura de Producto de Datos
## Plan Magisterial

### Resultados de aprendizaje de la asignatura
- Traduce problemas de negocio en un plan arquitectónico de producto de datos enfocandose en primer lugar en la alineación del problema de negocio a resolver con la misión y en segundo lugar la solución tecnológica-
- Diseña planes arquitectonicos de datos a partir de servicios e infrastructuras modernas de datos.
- Utiliza servicios de datos en la nube relacionados a almacenaje, procesamiento de grandes volúmenes de datos y modelado de aprendizaje de máquina
- Traduce planes arquitectónicos en un diseño de grafo acíclico dirigido para ser ejecutado por un orqueestador
- Implementa producto de datos funcioanales en la nube para aplicaciones de analiítica descriptiva y predictiva. 

---
## Competencias por tópico

#### 1. ¿Por qué construir productos de datos?

- El alumno conoce el etos de una organización/startup.
- El alumno aproxima el diseño de producto de datos con base en la mision y problema de negocio.
- El alumno conoce el rol de un producto de datos en una organización.

    - [The Learn Startup, Chapter 1: Start, Chapter 2: Define](https://www.getstoryshots.com/books/the-lean-startup-summary/#PART_1_Vision)
    - [Forget about building an AI-first business. Start with a mission](https://www.technologyreview.com/2021/03/26/1021258/ai-pioneer-andrew-ng-machine-learning-business/)
    - [When Data Creates Competitive Advantage](https://hbr.org/2020/01/when-data-creates-competitive-advantage)
    - [Don't Let Metrics (Data) Underimne your Business (version 1) ](https://sloanreview.mit.edu/article/dont-let-metric-critics-undermine-your-business/)
    - [Don't Let Metrics (Data) Underimne your Business (version 2)](https://hbr.org/2019/09/dont-let-metrics-undermine-your-business)
    - [https://hbr.org/2020/01/competing-in-the-age-of-ai](Competing in the Age of AI)
    - [*Emerging Architectures for Modern Data Infrastructure*](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/)


#### 2. Arquitectura de Producto de datos
- El alumno es un pensador crítico qué es capaz de evaluar el triage del problema y el impacto de una solución de producto de datos.
- El alumno conoce el proceso de diseñar un producto de datos y evaluar el trade-off de implementación-deuda técnica de una organización
- El alumno es capaz de plantear el alcance, amplitud y extensión de un producto de datos.
- El alumno conoce los riesgos e implicaciones del impacto de un producto exitoso/fallido.



#### 3. Infraestructura de datos en la nube: máquinas virtuales, almacén de objetos, y almacén de datos.
- El alumno conoce las distintas plataformas de servicios de infrastructura de datos en la nube. 
- El alumno es capaz de interactuar con los servicios básicos de almacenaje y procesamiento en la nube. 
- El alumno explica y demuestra el entendimiento de abstracciones de infrastructura de datos como "serverless", "Managed SaaS"
- El alumno es conoce los retos para estructurar un proyecto en la nube tanto tecnicos como no tecnicos. 


#### 4. Máquinas Virtuales y aceleradores GPU/TPU
- El alumno conoce el uso de máquinas virtuales en la nube para ciencia de datos
- El alumno es capaz de crear máquinas virtuales con aceleradores para trabajos de modelado de aprendizaje de máquina en la nube.
- El alumno es capaz de comunicarse vía remota a una máquina virtual y ejecutar scripts de modelados de aprendizaje de máquina autoescalables. 


#### 5. Fuentes de datos: API como caso de uso
- El alumno tiene un conocimiento general del uso de las APIs dentro del ecosistema de ciencia de datos.
- El alumno es capaz de investigar y conocer el uso general de una API.
- El alumno es capaz de establecer una comunicación constante en la nuba para la recolección de datos a través de una API.
- El alumno es capaz de ingestar datos y cargar datos en la nube


#### 6. Almacenamiento (Data Lake): Google Cloud Storage
- El alumno es capaz de crear cubetas de almacenaje en la nube.
- El alumno entiende las políticas de permisos para compartir datos en la nube. 
- El alumno es capaz de cargar distintos tipos de archivos. 
- El alumno conoce las alternativas de almacenamiento. 


#### 7. ETL vs ELT y el nuevo paradigma de MLOps
- El alumno puede dicernir entre la aplicación de un ETL y un ELT. 
- El alumno reconoce las distintas aplicaciones de extracción, transformación y carga para distintos problemas de negocio.
- El alumno conoce las tecnologías disponibles para hacer una ingesta de grandes volumnes de datos. 
- El alumno es capaz de diseñar un sistema que involucra la extracción, transformación y carga con servicios de infrastructura de nube. 


#### 8. Orquestador: Airflow vs Kubeflow vs Cloud Pipelines (AI Pipelines)
- El alumno tiene un conocimiento general de los distintas tecnologias y aproximaciones de orquestación para el tratamiento de datos 
- El alumno es capaz de poner en marcha Airflow como orquestador auto-manejado en la nube
- El alumno diseña archivos de grafos acíclicos dirigidos a través de operadores.
- El alumno ejecuta archivos de grafos acícicos dirigidos para el tratamiento de datos


---

### Analítica de Datos de Analítica Descriptiva
#### 9. Ingeniería de datos para grandes volúmenes de datos: Apache Beam vs Spark vs Bigquery
- El alumno conoce distintos motores de procesamiento de datos utilizados para grandes volumnes de datos
- El almuno es capaz de ejecutar procesos de transformaciones para grandes volumnes de datos. 


#### 10. Almacén de Datos (Data Warehouse): BigQuery
- El alumno conoce el uso de caso de un Almacén de Datos
- El alumno conoce las capacidades generales de un almacén de datos moderno
- El alumno es capaz de ejecutar queries de lectura y de transformación en bases de datos relacionales
- El alumno es capaz de ejecutar queries de modelado utilizando BigQuery ML


#### 11. Inteligencia de Datos: Looker
- El alumno conoce el uso de caso de inteligencia de negocio basado en analítica descriptiva
- El alumno es capaz de poner en marcha una instancia de Looker conectada a un almacén de datos 
- El alumno desarrolla vistas, exploradores y dashboards utilizando Looker

---

### Arquitectura de Datos de Analítica Predictiva
#### 12. MLOps
- El alumno conoce el paradigma de MLOps y las nuevas herramientas de lineaje de modelos
- El alumno es capaz de aplicar conoceptos de registro de modelo, almacenaje de features

#### 13. Ingeniería de Aprendizaje de Máquina: Producción
- El alumno conoce las vías de producción-prediccion 
- El alumno es capaz de generar predicciones en tiempo real.

#### 14. Unit testing y Monitorización
- El alumno es capaz de poner en marcha un API de consumo en la nube.
- El alumno es capaz de poner hacer unit testing para comprobar el funcionamiento de un modelo de aprendizaje de máquina.
- El alumno es capaz de tener información en tiempo real del funcionamiento del modelo en producción.
- El alumno es capaz de identificar "model drifts" con base en el monitoreo de los sistemas en producción. 
