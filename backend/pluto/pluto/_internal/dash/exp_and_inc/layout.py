from dash import dcc, html  # type: ignore

layout = html.Div(children=[dcc.Location(id="url"), dcc.Graph(id="graph")])
