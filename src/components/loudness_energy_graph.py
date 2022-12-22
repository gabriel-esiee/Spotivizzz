from dash import html, dcc
import plotly.express as px
from ..utils import api

df = api.fake_loudness_by_energy()
fig = px.scatter(df, x="Volume", y="Energie",
                 title="Correlation entre volume et energie")

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
