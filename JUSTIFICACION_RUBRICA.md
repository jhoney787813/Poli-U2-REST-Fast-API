# Justificación de la Rúbrica - Poli U2 REST Fast API

Este documento detalla cómo el proyecto cumple con cada uno de los criterios de evaluación de la Unidad 2, aportando fragmentos de código como evidencia técnica.

---

## 1. Arquitectura de la Solución (Feature-based)
**Criterio:** Organización del código en una estructura modular y escalable.

**Justificación:** El proyecto utiliza una arquitectura basada en características (**Feature-based**), donde cada entidad del dominio (como `products`) reside en su propio paquete con todas sus capas. Esto separa las preocupaciones y facilita el mantenimiento.

**Ejemplo de código (Estructura de archivos):**
```text
app/
├── core/               # Lógica global (DB, Config)
└── features/
    └── products/       # Módulo autónomo de productos
        ├── router.py   # Controladores REST
        ├── service.py  # Lógica de Negocio
        ├── repository.py # Acceso a Datos (Firestore)
        └── schemas.py  # Modelos/Validación (Pydantic)
```

---

## 2. Implementación de CRUD Completo
**Criterio:** Desarrollo de las operaciones básicas (Create, Read, Update, Delete).

**Justificación:** Se implementaron los 5 métodos estándar de una API RESTful, utilizando los verbos HTTP correctos y manejando las respuestas adecuadamente.

**Ejemplo de código (`app/features/products/router.py`):**
```python
@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    return service.create_product(product)

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: str):
    # ... lógica de obtención ...
```

---

## 3. Integración con Base de Datos (Firebase Firestore)
**Criterio:** Uso de un servicio de persistencia externo y un ODM/SDK.

**Justificación:** Se integra **Google Cloud Firestore** mediante el SDK oficial `firebase-admin`. No se realizaron "queries" manuales en crudo, cumpliendo con el uso de un ODM.

**Ejemplo de código (`app/features/products/repository.py`):**
```python
def __init__(self):
    self.db = get_db()
    self.collection_name = "productos"

def create(self, product: ProductCreate) -> dict:
    doc_ref = self.db.collection(self.collection_name).document()
    product_data = product.model_dump()
    doc_ref.set(product_data)  # Persistencia en Firebase
    return {**product_data, "id": doc_ref.id}
```

---

## 4. Principios SOLID, GRASP y YAGNI
**Criterio:** Aplicación de buenas prácticas de diseño de software.

**Justificación:**
- **Single Responsibility (SOLID):** El `Repository` solo toca la BD, el `Service` solo maneja lógica y el `Router` solo peticiones HTTP.
- **Dependency Inversion (SOLID):** El Router recibe una instancia del Servicio, y el Servicio recibe el Repositorio inyectado.
- **Expert (GRASP):** El Repository es el experto en la colección "productos".
- **YAGNI:** La base de código es limpia y no tiene funcionalidades extra innecesarias (como auth compleja) para cumplir con la rúbrica de forma eficiente.

**Ejemplo de código (`app/features/products/service.py`):**
```python
class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository # Inyección de dependencias
```

---

## 5. Modelo de Madurez de Richardson (Nivel 2)
**Criterio:** Implementación correcta de estándares REST.

**Justificación:** El proyecto alcanza el **Nivel 2** del modelo de Richardson al cumplir con:
1.  **Recursos:** URL únicas para identificar entidades (`/products/{id}`).
2.  **Verbos HTTP:** Uso de `GET`, `POST`, `PUT`, y `DELETE` para operaciones semánticas.

**Evidencia (Códigos de Estado Semánticos):**
```python
# app/features/products/router.py
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: str):
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, ...) # Error semántico
```

---

## 6. Pruebas y Validación
**Criterio:** Evidencia de que el sistema funciona según lo esperado.

**Justificación:** Se incluye un script de pruebas automatizadas (`test_api.py`) y un script de carga de datos (`seed_test_data.py`) que demuestran la conectividad y el éxito de las operaciones.

**Ejemplo de código (`test_api.py`):**
```python
def test_create_product():
    response = requests.post(f"{BASE_URL}/products/", json={
        "nombre": "Test", "descripcion": "Desc", "precio": 10.0
    })
    assert response.status_code == 201
```

---

## 7. Manejo de Errores
**Criterio:** Controlar fallos del sistema y devolver respuestas claras.

**Justificación:** Se gestionan excepciones para evitar que el servidor falle (500) y en su lugar devuelva errores informativos al cliente.

**Ejemplo de código:**
```python
if not product:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID {product_id} not found"
    )
```
