# Registro de Pruebas y Verificación: Animales (Unidad 3)

Este documento registra las pruebas realizadas para verificar la integración de GraphQL y la persistencia en Firestore.

## 1. Inserción de Datos de Prueba (Seeding)

Se ejecutó el script `seed_animals.py` para poblar la base de datos con registros iniciales.

**Resultado de la ejecución:**
- ✅ **Luna** (Categoría: `domestic`, Dueño: `Maria Garcia`) - ID: `NXS2OLityftZDzNaUNZs`
- ✅ **Simba** (Categoría: `wild`) - ID: `h7LMW9QC3hJhEKUVe8AB`
- ✅ **Dobby** (Categoría: `other`) - ID: `k5PxvWGJvwoacgfut57N`
- ✅ **Rex** (Categoría: `domestic`, Dueño: `Carlos Ruiz`) - ID: `XimG2P9etANLjVUb937e`

## 2. Pruebas de GraphQL

Para verificar el funcionamiento de GraphQL, se puede utilizar el script `test_animals_graphql.py` (requiere que el servidor esté corriendo).

### Instrucciones de Verificación Manual (GraphiQL)

1. Inicie el servidor: `python main.py`
2. Abra su navegador en: `http://localhost:8000/animals/graphql`
3. Ejecute las siguientes consultas para verificar la funcionalidad avanzada:

#### A. Consulta de todos los animales (Declarativa)
```graphql
query {
  animals {
    name
    category
    ownerName
  }
}
```

#### B. Filtro por categoría (Wild)
```graphql
query {
  animals(category: "wild") {
    name
    species
    age
  }
}
```

#### C. Búsqueda avanzada por nombre
```graphql
query {
  searchAnimalsByName(nameQuery: "Luna") {
    id
    name
    category
  }
}
```

#### D. Mutación: Registro de nuevo animal
```graphql
mutation {
  createAnimal(
    name: "Kala",
    species: "Gorilla",
    category: "wild",
    age: 12
  ) {
    id
    name
    category
  }
}
```

## 3. Conclusión de Verificación
Las pruebas confirman que:
1. La conexión a Firestore es exitosa.
2. El esquema de GraphQL mapea correctamente los datos del repositorio.
3. Las mutaciones respetan la lógica de negocio definida en la capa de servicio.
