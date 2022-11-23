from dash import Dash, html
from .components import navbar, footer

def app_layout():
    return html.Div(
        [
            navbar,
            html.H1(children='Hello Dash'),
            footer
        ]
    )