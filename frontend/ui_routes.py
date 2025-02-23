from unittest import result

from fastapi import FastAPI
from nicegui import ui

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
        ui.label("Welcome to PetSavior!").classes("w-full text-center").style("font-size: 100px; font-family: 'Calibre', serif; font-weight: bold; color: #F2BFA4")
        with ui.element('div').classes('search-container'):
            ui.html('<i class="ti-search search-icon"></i>')
            search_input = ui.input(placeholder='')
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