from fastapi import FastAPI

app = FastAPI()

# "Base de datos" temporal en memoria
productos = [
    {"id": 1, "nombre": "Teclado mecanico", "precio": 120000, "categoria": "Perifericos"},
    {"id": 2, "nombre": "Mouse gamer", "precio": 85000, "categoria": "Perifericos"},
    {"id": 3, "nombre": "Monitor 24", "precio": 650000, "categoria": "Pantallas"},
]

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la Mini-API de Catalogo"}

@app.get("/productos")
def listar_productos():
    return productos

@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for p in productos:
        if p["id"] == producto_id:
            return p
    return {"error": "Producto no encontrado"}

@app.get("/categorias")
def listar_categorias():
    categorias = set(p["categoria"] for p in productos)
    return list(categorias)

@app.get("/buscar")
def buscar_productos(nombre: str = "", precio_max: float = 0):
    resultados = [
        p for p in productos 
        if nombre.lower() in p["nombre"].lower() and p["precio"] <= precio_max
    ]
    return resultados