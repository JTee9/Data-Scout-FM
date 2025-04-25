# Todo ------------------
# 1. Add README

import dash
from dash import Dash, html, dcc, Output, Input, State, ctx
import dash_bootstrap_components as dbc
import pandas as pd
from transform_attributes import build_shortlist_attributes_dataframe, build_squad_attributes_dataframe
from transform_stats import build_stats_dataframe
from config import language_dict, feedback_categories, issue_categories
import base64
import io
from warnings import simplefilter
from datetime import datetime
import os

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# Create app
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SUPERHERO], title='Data Scout FM')
server = app.server

FEEDBACK_FILE = 'feedback.csv'
REPORT_FILE = 'report.csv'

# Feedback modal to allow users to rate their satisfaction with the app and share detailed feedback.
feedback_modal = (
    dbc.Modal([
        dbc.ModalHeader('Share Your Feedback'),
        dbc.ModalBody([
            # Optional Input Fields for User Identity
            html.Div([
                html.Label('Your Manager Name in FM (optional): '),
                html.Br(),
                dcc.Input(id='user-name-input',
                          placeholder='Enter your name here.', style={'width': '50%'}),
                html.Br(),
                html.Label('Your personal accolades in FM (optional): '),
                html.Br(),
                dcc.Textarea(id='accolades-text',
                             placeholder='Please provide a brief summary of your career.',
                             style={'width': '100%', 'height': '100px'})
            ]),
            html.Div([
                html.Label('What rating would you give this Data Scout FM app?'),
                dcc.Dropdown(id='feedback-dropdown', options=feedback_categories, value='', clearable=False,
                             style={'text-align': 'left', 'width': '50%'}),
                html.Label('Detailed Feedback'),
                html.Br(),
                dcc.Textarea(id='feedback-text',
                             placeholder='Please provide details on what you like about the app '
                                         'and what you feel could be improved.',
                             style={'text-align': 'left', 'width': '100%', 'height': '150px'}),
                html.Br(),
                dbc.Button('Submit', id='submit-feedback-button',
                           className='modal_conditions_button', n_clicks=0),
                html.Br(),
                html.Div(id="feedback-submission-status", style={'margin-top': '15px'})
            ])
        ]),
        dbc.ModalFooter(
            dbc.Button('Close', id='close-feedback-button',
                       className='modal_conditions_button', n_clicks=0)
        ),
    ], id='feedback-modal', className='filter-modal', is_open=False)
)

# Report modal to allow users to report bugs and issues they experience with the app.
report_modal = (
    dbc.Modal([
        dbc.ModalHeader('Report a Problem'),
        dbc.ModalBody([
            html.Label('Select the category for the problem you would like to report.'),
            html.Br(),
            dcc.Dropdown(id='report-dropdown', options=issue_categories, value='', clearable=False,
                         style={'width': '65%'}),
            html.Br(),
            html.Label('Detailed Feedback'),
            html.Br(),
            dcc.Textarea(id='report-text',
                         placeholder='Please provide details on the problem you experienced.',
                         style={'width': '100%', 'height': '100px'}),
            html.Br(),
            dbc.Button('Submit', id='submit-report-button',
                       className='modal_conditions_button', n_clicks=0),
            html.Div(id="report-submission-status", style={'margin-top': '15px'})
        ]),
        dbc.ModalFooter(
            dbc.Button('Close', id='close-report-button',
                       className='modal_conditions_button', n_clicks=0)
        ),
    ], id='report-modal', className='filter-modal', is_open=False)
)

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

            html.Div([
                html.Label('FM Custom Views'),
                html.Div([
                    dbc.Button('Download', id='download-button', n_clicks=0,
                               className='container-button', style={'margin-top': '5px'}),
                    dcc.Download(id='download-custom-views')
                ])
            ], style={'text-align': 'left', 'margin-top': '30px', 'margin-left': '10px'}),

            html.Div([
                html.Label('Select data to analyze'),
                # Create Two Buttons to toggle between Stats and Attributes pages
                html.Div([
                    dcc.Link(dbc.Button('Stats', id='stats-button', n_clicks=0,
                                        className='container-button', style={'margin-right': '5px'}), href='/stats'),
                    dcc.Link(dbc.Button('Attributes', id='attributes-button', n_clicks=0,
                                        className='container-button', style={'margin-left': '5px'}), href='/attributes')
                ],
                    style={'display': 'flex', 'margin-top': '5px'})
            ], style={'text-align': 'left', 'margin-top': '50px', 'margin-left': '10px'},),

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
                dcc.Loading(id='loading-upload', type='dot', children=[
                    html.Div(id='uploaded-files', children='No files uploaded')
                ]),
                dcc.Store(id='stored-uploads', data={}),
            ]),

            # Report Issue & Share Feedback Buttons
            html.Div([
                html.Label("How's the app?"),
                html.Div([
                    dbc.Button('Feedback', id='feedback-button', n_clicks=0, className='container-button',
                               style={'margin-right': '5px'}),
                    feedback_modal,
                    dbc.Button('Report', id='report-button', n_clicks=0, className='container-button',
                               style={'margin-left': '5px'}),
                    report_modal,
                ], style={'display': 'flex', 'margin-top': '5px'})
            ], style={'text-align': 'left', 'margin-top': '50px', 'margin-left': '10px'})
        ], style={
            'flex': '0 0 10%',
            'padding': '10px',
            'margin': '30px',
            'height': 'calc(100vh - 60px)',
        }),
    # Right Side
    html.Div(dash.page_container, className='right-container', style={
            'flex': '0 0 80%',
            'border': '1px solid #ddd',
            'padding': '10px',
            'margin': '15px',
            'border-radius': '20px',
            'height': 'calc(100vh - 30px)'
        })
],
    # Container split horizontally
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


# Handle Feedback Button
@app.callback(
    Output("feedback-modal", "is_open"),
    [Input("feedback-button", "n_clicks"),
     Input("close-feedback-button", "n_clicks")],
    [State("feedback-modal", "is_open")]
)
def toggle_modal(open_clicks, close_clicks, is_open):
    if not ctx.triggered:
        return is_open

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "feedback-button":
        return True
    elif button_id == "close-feedback-button":
        return False

    return is_open


# Handle Report Button
@app.callback(
    Output("report-modal", "is_open"),
    [Input("report-button", "n_clicks"),
     Input("close-report-button", "n_clicks")],
    [State("report-modal", "is_open")]
)
def toggle_modal(open_clicks, close_clicks, is_open):
    if not ctx.triggered:
        return is_open

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "report-button":
        return True
    elif button_id == "close-report-button":
        return False

    return is_open


# Handle Submit Feedback Button
@app.callback(
    Output("feedback-submission-status", "children"),
    Input("submit-feedback-button", "n_clicks"),
    State("user-name-input", "value"),
    State("accolades-text", "value"),
    State("feedback-dropdown", "value"),
    State("feedback-text", "value"),
    prevent_initial_call=True,
)
def process_modal_feedback(n_clicks, user_name, user_bio, selected_rating, feedback_text):

    def save_feedback(name, bio, rating, text):
        """Saves the feedback to a CSV file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_feedback = pd.DataFrame({
            'Timestamp': [timestamp], 'Name': [name], 'Bio': [bio], 'Rating': [rating], 'Feedback': [text]
        })

        if os.path.exists(FEEDBACK_FILE):
            existing_data = pd.read_csv(FEEDBACK_FILE)
            updated_data = pd.concat([existing_data, new_feedback], ignore_index=True)
            updated_data.to_csv(FEEDBACK_FILE, index=False)
        else:
            new_feedback.to_csv(FEEDBACK_FILE, index=False)

    if n_clicks > 0:
        if selected_rating and feedback_text:
            save_feedback(user_name, user_bio, selected_rating, feedback_text)
            return f"Successfully submitted. Thank you for your feedback!"
        else:
            return 'Please make sure to select a Rating and write your feedback in the text area.'
    return ""


# Handle Submit Report Button
@app.callback(
    Output("report-submission-status", "children"),
    Input("submit-report-button", "n_clicks"),
    State("report-dropdown", "value"),
    State("report-text", "value"),
    prevent_initial_call=True,
)
def process_modal_feedback(n_clicks, selected_category, report_text):
    def save_report(category, text):
        """Saves the feedback to a CSV file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_report = pd.DataFrame({'Timestamp': [timestamp], 'Category': [category], 'Feedback': [text]})

        if os.path.exists(REPORT_FILE):
            existing_data = pd.read_csv(REPORT_FILE)
            updated_data = pd.concat([existing_data, new_report], ignore_index=True)
            updated_data.to_csv(REPORT_FILE, index=False)
        else:
            new_report.to_csv(REPORT_FILE, index=False)

    if n_clicks > 0:
        if selected_category and report_text:
            save_report(selected_category, report_text)
            return f"Successfully submitted. Thank you for reporting the issue!"
        else:
            return 'Please make sure to select a Category and to describe the issue in the text area.'
    return ""


if __name__ == '__main__':
    app.run(debug=True, port=8050)
