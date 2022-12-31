# map_graph.py est responsable de la construction de graphique
# de la carte du monde et de la gestions de ses callback (notamment les
# callbacks du select).

import random
from dash import html, dcc, Input, Output
import plotly.express as px
from ..utils import api

# Récupération des données.
# Les données sont déja traités dans utils/api.py.
df = api.map_values()
fig = px.choropleth(
    df,
    locations="countries_codes",
    color="top_artists",
    hover_name="top_artists",
    projection="natural earth",
    title="Top artistes de chaque pays"
)

long_color_sequence = [ "#88e99a",
                        "#0f1f14",
                        "#6df6fe",
                        "#18857f",
                        "#ecf1fa",
                        "#2a9739",
                        "#caf243",
                        "#602e01",
                        "#ee983a",
                        "#c92d34",
                        "#ef8ead",
                        "#90705e",
                        "#dec651",
                        "#6a7f2f",
                        "#2af464",
                        "#0f1f5f",
                        "#68affc",
                        "#3c5da0",
                        "#b687f8",
                        "#3f1ba1",
                        "#0f1745",
                        "#239eb3",
                        "#085782",
                        "#b0fff9",
                        "#0b5313",
                        "#36c272",
                        "#dffc98",
                        "#9db46a",
                        "#743502",
                        "#de8a2c",
                        "#ab2b60",
                        "#fdb5ac",
                        "#ff0087",
                        "#cb2c09",
                        "#b4726b",
                        "#76f014",
                        "#3a1283",
                        "#e89ff0",
                        "#476af9",
                        "#759ee5",
                        "#68affc",
                        "#043255",
                        "#1eefc9",
                        "#197959",
                        "#9be2d3",
                        "#012d03",
                        "#88dc40",
                        "#48950f",
                        "#fbf66d",
                        "#5a310c",
                        "#cda19a",
                        "#821f48",
                        "#eb6382",
                        "#f6eefa",
                        "#d54416",
                        "#ff0087",
                        "#ee983a",
                        "#1d70a5",
                        "#060369",
                        "#7d76e4",
                        "#c5d5f0",
                        "#252049",
                        "#8f68ff",
                        "#7b038e",
                        "#5975bb",
                        "#9bf4ce",
                        "#22695e",
                        "#2dadb8",
                        "#042c17",
                        "#83cc3f",
                        "#378811",
                        "#e9e876",
                        "#462a09",
                        "#d58e43",
                        "#ea1349",
                        "#972b2d",
                        "#ea7c97",
                        "#96a467",
                        "#00d618",
                        "#a07a7c",
                        "#208eb7",
                        "#9be4c0",
                        "#214d4e",
                        "#5eff92",
                        "#4c0634",
                        "#c7c2ec",
                        "#440583",
                        "#c1f274",
                        "#9a4058",
                        "#6a9c75",
                        "#ff1c5d",
                        "#88fe0e",
                        "#ee80fe",
                        "#7fac0c",
                        "#01102c",
                        "#ebaa8c",
                        "#a43e03",
                        "#6a7fd2",
                        "#bf11af",
                        "#ffe254"]



# Fonction de création du graph.
# La fonction prend aussi en charge les callback.
def create_map_graph(app):
    """Create the map graph

    Args:
        app (Any): the dash app

    Returns:
        html: the html element
    """

    # Callback lorsque le select change de valeur.
    @app.callback(
        Output(component_id='world-map-graph', component_property='figure'),
        Input(component_id='world-map-select', component_property='value')
    )
    def update_output_fig(value):
        # Lorsque le select change de valeur, regénérer le graphique en
        # en fonction du choix de l'utilisateur.
        config = {
            "title": "Countries Top Artist",
            "hover_title": "top_artists",
            "color": "top_artists",
            "color_discrete_sequence": long_color_sequence,
            "color_continuous_scale": None,
            "labels": {"countries_names":   "Country",
                       "countries_codes":   "Alpha3 Code",
                       "top_artists":       "Top Artist",
            },
            "hover_data": ["countries_names"],
            
        }
        df = api.map_values()

        if (value == "BPMM"):
            config = {
                "title": "Countries Average BPM",
                "hover_title": "averages_BPM",
                "color": "averages_BPM",
                "color_discrete_sequence": None,
                "color_continuous_scale": px.colors.sequential.OrRd,
                "labels": {"countries_names":   "Country",
                           "countries_codes":   "Alpha3 Code",
                           "averages_BPM":      "Average BPM",
                },
                "hover_data": ["countries_names"],
            }
        
        if (value == "TOPT"):
            config = {
                "title": "Countries Top Tracks",
                "hover_title": "top_tracks_and_artists",
                "color": "top_tracks_and_artists",
                "color_discrete_sequence": long_color_sequence,
                "color_continuous_scale": None,
                "hover_data": ["countries_names"],
                "labels": {"countries_names":   "Country",
                           "countries_codes":   "Alpha3 Code",
                           "top_tracks_and_artists": "Top Track"
                },
            }
        
        if (value == "DURM"):
            config = {
                "title": "Countries Tracks Average Duration",
                "hover_title": "average_formated_duration",
                "color": "average_duration",
                "color_discrete_sequence": None,
                "color_continuous_scale": px.colors.sequential.deep,
                "labels": {"countries_names":   "Country",
                           "countries_codes":   "Alpha3 Code",
                           "average_duration": "Average Duration (seconds)",
                           "average_formated_duration": "Average Duration"
                },
                "hover_data": ["countries_names", "average_formated_duration"],
            }
        
        if (value == "TOPG"):
            random.shuffle(long_color_sequence)
            config = {
                "title": "Countries Top Genre",
                "hover_title": "top_genre",
                "color": "top_genre",
                "color_discrete_sequence": long_color_sequence,
                "color_continuous_scale": None,
                "labels": {"countries_names":   "Country",
                           "countries_codes":   "Alpha3 Code",
                           "top_genre":         "Top Genre"
                },
                "hover_data": ["countries_names"],
            }
        
        fig = px.choropleth(
            df,
            locations="countries_codes",
            color=config["color"],
            color_discrete_sequence=config["color_discrete_sequence"],
            color_continuous_scale= config["color_continuous_scale"],
            projection="natural earth",
            hover_name=config['hover_title'],
            hover_data=config['hover_data'],
            title=config['title'],
            labels=config['labels']
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
                    {'label': 'Top Artists',  'value': 'TOPA'},
                    {'label': 'Top Tracks',  'value': 'TOPT'},
                    {'label': 'Average BPM',     'value': 'BPMM'},
                    {'label': 'Average Duration', 'value': 'DURM'},
                    {'label': 'Top Genre', 'value': 'TOPG'},
                ],
                value='TOPA',
                id="world-map-select",
                className="world-map-select"
            )
        ]
    )