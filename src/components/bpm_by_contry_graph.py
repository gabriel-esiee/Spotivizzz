# bpm_by_contry_graph.py est responsable de la construction
# du graphique à points représentant le bpm moyen en fonction
# du pays.

from dash import html, dcc
import plotly.express as px
import statsmodels.api as sm
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.bpm_by_country()
fig = px.scatter(
    df,
    x="duration",
    y="bpm",
    color="continents_names",
    title="BPM and Duration Correlation on Nationals Top 50s",
    hover_name="country",
    hover_data=["formated_duration"],
    labels={
        "continents_names": "Continent",
        "country": "Countries",
        "bpm":  "Average BPM",
        "duration": "Average Duration",
        "formated_duration": "Average Duration",
        "population": "Population",
    },
    size="population",
    size_max=50
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
