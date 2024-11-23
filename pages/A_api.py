import reflex as rx
from links import Links
from styles.styles import format_page


@rx.page(
    route="/fastapi/",
)
def api_page() -> rx.Component:
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading("Machine Learning FastApi", size="8"),
                rx.markdown(
                    """
                    Machine Learning is a vast field of study, but anyone with a basic understanding of statistics and mathematics can grasp the theory. Let’s imagine this person is called Juan Cruz. Juan Cruz owns a shop and wants to use machine learning models to improve business sales and efficiency. However, the problem is that Juan doesn’t know how to code. While he understands the theory, he would need to hire a developer or data scientist to achieve his goal.

                    With this in mind, I’ve come up with the idea of developing a web app where users can easily build machine learning models. Once they create their models, they will be able to download them or use them directly within the web app. This concept is the foundation of my project.

                    So far, I’ve developed an API using FastAPI. This API allows users to train a Random Forest Regressor model. It also enables dataset splitting, training, and making predictions. This project will serve as the basic framework I can build upon to expand my app and turn it into a fully functional tool.
                                    """
                ),
                rx.hstack(
                    rx.text(rx.text.strong("Repository: ")),
                    rx.link(
                        rx.icon("github"),
                        href=Links.Api.value,
                        is_external=True,
                        padding_top="5px",
                    ),
                    align="start",
                ),
                **format_page,
            ),
        ),
    )
