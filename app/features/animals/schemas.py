from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class AnimalCategory(str, Enum):
    DOMESTIC = "domestic"
    WILD = "wild"
    OTHER = "other"

class AnimalBase(BaseModel):
    name: str = Field(..., example="Fido")
    species: str = Field(..., example="Dog")
    category: AnimalCategory = Field(..., example="domestic")
    age: Optional[int] = Field(None, example=3)
    owner_name: Optional[str] = Field(None, description="Name of the owner, required for domestic animals", example="John Doe")

class AnimalCreate(AnimalBase):
    pass

class AnimalUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    category: Optional[AnimalCategory] = None
    age: Optional[int] = None
    owner_name: Optional[str] = None

class Animal(AnimalBase):
    id: str

class GraphQLQuery(BaseModel):
    query: str = Field(..., example="query { animals { name species category ownerName } }")
    variables: Optional[dict] = None
