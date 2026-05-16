# Guion Técnico: Integración de GraphQL en FastAPI (Unidad 3)

Este guion está diseñado para un video de **3 a 5 minutos**, cumpliendo con los criterios de "Sobresaliente" de la rúbrica.

---

## ⏱️ Estructura del Tiempo

| Sección | Duración | Objetivo |
| :--- | :--- | :--- |
| **1. Introducción** | 0:00 - 0:45 | Presentar el stack tecnológico (FastAPI + Strawberry). |
| **2. Arquitectura** | 0:45 - 1:30 | Mostrar la organización de carpetas y capas. |
| **3. Instalación** | 1:30 - 2:15 | Mostrar los comandos y la configuración de Firebase. |
| **4. Demo en Vivo** | 2:15 - 4:15 | Consultas avanzadas, mutaciones y validaciones. |
| **5. Conclusión** | 4:15 - 5:00 | Justificación técnica y cierre. |

---

## 🎙️ Script Paso a Paso

### 1. Introducción (0:00 - 0:45)
*   **Acción**: Muestra el archivo `main.py` y la raíz del proyecto.
*   **Diálogo**: *"Buen día. En esta actividad demostraré la integración de la librería GraphQL en un framework de alto rendimiento. He seleccionado **FastAPI** por su soporte nativo para tipos de Python y **Strawberry GraphQL** como la librería de integración, debido a su enfoque 'code-first' y compatibilidad con Pydantic."*

### 2. Arquitectura de la Solución (0:45 - 1:30)
*   **Acción**: Navega por la carpeta `app/features/animals`.
*   **Diálogo**: *"El proyecto sigue una arquitectura basada en características o 'Feature-based'. Dentro del módulo 'animals', hemos separado las preocupaciones en: `schemas` para validación, `repository` para el acceso a Firestore de Firebase, `service` para la lógica de negocio y `graphql_schema` donde definimos nuestros tipos y consultas de GraphQL."*

### 3. Proceso de Instalación y Configuración (1:30 - 2:15)
*   **Acción**: Abre una terminal o muestra el archivo `requirements.txt`.
*   **Diálogo**: *"Para la instalación, utilizamos el gestor de paquetes `pip` ejecutando: `pip install strawberry-graphql[fastapi]`. La configuración se realiza inyectando el esquema de Strawberry dentro de los routers de FastAPI, permitiendo que convivan endpoints REST y GraphQL en la misma aplicación bajo el prefijo `/animals`."*

### 4. Demostración Práctica (2:15 - 4:15)
*   **Acción 1**: Abre [http://localhost:8000/docs](http://localhost:8000/docs) y muestra el endpoint `/animals/graphql-test`.
*   **Diálogo**: *"Gracias a la integración con Swagger, podemos probar contratos de GraphQL directamente. Ejecutaré una consulta avanzada que busca animales por nombre y categoría."* (Ejecuta una consulta).
*   **Acción 2**: Abre [http://localhost:8000/animals/graphql](http://localhost:8000/animals/graphql) (GraphiQL).
*   **Diálogo**: *"Ahora, desde la interfaz de GraphiQL, realizaremos una **Mutación**. Vamos a registrar un animal doméstico. Noten que si omito el nombre del dueño, el sistema arroja un error de validación, cumpliendo con nuestra regla de negocio."* (Muestra el error y luego corrígelo agregando `ownerName`).

### 5. Conclusión (4:15 - 5:00)
*   **Acción**: Muestra la carpeta `animal/` con la documentación generada.
*   **Diálogo**: *"En conclusión, la integración de GraphQL aporta una flexibilidad enorme para que los clientes consuman solo los datos necesarios, optimizando el ancho de banda y mejorando la experiencia de desarrollo. Toda la implementación está respaldada por Firebase Firestore para una persistencia escalable. Gracias por su atención."*

---

## 💡 Tips para el Éxito
1.  **Zoom**: Aumenta el tamaño de la fuente en VS Code y el Navegador (Ctrl/Cmd + '+').
2.  **Preparación**: Ten el servidor corriendo (`python3 main.py`) antes de empezar a grabar.
3.  **Copiar/Pegar**: Usa el archivo `CONTRATOS_PRUEBAS.md` para copiar las consultas rápidamente y evitar errores de escritura durante el video.
