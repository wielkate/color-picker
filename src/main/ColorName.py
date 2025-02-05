from flet import *


def __get_text__(text) -> Text:
    return Text(value=text, size=16, weight=FontWeight.BOLD, color=Colors.WHITE, text_align=TextAlign.CENTER)


class ColorName(Container):
    def __init__(self):
        super().__init__()
        self.content = __get_text__("Detekcja koloru")
        self.width = 180
        self.padding = padding.symmetric(horizontal=20)

    def update_name(self, color_name):
        self.content= __get_text__(color_name)
        self.update()