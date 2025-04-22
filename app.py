# Todo ------------------
# 1. Add README
# 2. Celery, long callback, loading bar for file upload

import dash
from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
from transform_attributes import build_shortlist_attributes_dataframe, build_squad_attributes_dataframe
from transform_stats import build_stats_dataframe
from config import language_dict
import base64
import io
from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# Create app
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SUPERHERO], title='Data Scout FM')
server = app.server

app.layout = dbc.Container([
    # Left Side
    html.Div(
        id='main-content', className='left-container', children=[
            dbc.Button(id='home-button', className='home-button', href='/', children=[
                    html.Img(
                        src='assets/Img/data-scout-fm-logo.png',
                        style={
                            'border-radius': '50%',
                            'width': '90%',
                            'margin-left': '-10px'
                        })
                ], style={'margin-top': '50px', 'text-align': 'left'}),

            html.Div(style={'text-align': 'left', 'margin-top': '30px', 'margin-left': '10px'}, children=[
                html.Label('FM Custom Views'),
                html.Div([
                    dbc.Button('Download', id='download-button', n_clicks=0, className='container-button', style={'margin-top': '10px', 'borderRadius': '10px'}),
                    dcc.Download(id='download-custom-views')
                ])
            ]),

            html.Div(style={'text-align': 'left', 'margin-top': '50px', 'margin-left': '10px'}, children=[
                html.Label('Select data to analyze'),
                # Create Two Buttons to toggle between Stats and Attributes pages
                html.Div(children=[
                    dcc.Link(dbc.Button('Stats', id='stats-button', n_clicks=0, className='container-button', style={'margin': '5px'}), href='/stats'),
                    dcc.Link(dbc.Button('Attributes', id='attributes-button', n_clicks=0, className='container-button', style={'margin': '5px'}), href='/attributes')
                ],
                    style={
                        'margin-top': '5px',
                        'display': 'flex',
                        'margin-left': '-6px'
                    })
            ]),

            html.Div(style={'text-align': 'left', 'font-size': '14px', 'margin-top': '50px', 'margin-left': '10px'}, children=[
                html.Label('Upload Files from FM'),
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([html.A('Drag or Select Files')]),
                    style={
                        # 'height': '60px',
                        'width': '150px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px',
                        'margin-left': '-3px'
                    },
                    multiple=True
                ),
                dcc.Loading(id='loading-upload', type='graph', children=[
                    html.Div(id='uploaded-files', children='No files uploaded')
                ]),
                dcc.Store(id='stored-uploads', data={}),
            ])
        ], style={
            'flex': '0 0 10%',
            'padding': '10px',  # Add some padding
            'margin': '30px',  # Add some margin
            # 'border-radius': '10px', # rounded corners
            'height': 'calc(100vh - 60px)'
        }),
    # Right Side
    html.Div(dash.page_container, className='right-container', style={
            'flex': '0 0 80%',
            'border': '1px solid #ddd',  # Add a border
            'padding': '10px',  # Add some padding
            'margin': '15px',  # Add some margin
            'border-radius': '20px', # rounded corners
            'height': 'calc(100vh - 30px)'
        })
],
    # Container split horizontally (flex)
    style={'display': 'flex'},
    fluid=True,
    className='dashboard-container')


# Callback ----------------------------
@app.callback(
    Output('uploaded-files', 'children'),
    Output('stored-uploads', 'data'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
)
def update_output(list_of_contents, list_of_names):
    # If no files are uploaded
    if list_of_contents is None and list_of_names is None:
        return html.Label('No files uploaded'), {}

    # If upload-data input is not empty, check to see if the four required files are present and build the dataframes.
    try:
        filename_list = []
        data_list = {}
        stats_dataframes = []

        for content, filename in zip(list_of_contents, list_of_names):
            filename_list.append(filename)  # add filename to filename_list.
            content_type, content_string = content.split(',')
            decoded = base64.b64decode(content_string)

            if 'squad_stats' in filename:
                print(f"Processing file: {filename}")
                squad_stats_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                stats_dataframes.append(squad_stats_data)
                language_check_data = squad_stats_data
                language_check_data[0].columns = language_check_data[0].columns.str.replace('\u200b', '')
            elif 'squad_attributes' in filename:
                print(f"Processing file: {filename}")
                squad_att_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
            elif 'shortlist_attributes' in filename:
                print(f"Processing file: {filename}")
                scouting_att_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
            elif 'player_search_stats' in filename:
                print(f"Processing file: {filename}")
                player_search_stats_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                stats_dataframes.append(player_search_stats_data)

        # Check user's language preference from squad_stats file 'Wage' column
        print(f'Number of files uploaded: {len(filename_list)}')
        language_key = str(language_check_data[0].columns[6])
        language_preference = str(language_dict[language_key])
        print(f'Language Key: {language_key}')
        print(f'Language Preference: {language_preference}')
        # Add created dataframes and language key to dcc.Store
        data_list['language_preference'] = language_preference
        print('Initiating build squad attributes df...')
        data_list['squad_attributes'] = build_squad_attributes_dataframe(squad_att_data, language_preference).to_json(date_format='iso', orient='split')
        print('Initiating build shortlist attributes df...')
        data_list['shortlist_attributes'] = build_shortlist_attributes_dataframe(scouting_att_data, language_preference).to_json(date_format='iso', orient='split')
        print('Initiating build stats df...')
        data_list['stats'] = build_stats_dataframe(squad_stats_data, player_search_stats_data, language_preference).to_json(date_format='iso', orient='split')
        # Show user how many of the required files were successfully uploaded
        children = f'{len(filename_list)}/4 files uploaded'
        return children, data_list
    except Exception as inner_e:
        print(f"Error processing file '{filename}': {inner_e}")
        return html.Div([f'Error processing file {filename}: {inner_e}']), {}


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


if __name__ == '__main__':
    app.run(debug=True, port=8050)
