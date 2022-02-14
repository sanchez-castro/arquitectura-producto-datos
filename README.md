# Temario

# Arquitectura de Producto de Datos

**Clase:** 8:00-9:30 AM (Central Time), **Martes** y **Viernes**

**Campus:** Rio Hondo

**Formato:** Online ([Zoom](https://itam.zoom.us/j/97791165619?pwd=a09lc1AzUkZienlIdlJiUVZHYmt0UT09))

**Horarios de oficina virtual: 
Adrian:** [https://calendly.com/adrian-sanchez-castro/30min](https://calendly.com/adrian-sanchez-castro/30min)
**Jake:** [https://calendly.com/jake-d-klein/15min](https://calendly.com/jake-d-klein/15min) 

**(Pre)requisitos:** Intro a Aprendizaje de Máquina + SQL, Bash/Shell, Python,

**Programa(s):** Maestría Ciencia de Datos, Maestría Computación, Licenciatura de Ciencia de Datos (tercer año), Licenciatura de Computación (tercer año)

**Profesor: [Adrian Sanchez-Castro](https://www.notion.so/Adrian-Sanchez-Castro-19398ce833df41e7831a51ff6331e56a)**

**Email:** jorge.sanchez.castro@itam.edu.mx

**Profesor Asociado: [Jake Klein](https://www.notion.so/Jake-Klein-6362f738b2e04fc9acee9fa0f83b9998)** 

**Email:** jakeklein94@gmail.com

---

# Descripción del curso

Esta clase tiene como objetivo brindar una introducción a la ingeniería de datos e ingeniería de aprendizaje de máquina para científicos de datos tomando en cuenta las últimas prácticas y tecnologías mayormente adoptadas y validadas por las empresas tecnológicas más maduras del mundo.

# **Aproximación de la materia**

---

El objetivo es **(1)** dar una perspectiva holística del [ecosistema de infraestructura de datos actualizada](https://mattturck.com/data2021/), **(2)** contextualizar el trabajo del científico de datos dentro de una organización y **(3)** desarrollar las habilidades necesarias para diseñar e implementar una infraestructura de datos escalable para resolver un problema de negocio con base en los pilares anteriormente mencionados.

### **1) Perspectiva holística del ecosistema de infrastructura de datos**

Se estudiará el ciclo de ingeniería de datos a través del análisis "Arquitecturas Modernas de Infraestructura de Datos" planteado por Matt Bornstein, Martin Casado, y Jennifer Li en su artículo *[Emerging Architectures for Modern Data Infrastructure](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/)* enfatizando el nuevo paradigma de cómputo en la nube sin servidores (*serverless computing*) y el surgimiento de Servicios de Software (SaaS) auto-gestionables (managed services) especializados en sistemas de análisis de datos y de operación de aprendizaje de máquina.

### 2**) Trade-off entre agilidad de producción y deuda técnica**

Se diseñará y desarrollará una arquitectura de producto de datos bajo el análisis del *trade-off* entre la agilidad de producción y la deuda técnica que suele incurrirse por la falta diseños robustos para la manutención y escalamiento de arquitecturas de productos de datos. Inspirado en el debate presentado en el artículo *[Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)* por investigadores del equipo de Google .

### 3**) El rol del científico de datos dentro de una organización**

Se contextualizará el trabajo del científico de datos dentro de una organización, donde la toma decisiones, basada en evidencia, es la tarea principal de un equipo (de datos) cuyos roles se han especializado en los últimos años para tener responsabilidades y habilidades más enfocadas y específicas dentro del ciclo de ingeniería de datos.

---

# **Formato de enseñanza**

**Horario:** Martes y Viernes, 8.00 AM - 9.30 AM. 

Las clase tendrán un enfoque de ***learning by doing***:

- La clase será impartida durante dos sesiones de 1.5 horas por clase con un break de 5 minutos.
- La primera sesión estará enfocada a teoría, discusión en clase y, dependiendo del tema, se trabajarán algunos ejercicios básicos de programación.
- La segunda sesión estará enfocada a aplicar los conceptos aprendidos en la sesión anterior en un ambiente real en la nube. Se trabajará en un ejemplo *end-to-end* durante la clase para que los alumnos puedan replicarlo en su proyecto final (que podrá ir completando en el transcurso del semestre.

## **Formato**

La clase tendrá como objetivo la implementación de un proyecto de "principio a fin" de una arquitectura de producto de datos en la nube a través de ***checkpoints*** de avance durante el transcurso del semestre.

Se formarán **equipos de 4 personas** que se organizarán durante el primer día de clase tomando en cuenta la experiencia y la educación previa de los estudiantes. La idea es tener grupos mixtos de disciplinas y experiencias para reflejar y emular la manera en como un científico de datos trabaja en el mundo real laboral.

## **Checkpoints**

Habrán 6 ***checkpoints*** que trendrán que ser reflejados en un repositorio de github.

1. Definición de projecto en la nube y ambiente de repositorio
2. Manual ETL/ELT
3. Modelo entrenado en la nube
4. Puesta en marcha de Airflow
5. Automatización del ETL/ELT
6. Automatización de modelo de ML en la nube. 

## 🏆 Calificación

- Cada checkpoint contribuirá a un punto de la calificación total. Entre ellos podrán sumar un total de 3 de los diez puntos de calificación.
- Los 7 puntos restantes serán ponderados a través de una presentación final y un entregable
    - *Cada [checkpoint](https://www.notion.so/Checkpoints-b9f131a629d149359e499b1f085215e4) y la presentación final serán calculados por rúbricas disponibles a los estudiantes.

# 😢 Plagio

<aside>
⚠️ Presentar el trabajo de otros como suyo es una seria ofensa académica. 
Por favor documenten todo su trabajo. 
Si utilizan código o recursos de otras fuentes/autores favor de compartirlas apropiadamente.

</aside>

---

# **Temario**

1. Arquitectura de Producto de Datos: 
Arquitecturas Emergentes para la Infraestructura de Datos Moderna
2. Nube e Infrastructura de datos en la nube
    1. almacén de objetos
    2. máquinas virtuales
    3. almacén de datos 
3. APIs
    1. APIs para accesar datos
    2. APIs para accesar a servicios
4. Almacén de Objetos (Data Lake)
5. Bases de Datos y ETL
6. Almacén de datos y ELT
    1. Almacén de Datos (Data Warehouse): BigQuery
    2. Ingeniería de datos para grandes volúmenes de datos: Spark vs BigQuery
7. Sistemas de Aprendizaje de Maquina (en la nube)
    - AutmoML como baseline
    - BigQuery ML
    - Notebooks vs Py-Script: Sagemaker vs Vertex AI
    - Empaquetamiento de modelo (Docker vs "Python-package")
    - Máquinas Virtuales con aceleradores GPU/TPU
8. Orquestación de Aprendizaje de Maquina: MLOps (CI/CD)
    1. Airflow vs Kubeflow vs Cloud Pipelines (AI Pipelines)
9. Business Analytics
    1. Looker
10. Analítica de Ingeniería de Aprendizaje de Máquina: 
    1. Producción
    2. Monitorización
11.  Data Strategy

# 🗓 Calendario

[Calendario de clases](https://www.notion.so/5056e557fba245cbbbf45f1373d6bd33)

## **Principios en la construcción de arquitecturas deproducto de datos**

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

---

# Class culture

- No question is dumb
- No condescending attitude is going to be tolerated
- Please respect/praise other’s work
- Please share your thoughts/feedback
- Please ask for help and help each other
- It’s all about attitude; if you don’t make mistakes, you are not trying hard enough

---

# 📚 Recursos

[Recursos](https://www.notion.so/7f02d9c71ac14c109e43a650c9b76be4)

---

---

## **Organizaciones invitadas a dar *Perspectivas* sobre productos de datos**

- Google
- Twitter
- New York Times
- Amazon
- Walmart
- Nike

---

# 🙏🏻 **Revisión y retroalimentación**

- Memo González - Ingeniero de Aprendizaje de Maquina - Google
- Anders Christiansen - VP de Ciencia de Datos - Kavak
- Alejandra Garay - Ingeniera de Datos Lead - Cinépolis
- Gustavo Salaiz - Director de Datos - Albo
- Gerardo Mathus - Director de Ingeniería - Nextia
- Esteban Wasson - Manager de Producto - CoverWallet - Profesor Data Visualization and Analytics - Yeshiva University
- Santiago Battezzati - Científico de datos - OPI