# Mini-API de Catálogo - FastAPI

## Descripción
API de solo lectura para el catálogo de una tienda de comercio electrónico. Los productos están almacenados en memoria (lista en Python). No se utiliza base de datos.

## Instalación y Ejecución

### 1. Clonar o descargar el repositorio
```bash
git clone <tu-repositorio>
cd mi-api
```

### 2. Crear y activar el entorno virtual

#### En Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\activate.ps1
```

#### En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install fastapi "uvicorn[standard]"
```

### 4. Ejecutar el servidor
```bash
uvicorn main:app --reload
```

La API estará disponible en: http://127.0.0.1:8000

### 5. Acceder a la documentación interactiva

Abre tu navegador en:

- **Swagger UI:** http://127.0.0.1:8000/docs
  - Aquí puedes probar todos los endpoints desde el navegador
  - Pulsa "Try it out" y luego "Execute"

- **ReDoc:** http://127.0.0.1:8000/redoc
  - Documentación de lectura más formal

## Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Mensaje de bienvenida |
| GET | `/productos` | Devuelve la lista completa de productos |
| GET | `/productos/{producto_id}` | Busca un producto por su ID |
| GET | `/categorias` | Devuelve las categorías distintas de los productos |
| GET | `/buscar` | Filtra productos por nombre y precio máximo |

## Ejemplos de uso

### Obtener todos los productos
```
GET http://127.0.0.1:8000/productos
```

### Obtener producto por ID (ejemplo: ID 1)
```
GET http://127.0.0.1:8000/productos/1
```

### Buscar productos por nombre (ejemplo: "Teclado")
```
GET http://127.0.0.1:8000/buscar?nombre=Teclado
```

### Buscar con filtro de precio máximo
```
GET http://127.0.0.1:8000/buscar?nombre=Teclado&precio_max=100000
```

## Tecnologías utilizadas
- **FastAPI:** Framework de Python para APIs modernas
- **Uvicorn:** Servidor ASGI que ejecuta la aplicación
- **Python 3.13:** Lenguaje de programación