from dash import Dash, html
from .components import navbar, footer
from .pages import home

def app_layout():
    return html.Div(
        [
            navbar,
            home,
            footer
        ]
    )