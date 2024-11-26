import reflex as rx
from links import Links
from styles.styles import format_page


@rx.page(
    route="/crud/",
)
def crud_page() -> rx.Component:
    return rx.box(
        rx.container(
            rx.heading(
                "Crud Aplication",
                size="8",
                align="center",
                width="100%",
            ),
            rx.markdown(
                """
                    This is a CRUD project, and it can be defined as follows: CRUD is an acronym for Create, Read, Update, and Delete. Each of these performs a different operation, but they all aim to track and manage data from a database. I developed this CRUD project using Python code and MySQL as the database. I used a library called SQLModel, which is similar to SQLAlchemy, but the key difference is its integration with Pydantic.

                    In my case, I chose this library because it is easier to integrate with FastAPI, as they share the same creator. This CRUD app is designed for an ice cream shop, allowing the user to insert data for products and weekly purchases. It is a very simple database that contains three tables:
                    - Product: Contains all the possible products.
                    - Purchase: Records weekly purchases of raw materials.
                    - Receipt: Contains the receipt data. I created this table to minimize redundancy in the second table. Without it, if a weekly purchase includes 15 different ice cream flavors on the same receipt, the receipt data would be repeated 15 times.
                    
                    My Python code is organized into classes. Initially, I planned to create a class for each table, but then I realized that this would result in repetitive code (each class would have the same CRUD operations). So, I changed my approach. I developed a class for each CRUD operation, so each class is responsible for just one CRUD action. To test the application, I included tests using pytest, which test each function.
                    """,
                margin="1em",
            ),
            rx.text(
                rx.text.strong("Entity Relationship Diagram:"),
                margin="1em",
            ),
            rx.image(
                "/ERD.png",
                width="autox",
                height="auto",
            ),
            rx.center(
                rx.hstack(
                    rx.text(rx.text.strong("Repository: ")),
                    rx.link(
                        rx.icon("github"),
                        href=Links.Crud.value,
                        is_external=True,
                        padding_top="5px",
                    ),
                    align="center",
                    margin="1em",
                ),
            ),
        ),
    )
