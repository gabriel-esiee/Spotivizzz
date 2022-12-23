# genre_comparing_graph.py est responsable de la construction
# du graphique comparant deux genres entre eux.

from dash import html, dcc
import plotly.express as px
from ..utils import api

# Construction des éléments HTML.
genre_comparing_graph = html.Div(
    className="graph-container",
    children=[
        html.P(
            children="Graphique de comparaison des genres ici."
        )
    ]
)
