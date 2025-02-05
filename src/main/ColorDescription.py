from flet import *


def __get_text__(text) -> Text:
    return Text(text, size=12, weight=FontWeight.W_100, color=Colors.WHITE, text_align=TextAlign.JUSTIFY)


class ColorDescription(Container):
    def __init__(self):
        super().__init__()
        self.content = __get_text__("Po instrukcję naciśnij << ? >> w prawym górnym rogu")
        self.width = 180
        self.padding = padding.symmetric(horizontal=15)

    def update_description(self, color_name):
        self.content = __get_text__(color_name)
        self.update()
