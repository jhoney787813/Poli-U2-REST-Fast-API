from typing import List, Optional
from .repository import ProductRepository
from .schemas import ProductCreate, ProductUpdate

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_all_products(self) -> List[dict]:
        return self.repository.get_all()

    def get_product(self, product_id: str) -> Optional[dict]:
        return self.repository.get_by_id(product_id)

    def create_product(self, product: ProductCreate) -> dict:
        return self.repository.create(product)

    def update_product(self, product_id: str, product: ProductUpdate) -> Optional[dict]:
        return self.repository.update(product_id, product)

    def delete_product(self, product_id: str) -> bool:
        return self.repository.delete(product_id)
