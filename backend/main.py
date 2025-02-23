from fastapi import FastAPI
from nicegui import ui
from backend.api_routes import add_api_routes
from frontend.ui_routes import add_ui_routes

app = FastAPI()

add_api_routes(app)
add_ui_routes()

ui.run_with(app)
