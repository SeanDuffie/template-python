from fastapi import FastAPI
from project.logic import process_data

app = FastAPI()

@app.get("/compute/{value}")
async def get_compute(value: int):
    result = process_data(value)
    return {"result": result}
