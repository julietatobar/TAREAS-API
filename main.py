from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de datos simulada
db = {"1": {"tarea": "Estudiar Python"}, "2": {"tarea": "Practicar APIs"}}

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a tu API de tareas, Víctor"}

@app.get("/tasks")
def obtener_tareas():
    return db

@app.get("/tasks/{task_id}")
def obtener_tarea(task_id: str):
    if task_id not in db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db[task_id]

@app.post("/tasks")
def crear_tarea(task_id: str, tarea: str):
    if task_id in db:
        raise HTTPException(status_code=400, detail="La tarea ya existe")
    db[task_id] = {"tarea": tarea}
    return {"mensaje": "Tarea creada correctamente"}

@app.delete("/tasks/{task_id}", status_code=204)
def eliminar_tarea(task_id: str):
    if task_id not in db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    del db[task_id]
    return None
