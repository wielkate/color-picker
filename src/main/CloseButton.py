from flet import *


def close_button_clicked(page):
    page.window.close()


class CloseButton(IconButton):
    def __init__(self, page):
        super().__init__()
        self.icon = Icons.CLOSE_ROUNDED
        self.icon_color = Colors.WHITE
        self.icon_size = 14
        self.top = 10
        self.right = 10
        self.tooltip = Tooltip(message="Zamknij aplikację", bgcolor=Colors.BLACK, border_radius=15,
                               wait_duration=Duration(milliseconds=500))
        self.on_click = lambda e: close_button_clicked(page)
        self.hover_color = Colors.GREY_600
