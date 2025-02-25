from unittest import result
from fastapi import FastAPI, requests
from nicegui import ui
import asyncio
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Animals
from backend.api_routes import search_pets

head_html = '''
            <style>
                .search-container { position: relative; width: 650px; margin: 0 auto;  /* centers the container horizontally */ }
                .search-container input {}
                .q-field__append .q-icon { color: inherit; }
                .q-field--focused .q-field__append .q-icon { color: black; }
            </style>
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />
            <link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />
        '''

search_bar_props = 'rounded outlined color=teal bg-color=grey-1 input-style="color: black; font-size: 20px"'

def display_dog():
    src = 'https://lottie.host/0bc74d91-888a-453c-a078-cfefaf784e45/FJLJ2LV1bw.json'
    ui.html(f'<lottie-player src="{src}" loop autoplay />').style(
        "width: 400px; margin: 0 auto; text-align: center; ")


def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.add_head_html(head_html)
        ui.query('body').style('background-color: #F5E7DE')
        ui.label("Welcome to Pet Savior!").classes("w-full text-center").style(
            "font-size: 100px; font-family: 'Calibre', serif; font-weight: bold; color: #F2BFA4")

        # Center search bar
        with ui.element('div').classes('search-container'):
            # ui.html('<i class="ti-search search-icon"></i>')
            # ui.icon('eva-search-outline')
            search_input = ui.input(placeholder='Search for Pets...')
            # On hitting enter, navigate to search page
            search_input.on('keydown.enter', lambda: ui.navigate.to(f'/search?query={search_input.value}'))
            search_input.props(search_bar_props) # Customize nicegui input box
            with search_input.add_slot('prepend'):
                ui.icon('eva-search-outline').props('size=30px')

        display_dog()

    @ui.page("/search")
    async def search_page(query: str = None, sex: str = "Any", breed: str = None, min_age: int = 1, max_age: int = 30):
        ui.add_head_html(head_html)

        # Results container
        results_container = ui.row().classes("w-full flex-wrap justify-center")

        # Search bar and filters
        with ui.row().classes("justify-center items-center w-full text-center gap-4"):
            search_input = ui.input(value=query or '', placeholder='Search for Pets...').classes('search-input')
            sex_select = ui.select(options=['Any', 'Male', 'Female', 'Unknown'], value=sex).classes('w-40')
            breed_input = ui.input(value=breed or '', placeholder='Breed').classes('w-40')
            min_age_input = ui.input(value=str(min_age) if min_age else 1, placeholder='Min Age').classes('w-20')
            max_age_input = ui.input(value=str(max_age) if max_age else 30, placeholder='Max Age').classes('w-20')

            search_input.on('keydown.enter', lambda: ui.navigate.to(
                f"/search?query={search_input.value}"
                f"&sex={sex_select.value}"
                f"&breed={breed_input.value}"
                f"&min_age={min_age_input.value if min_age_input.value.isdigit() else 1}"
                f"&max_age={max_age_input.value if max_age_input.value.isdigit() else 30}"
            ))

        try:
            # Directly call search_pets with all filters (now properly awaited)
            from backend.api_routes import search_pets
            pets = await search_pets(  # Add await here
                query=query,
                sex=sex_select.value if sex_select.value != 'Any' else 'Any',
                breed=breed_input.value or None,
                min_age=int(min_age_input.value) if min_age_input.value else 1,
                max_age=int(max_age_input.value) if max_age_input.value else 30
            )

            # Clear previous results
            results_container.clear()
            with results_container:
                if not pets:
                    ui.label("No pets found").classes("text-xl")
                else:
                    # Display results in cards
                    for pet in pets:
                        with ui.card().classes("w-64 m-4"):
                            if pet['image_url']:
                                ui.image(pet['image_url']).classes("w-64 h-64 object-cover")
                            with ui.card_section():
                                ui.label(pet['name']).classes("text-xl font-bold")
                                ui.label(f"Breed: {pet['breed'] or 'Unknown'}")
                                ui.label(f"Age: {pet['age'] or '?'}")
                                ui.label(f"Sex: {pet['sex'] or 'Unknown'}")
                                ui.label(f"Location: {pet['location']}")

        except Exception as e:
            with results_container:
                ui.label(f"Error: {str(e)}").classes("text-red-500 text-xl")
