from fastapi import FastAPI
from app.features.products.router import router as products_router

app = FastAPI(
    title="Poli U2 REST Fast API",
    description="API RESTful para la gestión de productos - Unidad 2",
    version="1.0.0"
)

# Root endpoint
@app.get("/", tags=["root"])
def read_root():
    return {
        "status": "online",
        "message": "Bienvenido a la API de Gestión de Productos",
        "docs": "/docs"
    }

# Register routers
app.include_router(products_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)