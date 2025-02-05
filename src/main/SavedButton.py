from flet import *


def button_hovered(e):
    e.control.bgcolor = Colors.GREY_600 if e.data == "true" else Colors.TRANSPARENT
    e.control.update()


class SavedButton(FilledButton):
    def __init__(self):
        super().__init__()
        self.right = -10
        self.bottom = 10
        self.content = Column(
            [
                Icon(name=Icons.BOOKMARK_BORDER_ROUNDED, size=24),
                Text("Zapisane", size=12, color=Colors.WHITE, weight=FontWeight.W_100)
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.SPACE_EVENLY,
            spacing=0
        )
        self.tooltip = Tooltip(message="Przejdź do zapisanych kolorów", bgcolor=Colors.BLACK, border_radius=15,
                               wait_duration=Duration(milliseconds=500))
        self.bgcolor = Colors.TRANSPARENT
        self.style = ButtonStyle(
            padding=26,
            shape=CircleBorder()
        )
        self.on_hover = button_hovered
