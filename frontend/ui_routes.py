from unittest import result

from fastapi import FastAPI
from nicegui import ui


def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.add_head_html('''
            <style>
                .search-input { border-radius: 25px; padding: 10px; border: 1px solid #008080; font-size: 16px; width: 650px; }
            </style>
            <link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />
            <link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />
        ''')


        # Big Welcome Label
        ui.label("Welcome to PetSavior!").classes("w-full text-center").style("font-size: 100px; font-weight: bold;")

        # Center
        with (ui.row().classes("justify-center items-center w-full text-center")):
            # Search bar sends to search page on 'Enter'
            search_input = ui.input(placeholder='Search for Pets...').classes('search-input')
            search_input.on('keydown.enter', lambda: ui.navigate.to(f'/search?query={search_input.value}'))
            # Icon
            ui.icon('eva-search-outline').classes('text-5xl').style('margin-right: 10px')

    @ui.page("/search")
    def search_page(query: str = None):

        # On any change it should search database again?
        with ui.row().classes("justify-center items-center w-full text-center"):
            if query is not None:
                search_input = ui.input(value=query, placeholder='Search for Pets...')
            else:
                search_input = ui.input(placeholder='Search for Pets...')

            # On enter, search again
            search_input.classes('search-input')
            search_input.on('keydown.enter', lambda: ui.navigate.to(f'/search?query={search_input.value}'))
            # Icon
            ui.icon('eva-search-outline').classes('text-5xl').style('margin-right: 10px')
