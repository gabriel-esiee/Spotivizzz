from dash import html, dcc, Input, Output
import plotly.express as px
from ..utils import api

df = api.fake_map_values()
fig = px.scatter_geo(
    df,
    locations="countries_codes",
    color="continents_names",
    hover_name="top_artists",
    projection="natural earth",
    title="Top artistes de chaque pays"
)

# Create graph function.
def create_map_graph(app):

    # Create callback for changing select value.
    @app.callback(
        Output(component_id='world-map-graph', component_property='figure'),
        Input(component_id='world-map-select', component_property='value')
    )
    def update_output_fig(value):
        print("New select value: " + value)

        # Select correct value to show depending
        # on the user choice.
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

        # Rebuild graph.
        df = api.fake_map_values()
        fig = px.scatter_geo(
            df,
            locations="countries_codes",
            color="continents_names",
            projection="natural earth",
            size=config['size'],
            hover_name=config['hover_title'],
            title=config['title']
        )

        return fig
    ##

    return html.Div(
        className="graph-container",
        children=[
            dcc.Graph(
                figure=fig,
                className="fig",
                config={
                    "displayModeBar": False
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