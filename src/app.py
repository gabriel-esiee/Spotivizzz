from dash import Dash, html
from .components import navbar, footer
from .pages import create_home

def app_layout(app):
    return html.Div(
        [
            navbar,
            create_home(app),
            footer
        ]
    )