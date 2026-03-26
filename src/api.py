from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando 🚀"}

@app.get("/generar")
def generar():
    return {"password": "test1234"}