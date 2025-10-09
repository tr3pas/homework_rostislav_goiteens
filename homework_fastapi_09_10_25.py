from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()


@app.get("/calculate")
def calculate(op: str = Query(..., description="Operation +,-,*,/"),
               a: int = Query(..., description="frist numer"),
               b: int = Query(None, description="second number")):
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            raise HTTPException(status_code=404, detail="You can't divide by 0")
        else:
            result = a / b
    else:
        raise HTTPException(status_code=404, detail="Program didn't find operator, plese use the +,-,*,/")

    return {
        "operation": op,
        "first number": a,
        "second number": b,
        "result" : result

    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app= f"{__name__}:app", reload=True, port=8000)