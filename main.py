from fastapi import FastAPI
from app.features.products.router import router as products_router
from app.features.animals.router import router as animals_router

app = FastAPI(
    title="Poli U2 REST Fast API",
    description="API RESTful para la gestión de productos y animales - Unidad 3",
    version="1.1.0"
)

# Root endpoint
@app.get("/", tags=["root"])
def read_root():
    return {
        "status": "online",
        "message": "Bienvenido a la API de Gestión de Productos y Animales",
        "docs": "/docs",
        "graphql": "/animals/graphql"
    }

# Register routers
app.include_router(products_router)
app.include_router(animals_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)