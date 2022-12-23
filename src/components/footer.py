# footer.py est responsable de la création du footer
# qui comprend un container et un texte de crédits.

from dash import html

# Construction des éléments HTML.
footer = html.Div(
    className="footer",
    children=[
        html.P(
            children="Développé par Clément ZELTER et Gabriel ROULEAU."
        )
    ]
)