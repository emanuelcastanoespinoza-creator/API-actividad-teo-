# Cuadro Comparativo: Flask vs FastAPI

| Aspecto | Flask | FastAPI |
|---------|-------|---------|
| **Validación de datos** | Manual, escrita por el programador | Automática, por tipos de Python |
| **Documentación** | Se escribe aparte | Se genera sola (`/docs`) |
| **Rendimiento** | Bueno (síncrono) | Muy alto (asíncrono) |
| **Curva inicial** | Sencilla | Sencilla y muy guiada |
| **Características principales** | Microframework clásico, muy flexible | Moderno, rápido, con validación y documentación automática |

## Mapa Conceptual

```
API
├── HTTP (protocolo de comunicación)
│   ├── Métodos (GET, POST, PUT, DELETE)
│   └── Códigos de estado (200, 201, 404, 422, 500)
├── REST (estilo de arquitectura)
│   ├── Recursos (productos, categorías, usuarios)
│   └── Endpoints (direcciones URL)
├── JSON (formato de intercambio de datos)
└── Endpoint (dirección URL de la API)
```

## Glosario Rápido

- **API**: Interfaz de Programación de Aplicaciones
- **REST**: Estilo que organiza la API alrededor de recursos por URL
- **HTTP**: Protocolo de la web con métodos y códigos de estado
- **Endpoint**: Cada dirección URL de la API
- **JSON**: Formato de texto para intercambiar datos
- **FastAPI**: Framework de Python convalidación y docs automáticas
- **Uvicorn**: Servidor que ejecuta FastAPI
- **Entorno virtual**: Caja aislada de librerías
- **Decorador**: `@app.get` que asocia función con ruta
- **Parámetro de ruta**: `/productos/{id}` dentro de la URL
- **Parámetro de consulta**: `?nombre=teclado` después de signo ?
- **Swagger UI**: `/docs` - Probar API desde navegador