from fastapi import FastAPI

app = FastAPI()

# "Base de datos" temporal en memoria
productos = [
    {"id": 1, "nombre": "Teclado mecanico", "precio": 120000, "categoria": "Perifericos"},
<<<<<<< HEAD
    {"id": 2, "nombre": "Mouse gamer", "precio": 85000, "categoria": "Perifericos"},
    {"id": 3, "nombre": "Monitor 24", "precio": 650000, "categoria": "Pantallas"},
=======
    {"id": 2, "nombre": "Mouse gamer",      "precio": 85000,  "categoria": "Perifericos"},
    {"id": 3, "nombre": "Monitor 24",       "precio": 650000, "categoria": "Pantallas"},
>>>>>>> ccbef893c841119c5f091793c5cded15afa88ede
]

@app.get("/")
def inicio():
<<<<<<< HEAD
    return {"mensaje": "Bienvenido a la Mini-API de Catalogo"}
=======
    return {"mensaje": "Bienvenido a la Mini-Api de Catalogo"}
>>>>>>> ccbef893c841119c5f091793c5cded15afa88ede

@app.get("/productos")
def listar_productos():
    return productos

@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for p in productos:
        if p["id"] == producto_id:
<<<<<<< HEAD
            return p
=======
            return {
                "id": p["id"],
                "nombre": p["nombre"],
                "precio": p["precio"],
                "categoria": p["categoria"]
            }
>>>>>>> ccbef893c841119c5f091793c5cded15afa88ede
    return {"error": "Producto no encontrado"}

@app.get("/categorias")
def listar_categorias():
    categorias = set(p["categoria"] for p in productos)
    return list(categorias)

@app.get("/buscar")
def buscar_productos(nombre: str = "", precio_max: float = 0):
<<<<<<< HEAD
    resultados = [
        p for p in productos 
        if nombre.lower() in p["nombre"].lower() and p["precio"] <= precio_max
    ]
    return resultados
=======
    return {
        "buscando": nombre,
        "precio_maximo": precio_max
    }
>>>>>>> ccbef893c841119c5f091793c5cded15afa88ede
