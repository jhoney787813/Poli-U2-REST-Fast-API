from typing import List, Optional
from google.cloud.firestore_v1.base_client import BaseClient
from .schemas import ProductCreate, ProductUpdate
from app.core.database import get_db

class ProductRepository:
    def __init__(self):
        self.db = get_db()
        self.collection_name = "productos"

    def get_all(self) -> List[dict]:
        docs = self.db.collection(self.collection_name).stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    def get_by_id(self, product_id: str) -> Optional[dict]:
        doc_ref = self.db.collection(self.collection_name).document(product_id)
        doc = doc_ref.get()
        if doc.exists:
            return {**doc.to_dict(), "id": doc.id}
        return None

    def create(self, product: ProductCreate) -> dict:
        doc_ref = self.db.collection(self.collection_name).document()
        product_data = product.model_dump()
        doc_ref.set(product_data)
        return {**product_data, "id": doc_ref.id}

    def update(self, product_id: str, product: ProductUpdate) -> Optional[dict]:
        doc_ref = self.db.collection(self.collection_name).document(product_id)
        doc = doc_ref.get()
        if not doc.exists:
            return None
        
        update_data = product.model_dump(exclude_unset=True)
        doc_ref.update(update_data)
        updated_doc = doc_ref.get()
        return {**updated_doc.to_dict(), "id": updated_doc.id}

    def delete(self, product_id: str) -> bool:
        doc_ref = self.db.collection(self.collection_name).document(product_id)
        doc = doc_ref.get()
        if not doc.exists:
            return False
        doc_ref.delete()
        return True
