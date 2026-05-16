# Contratos de Interfaz y Guía de Pruebas: Animales (Unidad 3)

Este documento detalla todas las estructuras para interactuar con la API de Animales, incluyendo REST y todos los casos de uso de GraphQL.

---

## 1. REST API (Tradicional)

### Registrar Animal (POST)
**Endpoint**: `POST /animals/`
```json
{
  "name": "Boby",
  "species": "Labrador",
  "category": "domestic",
  "age": 5,
  "owner_name": "Ana Martinez"
}
```

---

## 2. GraphQL API (Avanzado)

**Endpoint**: `POST /animals/graphql` o `POST /animals/graphql-test`

### A. Consultas (Queries)

#### 1. Listado General (Campos Declarativos)
Obtén solo lo que necesitas.
```json
{
  "query": "{ animals { name category species } }"
}
```

#### 2. Obtener por ID
```json
{
  "query": "{ animal(id: \"Z_COLLECTION_ID\") { name age ownerName } }"
}
```

#### 3. Filtrar por Categoría (Wild/Domestic/Other)
```json
{
  "query": "{ animals(category: \"wild\") { name species } }"
}
```

#### 4. Búsqueda por Nombre (Contiene texto)
```json
{
  "query": "{ searchAnimalsByName(nameQuery: \"Simba\") { id name category } }"
}
```

#### 5. Uso de Variables (Nivel Experto)
Ideal para aplicaciones reales.
```json
{
  "query": "query GetAnimals($c: String!) { animals(category: $c) { name species } }",
  "variables": { "c": "domestic" }
}
```

### B. Mutaciones (Registro de Datos)

#### 1. Crear Animal Doméstico (Requiere Dueño)
```json
{
  "query": "mutation { createAnimal(name: \"Luna\", species: \"Gato\", category: \"domestic\", ownerName: \"Maria Garcia\") { id name ownerName } }"
}
```

#### 2. Crear Animal Salvaje (Sin Dueño)
```json
{
  "query": "mutation { createAnimal(name: \"Shere Khan\", species: \"Tigre\", category: \"wild\", age: 7) { id name species } }"
}
```

### C. Manejo de Errores y Reglas de Negocio

#### Caso: Registro Doméstico sin Dueño (Error 400 esperado)
GraphQL devolverá un error descriptivo si se viola la regla de negocio.
```json
{
  "query": "mutation { createAnimal(name: \"Falla\", species: \"Perro\", category: \"domestic\") { id } }"
}
```

---

## 3. Guía de Ejecución de Pruebas

1. **Vía Swagger**: Usa el endpoint `/animals/graphql-test` para pegar estos JSONs directamente.
2. **Vía GraphiQL**: Usa la interfaz en `/animals/graphql` para autocompletado.
3. **Vía Terminal**:
   ```bash
   python3 test_animals_graphql.py
   ```

---
*Documento generado para soporte de la Actividad Formativa - Arquitectura de Aplicaciones Web.*
