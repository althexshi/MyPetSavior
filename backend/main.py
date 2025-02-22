from fastapi import FastAPI
from nicegui import ui

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/search")
async def search():
    return {"message": "Search results?"}

@app.get("/pet/{id}")
async def get_pet(id):
    return {"message": f"Pet: {id}"}


