import csv
import time

from flet import *

from Card import Card
from Circle import Circle
from CloseButton import CloseButton
from ColorData import ColorData
from ColorDescription import ColorDescription
from ColorName import ColorName
from HelpButton import HelpButton
from SavedButton import SavedButton
from StartButton import StartButton


def get_color_data():
    file = open(file='Colors.csv', mode='r', encoding='utf-8')
    return [ColorData(row) for row in csv.reader(file, delimiter=';')]


def setup_page(page):
    window = page.window
    window.height = 360
    window.width = 180
    window.resizable = False
    window.maximizable = False
    window.minimizable = False
    window.always_on_top = True
    window.title_bar_hidden = True
    window.frameless = True

    font = 'Comfortaa'
    page.fonts = {font: '/fonts/Comfortaa.ttf'}
    page.theme = Theme(font_family='Comfortaa',
                       shadow_color=Colors.BLACK,
                       icon_theme=IconTheme(
                           color=Colors.WHITE
                       ),
                       )
    page.padding = 0
    page.spacing = 0

    window.bgcolor = Colors.TRANSPARENT
    page.bgcolor = Colors.TRANSPARENT


def main(page: Page):
    setup_page(page)

    card = Card()
    circle = Circle()
    color_name = ColorName()
    color_description = ColorDescription()
    start_button = StartButton()
    saved_button = SavedButton()
    close_button = CloseButton(page)
    help_button = HelpButton()

    start_page = Stack(
        controls=[
            card,
            circle,
            Column(
                controls=[color_name,
                          color_description],
                top=135,
                spacing=10,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            close_button,
            help_button,
            start_button,
            saved_button,
        ],
        alignment=Alignment(0, 0)
    )

    page.add(WindowDragArea(content=start_page,
                            maximizable=False))

    for i in get_color_data():
        color_name.update_name(i.name)
        color_description.update_description(i.description)
        circle.update_color(i.hex)
        time.sleep(1)


app(target=main, assets_dir="assets")
