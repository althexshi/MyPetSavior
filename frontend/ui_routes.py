from fastapi import FastAPI
from nicegui import ui

result = ui.label('')

@ui.page("/")
def main_page():
    ui.label("Welcome to PetSavior!").style("font-size: 24px; font-weight: bold;")
    ui.button("Find a Pet", on_click=lambda: ui.notify("Coming soon!"))
    ui.input(label='Text', placeholder='start typing', on_change=lambda e: result.set_text('you typed: ' + e.value),
             validation={'Input too long': lambda value: len(value) < 20})

ui.run()

