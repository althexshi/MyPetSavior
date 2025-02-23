from unittest import result

from fastapi import FastAPI
from nicegui import ui

def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.add_head_html('<link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />')
        ui.label("Welcome to PetSavior!").style("font-size: 24px; font-weight: bold;")
        ui.button("Find a Pet", on_click=lambda: ui.notify("Coming soon!"))
        with ui.row().classes('items-center'):
            ui.icon('ti-heart').classes('text-5xl').style('margin-right: 10px;')
            search_input = ui.input(placeholder='Search For Pets...')
            search_input.style(
                'border-radius: 25px; '
                'padding: 10px; '
                'border: 1px solid #008080; '
                'font-size: 16px; '
                'width: 650px;'
            )

