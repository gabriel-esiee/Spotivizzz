from dash import html, dcc
import plotly.express as px
from ..utils import api

df = api.fake_bpm_by_country()
fig = px.scatter(df, x="Pays", y="BPM", color="Pays",
                 title="BPM moyen selon le pays",
                 labels={"salary":"BPM moyen"} # customize axis label
                )

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
