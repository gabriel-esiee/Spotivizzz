from dash import html
from ..components import simple_graph, create_map_graph, table_graph, horizontal_bar_graph, bpm_by_contry_graph, loudness_energy_graph

app_ref = None

def create_home(app):
    app_ref = app

    return html.Div(
        className="home large-container",
        children=[
            html.Section(
                children=[
                    html.H2(
                        children="World dashboard"
                    ),
                    html.Div(
                        className="graph-grid",
                        children=[
                            html.Div(
                                className="container-graph world-map",
                                children=create_map_graph(app_ref)
                            ),
                            html.Div(
                                className="container-graph",
                                children=simple_graph
                            ),
                            html.Div(
                                className="container-graph",
                                children=loudness_energy_graph

                            ),
                            html.Div(
                                className="container-graph",
                                children=bpm_by_contry_graph
                            ),
                            html.Div(
                                className="container-graph",
                                children=horizontal_bar_graph
                            )
                        ]
                    ),
                ]
            ),

        ]
    )