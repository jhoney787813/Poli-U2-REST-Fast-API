import httpx
import json

BASE_URL = "http://localhost:8000"
GRAPHQL_URL = f"{BASE_URL}/animals/graphql"

def test_graphql():
    print("--- 🧬 Iniciando Pruebas de GraphQL para Animales ---")
    
    with httpx.Client() as client:
        # 1. Mutación: Crear un animal salvaje
        print("\n1. Probando Mutación (createAnimal)...")
        mutation = """
        mutation {
          createAnimal(
            name: "Kala",
            species: "Gorilla",
            category: "wild",
            age: 12
          ) {
            id
            name
            species
            category
          }
        }
        """
        response = client.post(GRAPHQL_URL, json={"query": mutation})
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            if "errors" in data:
                print(f"❌ Error en GraphQL: {data['errors']}")
            else:
                animal = data["data"]["createAnimal"]
                print(f"✅ Animal creado via GraphQL: {json.dumps(animal, indent=2)}")
        else:
            print("❌ El servidor no está respondiendo (Asegúrate de ejecutar python main.py)")

        # 2. Consulta: Listar todos los animales
        print("\n2. Probando Consulta (animals)...")
        query = """
        query {
          animals {
            name
            category
            ownerName
          }
        }
        """
        response = client.post(GRAPHQL_URL, json={"query": query})
        if response.status_code == 200:
            data = response.json()
            animals = data["data"]["animals"]
            print(f"✅ Total animales encontrados: {len(animals)}")
            print(f"Muestra: {json.dumps(animals[:2], indent=2)}")

        # 3. Consulta Avanzada: Filtrar por categoría 'domestic'
        print("\n3. Probando Filtro por Categoría (domestic)...")
        query_filter = """
        query {
          animals(category: "domestic") {
            name
            ownerName
          }
        }
        """
        response = client.post(GRAPHQL_URL, json={"query": query_filter})
        if response.status_code == 200:
            domestics = response.json()["data"]["animals"]
            print(f"✅ Animales domésticos: {json.dumps(domestics, indent=2)}")

        # 4. Búsqueda por Nombre
        print("\n4. Probando Búsqueda por Nombre (searchAnimalsByName)...")
        query_search = """
        query {
          searchAnimalsByName(nameQuery: "Luna") {
            name
            species
            category
          }
        }
        """
        response = client.post(GRAPHQL_URL, json={"query": query_search})
        if response.status_code == 200:
            results = response.json()["data"]["searchAnimalsByName"]
            print(f"✅ Resultados de búsqueda: {json.dumps(results, indent=2)}")

if __name__ == "__main__":
    test_graphql()
