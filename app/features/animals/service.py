from typing import List, Optional
from fastapi import HTTPException, status
from .repository import AnimalRepository
from .schemas import AnimalCreate, AnimalUpdate, AnimalCategory

class AnimalService:
    def __init__(self, repository: AnimalRepository):
        self.repository = repository

    def get_all_animals(self, category: Optional[str] = None) -> List[dict]:
        return self.repository.get_all(category)

    def get_animal(self, animal_id: str) -> Optional[dict]:
        return self.repository.get_by_id(animal_id)

    def create_animal(self, animal: AnimalCreate) -> dict:
        # Business Rule: Domestic animals MUST have an owner_name
        if animal.category == AnimalCategory.DOMESTIC and not animal.owner_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Domestic animals must have an owner name associated."
            )
        return self.repository.create(animal)

    def update_animal(self, animal_id: str, animal: AnimalUpdate) -> Optional[dict]:
        # If updating category to domestic, check owner_name
        existing_animal = self.repository.get_by_id(animal_id)
        if not existing_animal:
            return None
        
        new_category = animal.category or existing_animal.get("category")
        new_owner = animal.owner_name or existing_animal.get("owner_name")
        
        if new_category == AnimalCategory.DOMESTIC and not new_owner:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Domestic animals must have an owner name associated."
            )
            
        return self.repository.update(animal_id, animal)

    def delete_animal(self, animal_id: str) -> bool:
        return self.repository.delete(animal_id)
