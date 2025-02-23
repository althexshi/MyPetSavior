from unittest import result

from fastapi import FastAPI
from nicegui import ui

def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.label("Welcome to PetSavior!").style("font-size: 24px; font-weight: bold;")
        ui.button("Find a Pet", on_click=lambda: ui.notify("Coming soon!"))
        search_input = ui.input(placeholder='Search For Pets...')
        search_input.style(
            'border-radius: 25px; '
            'padding: 10px; '
            'border: 5px solid #008080; '
            'font-size: 16px; '
            'width: 600px;'
)

