from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hi():
    return {"data": "hi"}

