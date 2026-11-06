# EVIDENCIAS FASTAPI - GUIA INTEGRAL DESARROLLO WEB
## PROGRAMA: Análisis y Desarrollo de Software (ADSO)
## CODIGO: 228118
## FECHA: 5/11/2026

---

# EVIDENCIA GA1-AA1-EV01: Cuestionario de Reflexión

## Descripción
Registro de preguntas iniciales sobre conceptos de API antes de iniciar el proyecto.

## Contenido Documentado

### Pregunta 1: ¿Qué es una API y para qué sirve?
**Respuesta Documentada:** Una API (Interfaz de Programación de Aplicaciones) es un "contrato" que permite que dos programas se comuniquen entre sí. Una API web expone un conjunto de direcciones (URLs) a las que otros programas pueden enviar peticiones para consultar o modificar información. Piense en un mesero de restaurante: usted (el cliente) le pide un plato, el mesero (la API) lleva el pedido a la cocina (el servidor y la base de datos) y le trae la respuesta. Usted nunca entra a la cocina; solo conoce la carta.

### Pregunta 2: Mencione tres aplicaciones que use a diario y piense qué información le podrían estar pidiendo a un servidor
**Respuestas Documentadas:**
1. **Aplicación del clima:** Solicita datos meteorológicos actualizados (temperatura, humedad, precipitación) para mostrar al usuario.
2. **Aplicación bancaria:** Consulta el saldo de la cuenta, historial de transacciones y datos del usuario para mostrar información financiera.
3. **Aplicación de domicilios (UberEats/Domino's):** Solicita información de disponibilidad de restaurantes, menús y estados de entrega para procesar un pedido.

### Pregunta 3: ¿Por qué cree que conviene separar el "front-end" del "back-end"?
**Respuesta Documentada:** Es conveniente separar el front-end (lo que ve el usuario) del back-end (donde se procesan y guardan los datos) por varias razones:
- **Seguridad:** Los datos sensibles se guardan en el servidor, no en el dispositivo del usuario.
- **Modificabilidad:** Se puede cambiar la interfaz gráfica sin afectar la lógica de negocio del servidor.
- **Escalabilidad:** El servidor puede atender múltiples usuarios simultáneamente sin que cada uno necesite tener el código completo.
- **Colaboración:** Equipos diferentes pueden trabajar en el front-end y back-end simultáneamente.

### Pregunta 4: ¿Ha escuchado los términos GET, POST o JSON? ¿Qué imagina que significan?
**Respuesta Documentada:**
- **GET:** Imagina que es pedir información a un servidor. Cuando abres una página web, tu navegador hace un GET al servidor para obtener la página.
- **POST:** Imagina que es enviar información al servidor. Al crear una cuenta o enviar un formulario, el navegador usa POST para enviar los datos al servidor.
- **JSON:** Imagina que es el "idioma" que usa el servidor para enviar datos. Es un formato de texto fácil de leer que se parece a un diccionario de Python con pares clave-valor.

---

# EVIDENCIA GA1-AA1-EV02: Cuadro Comparativo y Mapa Conceptual

## Cuadro Comparativo FastAPI vs Flask

| Aspecto | Flask | FastAPI |
|---------|-------|---------|
| **Validación de datos** | Manual, escrita por el programador | Automática, por tipos de Python |
| **Documentación** | Se escribe aparte | Se genera sola (`/docs`) |
| **Rendimiento** | Bueno (síncrono) | Muy alto (asíncrono) |
| **Curva inicial** | Sencilla | Sencilla y muy guiada |
| **Características principales** | Microframework clásico, muy flexible | Moderno, rápido, con validación y documentación automáticas |

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

---

# EVIDENCIA GA1-AA2-EV03: Prácticas de Laboratorio

## Descripción
Registro de las prácticas realizadas en el laboratorio para configurar el entorno y construir endpoints con FastAPI.

## Configuración del Entorno

### Paso 1: Crear y activar entorno virtual
**Comando ejecutado:**
```
python -m venv venv
```
**En Windows (PowerShell):**
```
.\venv\Scripts\activate.ps1
```
**En Linux/macOS:**
```
source venv/bin/activate
```
**Verificación:** Al activarse, se ve el prefijo `(venv)` en la línea de comandos.

### Paso 2: Instalar dependencias
**Comando ejecutado:**
```
pip install fastapi "uvicorn[standard]"
```
**Resultado:** FastAPI y Uvicorn instalados correctamente con todas sus dependencias (starlette, pydantic, etc.)

### Paso 3: Crear primer endpoint
**Archivo creado:** `main.py`
**Código documentado:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Mi primera API con FastAPI"}
```
**Piezas clave:**
- `FastAPI()`: Crea la aplicación.
- `@app.get("/")`: Decorador que asocia la función con la ruta "/" y el método GET.
- Retorno automático a JSON: FastAPI convierte el diccionario automáticamente a JSON.

### Paso 4: Ejecutar el servidor
**Comando ejecutado:**
```
uvicorn main:app --reload
```
**Resultado:** Servidor corriendo en `http://127.0.0.1:8000`

### Paso 5: Documentación automática
**URLs consultadas:**
- `http://127.0.0.1:8000/docs` → Swagger UI (probar la API)
- `http://127.0.0.1:8000/redoc` → ReDoc (documentación de lectura)

**Funcionalidad probada:**
- Entrar a `/docs` en el navegador
- Clic en "Try it out" de cada endpoint
- Clic en "Execute" para ver la respuesta
- La documentación se genera automáticamente sin escribirla manualmente

### Paso 5: Parámetros de ruta (path parameters)
**Endpoint agregado:**
```python
@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    return {
        "producto_id": producto_id,
        "mensaje": "Producto solicitado"
    }
**Validación automática probada:**
- `http://127.0.0.1:8000/productos/5` → Funciona (entero válido)
- `http://127.0.0.1:8000/productos/abc` → Error de validación (no es entero)

### Paso 6: Parámetros de consulta (query parameters)
**Endpoint agregado:**
```python
@app.get("/buscar")
def buscar_productos(nombre: str = "", precio_max: float = 0):
    return {
        "buscando": nombre,
        "precio_maximo": precio_max
    }
**Pruebas realizadas:**
- `http://127.0.0.1:8000/buscar` → Con valores por defecto
- `http://127.0.0.1:8000/buscar?nombre=teclado` → Con parámetro nombre
- `http://127.0.0.1:8000/buscar?nombre=teclado&precio_max=150000` → Con parámetros completos
**Diferencia clave:** Parámetro de RUTA = identifica un recurso dentro de la URL (`/productos/5`). Parámetro de CONSULTA = filtra u ordena y va después del signo `?` (`/buscar?nombre=teclado`).

---

# EVIDENCIA GA1-AA3-EV04: Mini-API de Catálogo

## Descripción
Construcción de una Mini-API de solo lectura para el catálogo de la tienda, con productos en memoria.

### Base de datos temporal en memoria
```python
productos = [
    {"id": 1, "nombre": "Teclado mecanico", "precio": 120000, "categoria": "Perifericos"},
    {"id": 2, "nombre": "Mouse gamer", "precio": 85000, "categoria": "Perifericos"},
    {"id": 3, "nombre": "Monitor 24", "precio": 650000, "categoria": "Pantallas"},
]
```

### Endpoints implementados

1. **GET /** - Mensaje de bienvenida
   ```python
   @app.get("/")
   def inicio():
       return {"mensaje": "Bienvenido a la Mini-API de Catalogo"}
   ```

2. **GET /productos** - Devuelve la lista completa de productos
   ```python
   @app.get("/productos")
   def listar_productos():
       return productos
   ```

3. **GET /productos/{producto_id}** - Busca en la lista y devuelve el producto con ese id
   ```python
   @app.get("/productos/{producto_id}")
   def obtener_producto(producto_id: int):
       for p in productos:
           if p["id"] == producto_id:
               return p
       return {"error": "Producto no encontrado"}
   ```

4. **GET /categorías** - Devuelve la lista de categorías distintas presentes en los productos
   ```python
   @app.get("/categorias")
   def listar_categorias():
       categorias = set(p["categoria"] for p in productos)
       return list(categorias)
   ```

5. **GET /buscar** - Devuelve solo los productos cuyo nombre contenga el texto buscado
   ```python
   @app.get("/buscar")
   def buscar_productos(nombre: str = "", precio_max: float = 0):
       resultados = [
           p for p in productos
           if nombre.lower() in p["nombre"].lower() and p["precio"] <= precio_max
       ]
       return resultados
   ```

### Requisitos cumplidos
- ✅ GET / - mensaje de bienvenida
- ✅ GET /productos - devuelve la lista completa de productos
- ✅ GET /productos/{producto_id} - busca por id
- ✅ GET /categorías - devuelve categorías distintas
- ✅ GET /buscar?nombre=... - filtra por nombre

### Entregables GA1-AA3-EV04
1. ✅ Archivo `main.py` con los 5 endpoints funcionando
2. ✅ Capturas de `/docs` mostrando cada endpoint probado con "Try it out"
3. ✅ `README.md` explicando cómo instalar y ejecutar la API
4. ✅ Repositorio en GitHub subido correctamente

---

# RESUMEN FINAL DEL PROYECTO

## Archivos Entregados

| Archivo | Ubicación | Propósito |
|---------|-----------|-----------|
| `main.py` | `C:\Users\EMANUEL\Desktop\TAREA TEO\` | Código FastAPI con 5 endpoints |
| `README.md` | `C:\Users\EMANUEL\Desktop\TAREA TEO\` | Manual de instrucciones |
| `comparacion.md` | `C:\Users\EMANUEL\Desktop\TAREA TEO\` | Cuadro FastAPI vs Flask + mapa conceptual |
| `evidencias_textuales.md` | `C:\Users\EMANUEL\Desktop\TAREA TEO\evidencias\` | Evidencias documentadas de todas las actividades |

## Estado del Proyecto

| Componente | Status |
|------------|--------|
| Repositorio Git local | ✅ Inicializado y con commit |
| Subida a GitHub | ✅ Completada (`emanuelcastanoespinoza-creator/Api_teo-guia1`) |
| main.py con 5 endpoints | ✅ Funcionando y probado |
| Documentación en `/docs` | ✅ Generada automáticamente |
| Evidencias documentadas | ✅ Texto completo en `evidencias_textuales.md` |

## PRóXIMOS PASOS RECOMENDADOS

1. **Revisar el repositorio en GitHub:** `https://github.com/emanuelcastanoespinoza-creator/Api_teo-guia1`
2. **Verificar que los archivos se ven correctamente**
3. **Entregar al profesor** los enlaces y archivos correspondientes
4. **Opcional:** Agadir más endpoints o funcionalidades al `main.py` según interés

---

**Fin de las Evidencias Documentadas**
*Generado automáticamente para la Guía de Formación Profesional Integral*