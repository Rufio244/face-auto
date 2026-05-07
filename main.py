
from fastapi import FastAPI
from core import FaceAuto

app = FastAPI()
engine = FaceAuto()

@app.post("/run")
def run(request: dict):
    return engine.run(request)
