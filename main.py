import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()



class Calculator:
    def __init__(self):
        self.memory = []

    def add(self, alga:float):
        self.memory.append(alga)
        return alga


    def get_memory(self):
        return self.memory

calc = Calculator()

@app.get("/calc/memory", summary="память")
def show_memory():
    return {"status": "success", "memory": calc.get_memory() }


@app.get("/calc/plus", summary="сложение")
def plus(a:float,b:float):
    res_plus = calc.add(a + b)
    return {"status": "succes", "result": res_plus}

@app.get("/calc/minus", summary="вычитание")
def minus(a:float,b:float):
    res_minus = calc.add(a - b)
    return {"status": "succes", "result": res_minus}

@app.get("/calc/multiplicate", summary="умножениу")
def mult(a:float,b:float):
    res_mult = calc.add(a * b)
    return {"status": "succes", "result": res_mult}

@app.get("/calc/division", summary="деление")
def div(a:float,b:float):
    if (b or a) == 0:
        raise HTTPException(status_code=400, details="деление на ноль")
    res_div = calc.add(a / b)
    return {"status": "succes", "result": res_div}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
