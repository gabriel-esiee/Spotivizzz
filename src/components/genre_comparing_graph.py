# genre_comparing_graph.py est responsable de la construction
# du graphique comparant deux genres entre eux.

import pandas as pd
from dash import html, dcc
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
genres_df = api.dual_genre_comparaison()
#genre_data = genres_df[""]

genre = 'pop'
genre_analysis_values = ['energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']
values = genres_df[genres_df['genre'] == genre][genre_analysis_values].values.tolist()
print(values[0])

df = pd.DataFrame(dict(
    r=values[0],
    theta=genre_analysis_values,))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')

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
