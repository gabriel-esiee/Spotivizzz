from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
from ..utils import api

fake_values = api.fake_table_values()
fig = go.Figure(data=[go.Table(header=fake_values[0], cells=fake_values[1])])

table_graph = html.Div(
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
