from dash import Dash, html, dcc
import plotly.express as px

app = Dash("Spotiviz dashboard")

# Dashboard component: Table
def build_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Build main page layout
def build_main_layout(dataframe):

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        build_table(dataframe)
    ])

# Start dashoard server
def start():

    app.run_server(debug=True)