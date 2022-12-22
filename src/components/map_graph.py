from dash import html, dcc
import plotly.express as px
from ..utils import api

df = api.fake_map_values()
fig = px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop", projection="natural earth")

map_graph = html.Div(
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
