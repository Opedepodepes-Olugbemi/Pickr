from rxconfig import config

import reflex as rx

def index() -> rx.Component:
    return rx.container(
        rx.box(
            "Pickr App",
            #the users question will be on the right
            text_align="right",
        ),
        rx.box(
            "Homefeed a place where you see all accessed photos",
            #the users question will be on the left
            text_align="left",
        ),
    )

#Add state and page to the app
app = rx.App()
app.add_page(index)
app.compile()