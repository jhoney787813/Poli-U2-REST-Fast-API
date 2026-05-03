from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: str = Field(..., min_length=5, max_length=500)
    precio: float = Field(..., gt=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    descripcion: Optional[str] = Field(None, min_length=5, max_length=500)
    precio: Optional[float] = Field(None, gt=0)

class Product(ProductBase):
    id: str

    class Config:
        from_attributes = True
