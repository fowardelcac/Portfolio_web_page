import reflex as rx
from links import Links
from styles.styles import format_page


@rx.page(
    route="/wine/",
)
def wine_page() -> rx.Component:
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading("Streamlit Dashboard", size="8"),
                rx.markdown(
                    """
                    This project comes from one of my college subjects. The aim was to build a visualization or dashboard where I could summarize the dataset and present it in an easy-to-understand format, making it easier to analyze and interpret the data. In this case, the dataset contained wine reviews, which included information about wines reviewed by sommeliers. Among the columns, you can find data on wine geography, sommelier information, wine descriptions, prices, and ratings.

                    First, I had to clean and process the data. I organized it by continents, removed duplicates, and imputed missing numeric values. I also performed sentiment analysis on the wine descriptions to classify them as positive, negative, or neutral, among other things.
                    Next, I divided the analysis into three segments:
                    - Geographic Analysis: I analyzed the reviews based on geographic data, such as continent of production, and examined metrics like average price by country.
                    - Winery Analysis: I focused on basic data about the producers, such as total production and prices.
                    - Price Analysis: I wanted to verify the following hypothesis: "Older wines are better, and therefore should be more expensive." In this dataset, however, this assumption was not accurate. I first conducted a correlation analysis, which showed no relationship between wine age and price. Then, I created a graphic comparing price, age, and ratings, which further confirmed the lack of correlation
                """
                ),
                rx.hstack(
                    rx.text(rx.text.strong("Repository: ")),
                    rx.link(
                        rx.icon("github"),
                        href=Links.Wine.value,
                        is_external=True,
                        padding_top="5px",
                    ),
                    align="start",
                ),
                rx.text("# If you don't want to download the entire project, I’ve added a preview video."),
                rx.video(
                    url="/wine_record.mp4",
                    width="800px",
                    height="auto",
                ),
                **format_page
            ),
        ),
    )
