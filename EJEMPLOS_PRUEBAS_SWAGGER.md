# Contratos de Prueba para Swagger

Usa estos fragmentos JSON para probar tus endpoints en `http://localhost:8000/docs`. He preparado 2 ejemplos por cada operación que requiere un cuerpo de mensaje (Body).

---

## 1. POST /products/ (Crear Producto)
*Copia y pega esto en el campo "Request body" al probar el método POST.*

### Ejemplo 1: Smartphone
```json
{
  "nombre": "iPhone 15 Pro",
  "descripcion": "Smartphone de última generación con chip A17 Pro y cámara de 48MP",
  "precio": 999.99
}
```

### Ejemplo 2: Monitor Gamer
```json
{
  "nombre": "Monitor LG UltraGear",
  "descripcion": "Monitor de 27 pulgadas, 144Hz, 1ms de respuesta con panel IPS",
  "precio": 349.50
}
```

---

## 2. PUT /products/{id} (Actualizar Producto)
*Primero obtén un ID de un producto existente y pégalo en el campo "product_id". Luego usa estos JSON en el body.*

### Ejemplo 1: Rebaja de Precio (Smartphone)
```json
{
  "nombre": "iPhone 15 Pro - Oferta",
  "precio": 899.99
}
```

### Ejemplo 2: Cambio de Descripción (Monitor)
```json
{
  "descripcion": "Monitor LG UltraGear (Última Unidad) - 27 pulgadas, QHD, 144Hz",
  "precio": 320.00
}
```

---

## 3. GET y DELETE /products/{id}
*Para estos endpoints no necesitas un archivo JSON, solo el **ID** del producto que quieras consultar o borrar.*

**Pasos:**
1.  Ejecuta primero `GET /products/` para ver la lista de IDs disponibles.
2.  Copia un ID (ej: `4jqmcSfu0ZSQBwwXb2zj`).
3.  Pégalo en el parámetro `product_id` de Swagger y dale a "Execute".

---

## 📝 Notas de Validación (Pydantic)
- **Nombre:** Mínimo 2 caracteres, máximo 100.
- **Descripción:** Mínimo 5 caracteres, máximo 500.
- **Precio:** Debe ser mayor a 0.
