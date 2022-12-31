# popularity_by_countries_graph.py est responsable de la construction
# du graphique à barres représentant la popularité moyenne des morceaux
# pour chacuns des pays.

from dash import html, dcc
import plotly.express as px
from ..utils import api

long_color_sequence = [ "#6a45c2",
                        "#f33b5d",
                        "#3c5da0",
                        "#f6a946",
                        "#8c0250",
                        "#88a58b",
                        "#1e5c4a",
                        "#dbaea7",
                        "#83acf3",
                        "#6e4943",
                        "#2eceb7",
                        "#8d12dc",
                        "#57e24c",
                        "#1c9820",
                        "#c582ef",
                        "#fd3fbe",
                        "#b3d342",
                        "#748d13",
                        "#957206",
                        "#fe5900",
                        "#5f86b7",
                        "#fe5900",
                        "#e09f2b",
                        "#9a6d56",
                        "#8270f6",
                        "#d945c2",
                        "#35e0a9",
                        "#e81659",
                        "#266d01",
                        "#69306e",
                        "#79be02",
                        "#e4b8ec",
                        "#154e56",
                        "#2524f9",
                        "#a1c293",
                        "#b4464c",
                        "#24e53d",
                        "#9ecbf4",
                        "#d0cc36",
                        "#1c35b7",
                        "#68affc",
                        "#b687f8",
                        "#5252b9",
                        "#154975",
                        "#f68d92",
                        "#518413",
                        "#784533",
                        "#5735f6",
                        "#cec6b4",
                        "#75db96",
                        "#75887b",
                        "#dac925",
                        "#f43a54",
                        "#bf11af",
                        "#df8a1d",
                        "#54d7eb",
                        "#fe74fe",
                        "#8a1341",
                        "#4ed31b",
                        "#05957a"]

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.fake_popularity_by_countries()
fig = px.bar(
    df,
    x="genre",
    y="popularity_by_population",
    color="countries",
    title="Genres Popularity among the World",
    labels={
        "genre":  "Genres",
        "popularity_by_population": "Popularity Index",
        "countries": "Country"
    },
    color_discrete_sequence= long_color_sequence
)

fig.update_layout(xaxis={'categoryorder':'total descending'})

# Construction des éléments HTML.
popularity_by_countries_graph = html.Div(
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
