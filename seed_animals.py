import sys
import os

# Añadir el directorio actual al path para poder importar 'app'
sys.path.append(os.getcwd())

from app.features.animals.repository import AnimalRepository
from app.features.animals.schemas import AnimalCreate, AnimalCategory

def seed_animals():
    repo = AnimalRepository()
    
    test_animals = [
        {
            "name": "Luna",
            "species": "Cat",
            "category": AnimalCategory.DOMESTIC,
            "age": 2,
            "owner_name": "Maria Garcia"
        },
        {
            "name": "Simba",
            "species": "Lion",
            "category": AnimalCategory.WILD,
            "age": 5
        },
        {
            "name": "Dobby",
            "species": "Elf",
            "category": AnimalCategory.OTHER,
            "age": 10
        },
        {
            "name": "Rex",
            "species": "Golden Retriever",
            "category": AnimalCategory.DOMESTIC,
            "age": 4,
            "owner_name": "Carlos Ruiz"
        }
    ]
    
    print("🐾 Conectando a Firebase e insertando animales de prueba...")
    
    for item in test_animals:
        animal_in = AnimalCreate(**item)
        try:
            created = repo.create(animal_in)
            print(f"✅ Insertado: {created['name']} ({created['category']}) - ID: {created['id']}")
        except Exception as e:
            print(f"❌ Error al insertar {item['name']}: {e}")

if __name__ == "__main__":
    seed_animals()
