# app.py est responsable de la création du layout général de l'application
# et appel la création de la navbar, la page d'accueil et du footer.

from dash import Dash, html
from .components import navbar, footer
from .pages import create_home

# Construction des élément HTML.
def app_layout(app):
    return html.Div(
        [
            navbar,
            create_home(app),
            footer
        ]
    )