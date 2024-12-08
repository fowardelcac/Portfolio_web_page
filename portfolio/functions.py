import reflex as rx
from links import Links


def profile_icons() -> rx.Component:
    return rx.container(
        rx.center(
            rx.hstack(
                rx.link(
                    rx.icon("linkedin"), href=Links.Linkedin.value, is_external=True
                ),
                rx.link(rx.icon("github"), href=Links.Github.value, is_external=True),
                rx.link(
                    rx.icon("file-text"),
                    href=Links.Cv.value,
                    is_external=True,
                ),
                rx.link(
                    rx.icon(
                        "mail",
                        on_click=[
                            rx.set_clipboard("juansaldano01@gmail.com"),
                            rx.toast("Gmail copied!"),
                        ],
                    ),
                ),
            ),
            align="center",
        ),
        width="100%",
    )


def title() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Jr Data Scientist and Python Dev", size="8", align="center", width="100%"
        ),
        rx.text(
            "Welcome to my portfolio! I'm Juan Cruz from Argentina. I'm Jr Data scientist and Python dev.",
            align="center",
            width="100%",
        ),
        profile_icons(),
    )


def about_me() -> rx.Component:
    return rx.section(
        rx.center(rx.heading("About me")),
        rx.markdown(
            """
                Hi! I'm Juan Cruz from Argentina. I’m a Junior Data Scientist, and I know to code in Python. Currently, I’m in my final year of college at Siglo 21 University, where I’m about to graduate as a Data Scientist. I’m passionate about coding, whether it’s for data analysis, automating tasks, web scraping, or building applications, both desktop and web-based.

                Regarding data science, I have experience in all stages of the data lifecycle. I can collect data using web scraping tools like Scrapy, BeautifulSoup, and Selenium, and then process and analyze it using Python libraries such as Pandas. I also enjoy creating clear, meaningful data visualizations and building machine learning models with Scikit-learn.

                My first job was at Latam Connect, where I worked on data extraction and processing. I also automated tasks by integrating Python with Google Sheets, which helped me develop strong skills in data management and creating efficient solutions.

                Currently, I’m looking for new opportunities where I can continue to grow and apply my skills to exciting projects. I’m particularly interested in backend positions and data-related roles such as Data Scientist or Data Analyst.
            """,
            padding_top="1px",
            margin="1em",
        ),
    )


def experience() -> rx.Component:
    return (
        rx.section(
            rx.center(rx.heading("Experience")),
            rx.markdown(
                f"""- <a href="{Links.Latam.value}" target="_blank" rel="noopener noreferrer"><strong>Latam Connect</strong></a> | Data analyst.     January 2024 - April 2024""",
                padding_top="15px",
            ),
            rx.text(
                """  I worked as an intern at a successful Spanish company called Latam Connect. My role was as a Data Analyst, and I was responsible for extracting data from the web and delivering it in Excel format. At that time, we used Google Sheets a lot, and part of my job was to manually add information to enrich the data. This task could take hours, especially with large amounts of data.
                        To solve this, I found a way to integrate Python with Google Sheets. I created a script that performed Google searches based on queries made from other columns in the sheet. This automation saved us a lot of time and made the process much more efficient.""",
            ),
            margin="1em",
        ),
    )


def projects() -> rx.Component:
    return rx.flex(
        rx.center(rx.heading("Projects"), padding_bottom="15px"),
        rx.section(
            rx.box(
                rx.link(
                    rx.heading("Machin Learning API"),
                    href="/fastapi/",
                    is_external=True,
                ),
                rx.text(
                    "Using an API developed with FastAPI, users can train a Random Forest Regressor model, split datasets, and make predictions. ",
                    margin_top="0.5em",
                ),
                padding="2em",
                border_width="1px",
            ),
            padding_top="1px",
        ),
        rx.section(
            rx.box(
                rx.link(
                    rx.heading("Wine Visualization"),
                    href="/wine/",
                    is_external=True,
                ),
                rx.text(
                    "This project involves creating a dashboard to visualize and analyze a wine review dataset. ",
                    margin_top="0.5em",
                ),
                padding="2em",
                border_width="1px",
            ),
            padding_top="1px",
        ),
        rx.section(
            rx.box(
                rx.link(
                    rx.heading("Crud App"),
                    href="/crud/",
                    is_external=True,
                ),
                rx.text(
                    "This is a CRUD project developed using Python and MySQL. ",
                    margin_top="0.5em",
                ),
                padding="2em",
                border_width="1px",
            ),
            padding_top="1px",
        ),
        width="100%",
        # flex_direction=["column", "row"],
        direction="column",
    )
