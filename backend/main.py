from fastapi import FastAPI
from nicegui import ui
from backend.api_routes import router as api_router
from frontend.ui_routes import add_ui_routes

app = FastAPI()

app.include_router(api_router)
add_ui_routes()

ui.run_with(app)
