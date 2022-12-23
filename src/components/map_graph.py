# map_graph.py est responsable de la construction de graphique
# de la carte du monde et de la gestions de ses callback (notamment les
# callbacks du select).

from dash import html, dcc, Input, Output
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.fake_map_values()
fig = px.scatter_geo(
    df,
    locations="countries_codes",
    color="continents_names",
    hover_name="top_artists",
    projection="natural earth",
    title="Top artistes de chaque pays"
)

# Fonction de création du graph.
# La fonction prend aussi en charge les callback.
def create_map_graph(app):

    # Callback lorsque le select change de valeur.
    @app.callback(
        Output(component_id='world-map-graph', component_property='figure'),
        Input(component_id='world-map-select', component_property='value')
    )
    def update_output_fig(value):
        # Lorsque le select change de valeur, regénérer le graphique en
        # en fonction du choix de l'utilisateur.
        config = {
            "title": "Top artistes de chaque pays",
            "hover_title": "top_artists",
            "size": None
        }
        if (value == "BPMM"):
            config = {
                "title": "BPM moyen pour chaque pays",
                "hover_title": "averages_BPM",
                "size": "averages_BPM"
            }

        # Regénération des nouvelles données avec les paramètres adaptés.
        df = api.fake_map_values()
        fig = px.scatter_geo(
            df,
            locations="countries_codes",
            color="continents_names",
            projection="natural earth",
            size=config['size'],
            hover_name=config['hover_title'],
            title=config['title'],
            labels={
                "continents_names":  "Continent",
                "countries_codes":   "Pays"
            }
        )
        fig.update_layout(dragmode=False)

        return fig
    ## Fin callback.

    ## Construction de l'élément HTML du graphique et du select.
    return html.Div(
        className="graph-container world-map",
        children=[
            dcc.Graph(
                figure=fig,
                className="fig",
                config={
                    "displayModeBar": False,
                    "scrollZoom": False
                },
                id='world-map-graph',
                style={'height': '100%'}
            ),
            dcc.Dropdown(
                options=[
                    {'label': 'Top artistes',  'value': 'TOPA'},
                    {'label': 'Top morceaux',  'value': 'TOPT'},
                    {'label': 'BPM moyen',     'value': 'BPMM'},
                    {'label': 'Durée moyenne', 'value': 'DURM'},
                ],
                value='TOPA',
                id="world-map-select",
                className="world-map-select"
            )
        ]
    )