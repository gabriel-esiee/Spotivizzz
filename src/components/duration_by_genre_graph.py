# duration_by_genre_graph.py est responsable de la construction
# du graphique à barres horizontales représentant la durée moyenne
# des morceaux pour chaque pays.

from dash import html, dcc
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.fake_duration_by_genre()
fig = px.bar(
    df,
    x="duration",
    y="genre",
    color="genre",
    orientation='h',
    title="Durée des morceaux selon le genre",
    labels={
        "duration": "Durée moyenne",
        "genre":    "Genre"
    }
)

# Construction des éléments HTML.
duration_by_genre_graph = html.Div(
    className="graph-container",
    children=[
        dcc.Graph(
            figure=fig,
            className="fig",
            config={
                "displayModeBar": False
            },
            style={'height': '100%'}
        )
    ]
)
