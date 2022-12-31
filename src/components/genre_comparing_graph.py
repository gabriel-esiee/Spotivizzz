# genre_comparing_graph.py est responsable de la construction
# du graphique comparant deux genres entre eux.

from dash import html, dcc
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.fake_duration_by_genre()
fig = px.bar(
    df,
    x="duration",
    y="genre",
    color="genre",
    orientation='h',
    title="Average Track Duration by Genres",
    text= "formated_duration",
    labels={
        "duration": "Average Duration",
        "formated_duration": "Average Duration",
        "genre":    "Genre"
    },
)

fig.update_layout(yaxis={'categoryorder':'total descending'})

# Get Genres List to update in the dropdowns
genres_list = api.dual_genre_comparaison()["genre"].to_list()

genres_options=[]
counter = 0
for item in genres_list:
    genre_dict= {'label': item,
                 'value': counter}
    genres_options.append(genre_dict)
    counter +=1



# Construction des éléments HTML.
genre_comparing_graph = html.Div(
    className="graph-container",
    children=[
        html.P(
            children="Genres Comparing",
            className="title"
        ),
        html.Div([
            html.P('Genre 1:'),
            html.Div([
                dcc.Dropdown(
                    options=genres_options,
                    value=0,
                    id="genre-1-select",
                    className="genre-1-select"
                ),
                dcc.Graph(
                    figure=fig,
                    className="fig",
                    config={
                        "displayModeBar": False
                    },
                    style={'height': '100%', 'padding-top': '20px'}
                )
            ])  
        ],
        className="genre-1"
        ),

        html.Div([
            html.P('Genre 2:'),
            html.Div([
                dcc.Dropdown(
                    options=genres_options,
                    value=0,
                    id="genre-2-select",
                    className="genre-2-select"
                ),
                dcc.Graph(
                    figure=fig,
                    className="fig",
                    config={
                        "displayModeBar": False
                    },
                    style={'height': '100%', 'padding-top': '20px'}
                )
            ])
        ],
        className="genre-2"
        )
    ]
)
