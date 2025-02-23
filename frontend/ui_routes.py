from unittest import result
from fastapi import FastAPI, requests
from nicegui import ui
import asyncio
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Animals
from backend.api_routes import search_pets

host_url = "http://127.0.0.1:8000/"

head_html = '''
            <style>
                .search-input { border-radius: 25px; padding: 10px; border: 1px solid #008080; font-size: 16px; width: 650px; }
            </style>
            <link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />
            <link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />
        '''

def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.add_head_html('''<style>.search-container {
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
                        }</style>''')
        ui.query('body').style('background-color: #F5E7DE')
        ui.add_head_html('<link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />')
        ui.label("Welcome to Pet Savior!").classes("w-full text-center").style("font-size: 100px; font-family: 'Calibre', serif; font-weight: bold; color: #F2BFA4")

        # Center search bar
        with ui.element('div').classes('search-container'):
            ui.html('<i class="ti-search search-icon"></i>')
            search_input = ui.input(placeholder='Search for Pets...')
            search_input.on('keydown.enter', lambda: ui.navigate.to(f'/search?query={search_input.value}'))
            search_input.style(
                'border-radius: 25px; '
                'padding: 10px; '
                'border: 1px solid #008080; '
                'font-size: 16px; '
                'width: 650px;'
        )

        states = [
            'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana',
            'Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada',
            'New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina',
            'South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming',
        ]
        state_select = ui.select(label='Pick your State: ', options=states, with_input=True,on_change=lambda e: ui.notify(e.value)).classes('w-40')

        shelter_name = ['shelter1', 'shelter2', 'shelter3']
        shelter_select = ui.select(label='Pick your Shelter: ', options=shelter_name, with_input=True,
                  on_change=lambda e: ui.notify(e.value)).classes('w-40')

        gender = ['Male', 'Female']
        gender_select = ui.select(label='Gender: ', options=gender, with_input=True, on_change=lambda e: ui.notify(e.value)).classes('w-40')

        animal = ['Adoptable Dogs', 'Adoptable Cats', 'Adoptable Small Animals']
        animal_select = ui.select(label='Animals: ', options=animal, with_input=True, on_change=lambda e: ui.notify(e.value)).classes('w-40')

        allergic = ['Yes', 'No']
        allergic_select = ui.select(label='Allergies? ', options=allergic, with_input=True, on_change=lambda e: ui.notify(e.value)).classes('w-40')

        preferred_age = ["None", "0-1 years", "2-5 years", "6-10 years old", "11+ years old"]
        preferred_age_select = ui.select(label='Preferred Age: ', options=preferred_age, with_input=True,on_change=lambda e: ui.notify(e.value)).classes('w-40')

        shelter_select.style('position: absolute; '
                             'left: 30%; '
                             'transform: translateX(-50%); '
                             'top: 370px;')
        state_select.style('position: absolute; '          
                     'left: 50%; '                   
                     'transform: translateX(-50%); ' 
                     'top: 370px;')
        gender_select.style('position: absolute; '          
                     'left: 70%; '                   
                     'transform: translateX(-50%); ' 
                     'top: 370px;')
        animal_select.style('position: absolute; '          
                     'left: 30%; '                   
                     'transform: translateX(-50%); ' 
                     'top: 500px;')
        allergic_select.style('position: absolute; '          
                     'left: 50%; '                   
                     'transform: translateX(-50%); ' 
                     'top: 500px;')
        preferred_age_select.style('position: absolute; '          
                     'left: 70%; '                   
                     'transform: translateX(-50%); ' 
                     'top: 500px;')

        pet_button = ui.button('Click here to find your pet!', on_click=lambda: ui.notify('Unavailable'))
        pet_button.style('position: absolute; '
                     'left: 50%; '
                         'transform: translateX(-50%); '
                         'top: 720px;')


    # @ui.page("/search")
    # async def search_page(query: str = None):
    #
    #     ui.add_head_html(head_html)
    #
    #
    #     pets = await search_pets(query, sex)
    #     if pets:
    #         ui.label(pets)
    #
    #     # On any change it should search database again?
    #     with ui.row().classes("justify-center items-center w-full text-center"):
    #         if query is not None:
    #             search_input = ui.input(value=query, placeholder='Search for Pets...')
    #         else:
    #             search_input = ui.input(placeholder='Search for Pets...')
    #
    #         # On enter, search again
    #         search_input.classes('search-input')
    #         search_input.on('keydown.enter', lambda: ui.navigate.to(f'/search?query={search_input.value}'))
    #         # Icon
    #         ui.icon('eva-search-outline').classes('text-5xl').style('margin-right: 10px')


    @ui.page("/search")
    async def search_page(query: str = None, sex: str = None, breed: str = None, min_age: int = 0, max_age: int = 30):
        ui.add_head_html(head_html)

        # Results container
        results_container = ui.row().classes("w-full flex-wrap justify-center")

        # Search bar and filters
        with ui.row().classes("justify-center items-center w-full text-center gap-4"):
            search_input = ui.input(value=query or '', placeholder='Search for Pets...').classes('search-input')
            sex_select = ui.select(options=['Any', 'Male', 'Female', 'Unknown'], value=sex).classes('w-40')
            breed_input = ui.input(value=breed or '', placeholder='Breed').classes('w-40')
            min_age_input = ui.input(value=str(min_age) if min_age else 0, placeholder='Min Age').classes('w-20')
            max_age_input = ui.input(value=str(max_age) if max_age else 30, placeholder='Max Age').classes('w-20')

            search_input.on('keydown.enter', lambda: ui.navigate.to(
                f"/search?query={search_input.value}"
                f"&sex={sex_select.value}"
                f"&breed={breed_input.value}"
                f"&min_age={min_age_input.value if min_age_input.value.isdigit() else 0}"
                f"&max_age={max_age_input.value if max_age_input.value.isdigit() else 30}"
            ))


        try:
            # Directly call search_pets with all filters (now properly awaited)
            from backend.api_routes import search_pets
            pets = await search_pets(  # Add await here
                query=query,
                sex=sex_select.value if sex_select.value != 'Any' else None,
                breed=breed_input.value or None,
                min_age=int(min_age_input.value) if min_age_input.value else None,
                max_age=int(max_age_input.value) if max_age_input.value else None
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