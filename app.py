# Todo --------------------------
# 1. Create beautiful cover page? Have users import FM filters and upload the required html files.
# 2. Make the site beautiful with Bootstrap

import os
import dash
from dash import Dash, html, dcc, Output, Input, State, ctx
import dash_bootstrap_components as dbc
import pandas as pd
from transform import build_scouting_attributes_dataframe, build_squad_attributes_dataframe, build_stats_dataframe
import base64
import io
from warnings import simplefilter


simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


# Create app
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB], title='Data Scout FM')


# Dashboard Layout. Creating a container which includes a navigation bar and plots
app.layout = dbc.Container([
    # Left Side
    html.Div(
        id='main-content', children=
        # Item 1
        [html.Div([
            html.H1([
                html.Span('Welcome,'),
                html.Br(),
                html.Span('Noob')
            ]),
            html.Div([dbc.Button('View Instructions', id='open-instructions-modal-button', n_clicks=0),
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
                                      html.Label('Step 2.2 - Select all players (Ctrl+A) and save as HTML file (Ctrl+P) for both views. **FILENAMES MUST INCLUDE "squad_attributes" and "squad_stats".'),
                                      html.Hr(),
                                      html.Label('Step 2.3 - Go to Scouting, Players, Players in Range. Import scouting_stats view'),
                                      html.Hr(),
                                      html.Label('Step 2.4 - Click "Edit Search" to filter the players you want to include in your data. e.g. add conditions for all the divisions you want to include.'),
                                      html.Hr(),
                                      html.Label('Step 2.5 - Select all players (Ctrl+A), scroll to the very bottom, and save as HTML (Ctrl+P). **FILENAME MUST INCLUDE "scouting_stats".'),
                                      html.Hr(),
                                      html.Label('Step 2.6 - Go to your Shortlist and import "scouting_attributes" view.'),
                                      html.Hr(),
                                      html.Label('Step 2.7 - Select all players (Ctrl+A), scroll to the very bottom, and save as HTML (Ctrl+P). **FILENAME MUST INCLUDE "scouting_attributes".'),
                                      html.Hr(),
                                      html.Label('Close this pop-up and click the Upload button to upload the four required files')
                                  ]
                              ),
                              dbc.ModalFooter(
                                  dbc.Button('Close', id='close-instructions-modal-button', className='ml-auto', n_clicks=0)
                              ),
                          ],
                          id='instructions-modal',
                          is_open=False,
                      ),]),
        ],
        style={
            'vertical-alignment': 'top',
            'height': 260
        }),
        # Item 2
        html.Div([
            dbc.Button('Download FM Custom Views', id='download-button', n_clicks=0),
            dcc.Download(id='download-custom-views')]),
        # Item 3
        html.Div([html.H2('Analyze Stats or Attributes?'),
            # Create Two Buttons to toggle between Stats and Attributes pages
            html.Div([
                dcc.Link(dbc.Button('Stats', id='stats-button', n_clicks=0), href='/stats'),
                dcc.Link(dbc.Button('Attributes', id='attributes-button', n_clicks=0), href='/attributes')
            ],
            style={
                'margin-left': 15,
                'margin-right': 15,
                'display': 'flex'
            })]
        ),
        # Item 4
        html.Div([
            html.H2('Upload Files from FM'),
            dcc.Upload(
                id='upload-data',
                children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                multiple=True
            ),
            html.Div(id='uploaded-files', children=html.H2('No files uploaded'),
                     style={
                         'width': '50%',
                     }),
            dcc.Store(id='stored-uploads', data={})
        ])
    ]),
    # Right Side
    dash.page_container
],
    # Container split horizontally (flex)
    style={'display': 'flex'},
    className='dashboard-container')


# Callback ----------------------------
@app.callback(
    Output('uploaded-files', 'children'),
    Output('stored-uploads', 'data'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
)
def update_output(list_of_contents, list_of_names):
    if list_of_contents is None and list_of_names is None:
        return html.H2('No files uploaded'), {}

    try:
        filename_list = []
        data_list = {}
        stats_dataframes = []
        for content, filename in zip(list_of_contents, list_of_names):
            filename_list.append(filename)  # add filename to filename_list.
            content_type, content_string = content.split(',')
            decoded = base64.b64decode(content_string)
            if 'squad_attributes' in filename:
                squad_att_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                data_list['squad_attributes'] = build_squad_attributes_dataframe(squad_att_data).to_json(date_format='iso', orient='split')
            elif 'scouting_attributes' in filename:
                scouting_att_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                scouting_attributes_df = build_scouting_attributes_dataframe(scouting_att_data).to_json(date_format='iso', orient='split')
                data_list['scouting_attributes'] = scouting_attributes_df
            elif 'squad_stats' in filename:
                squad_stats_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                stats_dataframes.append(squad_stats_data)
            elif 'scouting_stats' in filename:
                scouting_stats_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                stats_dataframes.append(scouting_stats_data)

        data_list['stats'] = build_stats_dataframe(squad_stats_data, scouting_stats_data).to_json(date_format='iso', orient='split')
        children = f'{len(filename_list)}/4 files uploaded'
        return children, data_list
    except Exception as e:
        print(f"Error in callback: {e}")
        return html.Div(['Error processing uploaded files.']), {}


# Download Callback
@app.callback(
    Output('download-custom-views', 'data'),
    Input('download-button', "n_clicks"),
    prevent_initial_call=True,
)
def download_custom_views(n_clicks):
    return dcc.send_file(
        'assets/fm_custom_views.zip'
    )


# Instruction modal callback
@app.callback(
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


if __name__ == '__main__':
    app.run(debug=True, port=5001)


## Website details
# Allow users to upload their fm files to analyze their data with tables and charts
# Have users register so that they can continue to access their files
