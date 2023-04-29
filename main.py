from fastapi import FastAPI

app = FastAPI()


@app.get("/get/{name}")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}