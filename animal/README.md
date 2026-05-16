# Documentación de la Implementación: Animales (Unidad 3)

Esta carpeta contiene el detalle de la implementación del feature `animals`, cumpliendo con los requisitos de la Unidad 3, incluyendo la integración de GraphQL y persistencia en Firestore.

## Arquitectura

La implementación sigue una arquitectura basada en características (feature-based):
- **Schemas (`schemas.py`)**: Modelos Pydantic para validación de datos.
- **Repository (`repository.py`)**: Capa de persistencia utilizando Google Firestore.
- **Service (`service.py`)**: Lógica de negocio (validaciones de categorías y dueños).
- **Router (`router.py`)**: Definición de endpoints REST y montura de GraphQL.
- **GraphQL Schema (`graphql_schema.py`)**: Definición de tipos y consultas avanzadas con Strawberry GraphQL.

## Reglas de Negocio

1. **Categorías**: Los animales pueden ser `domestic`, `wild` o `other`.
2. **Registro de Dueño**: Si un animal es de categoría `domestic`, el campo `owner_name` es **obligatorio**. Si no se proporciona, la API retornará un error 400.

## Endpoints REST (Prefijo: `/animals`)

- `GET /animals/`: Listar todos los animales (permite filtrar por `category`).
- `GET /animals/{id}`: Obtener un animal por su ID.
- `POST /animals/`: Registrar un nuevo animal.
- `PUT /animals/{id}`: Actualizar datos de un animal.
- `DELETE /animals/{id}`: Eliminar un registro.

## Consultas GraphQL (URL: `/animals/graphql`)

La API soporta consultas avanzadas a través de GraphQL. Puede acceder a la interfaz GraphiQL en la URL indicada.

### Ejemplos de Consultas

#### Listar todos los animales con campos específicos
```graphql
query {
  animals {
    id
    name
    category
    ownerName
  }
}
```

#### Filtrar por categoría
```graphql
query {
  animals(category: "wild") {
    name
    species
  }
}
```

#### Búsqueda por nombre (Consulta Avanzada)
```graphql
query {
  searchAnimalsByName(nameQuery: "Fido") {
    id
    name
    category
    ownerName
  }
}
```

#### Registrar un nuevo animal (Mutación)
```graphql
mutation {
  createAnimal(
    name: "Rex",
    species: "Dinosaur",
    category: "wild",
    age: 65000000
  ) {
    id
    name
  }
}
```

## Instalación y Configuración
   
1. **Dependencias**:
   ```bash
   pip install "strawberry-graphql[fastapi]" httpx python-dotenv
   ```
2. **Base de Datos**: Requiere `serviceAccountKey.json` en la raíz.
3. **Ejecución**: `python main.py`

## Pruebas y Verificación

Se han incluido herramientas para automatizar la verificación de la implementación:

1. **Poblar Base de Datos**: Ejecute `python seed_animals.py` para insertar registros de prueba iniciales en Firestore.
2. **Pruebas GraphQL**: Ejecute `python test_animals_graphql.py` para verificar consultas y mutaciones (asegúrese de que el servidor `main.py` esté activo).
3. **Registro de Pruebas**: Consulte el archivo [TEST_LOGS.md](file:///Users/deals/Documents/GIT/poli-u2-rest-fast-api/animal/TEST_LOGS.md) para ver los resultados de las pruebas de integración.

---
Implementación realizada para la Actividad Formativa - Unidad 3.
