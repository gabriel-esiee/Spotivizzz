from dash import html

home = html.Div(
    className="home large-container",
    children=[
        html.Section(
            children=[
                html.H2(
                    children="Your datas"
                ),
                html.Div(
                    className="graph-container"
                ),
            ]
        ),
        
        html.Section(
            children=[
                html.H2(
                    children="World dashboard"
                ),
                html.Div(
                    className="graph-grid",
                    children=[
                        html.Div(className="graph-container world-map"),
                        html.Div(className="graph-container"),
                        html.Div(className="graph-container"),
                        html.Div(className="graph-container"),
                        html.Div(className="graph-container")
                    ]
                ),
            ]
        ),

    ]
)