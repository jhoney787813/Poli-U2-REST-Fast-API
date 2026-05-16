import strawberry
from typing import List, Optional
from .repository import AnimalRepository
from .schemas import AnimalCategory

@strawberry.type
class AnimalType:
    id: str
    name: str
    species: str
    category: str
    age: Optional[int]
    owner_name: Optional[str]

@strawberry.type
class Query:
    @strawberry.field
    def animals(self, category: Optional[str] = None) -> List[AnimalType]:
        repo = AnimalRepository()
        animals_data = repo.get_all(category)
        return [AnimalType(**animal) for animal in animals_data]

    @strawberry.field
    def animal(self, id: str) -> Optional[AnimalType]:
        repo = AnimalRepository()
        animal_data = repo.get_by_id(id)
        if animal_data:
            return AnimalType(**animal_data)
        return None

    @strawberry.field
    def search_animals_by_name(self, name_query: str) -> List[AnimalType]:
        repo = AnimalRepository()
        animals_data = repo.get_all()
        # Simple search logic for demonstration
        return [
            AnimalType(**animal) 
            for animal in animals_data 
            if name_query.lower() in animal["name"].lower()
        ]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_animal(
        self, 
        name: str, 
        species: str, 
        category: str, 
        age: Optional[int] = None, 
        owner_name: Optional[str] = None
    ) -> AnimalType:
        from .schemas import AnimalCreate, AnimalCategory
        from .service import AnimalService
        
        repo = AnimalRepository()
        service = AnimalService(repo)
        
        animal_in = AnimalCreate(
            name=name,
            species=species,
            category=AnimalCategory(category),
            age=age,
            owner_name=owner_name
        )
        
        new_animal = service.create_animal(animal_in)
        return AnimalType(**new_animal)

schema = strawberry.Schema(query=Query, mutation=Mutation)
