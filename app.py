# Todo --------------------------
# 1. Create beautiful cover page? Have users import FM filters and upload the required html files.
# 2. Make the site beautiful with Bootstrap

import dash
from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
from transform import build_shortlist_attributes_dataframe, build_squad_attributes_dataframe, build_stats_dataframe
import base64
import io
from warnings import simplefilter


simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


# Create app
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.VAPOR], title='Data Scout FM')
server = app.server

app.layout = html.Div([
    # Left Side
    dbc.Container(
        id='main-content', children=[
            html.Div(style={'text-align': 'center'}, children=[
                html.H1([
                    html.Span('Welcome,'),
                    html.Br(),
                    html.Span('Noob')
                ]),
            ]),
            html.Div(style={'text-align': 'center', 'margin-top': '30px'}, children=[
                dbc.Button('Download FM Custom Views', id='download-button', n_clicks=0),
                dcc.Download(id='download-custom-views')]),
            html.Div(style={'text-align': 'center', 'margin-top': '50px'}, children=[
                html.Label('Analyze Stats or Attributes?'),
                # Create Two Buttons to toggle between Stats and Attributes pages
                html.Div([
                    dcc.Link(dbc.Button('Stats', id='stats-button', n_clicks=0), href='/stats'),
                    dcc.Link(dbc.Button('Attributes', id='attributes-button', n_clicks=0), href='/attributes')
                ],
                    style={
                        'margin-left': 15,
                        'margin-right': 15,
                        'display': 'flex',
                        'justify-content': 'center'
                    })]
                ),
            html.Div(style={'text-align': 'center', 'vertical-align': 'bottom', 'font-size': '14px', 'margin-top': '50px'}, children=[
                html.Label('Upload Files from FM'),
                dcc.Upload(
                    id='upload-data',
                    children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                    style={
                        'width': '70%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px',
                        'margin-left': '45px'
                    },
                    multiple=True
                ),
                html.Div(id='uploaded-files', children='No files uploaded'),
                dcc.Store(id='stored-uploads', data={})
            ])
        ], style={
            'width': '20%',
            'flex': '0 0 20%',
            'border': '1px solid #ddd',  # Add a border
            'padding': '10px',  # Add some padding
            'margin': '30px',  # Add some margin
            'border-radius': '10px', # rounded corners
            'height': 'calc(100vh - 60px)'
            # 'background-color': '#f9f9f9' #light background
        }),
    # Right Side
    dbc.Container(dash.page_container, style={
            'width': '70%',
            'flex': '0 0 70%',
            'border': '1px solid #ddd',  # Add a border
            'padding': '10px',  # Add some padding
            'margin': '30px',  # Add some margin
            'border-radius': '10px', # rounded corners
            'height': 'calc(100vh - 60px)'
            # 'background-color': '#f9f9f9' #light background
        })
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
        return html.Label('No files uploaded'), {}

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
            elif 'shortlist_attributes' in filename:
                scouting_att_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                shortlist_attributes_df = build_shortlist_attributes_dataframe(scouting_att_data).to_json(date_format='iso', orient='split')
                data_list['shortlist_attributes'] = shortlist_attributes_df
            elif 'squad_stats' in filename:
                squad_stats_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                stats_dataframes.append(squad_stats_data)
            elif 'player_search_stats' in filename:
                player_search_stats_data = pd.read_html(io.StringIO(decoded.decode('utf-8')))
                stats_dataframes.append(player_search_stats_data)

        data_list['stats'] = build_stats_dataframe(squad_stats_data, player_search_stats_data).to_json(date_format='iso', orient='split')
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


if __name__ == '__main__':
    app.run(debug=True, port=8050)
