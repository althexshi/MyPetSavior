from fastapi import FastAPI
from nicegui import ui

def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.label("Welcome to PetSavior!").style("font-size: 24px; font-weight: bold;")
        ui.button("Find a Pet", on_click=lambda: ui.notify("Coming soon!"))