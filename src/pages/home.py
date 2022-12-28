# home.py est responsable de la création de la
# page d'accueil en appleant la création de tous
# les composant nécéssaires.

from dash import html
from ..components import popularity_by_countries_graph, create_map_graph, duration_by_genre_graph, bpm_by_contry_graph, loudness_energy_graph, genre_comparing_graph

# Référence vers l'objet app qui est construit dans app.py.
app_ref = None

# Fonction de création de la page d'accueil.
def create_home(app):
    app_ref = app

    # Construction de tous les éléments HTML de la page.
    return html.Div(
        className="home large-container",
        children=[
            html.Section(
                children=[
                    # Titre.
                    html.H2(
                        children="World Music Stats"
                    ),

                    # Graphiques.
                    html.Div(
                        className="graph-grid",
                        children=[
                            html.Div(
                                className="container-graph world-map",
                                children=create_map_graph(app_ref)
                            ),
                            html.Div(
                                className="container-graph",
                                children=popularity_by_countries_graph
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
                                children=duration_by_genre_graph
                            ),
                            html.Div(
                                className="container-graph comparing",
                                children=genre_comparing_graph
                            )
                        ]
                    ),
                    
                ]
            ),

        ]
    )