# genre_comparing_graph.py est responsable de la construction
# du graphique comparant deux genres entre eux.
import random
import pandas as pd
from dash import html, dcc, Input, Output
import plotly.express as px
from ..utils import api


# Récupération des données.
# Les données sont déja traités dans utils/api.py.
genres_df = api.dual_genre_comparaison()
#genre_data = genres_df[""]

genre = 'pop'
genre_analysis_values = ['energy',
                        'speechiness',
                        'acousticness', 
                        'instrumentalness', 
                        'liveness', 
                        'valence']
values = genres_df[genres_df['genre'] == genre][genre_analysis_values].values.tolist()


df = pd.DataFrame(dict(
    r=values[0],
    theta=genre_analysis_values,))
fig = fig = px.line_polar(
            df,
            r='r',
            theta='theta',
            line_close=True,
            range_r=[0,1,],
            color_discrete_sequence= px.colors.sequential.Bluered
        )
fig.update_traces(fill='toself')

# Get Genres List to update in the dropdowns
genres_list = api.dual_genre_comparaison()["genre"].to_list()

genre_1_options=[]
for item in genres_list:
    genre_dict= {'label': item,
                'value': 'genre-1-'+item}
    genre_1_options.append(genre_dict)

genre_2_options=[]
for item in genres_list:
    genre_dict= {'label': item,
                'value': 'genre-2-'+item}
    genre_2_options.append(genre_dict)

def create_dual_comparaison(app):

    # Callback lorsque le select change de valeur.
    @app.callback(
        Output(component_id='genre-1-graph', component_property='figure'),
        Input(component_id='genre-1-select', component_property='value'),
    )

    @app.callback(
        Output(component_id='genre-2-graph', component_property='figure'),
        Input(component_id='genre-2-select', component_property='value')
    )

    def update_figs(value):
        global fig
        df = api.dual_genre_comparaison()
        fig.update_layout()
        if (isinstance(value, str)):
            if(value.startswith('genre-1')):
                current_genre = value.rsplit('-', 1)[1]
                graph_color = px.colors.sequential.Bluered_r
            if(value.startswith('genre-2')):
                current_genre = value.rsplit('-', 1)[1]
                graph_color = px.colors.sequential.Bluered
        else:
            graph_color = px.colors.sequential.Bluered
            current_genre = 'pop'
        
        genre = current_genre
        genre_analysis_values = ['energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']
        values = genres_df[genres_df['genre'] == genre][genre_analysis_values].values.tolist()

        df = pd.DataFrame(dict(
            r=values[0],
            theta=genre_analysis_values,))
        fig = px.line_polar(
            df,
            r='r',
            theta='theta',
            line_close=True,
            range_r=[0,1,],
            color_discrete_sequence= graph_color
        )
        fig.update_traces(fill='toself')

        return fig
    # Fin callback

    # Construction des éléments HTML.
    return html.Div(
        className="graph-container comparing",
        children=[
            html.P(
                children="Genres Comparator",
                className="title"
            ),
            html.Div([
                html.P('Genre 1:'),
                html.Div([
                    dcc.Dropdown(
                        options=genre_1_options,
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
                        style={'height': '100%', 'padding-top': '20px'},
                        id='genre-1-graph'
                    )
                ])  
            ],
            className="genre-1"
            ),

            html.Div([
                html.P('Genre 2:'),
                html.Div([
                    dcc.Dropdown(
                        options=genre_2_options,
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
                        style={'height': '100%', 'padding-top': '20px'},
                        id='genre-2-graph'
                    )
                ])
            ],
            className="genre-2"
            ),
        ]
    )