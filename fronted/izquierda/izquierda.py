from dash import html
import dash_bootstrap_components as dbc

izquierda = dbc.Container(
    [
         dbc.Row(
        [
            dbc.Col('input', md=12, style={'background-color':'brown'}),
            dbc.Col('tabla',md=12, style={'background-color':'white'}),
            dbc.Col('conclusiones',md=12, style={'background-color':'orange'})
        ]
        )  
    ]
)