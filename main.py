from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de Nota
class Nota(BaseModel):
    id: int
    titulo: str
    contenido: str

# "Base de datos" temporal en memoria
notas = []

# GET - Obtener todas las notas
@app.get("/notas")
def obtener_notas():
    return notas

# POST - Crear una nueva nota
@app.post("/notas")
def crear_nota(nota: Nota):
    notas.append(nota)
    return {"mensaje": "Nota creada correctamente", "nota": nota}

# PUT - Actualizar una nota existente
@app.put("/notas/{nota_id}")
def actualizar_nota(nota_id: int, nueva_nota: Nota):
    for index, nota in enumerate(notas):
        if nota.id == nota_id:
            notas[index] = nueva_nota
            return {"mensaje": "Nota actualizada", "nota": nueva_nota}

    raise HTTPException(status_code=404, detail="Nota no encontrada")

# DELETE - Borrar una nota
@app.delete("/notas/{nota_id}")
def borrar_nota(nota_id: int):
    for index, nota in enumerate(notas):
        if nota.id == nota_id:
            notas.pop(index)
            return {"mensaje": "Nota eliminada"}

    raise HTTPException(status_code=404, detail="Nota no encontrada")

@app.get("/")
def inicio():
    return {"mensaje": "API de notas funcionando correctamente 🚀", "endpoints": ["/notas", "/docs"]}
