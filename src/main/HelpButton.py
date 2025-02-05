from flet import *

class HelpButton(IconButton):
    def __init__(self):
        super().__init__()
        self.icon = Icons.QUESTION_MARK_ROUNDED
        self.icon_color = Colors.WHITE
        self.icon_size = 12
        self.top = 7
        self.right = 37
        self.tooltip = Tooltip(message="Naciśnij << Start >> i wybierz kolor z dowolnego miejsca na ekranie. Kliknięcie myszką zapisze wybrany kolor", bgcolor=Colors.BLACK, border_radius=15,
                               wait_duration=Duration(milliseconds=500))
        self.hover_color = Colors.GREY_600
