from flet import *


class Card(Container):
    def __init__(self):
        super().__init__()
        self.width = 180
        self.height = 360
        self.gradient = LinearGradient(colors=["#202b2b2b",
                                               "#2b2b2b",
                                               "#2b2b2b",
                                               "#902b2b2b"
                                               ],
                                       begin=alignment.top_center,
                                       end=alignment.bottom_center,
                                       stops=[0.0, 0.4, 0.7, 1.0])
        self.border = Border(
            top=BorderSide(
                width=1,
                color=Colors.GREY,
            ),
            left=BorderSide(
                width=1,
                color=Colors.GREY,
            ),
        )
        self.border_radius = 30
