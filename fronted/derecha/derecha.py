from dash import html
import dash_bootstrap_components as dbc

#importar componentes de la parte derecha
from .graficas.curva_granulometrica import curva_granulometrica
from .graficas.carta_plasticidad import carta_plasticidad

derecha = dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col(curva_granulometrica, md=6, style={'background-color':'skyblue'}),
            dbc.Col(carta_plasticidad,md=6, style={'background-color':'gray'})
        ]
        )     
    ]
)