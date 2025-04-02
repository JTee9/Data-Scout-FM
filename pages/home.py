import dash
from dash import callback, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

# Register Page
dash.register_page(__name__, path='/', title='Data Scout FM')

layout = html.Div([
    # Intro
    dbc.Row(className='overview-row', children=[
        html.Br(),
        html.H1('Welcome to Data Scout FM',
                style={'margin-top': '40px'}
                ),
        html.P('Analyze player stats from your FM save like a professional data scout.',
               style={
                   'margin-left': '5px'
               }),
    ],
            style={
                'text-align': 'left',
                'margin-top': '30px',
                'margin-left': '100px'
            }
            ),
    # App Overview Button & Modal
    dbc.Row([
        dbc.Button('App Overview', id='open-app-overview-modal-button', n_clicks=0, className='container-button',
                   style={'width': 'auto', 'margin-left': '125px'})]),
    dbc.Modal(
            [
                dbc.ModalHeader('App Overview'),
                dbc.ModalBody(
                    [
                        html.Label('1. Pull four HTML files from your FM save '
                                   '(Squad Attributes, Squad Stats, Player Search Stats, Shortlist Attributes) '
                                   'and upload them to the app.'),
                        html.Hr(),
                        html.Label("2. Use the Stats tab to generate Scatter, Table, and Radar Charts "
                                   "to identify top performers, compare your squad members' performance to others, "
                                   "or find players who fit your system."),
                        html.Hr(),
                        html.Label('3. Use the Attributes tab to compare players in your shortlist '
                                   'to your current squad members. '
                                   'The app allows you to compare attributes per position as well as '
                                   'Role Scores based on attributes required for each role.')
                    ]
                ),
                dbc.ModalFooter(
                    dbc.Button('Close', id='close-app-overview-modal-button', className='close-instructions-button', n_clicks=0)
                ),
            ],
            id='app-overview-modal',
            is_open=False
        ),
    # Instructions Button & Modal
    dbc.Row([
        html.H3('View the Instructions to get started',
                style={
                    'text-align': 'left',
                    'margin-top': '90px',
                    'margin-left': '112px'
                })
    ]),
    dbc.Row([
            dbc.Button('View Instructions', id='open-instructions-modal-button', n_clicks=0, className='container-button',
                       style={'width': 'auto', 'margin-left': '124px', 'margin-top': '10px'})]),
    dbc.Modal(
        [
            dbc.ModalHeader('Instructions'),
            dbc.ModalBody(
                [
                    html.Label('Step 1 - Download the Custom Views and move the files to Football Manager 2024/views'),
                    html.Hr(),
                    html.Label('Step 2 - Import the Custom Views into your FM file:'),
                    html.Hr(),
                    html.Label('Step 2.1 - Go to the Squad tab and Import "squad_attributes" and "squad_stats" views'),
                    html.Hr(),
                    html.Label('Step 2.2 - Select all players (Ctrl+A) and save as web page (Ctrl+P) for both views. **FILENAMES MUST INCLUDE "squad_attributes" and "squad_stats".'),
                    html.Hr(),
                    html.Label('Step 2.3 - Go to Scouting, Players, Players in Range. Import player_search_stats view'),
                    html.Hr(),
                    html.Label('Step 2.4 - Click "Edit Search" to filter the players you want to include in your data. e.g. add conditions for all the divisions you want to include.'),
                    html.Hr(),
                    html.Label('Step 2.5 - Select all players (Ctrl+A), scroll to the very bottom, and save as web page (Ctrl+P). **FILENAME MUST INCLUDE "player_search_stats".'),
                    html.Hr(),
                    html.Label('Step 2.6 - Go to your Shortlist and import "shortlist_attributes" view.'),
                    html.Hr(),
                    html.Label('Step 2.7 - Select all players (Ctrl+A), scroll to the very bottom, and save as web page (Ctrl+P). **FILENAME MUST INCLUDE "shortlist_attributes".'),
                    html.Hr(),
                    html.Label('Close this pop-up and upload the four required HTML files (squad_attributes, shortlist_attributes, squad_stats, player_search_stats).')
                ]
            ),
            dbc.ModalFooter(
                dbc.Button('Close', id='close-instructions-modal-button', className='close-instructions-button', n_clicks=0)
            ),
        ],
        id='instructions-modal',
        is_open=False,
    ),
], style={"display": "block", "justifyContent": "center"})


# Callback -------------------------------------
# App Overview modal callback
@callback(
    Output("app-overview-modal", "is_open"),
    [Input("open-app-overview-modal-button", "n_clicks"),
     Input("close-app-overview-modal-button", "n_clicks")],
    [State("app-overview-modal", "is_open")]
)
def toggle_modal(open_clicks, close_clicks, is_open):
    if not ctx.triggered:
        return is_open

    server_button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if server_button_id == "open-app-overview-modal-button":
        return True
    elif server_button_id == "close-app-overview-modal-button":
        return False

    return is_open

# Instruction modal callback
@callback(
    Output("instructions-modal", "is_open"),
    [Input("open-instructions-modal-button", "n_clicks"),
     Input("close-instructions-modal-button", "n_clicks")],
    [State("instructions-modal", "is_open")]
)
def toggle_modal(open_clicks, close_clicks, is_open):
    if not ctx.triggered:
        return is_open

    server_button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if server_button_id == "open-instructions-modal-button":
        return True
    elif server_button_id == "close-instructions-modal-button":
        return False

    return is_open




