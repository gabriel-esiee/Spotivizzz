# navbar.py est responsable de la création de la navbar
# qui comprend l'image d'entête de la page  d'accueil.

from dash import html

# Construction des éléments HTML.
navbar = html.Div(
    className="navbar",
    children=[
        html.Img(
            src="/assets/images/spotivizzz_banner.png"
        )
    ]
)