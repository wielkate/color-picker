from flet import *


class Circle(Container):
    def __init__(self):
        super().__init__()
        self.width = 70
        self.height = 70
        self.top = 50
        self.bgcolor = Colors.GREY
        self.border_radius = 360
        self.shadow =BoxShadow(
                0,
                5,
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER
            )

    def update_color(self, color_name):
        self.bgcolor=color_name
        self.update()
