# bpm_by_contry_graph.py est responsable de la construction
# du graphique à points représentant le bpm moyen en fonction
# du pays.

from dash import html, dcc
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.fake_bpm_by_country()
fig = px.scatter(
    df,
    x="Pays",
    y="BPM",
    color="Pays",
    title="BPM moyen selon le pays",
    labels={
        "Pays": "Pays",
        "BPM":  "BPM moyen"
    }
)

# Construction des éléments HTML.
bpm_by_contry_graph = html.Div(
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
