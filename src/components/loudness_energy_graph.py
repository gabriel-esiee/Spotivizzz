# loudness_energy_graph.py est responsable de la construction
# du graphique à points représentant la correlation entre le
# volume et l'energie des morceaux.

from dash import html, dcc
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.fake_loudness_by_energy()
fig = px.scatter(
    df,
    x="loudness",
    y="energy",
    title="Track Loudness and Energy Correlation",
    labels={
        "loudness": "Loudness (dB)",
        "energy":   "Energy"
    }
)

# Construction des éléments HTML.
loudness_energy_graph = html.Div(
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
