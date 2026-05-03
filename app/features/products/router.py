from fastapi import APIRouter, HTTPException, status
from typing import List
from .schemas import Product, ProductCreate, ProductUpdate
from .repository import ProductRepository
from .service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# Dependency injection
repository = ProductRepository()
service = ProductService(repository)

@router.get("/", response_model=List[Product], status_code=status.HTTP_200_OK)
def list_products():
    """List all products."""
    return service.get_all_products()

@router.get("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def get_product(product_id: str):
    """Get a product by ID."""
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found"
        )
    return product

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    """Create a new product."""
    return service.create_product(product)

@router.put("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def update_product(product_id: str, product: ProductUpdate):
    """Update an existing product."""
    updated_product = service.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found"
        )
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: str):
    """Delete a product."""
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found"
        )
    return None
