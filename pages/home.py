import dash
from dash import html

# Register Page
dash.register_page(__name__, path='/', title='Data Scout FM')

layout = html.Div([html.H1('View the Instructions to get started!')], style={'textAlign': 'center'})
