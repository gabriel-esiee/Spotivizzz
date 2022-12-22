from dash import html, dcc
import plotly.express as px
from ..utils import api

df = api.fake_line_values()
fig = px.line(df, x="year", y="lifeExp")

line_graph = html.Div(
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
