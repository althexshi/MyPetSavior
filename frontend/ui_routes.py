from unittest import result

from fastapi import FastAPI
from nicegui import ui
import asyncio
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Animals
from backend.api_routes import search_pets

host_url = "https://petsavior.onrender.com"

head_html = '''
            <style>
                .search-input { border-radius: 25px; padding: 10px; border: 1px solid #008080; font-size: 16px; width: 650px; }
                .search-container {
                            position: relative;
                            width: 650px;
                            margin: 0 auto;  /* centers the container horizontally */
                            
                        }
                .search-container input {
                            width: 100%;
                            padding-left: 50px;
                        }
                .search-icon {
                            position: absolute;
                            left: 15px;
                            top: 50%;
                            transform: translateY(-50%);
                            font-size: 24px;
                            color: #008080;
                        }
            </style>
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />
            <link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />
        '''


def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.add_head_html(head_html)

        states = [
            'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
            'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
            'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
            'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
            'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
            'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
            'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
            'Wisconsin', 'Wyoming',
        ]

        with ui.dialog() as filter_dialog:
            with ui.card():
                ui.label("Filter Options")
                # filter_dialog.props("max-width=800x")  # Adjust width
                # # filter_dialog.props("style=height:500px;")  # Adjust height

                state_select = ui.select(label='Pick your State: ', options=states, with_input=True,
                                         on_change=lambda e: ui.notify(e.value)).classes('w-40')

                shelter_name = ['shelter1', 'shelter2', 'shelter3']
                shelter_select = ui.select(label='Pick your Shelter: ', options=shelter_name, with_input=True,
                                           on_change=lambda e: ui.notify(e.value)).classes('w-40')
                gender = ['Male', 'Female']
                gender_select = ui.select(label='Gender: ', options=gender, with_input=True,
                                          on_change=lambda e: ui.notify(e.value)).classes('w-40')
                animal = ['Adoptable Dogs', 'Adoptable Cats', 'Adoptable Small Animals']
                animal_select = ui.select(label='Animals: ', options=animal, with_input=True,
                                          on_change=lambda e: ui.notify(e.value)).classes('w-40')
                allergic = ['Yes', 'No']
                allergic_select = ui.select(label='Allergies? ', options=allergic, with_input=True,
                                            on_change=lambda e: ui.notify(e.value)).classes('w-40')
                preferred_age = ["None", "0-1 years", "2-5 years", "6-10 years old", "11+ years old"]
                preferred_age_select = ui.select(label='Preferred Age: ', options=preferred_age, with_input=True,
                                                 on_change=lambda e: ui.notify(e.value)).classes('w-40')

                # Apply button
                with ui.row():
                    ui.button("Apply", on_click=lambda: print("Applied Settings!"))
                    ui.button("Close", on_click=filter_dialog.close)

        ui.query('body').style('background-color: #F5E7DE')
        ui.add_head_html(
            '<link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />')
        ui.label("Welcome to Pet Savior!").classes("w-full text-center").style(
            "font-size: 100px; font-family: 'Calibre', serif; font-weight: bold; color: #F2BFA4")

        # Center search bar
        with ui.element('div').classes('search-container flex items-center gap-2'):
            ui.html('<i class="ti-search search-icon"></i>')
            search_input = ui.input(placeholder='Search for Pets...').classes('search-input')
            search_input.on('keydown.enter', lambda: ui.navigate.to(f'/search?query={search_input.value}'))

        ui.button('filter', icon='eva-funnel-outline', on_click=lambda: filter_dialog.open()).style("margin: 0 auto;")


        src = 'https://lottie.host/0bc74d91-888a-453c-a078-cfefaf784e45/FJLJ2LV1bw.json'
        ui.html(f'<lottie-player src="{src}" loop autoplay />').style("width: 400px; margin: 0 auto; text-align: center; ")



    @ui.page("/search")
    async def search_page(query: str = None):

        ui.add_head_html(head_html)
        pets = await search_pets(query)
        if pets:
            ui.label(pets)

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
