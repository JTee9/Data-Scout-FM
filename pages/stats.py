# Todo ------------------
# 1. Make filter data modal UI more user-friendly. Buttons are confusing.
# 2. Long names overlap on the radar chart.
# 3. Fix radar reverse axis for negative stats
# 4. Fix decimal issue on Table

import base64
import io
from io import BytesIO
import dash
from dash import html, dcc, callback, ctx
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import *
from soccerplots.radar_chart import Radar
import matplotlib
matplotlib.use('agg')
from config import (international_position_filters, negative_stat_categories, international_stats_label_dict,
                    preset_radar_values_by_index, sample_filters_by_index)

# Register Page
dash.register_page(__name__, path='/stats', title='Scout FM Stats')

# Page Layout ----------------------------------------------
layout = html.Div([
    # Top Half
    html.Div(style={'text-align': 'left', 'margin-bottom': '15px'}, children=[
        # Top Label
        html.Div(
            html.Label(
                'Click "Filter Data" to add conditions for your Stats data '
                'or select a Sample Filter from the dropdown.',
                className='stats-label'),
            style={'text-align': 'left', 'margin-left': '7px'}
        ),
        # Player Search Modal
        html.Div([
            dbc.Button('Filter Data', id='open-modal-button', n_clicks=0, className='container-button',
                       style={'margin-top': '5px', 'margin-left': '5px', 'margin-bottom': '5px'}),
            dbc.Modal(
                [
                    dbc.ModalHeader('Player Search Filters'),
                    dbc.ModalBody([
                        # Filter dropdown to be populated after files uploaded.
                        html.Div(id='modal-dropdown-div', children=[]),
                        html.Label('Choose logical operator for multiple conditions:'),
                        # logical operator dropdown
                        html.Div([
                            dcc.Dropdown(
                                id='logical-operator',
                                options=[
                                    {'label': 'AND', 'value': 'AND'},
                                    {'label': 'OR', 'value': 'OR'}
                                ],
                                value='AND',
                                clearable=False
                            )], style={'width': '15%'}),
                        html.Br(),
                        # Buttons
                        html.Div([
                            # Buttons on the Left
                            html.Div([
                                # Button to add more filter conditions
                                dbc.Button("Add Condition", id="add-condition", className='modal_conditions_button',
                                           n_clicks=0),
                                html.Br(),
                                html.Br(),

                                # Button to reset dropdowns
                                dbc.Button('Reset Dropdowns', id='reset-dropdowns-button',
                                           className='modal_conditions_button', n_clicks=0),
                                html.Br(),
                                html.Br(),
                            ], style={'display': 'block'}),
                            # Buttons on the Right
                            html.Div([
                                # Button to apply filters
                                dbc.Button('Apply Filter', id='apply-filter-button',
                                           className='modal_conditions_button', n_clicks=0),
                                html.Br(),
                                html.Br(),
                                # Button to clear filters
                                dbc.Button('Clear Filter', id='clear-filter-button',
                                           className='modal_conditions_button', n_clicks=0),
                                html.Br(),
                            ], style={'display': 'block'}),
                        ], style={'display': 'flex', 'justify-content': 'space-between'}),

                        # Confirmation message after applying filters
                        html.Div(id='apply-feedback', children="")
                    ]),
                    # Button to close the modal
                    dbc.ModalFooter(
                        dbc.Button('Close', id='close-modal-button', className='modal_conditions_button', n_clicks=0)
                    ),
                ],
                id='filter-modal',
                className='filter_modal',
                is_open=False,
            ),
        ]),

        # Sample Filter dropdown
        html.Label('Sample Filters - Add other filters (e.g. Age, Transfer Value) '
                   'with the "Filter Data" Button',
                   className='stats-label', style={'margin-left': '7px'}),
        html.Div([
            dcc.Dropdown(
                id='sample-filter-dropdown',
                options=[{'label': key, 'value': key} for key in sample_filters_by_index.keys()],
                value='',
                clearable=True,
                placeholder='Select a Sample Filter'
            )], style={'width': '20%', 'margin-left': '5px'}),

        # Buttons for Graph, Table, or Radar selection
        html.Label('Toggle between Graph, Table, and Radar for your desired visualization.',
                   className='stats-label', style={'text-align': 'left', 'margin-left': '7px'}),
        html.Div([
            dbc.Button("Graph", id="stats-graph-button", n_clicks=0, className='container-button',
                       style={'margin': '5px'}),
            dbc.Button("Table", id="stats-table-button", n_clicks=0, className='container-button',
                       style={'margin': '5px'}),
            dbc.Button("Radar", id="stats-radar-button", n_clicks=0, className='container-button',
                       style={'margin': '5px'}),
        ]),
    ]),
    # Bottom Half
    # Output container for the selected chart
    html.Div([
        # Dataframe stored and updated based on filters
        dcc.Store(id='stored_df'),
        # Graph
        html.Div(id='graph-dropdown-container', children=[
            dbc.Collapse(id='scatter-object-collapse', is_open=False,
                         children=dcc.Graph(id='scatterplot-graph', style={'width': '100%', 'height': '500px'})),
            html.Div(id='graph-dropdowns', children=[
                html.Label('Select X Axis:', className='stats-label', style={'margin-left': '7px'}),
                # X Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='x-axis-dropdown',
                        options=[],
                        value='',
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
                html.Label('Select Y Axis:', className='stats-label', style={'margin-left': '7px'}),
                # Y Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='y-axis-dropdown',
                        options=[],
                        value='',
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'})
            ])
        ], style={'width': '100%', 'height': '100%', 'display': 'none'}),  # Initially hidden

        html.Div(id='stats-table-container', style={'width': '100%', 'height': '100%', 'display': 'none'}, children=[
            html.Label('Select Columns to Include in Table', className='stats-label'),
            dcc.Dropdown(
                id='stats-table-dropdown',
                options=[],
                value='',
                multi=True,
                clearable=True,
                optionHeight=40,
                style={
                    'width': '100%'
                }
            ),
            dbc.Collapse(id='table-object-collapse', is_open=False,
                         children=dcc.Graph(id='stats-data-table', style={'width': '100%', 'height': '600px'}))
        ]),

        html.Div(id='stats-radar-container', style={'width': '100%', 'height': '100%', 'display': 'none'}, children=[
            html.Div(id='stats-radar-dropdowns', children=[
                html.Div(children=[
                    html.Label('Select First Player for Radar Comparison Chart', className='stats-label'),
                    dcc.Dropdown(
                        id='player-dropdown',
                        options=[],
                        value='',
                        clearable=False,
                        optionHeight=40,
                        style={
                            'width': '100%'
                        }
                    )], style={'width': '50%', 'margin-right': '50px'}),
                html.Div(children=[
                    html.Label('Select Second Player for Radar Comparison Chart', className='stats-label'),
                    dcc.Dropdown(
                        id='player-dropdown1',
                        options=[],
                        value='',
                        clearable=False,
                        optionHeight=40,
                        style={
                            'width': '100%'
                        }
                    )], style={'width': '50%'})
            ], style={'width': '70%', 'display': 'flex', 'justify-content': 'space-between'}),

            html.Div(children=[
                dbc.Collapse(id='radar-object-collapse', is_open=False,
                             children=html.Img(id='stats-radar-chart', style={'width': '80%', 'height': '500px'})),
                html.Label('Select Radar Chart Metrics', className='stats-label'),
                dcc.Dropdown(
                    id='radar-preset-values-dropdown',
                    options=[{'label': key, 'value': key} for key in preset_radar_values_by_index.keys()],
                    value=list(preset_radar_values_by_index)[0],
                    clearable=False,
                    optionHeight=40,
                    style={
                        'width': '40%'
                    }
                ),
                html.Div(id='custom-radar-div', children=[
                    html.Label('Select Metrics to Include in Custom Radar Chart', className='stats-label'),
                    dcc.Dropdown(
                        id='custom-radar-values-dropdown',
                        options=[],
                        value=[],
                        multi=True,
                        clearable=True,
                        optionHeight=40,
                        style={'width': '100%'}
                    )],
                         style={
                             'display': 'none',
                         })
            ], style={'display': 'block', 'justify-content': 'space-around'})
        ])
    ])
])


# Callbacks -------------------------------------------------------------------------
# Pulling datasets from stored_uploads for graph dropdown
@callback(
    Output('graph-dropdowns', 'children'),
    Input('stored-uploads', 'data'),
    Input('sample-filter-dropdown', 'value'),
    State('x-axis-dropdown', 'value'),
    State('y-axis-dropdown', 'value')
)
def update_graph_dropdowns(uploaded_dataframes, selected_sample, current_x, current_y):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
    language_preference = uploaded_dataframes['language_preference']

    # if selected sample dropdown is empty
    if selected_sample == '':
        # Show the full column name if available in the international stats label dict
        if language_preference in international_stats_label_dict.keys():
            return (
                html.Label('Select X Axis:', className='stats-label', style={'margin-left': '7px'}),
                # X Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='x-axis-dropdown',
                        options=[{'label': international_stats_label_dict[language_preference][col], 'value': col}
                                 for col in stats_df.columns[:-14]],
                        value=current_x,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
                html.Label('Select Y Axis:', className='stats-label', style={'margin-left': '7px'}),
                # Y Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='y-axis-dropdown',
                        options=[{'label': international_stats_label_dict[language_preference][col], 'value': col}
                                 for col in stats_df.columns[:-14]],
                        value=current_y,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
            )
        # Pull default acronym column labels from dataframe if the user's language isn't available in the label dict.
        else:
            return (
                html.Label('Select X Axis:', className='stats-label', style={'margin-left': '7px'}),
                # X Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='x-axis-dropdown',
                        options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                        value=current_x,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
                html.Label('Select Y Axis:', className='stats-label', style={'margin-left': '7px'}),
                # Y Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='y-axis-dropdown',
                        options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                        value=current_y,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
            )
    # If user has selected a sample filter from the sample filter dropdown
    else:
        sample_x_index = sample_filters_by_index[selected_sample]['X']
        sample_y_index = sample_filters_by_index[selected_sample]['Y']
        sample_x_value = stats_df.columns[sample_x_index]
        sample_y_value = stats_df.columns[sample_y_index]
        if language_preference in international_stats_label_dict.keys():
            return (
                html.Label('Select X Axis:', className='stats-label', style={'margin-left': '7px'}),
                # X Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='x-axis-dropdown',
                        options=[{'label': international_stats_label_dict[language_preference][col], 'value': col}
                                 for col in stats_df.columns[:-14]],
                        value=sample_x_value,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
                html.Label('Select Y Axis:', className='stats-label', style={'margin-left': '7px'}),
                # Y Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='y-axis-dropdown',
                        options=[{'label': international_stats_label_dict[language_preference][col], 'value': col}
                                 for col in stats_df.columns[:-14]],
                        value=sample_y_value,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
            )
        else:
            return (
                html.Label('Select X Axis:', className='stats-label', style={'margin-left': '7px'}),
                # X Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='x-axis-dropdown',
                        options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                        value=sample_x_value,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
                html.Label('Select Y Axis:', className='stats-label', style={'margin-left': '7px'}),
                # Y Axis Dropdown
                html.Div([
                    dcc.Dropdown(
                        id='y-axis-dropdown',
                        options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                        value=sample_y_value,
                        clearable=False
                    )], style={'width': '35%', 'margin-left': '5px'}),
            )


# Pulling datasets from stored_uploads for table dropdown
@callback(
    Output('stats-table-container', 'children'),
    Input('stored-uploads', 'data')
)
def update_table_dropdowns(uploaded_data):
    stats_df = pd.read_json(io.StringIO(uploaded_data['stats']), orient='split')
    language_preference = uploaded_data['language_preference']
    default_dropdown_values = stats_df.columns[[0, 1, 2, 3]].to_list()

    if language_preference in international_stats_label_dict.keys():
        label_dict = international_stats_label_dict[language_preference]
        label_dict_values = list(label_dict.values())
        full_name_dropdown_values = [label_dict_values[n] for n in range(0, 4)]
        return (html.Label('Select Columns to Include in Table', className='stats-label'),
                dcc.Dropdown(
                    id='stats-table-dropdown',
                    options=[{'label': label_dict[col], 'value': col}
                             for col in stats_df.columns[:-14]],
                    value=full_name_dropdown_values,
                    multi=True,
                    clearable=True,
                    optionHeight=40,
                    style={
                        'width': '100%'
                    }
                ),
                dcc.Graph(id='stats-data-table', style={'width': '100%', 'height': '600px'})
                )
    else:
        return (html.Label('Select Columns to Include in Table', className='stats-label'),
                dcc.Dropdown(
                    id='stats-table-dropdown',
                    options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                    value=default_dropdown_values,
                    multi=True,
                    clearable=True,
                    optionHeight=40,
                    style={
                        'width': '100%'
                    }
                ),
                dcc.Graph(id='stats-data-table', style={'width': '100%', 'height': '600px'})
                )


# Pulling datasets from stored_uploads for custom radar dropdown
@callback(Output('custom-radar-values-dropdown', 'options'),
          Input('stored-uploads', 'data'))
def update_custom_radar_dropdown(uploaded_dataframes):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
    language_preference = uploaded_dataframes['language_preference']

    if language_preference in international_stats_label_dict.keys():
        return [{'label': international_stats_label_dict[language_preference][col], 'value': col}
                for col in stats_df.columns[:-14]]
    else:
        return [{'label': col, 'value': col} for col in stats_df.columns[:-14]]


# Combined callback for modal filter UI
@callback(
    Output('modal-dropdown-div', "children"),
    Input('stored-uploads', 'data'),
    Input('add-condition', 'n_clicks'),
    Input('clear-filter-button', 'n_clicks'),
    Input('reset-dropdowns-button', 'n_clicks'),

    State('modal-dropdown-div', "children"),
    prevent_initial_call=False
)
def update_filter_ui(uploaded_dataframes, add_clicks, clear_clicks, reset_clicks, existing_children):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
    language_preference = uploaded_dataframes['language_preference']

    df = stats_df
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    # Initial load
    if triggered_id is None or not existing_children:
        # Create initial filter UI with first dropdown
        if language_preference in international_stats_label_dict.keys():
            return [
                html.Div([
                    html.Label('Category'),
                    dcc.Dropdown(
                        id={'type': 'filter-column', 'index': 0},
                        options=[{'label': international_stats_label_dict[language_preference][col], 'value': col} for col in df.columns[:-14]],
                        value='',
                        placeholder='Select Category',
                        clearable=True
                    ),
                    html.Div(id={'type': 'filter-input-container', 'index': 0}, children=[])
                ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
            ]
        else:
            return [
                html.Div([
                    html.Label('Category'),
                    dcc.Dropdown(
                        id={'type': 'filter-column', 'index': 0},
                        options=[{'label': col, 'value': col} for col in df.columns[:-14]],
                        value='',
                        placeholder='Select Category',
                        clearable=True
                    ),
                    html.Div(id={'type': 'filter-input-container', 'index': 0}, children=[])
                ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
            ]

    # Add condition button clicked
    elif triggered_id == 'add-condition' and add_clicks > 0:
        # Create a new filter condition UI
        if language_preference in international_stats_label_dict.keys():
            new_condition = html.Div([
                html.Label('Category'),
                dcc.Dropdown(
                    id={'type': 'filter-column', 'index': add_clicks},
                    options=[{'label': international_stats_label_dict[language_preference][col], 'value': col}
                             for col in df.columns[:-14]],
                    value='',
                    placeholder='Select Category',
                    clearable=True
                ),
                html.Div(id={'type': 'filter-input-container', 'index': add_clicks}, children=[])
            ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
        else:
            new_condition = html.Div([
                html.Label('Category'),
                dcc.Dropdown(
                    id={'type': 'filter-column', 'index': add_clicks},
                    options=[{'label': col, 'value': col} for col in df.columns[:-14]],
                    value='',
                    placeholder='Select Category',
                    clearable=True
                ),
                html.Div(id={'type': 'filter-input-container', 'index': add_clicks}, children=[])
            ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})

        # Add to existing children
        updated_children = existing_children + [new_condition]
        return updated_children

    # Clear Filter button clicked
    elif triggered_id == 'clear-filter-button' and clear_clicks > 0:
        # Reset condition filter dropdowns
        if language_preference in international_stats_label_dict.keys():
            return [
                html.Div([
                    html.Label('Category'),
                    dcc.Dropdown(
                        id={'type': 'filter-column', 'index': 0},
                        options=[{'label': international_stats_label_dict[language_preference][col], 'value': col}
                                 for col in df.columns[:-14]],
                        value='',
                        placeholder='Select Category',
                        clearable=True
                    ),
                    html.Div(id={'type': 'filter-input-container', 'index': 0}, children=[])
                ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
            ]
        else:
            return [
                html.Div([
                    html.Label('Category'),
                    dcc.Dropdown(
                        id={'type': 'filter-column', 'index': 0},
                        options=[{'label': col, 'value': col} for col in df.columns[:-14]],
                        value='',
                        placeholder='Select Category',
                        clearable=True
                    ),
                    html.Div(id={'type': 'filter-input-container', 'index': 0}, children=[])
                ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
            ]

    # Close modal button clicked
    elif triggered_id == 'reset-dropdowns-button' and reset_clicks > 0:
        # Reset condition filter dropdowns
        if language_preference in international_stats_label_dict.keys():
            return [
                html.Div([
                    html.Label('Category'),
                    dcc.Dropdown(
                        id={'type': 'filter-column', 'index': 0},
                        options=[{'label': international_stats_label_dict[language_preference][col], 'value': col}
                                 for col in df.columns[:-14]],
                        value='',
                        placeholder='Select Category',
                        clearable=True
                    ),
                    html.Div(id={'type': 'filter-input-container', 'index': 0}, children=[])
                ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
            ]
        else:
            return [
                html.Div([
                    html.Label('Category'),
                    dcc.Dropdown(
                        id={'type': 'filter-column', 'index': 0},
                        options=[{'label': col, 'value': col} for col in df.columns[:-14]],
                        value='',
                        placeholder='Select Category',
                        clearable=True
                    ),
                    html.Div(id={'type': 'filter-input-container', 'index': 0}, children=[])
                ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
            ]

    # Default case
    return existing_children


@callback(
    Output({'type': 'filter-input-container', 'index': MATCH}, 'children'),
    [
        Input('stored-uploads', 'data'),
        Input({'type': 'filter-column', 'index': MATCH}, 'value'),
    ],
    prevent_initial_call=True
)
def update_filter_input_container(uploaded_dataframes, selected_column):
    if not selected_column:
        return []

    # Get the dataframe
    df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
    language_preference = uploaded_dataframes['language_preference']

    categorical_column_numbers = [0, 4, 3, 7, 126, 127]  # 'Name', 'Division', 'Club', 'Transfer Status', 'Media Description'
    categorical_columns = df.columns[categorical_column_numbers]
    numeric_column_numbers = [1, 5, 6, 117, 118, 122] # 'Age', 'Transfer Value', 'Wage', 'Apps', 'Starts', 'Int Apps'
    numeric_columns = df.columns[numeric_column_numbers]

    # Categorical columns (simple equals/not equals)
    if selected_column in categorical_columns:
        unique_values = df[selected_column].unique().tolist()
        # Alphabetically sort the list of unique values in the selected category
        unique_values.sort(key=str.lower)
        if language_preference in international_stats_label_dict.keys():
            return [
            html.Div([
                html.Label('Condition'),
                dcc.Dropdown(
                    id={'type': 'filter-condition', 'index': 0},
                    options=[
                        {'label': 'is', 'value': '='},
                        {'label': 'is not', 'value': '!='}
                    ],
                    value='=',
                    clearable=False
                ),
            ], style={'marginTop': '10px'}),
            html.Div([
                html.Label(f'Select {international_stats_label_dict[language_preference][selected_column]}'),
                dcc.Dropdown(
                    id={'type': 'filter-value', 'index': 0},
                    options=[{'label': str(val), 'value': str(val)} for val in unique_values],
                    value=str(unique_values[0]) if len(unique_values) > 0 else '',
                    clearable=False
                )
            ], style={'marginTop': '10px'})
        ]
        else:
            return [
                html.Div([
                    html.Label('Condition'),
                    dcc.Dropdown(
                        id={'type': 'filter-condition', 'index': 0},
                        options=[
                            {'label': 'is', 'value': '='},
                            {'label': 'is not', 'value': '!='}
                        ],
                        value='=',
                        clearable=False
                    ),
                ], style={'marginTop': '10px'}),
                html.Div([
                    html.Label(f'Select {selected_column}'),
                    dcc.Dropdown(
                        id={'type': 'filter-value', 'index': 0},
                        options=[{'label': str(val), 'value': str(val)} for val in unique_values],
                        value=str(unique_values[0]) if len(unique_values) > 0 else '',
                        clearable=False
                    )
                ], style={'marginTop': '10px'})
            ]

    # Position column (special handling)
    elif selected_column == df.columns[2]:
        position_values = international_position_filters[language_preference]
        return [
            html.Div([
                html.Label('Condition'),
                dcc.Dropdown(
                    id={'type': 'filter-condition', 'index': 0},
                    options=[
                        {'label': 'is', 'value': '='},
                        {'label': 'is not', 'value': '!='}
                    ],
                    value='=',
                    clearable=False
                ),
            ], style={'marginTop': '10px'}),
            html.Div([
                html.Label(f'Select {df.columns[2]}'),
                dcc.Dropdown(
                    id={'type': 'filter-value', 'index': 0},
                    options=[{'label': key, 'value': key} for key in position_values.keys()],
                    value=list(position_values.keys())[0] if position_values else '',
                    clearable=False
                )
            ], style={'marginTop': '10px'})
        ]

    # Numeric columns (can use >, <, =, !=)
    elif selected_column in numeric_columns:
        if language_preference in international_stats_label_dict.keys():
            return [
                html.Div([
                    html.Label('Condition'),
                    dcc.Dropdown(
                        id={'type': 'filter-condition', 'index': 0},
                        options=[
                            {'label': 'is', 'value': '='},
                            {'label': 'is greater than', 'value': '>'},
                            {'label': 'is less than', 'value': '<'},
                            {'label': 'is not', 'value': '!='}
                        ],
                        value='=',
                        clearable=False
                    ),
                ], style={'marginTop': '10px'}),
                html.Div([
                    html.Label(f'Enter {international_stats_label_dict[language_preference][selected_column]}: ', style={'margin-right': '5px'}),
                    dcc.Input(
                        id={'type': 'filter-value', 'index': 0},
                        type='number',
                        placeholder=f'Enter {international_stats_label_dict[language_preference][selected_column]}',
                        debounce=True
                    )
                ], style={'marginTop': '10px'})
            ]

        else:
            return [
                html.Div([
                    html.Label('Condition'),
                    dcc.Dropdown(
                        id={'type': 'filter-condition', 'index': 0},
                        options=[
                            {'label': 'is', 'value': '='},
                            {'label': 'is greater than', 'value': '>'},
                            {'label': 'is less than', 'value': '<'},
                            {'label': 'is not', 'value': '!='}
                        ],
                        value='=',
                        clearable=False
                    ),
                ], style={'marginTop': '10px'}),
                html.Div([
                    html.Label(f'Enter {selected_column}: ', style={'margin-right': '5px'}),
                    dcc.Input(
                        id={'type': 'filter-value', 'index': 0},
                        type='number',
                        placeholder=f'Enter {selected_column}',
                        debounce=True
                    )
                ], style={'marginTop': '10px'})
            ]

    # Stat columns (use percentile filtering)
    else:
        if language_preference in international_stats_label_dict.keys():
            return [
                html.Div([
                    html.Label('Condition'),
                    dcc.Dropdown(
                        id={'type': 'filter-condition', 'index': 0},
                        options=[
                            {'label': 'is', 'value': '='},
                            {'label': 'is not', 'value': '!='}
                        ],
                        value='=',
                        clearable=False
                    ),
                ], style={'marginTop': '10px'}),
                html.Div([
                    html.Label(f'Choose Percentile for {international_stats_label_dict[language_preference][selected_column]}'),
                    dcc.Dropdown(
                        id={'type': 'filter-value', 'index': 0},
                        options=[
                            {'label': 'Top 10%', 'value': 'top10'},
                            {'label': 'Top 25%', 'value': 'top25'},
                            {'label': 'Top 50%', 'value': 'top50'},
                        ],
                        value='top25',
                        clearable=False
                    )
                ], style={'marginTop': '10px'})
            ]
        else:
            return [
                html.Div([
                    html.Label('Condition'),
                    dcc.Dropdown(
                        id={'type': 'filter-condition', 'index': 0},
                        options=[
                            {'label': 'is', 'value': '='},
                            {'label': 'is not', 'value': '!='}
                        ],
                        value='=',
                        clearable=False
                    ),
                ], style={'marginTop': '10px'}),
                html.Div([
                    html.Label(f'Choose Percentile for {selected_column}'),
                    dcc.Dropdown(
                        id={'type': 'filter-value', 'index': 0},
                        options=[
                            {'label': 'Top 10%', 'value': 'top10'},
                            {'label': 'Top 25%', 'value': 'top25'},
                            {'label': 'Top 50%', 'value': 'top50'},
                        ],
                        value='top25',
                        clearable=False
                    )
                ], style={'marginTop': '10px'})
            ]


# Filter Application Callback
@callback(
    [
        Output('apply-feedback', 'children'),
        Output('stored_df', 'data'),
    ],
    [
        Input('stored-uploads', 'data'),
        Input('apply-filter-button', 'n_clicks'),
        Input('clear-filter-button', 'n_clicks'),
        Input('stored_df', 'data'),
        Input('sample-filter-dropdown', 'value')
    ],
    [
        State({'type': 'filter-column', 'index': ALL}, 'value'),
        State({'type': 'filter-condition', 'index': ALL}, 'value'),
        State({'type': 'filter-value', 'index': ALL}, 'value'),
        State('logical-operator', 'value')
    ],
    prevent_initial_call=True
)
def update_filtered_data(uploaded_dataframes, n_clicks_apply, n_clicks_clear, stored_data, sample_data,
                         filter_columns, filter_conditions, filter_values, logical_operator):
    # Function to convert input value to numeric or leave as string
    def convert_input_value(value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return value

    # Initialize the dataframe
    language_preference = uploaded_dataframes['language_preference']

    if stored_data:
        df = pd.read_json(io.StringIO(stored_data), orient='split')
    else:
        stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
        df = stats_df

    # Default feedback message
    player_count = len(df)
    feedback_message = f"{player_count} record(s) match the criteria."

    if not ctx.triggered:
        return feedback_message, df.to_json(date_format='iso', orient='split')

    if ctx.triggered[0]['value'] is None:
        trigger_id = 'Nothing triggered yet'
    else:
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        print(f"Triggered by: {trigger_id}")

    # Pull column names with column index numbers
    categorical_column_numbers = [0, 4, 3, 7, 126, 127]  # 'Name', 'Division', 'Club', 'Transfer Status', 'Media Description', 'Home-Grown Status'
    categorical_columns = df.columns[categorical_column_numbers]
    numeric_column_numbers = [1, 5, 6, 117, 118, 122] # 'Age', 'Transfer Value', 'Wage', 'Apps', 'Starts', 'Int Apps'
    numeric_columns = df.columns[numeric_column_numbers]

    # Clear Filters Button
    if trigger_id == 'clear-filter-button' and n_clicks_clear > 0:
        feedback_message = "Filters cleared."
        return feedback_message, []

    # Apply Filters Button
    elif trigger_id == 'apply-filter-button' and n_clicks_apply > 0:
        # Initialize filter conditions list
        filter_conditions_list = []
        active_filters = []

        # Convert filter values to numeric where possible
        converted_values = [convert_input_value(value) for value in filter_values]

        # Build the conditions
        for i, col in enumerate(filter_columns):
            if not col:  # Skip empty column selections
                continue

            condition = filter_conditions[i]
            value = converted_values[i]

            # Handle Categorical columns
            if col in categorical_columns:
                if condition == '=':
                    filter_conditions_list.append(df[col] == value)
                elif condition == '!=':
                    filter_conditions_list.append(df[col] != value)

            # Handle Positions
            elif col == df.columns[2]:
                if condition == '=':
                    filter_conditions_list.append(df[value] == True)
                elif condition == '!=':
                    filter_conditions_list.append(df[value] == False)

            # Handle numeric columns
            elif col in numeric_columns:
                try:
                    value = float(value)
                    if condition == '=':
                        filter_conditions_list.append(df[col] == value)
                    elif condition == '>':
                        filter_conditions_list.append(df[col] > value)
                    elif condition == '<':
                        filter_conditions_list.append(df[col] < value)
                    elif condition == '!=':
                        filter_conditions_list.append(df[col] != value)
                except (ValueError, TypeError):
                    continue

            # Handle percentile-based filters
            else:
                try:
                    if condition == '=':
                        if value == 'top10':
                            threshold = df[col].quantile(0.90)
                            filter_conditions_list.append(df[col] >= threshold)
                        elif value == 'top25':
                            threshold = df[col].quantile(0.75)
                            filter_conditions_list.append(df[col] >= threshold)
                        elif value == 'top50':
                            threshold = df[col].quantile(0.50)
                            filter_conditions_list.append(df[col] >= threshold)
                    elif condition == '!=':
                        if value == 'top10':
                            threshold = df[col].quantile(0.90)
                            filter_conditions_list.append(df[col] < threshold)
                        elif value == 'top25':
                            threshold = df[col].quantile(0.75)
                            filter_conditions_list.append(df[col] < threshold)
                        elif value == 'top50':
                            threshold = df[col].quantile(0.50)
                            filter_conditions_list.append(df[col] < threshold)
                except:
                    continue

            active_filters.append(f"{col} {condition} {value}")

        # If there are no valid conditions, return the original dataframe
        if not filter_conditions_list:
            feedback_message = "No valid filters found."
            return feedback_message, df.to_json(date_format='iso', orient='split')

        # Combine all conditions based on logical operator (AND/OR)
        try:
            if logical_operator == 'AND':
                combined_filter = filter_conditions_list[0]
                for condition in filter_conditions_list[1:]:
                    combined_filter &= condition
            else:  # 'OR'
                combined_filter = filter_conditions_list[0]
                for condition in filter_conditions_list[1:]:
                    combined_filter |= condition

            # Apply the final filter to the dataframe
            filtered_df = df[combined_filter]

            # Display feedback message
            filtered_count = len(filtered_df)
            feedback_message = f"Filters applied. {filtered_count} record(s) match the criteria."

            return feedback_message, filtered_df.to_json(date_format='iso', orient='split')
        except Exception as e:
            feedback_message = f"Error applying filters: {str(e)}"
            return feedback_message, df.to_json(date_format='iso', orient='split')

    # Handle Sample Filter Dropdown Changes
    elif trigger_id in 'sample-filter-dropdown' and sample_data:
        print('Filtering data based on Sample Filter Selection')
        df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
        print(f'Initialized dataframe with shape: {df.shape}')
        combined_filter = pd.Series([True] * len(df),
                                    index=df.index)  # Initialize with all True to start with AND logic
        try:
            print(f'sample_filters_by_index[sample_data].items(): {sample_filters_by_index[sample_data].items()}')
            for category, criteria in sample_filters_by_index[sample_data].items():
                # Handle position filters
                if 'Position' in category:
                    if isinstance(criteria, list):
                        def filter_dataframe_true_values(df, columns):
                            mask = df.iloc[:, columns].any(axis=1)
                            return df[mask]

                        filtered_df = filter_dataframe_true_values(df, criteria)
                        print(f'filtered_df: {filtered_df.shape}')
                    else:
                        filtered_df = df[df.iloc[:, criteria] == True]
                # Handle Age filter
                if 'Age' in category:
                    age_column = df.columns[1]
                    if 'Position' in category:
                        filtered_df = filtered_df[filtered_df.iloc[:, 1] <= criteria]
                    else:
                        filtered_df = df[df[age_column] <= criteria]
                # Handle top10 quantile filters
                if 'top10' in category:
                    top10_filter = pd.Series([False] * len(filtered_df), index=filtered_df.index)  # Initialize with False
                    for col in criteria:
                        try:
                            percentile_90 = filtered_df.iloc[:, col].quantile(0.90)
                            print(f'percentile_90 for {col}: {percentile_90}')
                            top10_filter = top10_filter | (filtered_df.iloc[:, col] >= percentile_90)  # OR operation
                        except Exception as e:
                            print(f'Could not apply top10 filter: {e}')
                    combined_filter = top10_filter
                if 'Media Description' in category:
                    media_description_filter = pd.Series([False] * len(filtered_df), index=filtered_df.index)  # Initialize with False
                    for description in criteria:
                        try:
                            media_description_filter = media_description_filter | filtered_df.iloc[:, 126].astype(
                                str).str.contains(description, case=False, na=False)
                        except Exception as e:
                            print(
                                f"Could not apply 'media_description_filter' for keyword '{description}': {e}")
                    if 'top10' in sample_filters_by_index[sample_data]:  # Check if top10 filter was also applied
                        combined_filter = combined_filter | media_description_filter
                    else:
                        combined_filter = media_description_filter
                if 'top10' in category or 'media_description_filter' in category:
                    sample_df = filtered_df[combined_filter]
                    print(f'sample_df: {sample_df.shape}')
            filtered_count = len(sample_df)
            feedback_message = f"{filtered_count} record(s) match the criteria."
            return feedback_message, sample_df.to_json(date_format='iso', orient='split')
        except Exception as e:
            feedback_message = f"Error applying sample chart filters: {str(e)}"
            return feedback_message, df.to_json(date_format='iso', orient='split')

    # Default return
    return feedback_message, df.to_json(date_format='iso', orient='split')


# Callback to display plot based on button clicked
@callback(
    Output('stats-table-container', 'style'),
    Output('graph-dropdown-container', 'style'),
    Output('stats-radar-container', 'style'),
    Input('stats-table-button', 'n_clicks'),
    Input('stats-graph-button', 'n_clicks'),
    Input('stats-radar-button', 'n_clicks')
)
def toggle_containers(table_clicks, graph_clicks, radar_clicks):
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if triggered_id == 'stats-table-button':
        return ({'width': '100%', 'height': '100%', 'display': 'block'},
                {'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'none'})
    elif triggered_id == 'stats-graph-button':
        return ({'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'block'},
                {'width': '100%', 'height': '100%', 'display': 'none'})
    elif triggered_id == 'stats-radar-button':
        return ({'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'block'})
    else:
        return ({'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'none'})


# Visualization Callback
@callback(
    [
        Output('scatterplot-graph', 'figure'),
        Output('stats-data-table', 'figure'),
        Output('stats-radar-chart', 'src'),
        Output('player-dropdown', 'options'),
        Output('player-dropdown1', 'options'),
    ],
    [
        Input('stored-uploads', 'data'),
        Input('stats-graph-button', 'n_clicks'),
        Input('stats-table-button', 'n_clicks'),
        Input('stats-radar-button', 'n_clicks'),
        Input('x-axis-dropdown', 'value'),
        Input('y-axis-dropdown', 'value'),
        Input('stats-table-dropdown', 'value'),
        Input('player-dropdown', 'value'),
        Input('player-dropdown1', 'value'),
        Input('radar-preset-values-dropdown', 'value'),
        Input('custom-radar-values-dropdown', 'value'),
        Input('sample-filter-dropdown', 'value'),
        Input('stored_df', 'data')
    ],
    prevent_initial_call=True
)
def update_visualization(uploaded_dataframes, graph_clicks, table_clicks, radar_clicks, selected_x, selected_y,
                         selected_col,
                         selected_player, selected_player1, selected_radar_preset, selected_metrics, selected_sample,
                         stored_data):
    # Get dataframes
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
    squad_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['squad_attributes']), orient='split')
    language_preference = uploaded_dataframes['language_preference']

    # Default empty figure
    empty_fig = px.scatter(x=[0], y=[0])
    empty_fig.update_layout(
        xaxis_title='X Axis',
        yaxis_title='Y Axis'
    )
    empty_table = {}
    empty_radar = ''
    default_player_options = [{'label': f'{name} - {position}', 'value': name}
                              for name, position in zip(stats_df.iloc[:, 0], stats_df.iloc[:, 2])]

    # Check for valid data
    if not stored_data:
        print("No stored data found")
        return empty_fig, empty_table, empty_radar, default_player_options, default_player_options,

    try:
        # Convert stored data to df
        stored_df = pd.read_json(io.StringIO(stored_data), orient='split')
        print(f"Successfully loaded DataFrame with shape: {stored_df.shape}")

    except Exception as e:
        print(f"Error converting stored data to DataFrame: {str(e)}")
        return empty_fig, empty_table, empty_radar, default_player_options, default_player_options,

    if not ctx.triggered:
        print("No context triggered")
        return empty_fig, empty_table, empty_radar, default_player_options, default_player_options,

    if ctx.triggered[0]['value'] is None:
        trigger_id = 'No clicks yet'
    else:
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        print(f"Triggered by: {trigger_id}")

    stored_player_options = [{'label': f'{name} - {position} - {club}', 'value': name}
                             for name, position, club in zip(stored_df.iloc[:, 0], stored_df.iloc[:, 2], stored_df.iloc[:, 3])]

    # Handle graph button
    if 'graph-button' in trigger_id and graph_clicks > 0:
        if selected_x and selected_y:
            print(f"Creating scatter plot with {selected_x} vs {selected_y}")
            try:
                def set_color(df):
                    values = df.iloc[:, 3].to_list()
                    color_list = []
                    for i in values:
                        if i == squad_attributes_df.iloc[0, 3]:
                            color_list.append('red')
                        else:
                            color_list.append('blue')
                    return color_list

                player_name = stored_df.columns[0]
                player_club = stored_df.columns[3]
                player_age = stored_df.columns[1]
                if language_preference in international_stats_label_dict.keys():
                    fig = px.scatter(stored_df, x=selected_x, y=selected_y,
                                     title=f"{international_stats_label_dict[language_preference][selected_x]} vs "
                                           f"{international_stats_label_dict[language_preference][selected_y]}",
                                     hover_data=[player_name, player_club, player_age])
                    fig.update_traces(marker=dict(color=set_color(stored_df)))
                else:
                    fig = px.scatter(stored_df, x=selected_x, y=selected_y,
                                     title=f"{selected_x} vs {selected_y}",
                                     hover_data=[player_name, player_club, player_age])
                    fig.update_traces(marker=dict(color=set_color(stored_df)))
                # Check and reverse x-axis
                print(f'Checking for reverse x-axis, stored_df: {stored_df.shape}')
                if stored_df.columns.get_loc(selected_x) in negative_stat_categories:
                    fig.update_layout(xaxis=dict(autorange="reversed"))
                else:
                    fig.update_layout(xaxis=dict(autorange=True))
                # Check and reverse y-axis
                if stored_df.columns.get_loc(selected_y) in negative_stat_categories:
                    fig.update_layout(yaxis=dict(autorange="reversed"))
                else:
                    fig.update_layout(yaxis=dict(autorange=True))
                return fig, empty_table, empty_radar, stored_player_options, stored_player_options,
            except Exception as e:
                print(f"Error creating scatter plot: {str(e)}")
                return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,
        else:
            print("Invalid axis selection")
            empty_fig.update_layout(title='Select X and Y Axis or Select a Sample Filter')
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle table button
    elif 'table-button' in trigger_id and table_clicks > 0:
        print("Creating table view")
        try:
            # Create a Table
            if selected_col == '':
                print('Creating table with all columns.')
                layout = Layout(
                    paper_bgcolor=px.colors.qualitative.Pastel1[8]
                )
                fig = go.Figure(data=[go.Table(
                    header=dict(values=list(stored_df.columns),
                                fill_color='lavender',
                                align='left'),
                    cells=dict(values=stored_df.transpose().values.tolist(),
                               fill_color='white',
                               align='left')
                )],
                    layout=layout)
                fig.update_layout(title='Data Table View',
                                  updatemenus=[
                                      {
                                          # a button for each table column
                                          'buttons': [
                                              {
                                                  'method': 'restyle',
                                                  'label': btn_label,
                                                  'args': [
                                                      {
                                                          'cells': {
                                                              'values': stored_df.sort_values(btn_label,
                                                                                              ascending=False).transpose().values.tolist(),
                                                              # update the cell values with the sorted data
                                                              # format table as before
                                                              'fill': dict(color=px.colors.qualitative.Pastel1[8]),
                                                              'align': 'left',
                                                          }
                                                      }
                                                  ],
                                              }
                                              for btn_label in stored_df.columns
                                          ],
                                          'direction': 'down',
                                      }
                                  ]
                                  )
                return empty_fig, fig, empty_radar, stored_player_options, stored_player_options,

            else:
                print(f'Creating table with columns {selected_col}.')
                new_df = stored_df[selected_col]
                layout = Layout(
                    paper_bgcolor=px.colors.qualitative.Pastel1[8]
                )
                fig = go.Figure(data=[go.Table(
                    header=dict(values=list(new_df.columns),
                                fill_color='lavender',
                                align='left'),
                    cells=dict(values=new_df.transpose().values.tolist(),
                               fill_color='white',
                               align='left')
                )],
                    layout=layout)
                fig.update_layout(title='Data Table View',
                                  updatemenus=[
                                      {
                                          # a button for each table column
                                          'buttons': [
                                              {
                                                  'method': 'restyle',
                                                  'label': btn_label,
                                                  'args': [
                                                      {
                                                          'cells': {
                                                              'values': new_df.sort_values(btn_label,
                                                                                           ascending=False).transpose().values.tolist(),
                                                              # update the cell values with the sorted data
                                                              # format table as before
                                                              'fill': dict(color=px.colors.qualitative.Pastel1[8]),
                                                              'align': 'left',
                                                          }
                                                      }
                                                  ],
                                              }
                                              for btn_label in new_df.columns
                                          ],
                                          'direction': 'down',
                                      }
                                  ]
                                  )
                return empty_fig, fig, empty_radar, stored_player_options, stored_player_options,

        except Exception as e:
            print(f"Error creating table: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle axis dropdown changes
    elif trigger_id in ['x-axis-dropdown', 'y-axis-dropdown'] and selected_x and selected_y:
        print(f"Updating plot for axis change: {selected_x} vs {selected_y}")
        try:
            def set_color(df):
                # Change color of squad players on scatter plot
                values = df.iloc[:, 3].to_list()
                color_list = []
                for i in values:
                    if i == squad_attributes_df.iloc[0, 3]:
                        color_list.append('red')
                    else:
                        color_list.append('blue')
                return color_list

            player_name = stored_df.columns[0]
            player_club = stored_df.columns[3]
            player_age = stored_df.columns[1]
            if language_preference in international_stats_label_dict.keys():
                fig = px.scatter(stored_df, x=selected_x, y=selected_y,
                                 title=f"{international_stats_label_dict[language_preference][selected_x]} vs "
                                       f"{international_stats_label_dict[language_preference][selected_y]}",
                                 hover_data=[player_name, player_club, player_age] if all(
                                     col in stored_df.columns for col in [player_name, player_club, player_age]) else None)
                fig.update_traces(marker=dict(color=set_color(stored_df)))
            else:
                fig = px.scatter(stored_df, x=selected_x, y=selected_y,
                                 title=f"{selected_x} vs {selected_y}",
                                 hover_data=[player_name, player_club, player_age] if all(
                                     col in stored_df.columns for col in
                                     [player_name, player_club, player_age]) else None)
                fig.update_traces(marker=dict(color=set_color(stored_df)))

            # Check and reverse x-axis
            if stored_df.columns.get_loc(selected_x) in negative_stat_categories:
                fig.update_layout(xaxis=dict(autorange="reversed"))
            else:
                fig.update_layout(xaxis=dict(autorange=True))
            # Check and reverse y-axis
            if stored_df.columns.get_loc(selected_y) in negative_stat_categories:
                fig.update_layout(yaxis=dict(autorange="reversed"))
            else:
                fig.update_layout(yaxis=dict(autorange=True))
            return fig, empty_table, empty_radar, stored_player_options, stored_player_options,
        except Exception as e:
            print(f"Error updating plot for axis change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle Sample Filter dropdown changes
    elif trigger_id in 'sample-filter-dropdown' and selected_sample:
        try:
            def set_color(df):
                # Change color of squad players on scatter plot
                values = df.iloc[:, 3].to_list()
                color_list = []
                for i in values:
                    if i == squad_attributes_df.iloc[0, 3]:
                        color_list.append('red')
                    else:
                        color_list.append('blue')
                return color_list

            player_name = stored_df.columns[0]
            player_club = stored_df.columns[3]
            player_age = stored_df.columns[1]
            sample_x_index = sample_filters_by_index[selected_sample]['X']
            sample_y_index = sample_filters_by_index[selected_sample]['Y']
            sample_x_value = stored_df.columns[sample_x_index]
            sample_y_value = stored_df.columns[sample_y_index]
            print(f'Creating scatter plot for {selected_sample} with X: {selected_x} and Y: {selected_y}')
            fig = px.scatter(stored_df, x=sample_x_value, y=sample_y_value,
                             title=f'{selected_sample}',
                             hover_data=[player_name, player_club, player_age] if all(
                                 col in stored_df.columns for col in [player_name, player_club, player_age]) else None)
            fig.update_traces(marker=dict(color=set_color(stored_df)))
            # Check and reverse x-axis
            if sample_x_index in negative_stat_categories:
                fig.update_layout(xaxis=dict(autorange='reversed'))
            else:
                fig.update_layout(xaxis=dict(autorange=True))
            # Check and reverse y-axis
            if sample_y_index in negative_stat_categories:
                fig.update_layout(yaxis=dict(autorange='reversed'))
            else:
                fig.update_layout(yaxis=dict(autorange=True))
            fig.update_layout(title=f'{selected_sample}')
            return fig, empty_table, empty_radar, stored_player_options, stored_player_options,
        except Exception as e:
            print(f"Error updating plot for axis change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle Table dropdown changes
    elif trigger_id in 'stats-table-dropdown' and selected_col:
        try:
            new_df = stored_df[selected_col]
            layout = Layout(paper_bgcolor=px.colors.qualitative.Pastel1[8])
            fig = go.Figure(data=[go.Table(
                header=dict(values=list(new_df.columns),
                            fill_color='lavender',
                            align='left'),
                cells=dict(values=new_df.transpose().values.tolist(),
                           fill_color='white',
                           align='left')
            )],
                layout=layout)
            fig.update_layout(title='Data Table View',
                              updatemenus=[
                                  {
                                      # a button for each table column
                                      'buttons': [
                                          {
                                              'method': 'restyle',
                                              'label': btn_label,
                                              'args': [
                                                  {
                                                      'cells': {
                                                          'values': new_df.sort_values(
                                                              btn_label, ascending=False).transpose().values.tolist(),
                                                          # update the cell values with the sorted data
                                                          # format table as before
                                                          'fill': dict(color=px.colors.qualitative.Pastel1[8]),
                                                          'align': 'left',
                                                      }
                                                  }
                                              ],
                                          }
                                          for btn_label in new_df.columns
                                      ],
                                      'direction': 'down',
                                  }
                              ]
                              )
            return empty_fig, fig, empty_radar, stored_player_options, stored_player_options,
        except Exception as e:
            print(f"Error updating table for dropdown change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle Radar Button
    elif 'radar-button' in trigger_id and radar_clicks > 0:
        if selected_player and selected_player1:
            print(f"Creating radar plot with {selected_player} vs {selected_player1}")
            try:
                # Reset stored_df index
                stored_df.reset_index(inplace=True, drop=True)

                ## player index. Pulling the df index number for the selected player names
                player_index = stored_df.index[stored_df.iloc[:, 0] == selected_player][0]
                player1_index = stored_df.index[stored_df.iloc[:, 0] == selected_player1][0]

                ## parameter names
                if selected_metrics == []:
                    param_columns = preset_radar_values_by_index[selected_radar_preset]
                    params = stored_df.columns[param_columns]
                else:
                    params = selected_metrics

                ## range values
                ranges = [(0, stored_df[metric].max()) for metric in params]

                ## parameter value
                player_values = []
                player1_values = []
                for metric in params:
                    player_values.append(stored_df.iloc[player_index][metric])
                for metric in params:
                    player1_values.append(stored_df.iloc[player1_index][metric])

                values = [player_values, player1_values]

                # Dynamically select radar chart font family to display characters in the user's language correctly
                if language_preference == 'Chinese':
                    font_family = 'SimSun'
                elif language_preference == 'Japanese':
                    font_family = 'MS Gothic'
                elif language_preference == 'Korean':
                    font_family = 'Malgun Gothic'
                else:
                    font_family = 'Arial'

                ## title
                title = dict(
                    title_name=stored_df.iloc[player_index, 0],
                    title_color='#FF69B4',
                    subtitle_name=stored_df.iloc[player_index, 3],
                    subtitle_color='#FF69B4',
                    title_name_2=stored_df.iloc[player1_index, 0],
                    title_color_2='#344D94',
                    subtitle_name_2=stored_df.iloc[player1_index, 3],
                    subtitle_color_2='#7FFF00',
                    title_fontsize=25,
                    subtitle_fontsize=20,
                )

                ## instantiate object
                radar = Radar(fontfamily=font_family, background_color='#483d8b', patch_color="#28252C",
                              label_color="#F0FFF0", range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

                ## plot radar -- compare
                fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values,
                                           radar_color=['#FF69B4', '#7FFF00'],
                                           title=title, compare=True)

                # Save it to a temporary buffer.
                buf = BytesIO()
                fig.savefig(buf, format="png")
                # Embed the result in the html output.
                fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
                fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

                return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options,

            except Exception as e:
                print(f"Error creating radar plot: {str(e)}")
                return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,
        else:
            print("Invalid player selection")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle radar player dropdown changes
    elif trigger_id in ['player-dropdown', 'player-dropdown1'] and selected_player and selected_player1:
        print(f"Updating plot for dropdown change: {selected_player} vs {selected_player1}")
        try:
            # Reset stored_df index
            stored_df.reset_index(inplace=True, drop=True)

            ## player index. Pulling the df index number for the selected player names
            player_index = stored_df.index[stored_df.iloc[:, 0] == selected_player][0]
            player1_index = stored_df.index[stored_df.iloc[:, 0] == selected_player1][0]

            ## parameter names
            if selected_metrics == []:
                param_columns = preset_radar_values_by_index[selected_radar_preset]
                params = stored_df.columns[param_columns]
            else:
                params = selected_metrics

            ## range values
            ranges = [(0, stored_df[metric].max()) for metric in params]

            ## parameter value
            player_values = []
            player1_values = []
            for metric in params:
                player_values.append(stored_df.iloc[player_index][metric])
            for metric in params:
                player1_values.append(stored_df.iloc[player1_index][metric])

            values = [player_values, player1_values]

            # Dynamically select radar chart font family to display characters in the user's language correctly
            if language_preference == 'Chinese':
                font_family = 'SimSun'
            elif language_preference == 'Japanese':
                font_family = 'MS Gothic'
            elif language_preference == 'Korean':
                font_family =  'Malgun Gothic'
            else:
                font_family =  'Arial'

            ## title
            title = dict(
                title_name=stored_df.iloc[player_index, 0],
                title_color='#FF69B4',
                subtitle_name=stored_df.iloc[player_index, 3],
                subtitle_color='#FF69B4',
                title_name_2=stored_df.iloc[player1_index, 0],
                title_color_2='#7FFF00',
                subtitle_name_2=stored_df.iloc[player1_index, 3],
                subtitle_color_2='#7FFF00',
                title_fontsize=25,
                subtitle_fontsize=20,
            )

            ## instantiate object
            radar = Radar(fontfamily=font_family, background_color='#483d8b', patch_color="#28252C", label_color="#F0FFF0",
                          range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

            ## plot radar -- compare
            fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values,
                                       radar_color=['#FF69B4', '#7FFF00'],
                                       title=title, compare=True)

            # Save it to a temporary buffer.
            buf = BytesIO()
            fig.savefig(buf, format="png")
            # Embed the result in the html output.
            fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
            fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

            return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options,

        except Exception as e:
            print(f"Error updating plot for axis change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle Radar Chart Preset Metrics Dropdown Changes
    elif trigger_id in 'radar-preset-values-dropdown' and selected_radar_preset:
        print(f"Updating plot for radar preset dropdown change: {selected_player} vs {selected_player1}")
        try:
            # Reset stored_df index
            stored_df.reset_index(inplace=True, drop=True)

            ## player index. Pulling the df index number for the selected player names
            player_index = stored_df.index[stored_df.iloc[:, 0] == selected_player][0]
            player1_index = stored_df.index[stored_df.iloc[:, 0] == selected_player1][0]

            ## parameter names
            if selected_metrics == []:
                param_columns = preset_radar_values_by_index[selected_radar_preset]
                params = stored_df.columns[param_columns]
            else:
                params = selected_metrics

            ## range values
            ranges = [(0, stored_df[metric].max()) for metric in params]

            ## parameter value
            player_values = []
            player1_values = []
            for metric in params:
                player_values.append(stored_df.iloc[player_index][metric])
            for metric in params:
                player1_values.append(stored_df.iloc[player1_index][metric])

            values = [player_values, player1_values]

            # Dynamically select radar chart font family to display characters in the user's language correctly
            if language_preference == 'Chinese':
                font_family = 'SimSun'
            elif language_preference == 'Japanese':
                font_family = 'MS Gothic'
            elif language_preference == 'Korean':
                font_family =  'Malgun Gothic'
            else:
                font_family =  'Arial'

            ## title
            title = dict(
                title_name=stored_df.iloc[player_index, 0],
                title_color='#FF69B4',
                subtitle_name=stored_df.iloc[player_index, 3],
                subtitle_color='#FF69B4',
                title_name_2=stored_df.iloc[player1_index, 0],
                title_color_2='#7FFF00',
                subtitle_name_2=stored_df.iloc[player1_index, 3],
                subtitle_color_2='#7FFF00',
                title_fontsize=25,
                subtitle_fontsize=20,
            )

            ## instantiate object
            radar = Radar(fontfamily=font_family, background_color='#483d8b', patch_color="#28252C", label_color="#F0FFF0",
                          range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

            ## plot radar -- compare
            fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values,
                                       radar_color=['#FF69B4', '#7FFF00'],
                                       title=title, compare=True)

            # Save it to a temporary buffer.
            buf = BytesIO()
            fig.savefig(buf, format="png")
            # Embed the result in the html output.
            fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
            fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

            return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options,


        except Exception as e:
            print(f"Error updating plot for radar preset change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Handle Custom Radar Metrics Dropdown Change
    elif trigger_id in 'custom-radar-values-dropdown' and selected_metrics:
        print(f"Updating plot for dropdown change: {selected_player} vs {selected_player1}")
        try:
            # Reset stored_df index
            stored_df.reset_index(inplace=True, drop=True)

            ## player index. Pulling the df index number for the selected player names
            player_index = stored_df.index[stored_df.iloc[:, 0] == selected_player][0]
            player1_index = stored_df.index[stored_df.iloc[:, 0] == selected_player1][0]

            ## parameter names
            if selected_metrics == []:
                param_columns = preset_radar_values_by_index[selected_radar_preset]
                params = stored_df.columns[param_columns]
            else:
                params = selected_metrics

            ## range values
            ranges = [(0, stored_df[metric].max()) for metric in params]

            ## parameter value
            player_values = []
            player1_values = []
            for metric in params:
                player_values.append(stored_df.iloc[player_index][metric])
            for metric in params:
                player1_values.append(stored_df.iloc[player1_index][metric])

            values = [player_values, player1_values]

            # Dynamically select radar chart font family to display characters in the user's language correctly
            if language_preference == 'Chinese':
                font_family = 'SimSun'
            elif language_preference == 'Japanese':
                font_family = 'MS Gothic'
            elif language_preference == 'Korean':
                font_family =  'Malgun Gothic'
            else:
                font_family =  'Arial'

            ## title
            title = dict(
                title_name=stored_df.iloc[player_index, 0],
                title_color='#FF69B4',
                subtitle_name=stored_df.iloc[player_index, 3],
                subtitle_color='#FF69B4',
                title_name_2=stored_df.iloc[player1_index, 0],
                title_color_2='#7FFF00',
                subtitle_name_2=stored_df.iloc[player1_index, 3],
                subtitle_color_2='#7FFF00',
                title_fontsize=25,
                subtitle_fontsize=20,
            )

            ## instantiate object
            radar = Radar(fontfamily=font_family, background_color='#483d8b', patch_color="#28252C", label_color="#F0FFF0",
                          range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

            ## plot radar -- compare
            fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values,
                                       radar_color=['#FF69B4', '#7FFF00'],
                                       title=title, compare=True)

            # Save it to a temporary buffer.
            buf = BytesIO()
            fig.savefig(buf, format="png")
            # Embed the result in the html output.
            fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
            fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

            return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options,

        except Exception as e:
            print(f"Error updating plot for custom radar change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,

    # Default return
    return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options,


# Handle the collapsed scatter plot
@callback(
    Output('scatter-object-collapse', 'is_open'),
    Input('scatterplot-graph', 'figure'),
    State('scatter-object-collapse', 'is_open'),
)
def toggle_collapsed_stats_scatter(scatter_fig, scatter_is_open):
    # Default empty figure
    empty_fig = px.scatter(x=[0], y=[0])
    empty_fig.update_layout(
        title='No data available',
        xaxis_title='X Axis',
        yaxis_title='Y Axis'
    )

    if scatter_fig == empty_fig:
        if scatter_is_open == True:
            return not scatter_is_open
        else:
            return scatter_is_open
    else:
        if scatter_is_open == True:
            return scatter_is_open
        else:
            return not scatter_is_open


# Handle the collapsed table
@callback(
    Output('table-object-collapse', 'is_open'),
    Input('stats-data-table', 'figure'),
    State('table-object-collapse', 'is_open')
)
def toggle_collapsed_stats_scatter(table_fig, table_is_open):
    # Default empty figure
    empty_table = {}

    if table_fig == empty_table:
        if table_is_open == True:
            return not table_is_open
        else:
            return table_is_open
    else:
        if table_is_open == True:
            return table_is_open
        else:
            return not table_is_open


# Handle the collapsed scatter plot
@callback(
    Output('radar-object-collapse', 'is_open'),
    Input('stats-radar-chart', 'src'),
    State('radar-object-collapse', 'is_open')
)
def toggle_collapsed_stats_scatter(radar_fig, radar_is_open):
    # Default empty figure
    empty_radar = ''

    if radar_fig == empty_radar:
        if radar_is_open == True:
            return not radar_is_open
        else:
            return radar_is_open
    else:
        if radar_is_open == True:
            return radar_is_open
        else:
            return not radar_is_open


@callback(
    Output('custom-radar-div', 'style'),
    Input('radar-preset-values-dropdown', 'value')
)
def show_custom_radar_values_dropdown(radar_preset_dropdown):
    if radar_preset_dropdown == 'Custom':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    [
        Output('apply-filter-button', 'n_clicks'),
        Output('clear-filter-button', 'n_clicks'),
        Output('stats-graph-button', 'n_clicks'),
        Output('stats-table-button', 'n_clicks'),
        Output('stats-radar-button', 'n_clicks'),
        Output('add-condition', 'n_clicks'),
    ],
    [
        Input('apply-filter-button', 'n_clicks'),
        Input('clear-filter-button', 'n_clicks'),
        Input('stats-graph-button', 'n_clicks'),
        Input('stats-table-button', 'n_clicks'),
        Input('stats-radar-button', 'n_clicks'),
        Input('add-condition', 'n_clicks'),
    ],
)
def reset_buttons(n_clicks_apply, n_clicks_clear, n_clicks_graph, n_clicks_table, n_clicks_radar, add_clicks):
    if not ctx.triggered:
        return 0, 0, 0, 0, 0, 0

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    # If Button 1 is clicked, reset other buttons' n_clicks to 0
    if button_id == 'apply-filter-button':
        return n_clicks_apply, 0, 0, 0, 0, 0
    # If Button 2 is clicked, reset other buttons' n_clicks to 0
    elif button_id == 'clear-filter-button':
        return 0, n_clicks_clear, 0, 0, 0, 0
    # If Button 3 is clicked, reset other buttons' n_clicks to 0
    elif button_id == 'stats-graph-button':
        return 0, 0, n_clicks_graph, 0, 0, 0
    elif button_id == 'stats-table-button':
        return 0, 0, 0, n_clicks_table, 0, 0
    elif button_id == 'stats-radar-button':
        return 0, 0, 0, 0, n_clicks_radar, 0
    elif button_id == 'add-condition':
        return 0, 0, 0, 0, 0, add_clicks

    return 0, 0, 0, 0, 0, 0


# filter modal callback
@callback(
    Output("filter-modal", "is_open"),
    [Input("open-modal-button", "n_clicks"),
     Input("close-modal-button", "n_clicks")],
    [State("filter-modal", "is_open")]
)
def toggle_modal(open_clicks, close_clicks, is_open):
    if not ctx.triggered:
        return is_open

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "open-modal-button":
        return True
    elif button_id == "close-modal-button":
        return False

    return is_open