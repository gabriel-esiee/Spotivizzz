from dash import html, dcc
import plotly.express as px
from ..utils import api

df = api.fake_bars_values()
fig = px.bar(df, x="Pays", y="Popularité", color="Pays", title="Popularité des morceaux selon le pays")

simple_graph = html.Div(
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
