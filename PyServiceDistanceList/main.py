from fastapi import FastAPI
from pydantic import BaseModel
from collections import Counter

app = FastAPI()

class ListsInput(BaseModel):
    left: list[int]
    right: list[int]

@app.post("/calcola")
def calcola(data: ListsInput):
    # PARTE 1 Calcolo distanze minime totali tra due liste
    L = sorted(data.left)
    R = sorted(data.right)
    totale = sum(abs(a - b) for a, b in zip(L, R))

    # PARTE 2 - Somme pesate per coincidenza valori tra le liste
    freq_right = Counter(R)
    total_similarity = sum(x * freq_right.get(x, 0) for x in L)
    return {"result": totale, "similarity": total_similarity}
