import dash
import dash_table
from dash import html

#Importamos back
from backend.curva_granulometrica import curva_granulometrica

# Crear datos para la tabla
tablatamices = [
    {'Malla': 4, 'Ensayo_1': 20, 'Ensayo_2': 'e', 'Ensayo_3': 'l'},
    {'Malla': 10, 'Ensayo_1': 35, 'Ensayo_2': 'f', 'Ensayo_3': 'm'},
    {'Malla': 20, 'Ensayo_1': 32, 'Ensayo_2': 'g', 'Ensayo_3': 'n'},
    {'Malla': 40, 'Ensayo_1': 29, 'Ensayo_2': 'h', 'Ensayo_3': 'o'},
    {'Malla': 100, 'Ensayo_1': 56, 'Ensayo_2': 'i', 'Ensayo_3': 'p'},
    {'Malla': 200, 'Ensayo_1': 38, 'Ensayo_2': 'j', 'Ensayo_3': 'q'},
    {'Malla': 'FONDO', 'Ensayo_1': 43, 'Ensayo_2': 'k', 'Ensayo_3': 'r'}
]

# Crear la tabla
tabla = dash_table.DataTable(
    data=tablatamices,
    columns=[{'id': c, 'name': c} for c in ['Malla', 'Ensayo_1', 'Ensayo_2', 'Ensayo_3']],
    style_cell={'textAlign': 'center'}
)


# Crear la gráfica
curva_granulometrica()

