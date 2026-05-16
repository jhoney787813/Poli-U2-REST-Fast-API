from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from strawberry.fastapi import GraphQLRouter
from .schemas import Animal, AnimalCreate, AnimalUpdate, GraphQLQuery
from .repository import AnimalRepository
from .service import AnimalService
from .graphql_schema import schema

router = APIRouter(
    prefix="/animals",
    tags=["animals con GraphQLs"]
)

# Dependency injection
repository = AnimalRepository()
service = AnimalService(repository)

@router.post("/graphql-test", tags=["animals con GraphQLs"])
async def test_graphql_endpoint(request: GraphQLQuery):
    """
    Endpoint optimizado para probar GraphQL directamente desde Swagger.
    Copia y pega una consulta en el campo 'query'.
    """
    result = await schema.execute(request.query, variable_values=request.variables)
    if result.errors:
        return {"errors": [str(e) for e in result.errors]}
    return {"data": result.data}

# REST Endpoints
@router.get("/", response_model=List[Animal], status_code=status.HTTP_200_OK)
def list_animals(category: Optional[str] = None):
    """List all animals, optionally filtered by category."""
    return service.get_all_animals(category)

@router.get("/{animal_id}", response_model=Animal, status_code=status.HTTP_200_OK)
def get_animal(animal_id: str):
    """Get an animal by ID."""
    animal = service.get_animal(animal_id)
    if not animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Animal with ID {animal_id} not found"
        )
    return animal

@router.post("/", response_model=Animal, status_code=status.HTTP_201_CREATED)
def create_animal(animal: AnimalCreate):
    """Create a new animal."""
    return service.create_animal(animal)

@router.put("/{animal_id}", response_model=Animal, status_code=status.HTTP_200_OK)
def update_animal(animal_id: str, animal: AnimalUpdate):
    """Update an existing animal."""
    updated_animal = service.update_animal(animal_id, animal)
    if not updated_animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Animal with ID {animal_id} not found"
        )
    return updated_animal

@router.delete("/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_animal(animal_id: str):
    """Delete an animal."""
    success = service.delete_animal(animal_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Animal with ID {animal_id} not found"
        )
    return None

@router.get("/graphql-examples", tags=["animals con GraphQLs"])
def get_graphql_examples():
    """Devuelve ejemplos de JSON para probar en el endpoint de GraphQL."""
    return {
        "list_all": {"query": "query { animals { id name category } }"},
        "filter_wild": {"query": "query { animals(category: \"wild\") { name species } }"},
        "search_name": {"query": "query { searchAnimalsByName(nameQuery: \"Luna\") { name ownerName } }"},
        "create_mutation": {
            "query": "mutation { createAnimal(name: \"Coco\", species: \"Loro\", category: \"domestic\", owner_name: \"Luis\") { id name } }"
        }
    }

# GraphQL Integration
graphql_app = GraphQLRouter(schema)
# Mounting at /graphql (full path /animals/graphql)
router.include_router(graphql_app, prefix="/graphql")
