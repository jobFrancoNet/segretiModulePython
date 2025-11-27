from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ListsInput(BaseModel):
    left: list[int]
    right: list[int]

@app.post("/calcola")
def calcola(data: ListsInput):
    L = sorted(data.left)
    R = sorted(data.right)
    totale = sum(abs(a - b) for a, b in zip(L, R))
    return {"result": totale}
