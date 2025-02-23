from unittest import result

from fastapi import FastAPI
from nicegui import ui

def add_ui_routes():
    @ui.page("/")
    def main_page():
        ui.add_head_html('''
                    <style>
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
                ''')
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

        shelter_name = ['shelter1', 'shelter2', 'shelter3']
        ui.select(label='Pick your Shelter: ', options=shelter_name, with_input=True,on_change=lambda e: ui.notify(e.value)).classes('w-40')

        states = [
            'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana',
            'Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada',
            'New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina',
            'South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming',
        ]
        ui.select(label='Pick your State: ', options=states, with_input=True,on_change=lambda e: ui.notify(e.value)).classes('w-40')

        gender = ['Male', 'Female']
        ui.select(label='Gender: ', options=gender, with_input=True, on_change=lambda e: ui.notify(e.value)).classes('w-40')

        animal = ['Adoptable Dogs', 'Adoptable Cats', 'Adoptable Small Animals']
        ui.select(label='Animals: ', options=animal, with_input=True, on_change=lambda e: ui.notify(e.value)).classes('w-40')

        allergic = ['Yes', 'No']
        ui.select(label='Allergies? ', options=allergic, with_input=True, on_change=lambda e: ui.notify(e.value)).classes('w-40')

        with ui.dropdown_button('Dogs & Puppies', icon='settings', split=True):
            with ui.row().classes('p-4 items-center'):
                ui.item('Item 1', on_click=lambda: ui.notify('You clicked item 1'))
                ui.item('Item 2', on_click=lambda: ui.notify('You clicked item 2'))


