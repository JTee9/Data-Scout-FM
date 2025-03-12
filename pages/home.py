import dash
from dash import callback, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

# Register Page
dash.register_page(__name__, path='/', title='Data Scout FM')

layout = html.Div([
    dbc.Row([html.H1('View the Instructions to get started!', style={'text-align': 'center', 'margin-top': '30px'})], justify='center'),
    dbc.Row([dbc.Button('View Instructions', id='open-instructions-modal-button', n_clicks=0, style={'width': 'auto'})], justify='center'),
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
                          dbc.Button('Close', id='close-instructions-modal-button', className='ml-auto', n_clicks=0)
                      ),
                  ],
                  id='instructions-modal',
                  is_open=False,
              ),
], style={"display": "block", "justifyContent": "center"})


# Callback -------------------------------------
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




