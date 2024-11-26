import reflex as rx
from pages.A_api import api_page
from pages.B_wine import wine_page
from pages.C_crud import crud_page
from .functions import *


def join_elemnts() -> rx.Component:
    return (title(), about_me(), experience(), projects())


def index() -> rx.Component:
    return (
        rx.box(
            rx.container(
                rx.desktop_only(
                    join_elemnts(),
                ),
                rx.mobile_only(
                    join_elemnts(),
                ),
            ),
            width="100%",
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)
app.add_page(index)
app.add_page(api_page)
app.add_page(wine_page)
app.add_page(crud_page)
