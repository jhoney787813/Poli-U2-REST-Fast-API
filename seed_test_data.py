import sys
import os

# Añadir el directorio actual al path para poder importar 'app'
sys.path.append(os.getcwd())

from app.features.products.repository import ProductRepository
from app.features.products.schemas import ProductCreate

def seed_data():
    repo = ProductRepository()
    
    test_products = [
        {
            "nombre": "Laptop Test",
            "descripcion": "Product inserted for testing purposes",
            "precio": 999.99
        },
        {
            "nombre": "Mouse Test",
            "descripcion": "Wireless mouse for test",
            "precio": 25.50
        },
        {
            "nombre": "Teclado Test",
            "descripcion": "Mechanical keyboard test record",
            "precio": 75.00
        }
    ]
    
    print("Conectando a Firebase e insertando registros de prueba...")
    
    for item in test_products:
        product_in = ProductCreate(**item)
        try:
            created = repo.create(product_in)
            print(f"✅ Insertado: {created['nombre']} (ID: {created['id']})")
        except Exception as e:
            print(f"❌ Error al insertar {item['nombre']}: {e}")

if __name__ == "__main__":
    seed_data()
