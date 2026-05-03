import httpx
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("--- 🚀 Iniciando Pruebas de API ---")
    
    with httpx.Client(base_url=BASE_URL) as client:
        # 1. Crear un producto
        print("\n1. Creando producto...")
        payload = {
            "nombre": "Laptop Gamer",
            "descripcion": "Laptop con RTX 4080 y 32GB RAM",
            "precio": 2500.99
        }
        response = client.post("/products/", json=payload)
        print(f"Status: {response.status_code}")
        if response.status_code == 201:
            product = response.json()
            product_id = product['id']
            print(f"Producto creado: {json.dumps(product, indent=2)}")
        else:
            print("Error al crear producto (¿Configuraste Firebase?)")
            return

        # 2. Listar productos
        print("\n2. Listando productos...")
        response = client.get("/products/")
        print(f"Status: {response.status_code}")
        print(f"Total productos: {len(response.json())}")

        # 3. Obtener el producto creado
        print(f"\n3. Obteniendo producto {product_id}...")
        response = client.get(f"/products/{product_id}")
        print(f"Status: {response.status_code}")
        print(response.json())

        # 4. Actualizar el producto
        print("\n4. Actualizando precio...")
        response = client.put(f"/products/{product_id}", json={"precio": 2399.99})
        print(f"Status: {response.status_code}")
        print(f"Nuevo precio: {response.json()['precio']}")

        # 5. Eliminar el producto
        print("\n5. Eliminando producto...")
        response = client.delete(f"/products/{product_id}")
        print(f"Status: {response.status_code}")
        if response.status_code == 204:
            print("Eliminación exitosa")

if __name__ == "__main__":
    test_api()
