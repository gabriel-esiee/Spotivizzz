from dash import html, dcc
import plotly.express as px
from ..utils import api

df = api.fake_duration_by_genre()
fig = px.bar(df, x="Durée", y="Genre", color="Genre", orientation='h', title="Durée des morceaux selon le genre")

horizontal_bar_graph = html.Div(
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
