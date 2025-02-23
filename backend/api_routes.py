from fastapi import FastAPI

def add_api_routes(app: FastAPI):
    @app.get("/hello/{name}")
    async def say_hello(name: str):
        return {"message": f"Hello {name}"}

    @app.get("/search")
    async def search():
        return {"message": "Search results?"}

    @app.get("/pet/{id}")
    async def get_pet(id):
        return {"message": f"Pet: {id}"}