# Informe de Entrega: Integración de API GraphQL (Unidad 3)

**Asignatura**: Arquitectura de Aplicaciones Web  
**Actividad**: Unidad 3 - Actividad Formativa  
**Framework**: FastAPI  
**Librería**: Strawberry GraphQL  
**Persistencia**: Google Firebase (Firestore)

---

## 1. Introducción y Resumen de la Actividad

La presente actividad consistió en la identificación, instalación e integración de la tecnología **GraphQL** dentro de un entorno de desarrollo moderno. Se seleccionó el framework **FastAPI** (Python) por su eficiencia y tipado estático, integrando la librería **Strawberry GraphQL**.

El objetivo principal fue construir una arquitectura robusta que permitiera gestionar un registro de animales clasificados en categorías (domésticos, salvajes y otros), implementando reglas de negocio específicas (como la obligatoriedad de un dueño para animales domésticos) y permitiendo consultas declarativas avanzadas.

## 2. Importancia de los Conceptos Aplicados

El dominio de GraphQL es fundamental en la arquitectura de software contemporánea por las siguientes razones:
*   **Eficiencia en la Transferencia de Datos**: A diferencia de REST, GraphQL permite al cliente solicitar exactamente los campos que necesita, eliminando el *over-fetching* y el *under-fetching*.
*   **Tipado Fuerte e Introspección**: Proporciona un contrato claro entre el cliente y el servidor, facilitando la validación automática y el autocompletado en herramientas de desarrollo.
*   **Agregación de Datos**: Permite consultar múltiples recursos en una sola petición, reduciendo la latencia de red.

## 3. Memoria de Implementación (Retos y Soluciones)

La realización de esta actividad implicó un proceso sistemático para cumplir con la rúbrica de evaluación:

1.  **Instalación y Entorno**: Se configuró un entorno virtual de Python, instalando `strawberry-graphql[fastapi]`. El reto principal fue asegurar la compatibilidad con los modelos de Pydantic existentes para mantener una arquitectura coherente.
2.  **Integración con Firestore**: Se diseñó una capa de repositorio que interactúa directamente con la base de datos de Firebase, permitiendo que las consultas de GraphQL fueran dinámicas y persistentes.
3.  **Lógica de Negocio**: Se implementó una capa de servicio que intercepta las peticiones de creación de animales. Si un animal es marcado como `domestic`, el sistema valida la presencia de un `owner_name`, arrojando un error 400 controlado en caso de ausencia.
4.  **Flexibilidad de Consulta**: Se añadieron funcionalidades avanzadas como la búsqueda por nombre y el filtrado por categoría, demostrando el poder de las consultas personalizadas de GraphQL.

## 4. Cumplimiento de la Rúbrica

Para asegurar la calificación de **Sobresaliente**, se realizaron las siguientes acciones:
*   **Configuración del Entorno**: Todo el proceso de instalación fue documentado en el archivo `README.md` y verificado mediante scripts de prueba.
*   **Estructura Técnica**: Se utilizó una arquitectura **Feature-based**, separando Schemas, Repositories, Services y Routers.
*   **Video Explicativo**: Se generó un guion técnico (`GUION_VIDEO_U3.md`) que guía la presentación paso a paso, asegurando que se cubran todos los puntos exigidos en el tiempo estipulado (3-5 minutos).

## 5. Conclusiones

La actividad ha permitido comprender que GraphQL no es solo una alternativa a REST, sino un cambio de paradigma en la forma en que los sistemas distribuidos se comunican. La integración exitosa con FastAPI y Firebase demuestra la versatilidad de estas herramientas para construir aplicaciones escalables y fáciles de mantener.

---

## 6. Referencias Bibliográficas (Normas APA)

*   FastAPI. (2024). *FastAPI Framework documentation*. https://fastapi.tiangolo.com/
*   GraphQL Foundation. (2024). *GraphQL: A query language for APIs*. https://graphql.org/
*   Strawberry GraphQL. (2024). *Pythonic GraphQL with Strawberry*. https://strawberry.rocks/docs
*   Google Cloud. (2024). *Cloud Firestore Documentation*. https://firebase.google.com/docs/firestore
