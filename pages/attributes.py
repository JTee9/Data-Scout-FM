# Todo -------------------------------------------------------
# 1. Fix tables in stats & attributes so that names are visible and the layout is prettier
# 2. Utilize Role scores

import dash
from dash import html, dcc, callback, ctx
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import io
from config import position_filters, attribute_filters


# Register Page
dash.register_page(__name__, path='/attributes', title='Scout FM Attributes')

layout = html.Div([
    html.Div([
            # Top Half
            # Dropdown Menu to select between Squad Attributes and Shortlist Attributes
            html.Div(id='dataset-selection-div', children=[
                html.Label('Analyze Squad or Shortlisted Players?', className='attributes-label'),
                      dcc.Dropdown(
                          id='dataset-dropdown',
                          options=[],
                          value='',
                          clearable=False,
                          optionHeight=40
                      )
                      ]),
            # Buttons to select Graph or Table
            html.Div([
                    dbc.Button('Table', id='table-button', n_clicks=0, className='container-button', style={'margin': '5px'}),
                    dbc.Button('Radar', id='radar-button', n_clicks=0, className='container-button', style={'margin': '5px'})
                ]),
            # Dropdown Menu to filter visible attributes in the Table
            html.Div([html.Label('Set Attributes to View on Table and Radar Chart', className='attributes-label'),
                      dcc.Dropdown(
                          id='attribute-dropdown',
                          options=[{'label': key, 'value': key} for key in attribute_filters.keys()],
                          value='Overall',
                          clearable=False,
                          optionHeight=40,
                          style={
                              'width': '80%'
                          }
                      ),
    ]),
        # Bottom Half
        html.Div(id='output-container', style={'width': '100%', 'height': '600px'}, children=[
            # Table
            dbc.Collapse(id='table-container', is_open=False, style={'width': '100%', 'height': '100%'}, children=[
                html.Label('Filter Players by Position', className='attributes-label'),
                dcc.Dropdown(
                    id='position-dropdown',
                    options=[{'label': key, 'value': key} for key in position_filters.keys()],
                    value='M (C)',
                    clearable=False,
                    optionHeight=40,
                    style={
                        'width': '80%'
                    }
                ),
                dcc.Graph(id='data-table', style={'width': '100%', 'height': '90%'})
            ]),
            # Radar
            dbc.Collapse(id='radar-container', is_open=False, style={'width': '100%', 'height': '100%'}, children=[
                html.Div(id='radar-dropdowns', children=[
                    html.Label('Select Player from Shortlist', className='attributes-label'),
                    dcc.Dropdown(
                        id='shortlist-dropdown',
                        options=[],
                        value='',
                        clearable=False,
                        optionHeight=40,
                        style={
                            'width': '80%'
                        }
                    ),
                    html.Label('Select Position Average or Player from Squad', className='attributes-label'),
                    dcc.Dropdown(
                        id='squad-dropdown',
                        options=[],
                        value='',
                        clearable=False,
                        optionHeight=40,
                        style={
                            'width': '80%'
                        }
                    )],
                    style={
                        'width': '100%',
                        'display': 'flex'
                    }),
                dcc.Graph(id='radar-chart', style={'width': '100%', 'height': '90%'})
            ])
        ])
    ])
])


# Callbacks -------------------------------------------------------------------------
# Pulling datasets from stored_uploads for dataset dropdown
@callback(
    Output('dataset-selection-div', 'children'),
    Input('stored-uploads', 'data')
)
def pull_uploaded_attributes_dataframes(uploaded_dataframes):
    squad_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['squad_attributes']), orient='split')
    shortlist_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['shortlist_attributes']), orient='split')

    att_datasets = {
        'Squad Attributes': squad_attributes_df,
        'Shortlist Attributes': shortlist_attributes_df,
    }
    return (html.Label('Analyze Squad or Shortlisted Players?', className='attributes-label'),
            dcc.Dropdown(
                id='dataset-dropdown',
                options=[{'label': key, 'value': key} for key in att_datasets.keys()],
                value=list(att_datasets)[0],
                clearable=False,
                optionHeight=40
            ))


# Pulling datasets from stored_uploads for radar chart dropdown
@callback(
    Output('radar-dropdowns', 'children'),
    Input('stored-uploads', 'data')
)
def update_radar_dropdowns(uploaded_dataframes):
    squad_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['squad_attributes']), orient='split')
    shortlist_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['shortlist_attributes']), orient='split')

    return (html.Label('Select Player from Shortlist', className='attributes-label'),
            dcc.Dropdown(
                id='shortlist-dropdown',
                options=[{'label': f'{name} - {position}', 'value': name}
                         for name, position in zip(shortlist_attributes_df.Name, shortlist_attributes_df.Position)],
                value=shortlist_attributes_df.iloc[0]['Name'],
                clearable=False,
                optionHeight=40,
                style={
                    'width': '80%'
                }
            ),
            html.Label('Select Player or Position Average from Squad', className='attributes-label'),
            dcc.Dropdown(
                id='squad-dropdown',
                options=[{'label': name if pd.isna(position) else f'{name} - {position}', 'value': name}
                         for name, position in zip(squad_attributes_df.Name, squad_attributes_df.Position)],
                value=squad_attributes_df.iloc[0]['Name'],
                clearable=False,
                optionHeight=40,
                style={
                    'width': '80%'
                }
            ))


# Manage collapsed plots
@callback(
    Output('table-container', 'is_open'),
    Output('radar-container', 'is_open'),
    Input('table-button', 'n_clicks'),
    Input('radar-button', 'n_clicks'),
    State('table-container', 'is_open'),
    State('radar-container', 'is_open')
)
def toggle_collapsed_charts(table_clicks, radar_clicks, table_is_open, radar_is_open):
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if triggered_id == 'table-button':
        if radar_is_open == True:
            return not table_is_open, not radar_is_open
        else:
            return not table_is_open, radar_is_open
    elif triggered_id == 'radar-button':
        if table_is_open == True:
            return not table_is_open, not radar_is_open
        else:
            return table_is_open, not radar_is_open,
    return table_is_open, radar_is_open


# Table callback
@callback(
    Output('data-table', 'figure'),
    Input('stored-uploads', 'data'),
    Input(component_id='dataset-dropdown', component_property='value'),
    Input(component_id='attribute-dropdown', component_property='value'),
    Input(component_id='position-dropdown', component_property='value'),
          )
def update_table(uploaded_dataframes, selected_dataset, selected_attribute_filter, selected_position_filter):
    # Get the selected dataset
    squad_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['squad_attributes']), orient='split')
    shortlist_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['shortlist_attributes']), orient='split')

    att_datasets = {
        'Squad Attributes': squad_attributes_df,
        'Shortlist Attributes': shortlist_attributes_df,
    }

    df = att_datasets[selected_dataset]
    # Apply Position Filter
    df = df[df[selected_position_filter] == True]
    # Apply Attribute Filter
    att_filter = attribute_filters[selected_attribute_filter]
    df_att_filter = df[att_filter].drop(columns=['Club', 'Division'])
    # Create Table figure
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(df_att_filter.columns),
            fill_color='lavender',
            align='left'
        ),
        cells=dict(
            values=df_att_filter.transpose().values.tolist(),
            fill_color='white',
            align='left'
        )
    )])
    fig.update_layout(
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
                                    'values': df_att_filter.sort_values(btn_label,
                                                                        ascending=False).transpose().values.tolist(),
                                    # update the cell values with the sorted data
                                    # format table as before
                                    'fill': dict(color=px.colors.qualitative.Pastel1[8]),
                                    'align': 'left',
                                }
                            }
                        ],
                    }
                    for btn_label in df_att_filter.columns
                ],
                'direction': 'down',
            }
        ]
    )
    return fig


# Radar callback
@callback(
    Output('radar-chart', 'figure'),
    Input('stored-uploads', 'data'),
    Input(component_id='attribute-dropdown', component_property='value'),
    Input(component_id='shortlist-dropdown', component_property='value'),
    Input(component_id='squad-dropdown', component_property='value')
)
def update_radar_chart(uploaded_dataframes, selected_attribute_filter, selected_shortlist, selected_squad):
    if selected_shortlist == '':
        raise PreventUpdate
    # Uploaded dataframes
    squad_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['squad_attributes']), orient='split')
    shortlist_attributes_df = pd.read_json(io.StringIO(uploaded_dataframes['shortlist_attributes']), orient='split')

    # Create Radar figure
    # Select a row based on dropdown player name selection
    shortlist_attributes_index = shortlist_attributes_df.index[shortlist_attributes_df['Name'] == selected_shortlist][0]
    squad_attributes_index = squad_attributes_df.index[squad_attributes_df['Name'] == selected_squad][0]

    # parameter names based on position_category
    categories = attribute_filters[selected_attribute_filter][5:]

    # parameter value
    shortlist_attributes_values = []
    squad_attributes_values = []
    for attribute in categories:
        shortlist_attributes_values.append(shortlist_attributes_df.iloc[shortlist_attributes_index][attribute])
    for attribute in categories:
        squad_attributes_values.append(squad_attributes_df.iloc[squad_attributes_index][attribute])

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=shortlist_attributes_values,
        theta=categories,
        fill='toself',
        name=shortlist_attributes_df.iloc[shortlist_attributes_index].Name
    ))
    fig.add_trace(go.Scatterpolar(
        r=squad_attributes_values,
        theta=categories,
        fill='toself',
        name=squad_attributes_df.iloc[squad_attributes_index].Name
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 20]
            )),
        showlegend=True
    )
    return fig
