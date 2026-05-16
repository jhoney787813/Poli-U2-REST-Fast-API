from typing import List, Optional
from .schemas import AnimalCreate, AnimalUpdate
from app.core.database import get_db

class AnimalRepository:
    def __init__(self):
        self.db = get_db()
        self.collection_name = "animals"

    def get_all(self, category: Optional[str] = None) -> List[dict]:
        query = self.db.collection(self.collection_name)
        if category:
            query = query.where("category", "==", category)
        docs = query.stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    def get_by_id(self, animal_id: str) -> Optional[dict]:
        doc_ref = self.db.collection(self.collection_name).document(animal_id)
        doc = doc_ref.get()
        if doc.exists:
            return {**doc.to_dict(), "id": doc.id}
        return None

    def create(self, animal: AnimalCreate) -> dict:
        doc_ref = self.db.collection(self.collection_name).document()
        animal_data = animal.model_dump()
        doc_ref.set(animal_data)
        return {**animal_data, "id": doc_ref.id}

    def update(self, animal_id: str, animal: AnimalUpdate) -> Optional[dict]:
        doc_ref = self.db.collection(self.collection_name).document(animal_id)
        doc = doc_ref.get()
        if not doc.exists:
            return None
        
        update_data = animal.model_dump(exclude_unset=True)
        doc_ref.update(update_data)
        updated_doc = doc_ref.get()
        return {**updated_doc.to_dict(), "id": updated_doc.id}

    def delete(self, animal_id: str) -> bool:
        doc_ref = self.db.collection(self.collection_name).document(animal_id)
        doc = doc_ref.get()
        if not doc.exists:
            return False
        doc_ref.delete()
        return True
