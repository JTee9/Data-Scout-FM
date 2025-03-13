# Todo ------------------
# 1. Long names overlap on the radar chart.
# 2. Fix empty fig objects to make the default page look better.

import base64
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
import io


# Register Page
dash.register_page(__name__, path='/stats', title='Scout FM Stats')


preset_radar_values = {
    'Goalkeeper': ['Apps', 'Av Rat', 'xSv %', 'xGP/90', 'Pens Saved Ratio', 'PoM', 'Saves/90', 'Clr/90', 'Pas %', 'Ps C/90', 'Sv %', 'Svh', 'Svp', 'Svt', 'Cln/90', 'Con/90'],
    'Central Defender': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Shts Blckd/90', 'Pr passes/90', 'Poss Won/90', 'Ps C/90', 'Pas %', 'Int/90', 'Hdrs W/90', 'Hdr %', 'Clr/90', 'Blk/90', 'Yel'],
    'Full-back': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Poss Won/90', 'Poss Lost/90', 'Ps C/90', 'Pas %', 'Int/90', 'Distance', 'Cr C/90', 'Cr C/A', 'Fls', 'Yel'],
    'Wing-Back': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Poss Won/90', 'Poss Lost/90', 'Pas %', 'Int/90', 'Distance', 'Cr C/90', 'Cr C/A', 'OP-Crs C/90', 'Ch C/90', 'Asts/90', 'Drb/90', 'Sprints/90'],
    'Defensive Midfielder': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Pr passes/90', 'Poss Won/90', 'Poss Lost/90', 'Ps C/90', 'Pas %', 'K Ps/90', 'Int/90', 'Pres C/90', 'Hdrs W/90', 'Hdr %',],
    'Central Midfielder': ['Apps', 'Av Rat', 'Tck/90', 'Int/90', 'Pr passes/90', 'Poss Won/90', 'Poss Lost/90', 'Pas %', 'K Ps/90', 'Distance', 'Ch C/90', 'Asts/90', 'Pres C/90', 'ShT/90'],
    'Attacking Midfielder': ['Apps', 'Av Rat', 'Pas %', 'Ch C/90', 'Asts/90', 'xA/90', 'Poss Lost/90', 'K Ps/90', 'OP-KP/90', 'Drb/90', 'xG/shot', 'Gls/90', 'xG/90'],
    'Winger': ['Apps', 'Av Rat', 'Poss Lost/90', 'Pres C/90', 'Drb/90', 'Sprints/90', 'FA', 'Ch C/90', 'OP-KP/90', 'Cr C/90', 'Cr C/A', 'OP-Crs C/90', 'xG/shot', 'Gls/90', 'xG/90'],
    'Striker': ['Apps', 'Av Rat', 'Pres C/90', 'Poss Won/90', 'Shot/90', 'Shot %', 'Sprints/90', 'Hdrs W/90', 'Hdr %', 'xG/shot', 'Conv %', 'Asts/90', 'NP-xG/90', 'Gls/90', 'xG/90'],
    'Custom': []
}

position_filters = {
        'GK': ['GK'],
        'D (C)': ['D (C)', 'D (RC)', 'D (LC)', 'D (RLC)'],
        'D (R)': ['D (R)', 'D (RL)', 'D (RC)', 'D (RLC)', 'D/WB (R)', 'D/WB (RL)',
                  'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M/AM (R)', 'D/WB/M/AM (RL)',
                  'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)', 'D/M (R)', 'D/M (RL)'],
        'D (L)': ['D (L)', 'D (RL)', 'D (LC)', 'D (RLC)', 'D/WB (L)', 'D/WB (RL)',
                  'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/M (L)', 'D/M (RL)'],
        'WB (R)': ['D/WB (R)', 'D/WB (RL)', 'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)',
                   'D/WB/M (RLC)', 'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)',
                   'D/WB/M/AM (RLC)', 'WB (R)', 'WB (RL)', 'WB/M (R)', 'WB/M (RL)',
                   'WB/M (RC)', 'WB/M (RLC)', 'WB/M/AM (R)', 'WB/M/AM (RL)'],
        'WB (L)': ['D/WB (L)', 'D/WB (RL)', 'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)',
                   'D/WB/M (RLC)', 'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)',
                   'D/WB/M/AM (RLC)', 'WB (L)', 'WB (RL)', 'WB/M (L)', 'WB/M (RL)',
                   'WB/M (LC)', 'WB/M (RLC)', 'WB/M/AM (L)', 'WB/M/AM (RL)'],
        'M (R)': ['D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)', 'D/WB/M/AM (R)',
                  'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)', 'WB/M (R)', 'WB/M (RL)',
                  'WB/M (RC)', 'WB/M (RLC)', 'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)',
                  'WB/M/AM (RLC)', 'M (R)', 'M (RL)', 'M (RC)', 'M (RLC)', 'M/AM (R)', 'M/AM (RL)',
                  'M/AM (RC)', 'M/AM (RLC)'],
        'M (L)': ['D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)', 'D/WB/M/AM (L)',
                  'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)', 'WB/M (L)', 'WB/M (RL)',
                  'WB/M (LC)', 'WB/M (RLC)', 'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)',
                  'WB/M/AM (RLC)', 'M (L)', 'M (RL)', 'M (LC)', 'M (RLC)', 'M/AM (L)', 'M/AM (RL)',
                  'M/AM (LC)', 'M/AM (RLC)'],
        'DM': ['DM'],
        'M (C)': ['M (C)', 'M (RC)', 'M (LC)', 'M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)'],
        'AM (C)': ['M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)',
                   'AM (C)', 'AM (RC)', 'AM (LC)', 'AM (RLC)'],
        'AM (R)': ['D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                   'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                   'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)',
                   'AM (R)', 'AM (RL)', 'AM (RC)', 'AM (RLC)'],
        'AM (L)': ['D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                   'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                   'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)',
                   'AM (L)', 'AM (RL)', 'AM (LC)', 'AM (RLC)'],
        'ST': ['ST (C)']
    }


layout = html.Div([
    # Top Half
    html.Div(style={'text-align': 'left', 'margin-bottom': '15px'}, children=[
            html.Div(html.P('Click "Filter Data" to start filtering your Stats data. Then toggle between Graph, Table, and Radar for your desired visualization.'),
                     style={'text-align': 'center'}),
            # Player Search Modal
            html.Div([dbc.Button('Filter Data', id='open-modal-button', n_clicks=0, className='container-button', style={'margin-left': '5px', 'margin-bottom': '5px'}),
                      dbc.Modal(
                          [
                              dbc.ModalHeader('Player Search Filters'),
                              dbc.ModalBody([
                                  html.Div(id='dropdown-container-div', children=[]),

                                  html.Label('Choose logical operator for multiple conditions:'),
                                  dcc.Dropdown(
                                      id='logical-operator',
                                      options=[
                                          {'label': 'AND', 'value': 'AND'},
                                          {'label': 'OR', 'value': 'OR'}
                                      ],
                                      value='AND',
                                      clearable=False
                                  ),

                                  # Button to add more filter conditions
                                  html.Br(),
                                  dbc.Button("Add Condition", id="add-condition", className='modal_conditions_button', n_clicks=0),
                                  html.Br(),
                                  html.Br(),

                                  # Button to apply filters
                                  dbc.Button('Apply Filter', id='apply-filter-button', className='modal_conditions_button', n_clicks=0),
                                  html.Br(),
                                  html.Br(),

                                  # Button to clear filters
                                  dbc.Button('Clear Filter', id='clear-filter-button', className='modal_conditions_button', n_clicks=0),
                                  html.Br(),

                                  # Confirmation message after applying filters
                                  html.Div(id="apply-feedback", children="")
                              ]),
                              dbc.ModalFooter(
                                  dbc.Button('Close', id='close-modal-button', className='modal_conditions_button', n_clicks=0)
                              ),
                          ],
                          id='filter-modal',
                          className='filter_modal',
                          is_open=False,
                      ),]),

                      # Dropdown for Graph or Table selection
            html.Div([
                dbc.Button("Graph", id="stats-graph-button", n_clicks=0, className='container-button', style={'margin': '5px'}),
                dbc.Button("Table", id="stats-table-button", n_clicks=0, className='container-button', style={'margin': '5px'}),
                dbc.Button("Radar", id="stats-radar-button", n_clicks=0, className='container-button', style={'margin': '5px'}),
            ]),
]),
    # Bottom Half
    # Output container for the selected plotly object
    html.Div([
        # Dataframe stored and updated based on filters
        dcc.Store(id='stored_df'),
        html.Div(id='graph-dropdown-container', children=[
            dbc.Collapse(id='scatter-object-collapse', is_open=False, children=dcc.Graph(id='scatterplot-graph', style={'width': '100%', 'height': '90%'})),
            html.Div(id='graph-dropdowns', children=[
                html.P('Select X Axis:'),
                dcc.Dropdown(
                    id='x-axis-dropdown',
                    options=[],
                    value='',
                    clearable=False
                ),
                html.P('Select Y Axis:'),
                dcc.Dropdown(
                    id='y-axis-dropdown',
                    options=[],
                    value='',
                    clearable=False
                )])
        ], style={'width': '100%', 'height': '100%', 'display': 'none'}), # Initially hidden

        html.Div(id='stats-table-container', style={'width': '100%', 'height': '100%', 'display': 'none'}, children=[
                html.P('Select Columns to Include in Table'),
                dcc.Dropdown(
                    id='stats-table-dropdown',
                    options=[],
                    value='',
                    multi=True,
                    clearable=True,
                    optionHeight=40,
                    style={
                        'width': '80%'
                    }
                ),
                dbc.Collapse(id='table-object-collapse', is_open=False, children=dcc.Graph(id='stats-data-table', style={'width': '100%', 'height': '100%'}))
            ]),

        html.Div(id='stats-radar-container', style={'width': '100%', 'height': '100%', 'display': 'none'}, children=[
                html.Div(id='stats-radar-dropdowns', children=[
                    html.Div(children=[
                        html.P('Select First Player for Radar Comparison Chart'),
                        dcc.Dropdown(
                            id='player-dropdown',
                            options=[],
                            value='',
                            clearable=False,
                            optionHeight=40,
                            style={
                                'width': '100%'
                            }
                        )]),
                    html.Div(children=[
                        html.P('Select Second Player for Radar Comparison Chart'),
                        dcc.Dropdown(
                            id='player-dropdown1',
                            options=[],
                            value='',
                            clearable=False,
                            optionHeight=40,
                            style={
                                'width': '100%'
                            }
                        )])
                ], style={'width': '70%', 'display': 'flex', 'justify-content': 'space-between'}),

                html.Div(children=[
                    dbc.Collapse(id='radar-object-collapse', is_open=False, children=html.Img(id='stats-radar-chart', style={'width': '80%', 'height': '60%'})),
                    html.P('Select Radar Chart Metrics'),
                    dcc.Dropdown(
                        id='radar-preset-values-dropdown',
                        options=[{'label': key, 'value': key} for key in preset_radar_values.keys()],
                        value=list(preset_radar_values)[0],
                        clearable=False,
                        optionHeight=40,
                        style={
                            'width': '70%'
                        }
                    ),
                    html.Div(id='custom-radar-div', children=[
                        html.P('Select Metrics to Include in Custom Radar Chart'),
                        dcc.Dropdown(
                            id='custom-radar-values-dropdown',
                            options=[],
                            value=[],
                            multi=True,
                            clearable=True,
                            optionHeight=40,
                            style={'width': '80%'}
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
    Input('stored-uploads', 'data')
)
def update_graph_dropdowns(uploaded_dataframes):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')

    return (html.P('Select X Axis:'),
            dcc.Dropdown(
                id='x-axis-dropdown',
                options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                value='Av Rat',
                clearable=False
            ),
            html.P('Select Y Axis:'),
            dcc.Dropdown(
                id='y-axis-dropdown',
                options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                value='Transfer Value',
                clearable=False
            ))


# Pulling datasets from stored_uploads for table dropdown
@callback(
    Output('stats-table-container', 'children'),
    Input('stored-uploads', 'data')
)
def update_table_dropdowns(uploaded_dataframes):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')

    return (html.P('Select Columns to Include in Table'),
            dcc.Dropdown(
                id='stats-table-dropdown',
                options=[{'label': col, 'value': col} for col in stats_df.columns[:-14]],
                value=['Name', 'Age', 'Position', 'Club'],
                multi=True,
                clearable=True,
                optionHeight=40,
                style={
                    'width': '80%'
                }
            ),
            dcc.Graph(id='stats-data-table', style={'width': '100%', 'height': '90%'})
            )


# Pulling datasets from stored_uploads for radar dropdown
@callback(Output('stats-radar-dropdowns', 'children'),
          Input('stored-uploads', 'data'))
def update_radar_dropdowns(uploaded_dataframes):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')

    return (html.Div([
        html.P('Select First Player for Radar Comparison Chart'),
        dcc.Dropdown(
            id='player-dropdown',
            options=[{'label': f'{name} - {position} - {club}', 'value': name}
                     for name, position, club in zip(stats_df.Name, stats_df.Position, stats_df.Club)],
            value='',
            clearable=False,
            optionHeight=40,
            style={
                'width': '100%'
            }
        )]),
        html.Div([
            html.P('Select Second Player for Radar Comparison Chart'),
            dcc.Dropdown(
                id='player-dropdown1',
                options=[{'label': f'{name} - {position} - {club}', 'value': name}
                         for name, position, club in zip(stats_df.Name, stats_df.Position, stats_df.Club)],
                value='',
                clearable=False,
                optionHeight=40,
                style={
                    'width': '100%'
                }
            )])
            )

# Pulling datasets from stored_uploads for custom radar dropdown
@callback(Output('custom-radar-values-dropdown', 'options'),
          Input('stored-uploads', 'data'))
def update_custom_radar_dropdown(uploaded_dataframes):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')

    return [{'label': col, 'value': col} for col in stats_df.columns[:-14]]


# Combined callback for filter UI
@callback(
    Output('dropdown-container-div', "children"),
    Input('stored-uploads', 'data'),
    Input('add-condition', 'n_clicks'),
    State('dropdown-container-div', "children"),
    prevent_initial_call=False
)
def update_filter_ui(uploaded_dataframes, n_clicks, existing_children):
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')

    df = stats_df
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    # Initial load
    if triggered_id is None or not existing_children:
        # Create initial filter UI with first dropdown
        return [
            html.Div([
                html.Label('Column'),
                dcc.Dropdown(
                    id={'type': 'filter-column', 'index': 0},
                    options=[{'label': col, 'value': col} for col in df.columns[:-14]],
                    value='',
                    placeholder='Select Column',
                    clearable=True
                ),
                html.Div(id={'type': 'filter-input-container', 'index': 0}, children=[])
            ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})
        ]

    # Add condition button clicked
    elif triggered_id == 'add-condition' and n_clicks > 0:
        # Create a new filter condition UI
        new_condition = html.Div([
            html.Label('Column'),
            dcc.Dropdown(
                id={'type': 'filter-column', 'index': n_clicks},
                options=[{'label': col, 'value': col} for col in df.columns[:-14]],
                value='',
                placeholder='Select Column',
                clearable=True
            ),
            html.Div(id={'type': 'filter-input-container', 'index': n_clicks}, children=[])
        ], style={'marginBottom': '15px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'})

        # Add to existing children
        updated_children = existing_children + [new_condition]
        return updated_children

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
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
    df = stats_df

    # Categorical columns (simple equals/not equals)
    if selected_column in ['Name', 'Division', 'Club', 'Transfer Status']:
        unique_values = df[selected_column].unique().tolist()
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
    elif selected_column == 'Position':
        position_values = position_filters.keys()
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
                html.Label('Select Position'),
                dcc.Dropdown(
                    id={'type': 'filter-value', 'index': 0},
                    options=[{'label': key, 'value': key} for key in position_values],
                    value=list(position_values)[0] if position_values else '',
                    clearable=False
                )
            ], style={'marginTop': '10px'})
        ]

    # Numeric columns (can use >, <, =, !=)
    elif selected_column in ['Age', 'Apps', 'Gls', 'Ast', 'Wage', 'Transfer Value']:
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
                html.Label(f'Enter {selected_column}'),
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
        Input('stored_df', 'data')
    ],
    [
        State({'type': 'filter-column', 'index': ALL}, 'value'),
        State({'type': 'filter-condition', 'index': ALL}, 'value'),
        State({'type': 'filter-value', 'index': ALL}, 'value'),
        State('logical-operator', 'value')
    ],
    prevent_initial_call=True
)
def update_filtered_data(uploaded_dataframes, n_clicks_apply, n_clicks_clear, stored_data, filter_columns,
                         filter_conditions, filter_values, logical_operator):
    # Function to convert input value to numeric or leave as string
    def convert_input_value(value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return value

    # Initialize the dataframe
    if stored_data:
        df = pd.read_json(io.StringIO(stored_data), orient='split')
    else:
        stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
        df = stats_df

    # Default feedback message
    feedback_message = "No filters applied."

    if not ctx.triggered:
        return feedback_message, df.to_json(date_format='iso', orient='split')

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Clear Filters Button
    if button_id == 'clear-filter-button' and n_clicks_clear > 0:
        feedback_message = "Filters cleared."
        return feedback_message, []

    # Apply Filters Button
    if button_id == 'apply-filter-button' and n_clicks_apply > 0:
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
            if col in ['Name', 'Division', 'Club', 'Transfer Status']:
                if condition == '=':
                    filter_conditions_list.append(df[col] == value)
                elif condition == '!=':
                    filter_conditions_list.append(df[col] != value)

            # Handle Positions
            elif col == 'Position':
                if condition == '=':
                    filter_conditions_list.append(df[value] == True)
                elif condition == '!=':
                    filter_conditions_list.append(df[value] == False)

            # Handle numeric columns
            elif col in ['Age', 'Wage', 'Transfer Value']:
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
        Output('player-dropdown1', 'options')
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
        Input('stored_df', 'data')
    ],
    prevent_initial_call=True
)
def update_visualization(uploaded_dataframes, graph_clicks, table_clicks, radar_clicks, selected_x, selected_y, selected_col,
                         selected_player, selected_player1, selected_radar_preset, selected_metrics, stored_data):

    # Get dataframes
    stats_df = pd.read_json(io.StringIO(uploaded_dataframes['stats']), orient='split')
    squad_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['squad_attributes']), orient='split')

    # Default empty figure
    empty_fig = px.scatter(x=[0], y=[0])
    empty_fig.update_layout(
        title='No data available',
        xaxis_title='X Axis',
        yaxis_title='Y Axis'
    )
    empty_table = {}
    empty_radar = ''
    default_player_options = [{'label': f'{name} - {position}', 'value': name}
                              for name, position in zip(stats_df.Name, stats_df.Position)]

    # Check for valid data
    if not stored_data:
        print("No stored data found")
        return empty_fig, empty_table, empty_radar, default_player_options, default_player_options

    try:
        # Convert stored data to df
        stored_df = pd.read_json(io.StringIO(stored_data), orient='split')
        print(f"Successfully loaded DataFrame with shape: {stored_df.shape}")

    except Exception as e:
        print(f"Error converting stored data to DataFrame: {str(e)}")
        return empty_fig, empty_table, empty_radar, default_player_options, default_player_options

    if not ctx.triggered:
        print("No context triggered")
        return empty_fig, empty_table, empty_radar, default_player_options, default_player_options

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f"Triggered by: {trigger_id}")

    stored_player_options = [{'label': f'{name} - {position}', 'value': name}
                             for name, position in zip(stored_df.Name, stored_df.Position)]

    # Handle graph button
    if 'graph-button' in trigger_id and graph_clicks > 0:
        if selected_x and selected_y:
            print(f"Creating scatter plot with {selected_x} vs {selected_y}")
            try:
                def set_color(df):
                    values = df['Club'].to_list()
                    color_list = []
                    for i in values:
                        if i == squad_attributes_df.loc[0]['Club']:
                            color_list.append('red')
                        else:
                            color_list.append('blue')
                    return color_list
                fig = px.scatter(stored_df, x=selected_x, y=selected_y,
                                 title=f"{selected_x} vs {selected_y}",
                                 hover_data=['Name', 'Club', 'Age'])
                fig.update_traces(marker=dict(color=set_color(stored_df)))
                return fig, empty_table, empty_radar, stored_player_options, stored_player_options
            except Exception as e:
                print(f"Error creating scatter plot: {str(e)}")
                return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options
        else:
            print("Invalid axis selection")
            empty_fig.update_layout(title='Invalid axis selection')
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

    # Handle table button
    elif 'table-button' in trigger_id and table_clicks > 0:
        print("Creating table view")
        try:
            # Create a Table
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
                                                          'values': stored_df.sort_values(btn_label, ascending=False).transpose().values.tolist(),
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
            return empty_fig, fig, empty_radar, stored_player_options, stored_player_options
        except Exception as e:
            print(f"Error creating table: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

    # Handle axis dropdown changes
    elif trigger_id in ['x-axis-dropdown', 'y-axis-dropdown'] and selected_x and selected_y:
        print(f"Updating plot for axis change: {selected_x} vs {selected_y}")
        try:
            def set_color(df):
                values = df['Club'].to_list()
                color_list = []
                for i in values:
                    if i == squad_attributes_df.loc[0]['Club']:
                        color_list.append('red')
                    else:
                        color_list.append('blue')
                return color_list
            fig = px.scatter(stored_df, x=selected_x, y=selected_y,
                             title=f"{selected_x} vs {selected_y}",
                             hover_data=['Name', 'Club', 'Age'] if all(
                                 col in stored_df.columns for col in ['Name', 'Club', 'Age']) else None)
            fig.update_traces(marker=dict(color=set_color(stored_df)))
            return fig, empty_table, empty_radar, stored_player_options, stored_player_options
        except Exception as e:
            print(f"Error updating plot for axis change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

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
            layout = layout)
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
            return empty_fig, fig, empty_radar, stored_player_options, stored_player_options
        except Exception as e:
            print(f"Error updating table for dropdown change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

    # Handle Radar Button
    elif 'radar-button' in trigger_id and radar_clicks > 0:
        if selected_player and selected_player1:
            print(f"Creating radar plot with {selected_player} vs {selected_player1}")
            try:
                # Reset stored_df index
                stored_df.reset_index(inplace=True, drop=True)

                ## player index
                player_index = stored_df.index[stored_df['Name'] == selected_player][0]
                player1_index = stored_df.index[stored_df['Name'] == selected_player1][0]

                ## parameter names
                if selected_metrics == []:
                    params = preset_radar_values[selected_radar_preset]
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

                ## title
                title = dict(
                    title_name=stored_df.iloc[player_index]['Name'],
                    title_color='#FF69B4',
                    subtitle_name=stored_df.iloc[player_index]['Club'],
                    subtitle_color='#FF69B4',
                    title_name_2=stored_df.iloc[player1_index]['Name'],
                    title_color_2='#344D94',
                    subtitle_name_2=stored_df.iloc[player1_index]['Club'],
                    subtitle_color_2='#7FFF00',
                    title_fontsize=25,
                    subtitle_fontsize=20,
                )

                ## instantiate object
                radar = Radar(fontfamily='Arial', background_color='#483d8b', patch_color="#28252C", label_color="#F0FFF0", range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

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

                return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options


            except Exception as e:
                print(f"Error creating radar plot: {str(e)}")
                return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options
        else:
            print("Invalid player selection")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

    # Handle radar player dropdown changes
    elif trigger_id in ['player-dropdown', 'player-dropdown1'] and selected_player and selected_player1:
        print(f"Updating plot for dropdown change: {selected_player} vs {selected_player1}")
        try:
            # Reset stored_df index
            stored_df.reset_index(inplace=True, drop=True)

            ## player index
            player_index = stored_df.index[stored_df['Name'] == selected_player][0]
            player1_index = stored_df.index[stored_df['Name'] == selected_player1][0]

            ## parameter names
            if selected_metrics == []:
                params = preset_radar_values[selected_radar_preset]
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

            ## title
            title = dict(
                title_name=stored_df.iloc[player_index]['Name'],
                title_color='#FF69B4',
                subtitle_name=stored_df.iloc[player_index]['Club'],
                subtitle_color='#FF69B4',
                title_name_2=stored_df.iloc[player1_index]['Name'],
                title_color_2='#7FFF00',
                subtitle_name_2=stored_df.iloc[player1_index]['Club'],
                subtitle_color_2='#7FFF00',
                title_fontsize=25,
                subtitle_fontsize=20,
            )

            ## instantiate object
            radar = Radar(fontfamily='Arial', background_color='#483d8b', patch_color="#28252C", label_color="#F0FFF0", range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

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

            return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options


        except Exception as e:
            print(f"Error updating plot for axis change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

    # Handle Radar Chart Preset Metrics Dropdown Changes
    elif trigger_id in 'radar-preset-values-dropdown' and selected_radar_preset:
        print(f"Updating plot for radar preset dropdown change: {selected_player} vs {selected_player1}")
        try:
            # Reset stored_df index
            stored_df.reset_index(inplace=True, drop=True)

            ## player index
            player_index = stored_df.index[stored_df['Name'] == selected_player][0]
            player1_index = stored_df.index[stored_df['Name'] == selected_player1][0]

            ## parameter names
            if selected_metrics == []:
                params = preset_radar_values[selected_radar_preset]
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

            ## title
            title = dict(
                title_name=stored_df.iloc[player_index]['Name'],
                title_color='#FF69B4',
                subtitle_name=stored_df.iloc[player_index]['Club'],
                subtitle_color='#FF69B4',
                title_name_2=stored_df.iloc[player1_index]['Name'],
                title_color_2='#7FFF00',
                subtitle_name_2=stored_df.iloc[player1_index]['Club'],
                subtitle_color_2='#7FFF00',
                title_fontsize=25,
                subtitle_fontsize=20,
            )

            ## instantiate object
            radar = Radar(fontfamily='Arial', background_color='#483d8b', patch_color="#28252C", label_color="#F0FFF0", range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

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

            return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options


        except Exception as e:
            print(f"Error updating plot for radar preset change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

    # Handle Custom Radar Metrics Dropdown Change
    elif trigger_id in 'custom-radar-values-dropdown' and selected_metrics:
        print(f"Updating plot for dropdown change: {selected_player} vs {selected_player1}")
        try:
            # Reset stored_df index
            stored_df.reset_index(inplace=True, drop=True)

            ## player index
            player_index = stored_df.index[stored_df['Name'] == selected_player][0]
            player1_index = stored_df.index[stored_df['Name'] == selected_player1][0]

            ## parameter names
            if selected_metrics == []:
                params = preset_radar_values[selected_radar_preset]
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

            ## title
            title = dict(
                title_name=stored_df.iloc[player_index]['Name'],
                title_color='#FF69B4',
                subtitle_name=stored_df.iloc[player_index]['Club'],
                subtitle_color = '#FF69B4',
                title_name_2 = stored_df.iloc[player1_index]['Name'],
                title_color_2 = '#7FFF00',
                subtitle_name_2 = stored_df.iloc[player1_index]['Club'],
                subtitle_color_2 = '#7FFF00',
                title_fontsize = 25,
                subtitle_fontsize = 20,
            )

            ## instantiate object
            radar = Radar(fontfamily='Arial', background_color='#483d8b', patch_color="#28252C", label_color="#F0FFF0", range_color="#F0FFF0", label_fontsize=16, range_fontsize=9)

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

            return empty_fig, empty_table, fig_bar_matplotlib, stored_player_options, stored_player_options


        except Exception as e:
            print(f"Error updating plot for custom radar change: {str(e)}")
            return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options

    # Default return
    return empty_fig, empty_table, empty_radar, stored_player_options, stored_player_options


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
