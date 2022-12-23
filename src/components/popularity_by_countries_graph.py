# popularity_by_countries_graph.py est responsable de la construction
# du graphique à barres représentant la popularité moyenne des morceaux
# pour chacuns des pays.

from dash import html, dcc
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.fake_popularity_by_countries()
fig = px.bar(
    df,
    x="countries",
    y="popularity",
    color="countries",
    title="Popularité moyenne des morceaux du Top 50 selon le pays",
    labels={
        "countries":  "Pays",
        "popularity": "Popularité moyenne"
    }
)

# Construction des éléments HTML.
popularity_by_countries_graph = html.Div(
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
