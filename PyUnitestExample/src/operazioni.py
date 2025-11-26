def somma(a, b):
    return a + b

def sottrai(a, b):
    return a - b

def dividi(a, b):
    if b == 0:
        raise ValueError("Impossibile dividere per zero")
    return a / b
