from flet import *


def button_hovered(e):
    e.control.bgcolor = Colors.GREY_600 if e.data == "true" else Colors.TRANSPARENT
    e.control.update()


class StartButton(FilledButton):
    def __init__(self):
        super().__init__()
        self.left = 5
        self.bottom = 10
        self.content = Column(
            [
                Icon(name=Icons.COLORIZE_ROUNDED, size=22),
                Text("Start", size=12, color=Colors.WHITE, weight=FontWeight.W_100)
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.SPACE_EVENLY,
            spacing=0
        )
        self.tooltip = Tooltip(message="Rozpocznij detekcję koloru", bgcolor=Colors.BLACK, border_radius=15,
                               wait_duration=Duration(milliseconds=500))
        self.bgcolor = Colors.TRANSPARENT
        self.style = ButtonStyle(
            padding=25,
            shape=CircleBorder()
        )
        self.on_hover = button_hovered
