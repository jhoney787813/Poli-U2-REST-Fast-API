# Poli U2 REST Fast API

Backend desarrollado con **FastAPI** y **Firebase** para la gestión de productos, siguiendo principios **SOLID, YAGNI, GRASP** y el **Modelo de Madurez de Richardson**.

## 🚀 Inicio Rápido

### 1. Requisitos Previos
- Python 3.9+
- Una cuenta en Firebase con Firestore habilitado.

### 2. Configuración
1. Clona el repositorio.
2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Coloca tu archivo de credenciales de Firebase como `serviceAccountKey.json` en la raíz del proyecto.

### 3. Ejecución
Inicia el servidor de desarrollo:
```bash
uvicorn main:app --reload
```
La API estará disponible en: `http://localhost:8000`

## 📚 Documentación
- **Swagger UI**: `http://localhost:8000/docs` (Pruebas interactivas)
- **Redoc**: `http://localhost:8000/redoc`
- **Manual de Arquitectura**: Consulta [ARCHITECTURE.md](./ARCHITECTURE.md) para detalles técnicos y diagramas.
- **Como se cumple con la rubrica?**: Consulta [RUBRICA.md](./JUSTIFICACION_RUBRICA.md) para ver la justificacion

## 🧪 Pruebas
He incluido un script de pruebas automatizadas:
```bash
python test_api.py
```

## 🛠️ Tecnologías Usadas
- **FastAPI**: Framework web moderno y rápido.
- **Firebase Admin SDK**: Integración con Firestore.
- **Pydantic**: Validación de datos y esquemas.
- **Uvicorn**: Servidor ASGI de alto rendimiento.

---
Módulo: Arquitectura de Aplicaciones Web - Unidad 2
