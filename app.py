import dash
from dash import html
import dash_bootstrap_components as dbc

#import fronted
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.izquierda.izquierda import izquierda

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col(navegador, md=12, style={'background-color':'red'}),
            dbc.Col(izquierda, md=0, style={'background-color':'blue'}),
            dbc.Col(derecha, md=0, style={'background-color':'green'}),
        ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
