# Todo -------------------------------------------------------
# 1. Fix tables in stats & attributes so that names are visible and the layout is prettier
# 2. Do something with 'Personality'?

import dash
from dash import Dash, html, dcc, Input, Output, callback, ctx
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# Register Page
dash.register_page(__name__, path='/attributes', title='Scout FM Attributes')

# Position filters
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

# Create attribute filters
attribute_filters = {
    'Overall': ['Name', 'Age', 'Position', 'Club', 'Division', 'Speed', 'Physical', 'Defending', 'Mental', 'Aerial', 'Technical', 'Attacking', 'Vision'],
    'GK Overall': ['Name', 'Age', 'Position', 'Club', 'Division', 'Speed', 'Physical', 'Shot Stopping', 'Distribution', 'Aerial (GK)', 'Ecc', 'Communication', 'Mental'],
    'Technical': ['Name', 'Age', 'Position', 'Club', 'Division', 'Cor', 'Cro', 'Dri', 'Fin', 'Fir', 'Fre', 'Hea', 'Lon', 'L Th', 'Mar', 'Pas', 'Pen', 'Tck', 'Tec'],
    'Mental': ['Name', 'Age', 'Position', 'Club', 'Division', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Det', 'Fla', 'Ldr', 'OtB', 'Pos', 'Tea', 'Vis', 'Wor'],
    'Physical': ['Name', 'Age', 'Position', 'Club', 'Division', 'Acc', 'Agi', 'Bal', 'Jum', 'Nat', 'Pac', 'Sta', 'Str'],
    'Goalkeeper': ['Name', 'Age', 'Position', 'Club', 'Division', 'Aer', 'Cmd', 'Com', 'Ecc', 'Fir', 'Han', 'Kic', 'TRO', '1v1', 'Pun', 'Ref', 'Thr'],
    'Central Defender': ['Name', 'Age', 'Position', 'Club', 'Division', 'Hea', 'Mar', 'Tck', 'Pos', 'Jum', 'Str'],
    'Full-back': ['Name', 'Age', 'Position', 'Club', 'Division', 'Cro', 'Dri', 'Tck', 'Tec', 'OtB', 'Tea', 'Wor', 'Acc', 'Pac', 'Sta'],
    'Wing-Back': ['Name', 'Age', 'Position', 'Club', 'Division', 'Cro', 'Dri', 'Tck', 'Tec', 'OtB', 'Tea', 'Wor', 'Acc', 'Pac', 'Sta'],
    'Defensive Midfielder': ['Name', 'Age', 'Position', 'Club', 'Division', 'Tck', 'Fir', 'Pas', 'Ant', 'Cnt', 'Pos', 'Tea', 'Wor', 'Sta'],
    'Central Midfielder': ['Name', 'Age', 'Position', 'Club', 'Division', 'Fir', 'Pas', 'Tck', 'Dec', 'Tea', 'OtB', 'Vis', 'Agi', 'Bal'],
    'Attacking Midfielder': ['Name', 'Age', 'Position', 'Club', 'Division', 'Fir', 'Pas', 'Tck', 'Dec', 'Tea', 'OtB', 'Vis', 'Agi', 'Bal'],
    'Winger': ['Name', 'Age', 'Position', 'Club', 'Division', 'Cro', 'Dri', 'Tec', 'Ant', 'Fla', 'Wor', 'Acc', 'Agi', 'Pac'],
    'Striker': ['Name', 'Age', 'Position', 'Club', 'Division', 'Dri', 'Fin', 'Fir', 'Tec', 'Cmp', 'OtB', 'Acc', 'Jum', 'Pac']
}

layout = html.Div([
    html.Div([
            # Top Half
            # Dropdown Menu to select between Squad Attributes and Shortlist Attributes
            html.Div(id='dataset-selection-div', children=[
                html.H2('Analyze Squad or Shortlisted Players?'),
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
                    dbc.Button('Table', id='table-button', n_clicks=0),
                    dbc.Button('Radar', id='radar-button', n_clicks=0)
                ]),
            # Dropdown Menu to filter visible attributes in the Table
            html.Div([html.H2('Attributes'),
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
            html.Div(id='table-container', style={'width': '100%', 'height': '100%', 'display': 'none'}, children=[
                html.H2('Filter by Position'),
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
            html.Div(id='radar-container', style={'width': '100%', 'height': '100%', 'display': 'none'}, children=[
                html.Div(id='radar-dropdowns', children=[
                    html.H2('Select Player from Shortlist'),
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
                    html.H2('Select Position Average or Player from Squad'),
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
    squad_attributes_df = pd.read_json(uploaded_dataframes['squad_attributes'], orient='split')
    scouting_attributes_df = pd.read_json(uploaded_dataframes['scouting_attributes'], orient='split')

    att_datasets = {
        'Squad Attributes': squad_attributes_df,
        'Shortlist Attributes': scouting_attributes_df,
    }
    return (html.H2('Analyze Squad or Shortlisted Players?'),
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
    squad_attributes_df = pd.read_json(uploaded_dataframes['squad_attributes'], orient='split')
    scouting_attributes_df = pd.read_json(uploaded_dataframes['scouting_attributes'], orient='split')

    return (html.H2('Select Player from Shortlist'),
            dcc.Dropdown(
                id='shortlist-dropdown',
                options=[{'label': f'{name} - {position}', 'value': name}
                         for name, position in zip(scouting_attributes_df.Name, scouting_attributes_df.Position)],
                value=scouting_attributes_df.iloc[0]['Name'],
                clearable=False,
                optionHeight=40,
                style={
                    'width': '80%'
                }
            ),
            html.H2('Select Position Average or Player from Squad'),
            dcc.Dropdown(
                id='squad-dropdown',
                options=[{'label': name, 'value': name} for name in squad_attributes_df.Name],
                value=squad_attributes_df.iloc[0]['Name'],
                clearable=False,
                optionHeight=40,
                style={
                    'width': '80%'
                }
            ))


# Manage buttons
@callback(
    Output('table-container', 'style'),
    Output('radar-container', 'style'),
    Input('table-button', 'n_clicks'),
    Input('radar-button', 'n_clicks')
)
def toggle_containers(table_clicks, radar_clicks):
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if triggered_id == 'table-button':
        return ({'width': '100%', 'height': '100%', 'display': 'block'},
                {'width': '100%', 'height': '100%', 'display': 'none'})
    elif triggered_id == 'radar-button':
        return ({'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'block'})
    else:
        return ({'width': '100%', 'height': '100%', 'display': 'none'},
                {'width': '100%', 'height': '100%', 'display': 'none'})


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
    squad_attributes_df = pd.read_json(uploaded_dataframes['squad_attributes'], orient='split')
    scouting_attributes_df = pd.read_json(uploaded_dataframes['scouting_attributes'], orient='split')

    att_datasets = {
        'Squad Attributes': squad_attributes_df,
        'Shortlist Attributes': scouting_attributes_df,
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
    squad_attributes_df = pd.read_json(uploaded_dataframes['squad_attributes'], orient='split')
    scouting_attributes_df = pd.read_json(uploaded_dataframes['scouting_attributes'], orient='split')

    # Create Radar figure
    # Select a row based on dropdown player name selection
    print(scouting_attributes_df)
    scouting_attributes_index = scouting_attributes_df.index[scouting_attributes_df['Name'] == selected_shortlist][0]
    squad_attributes_index = squad_attributes_df.index[squad_attributes_df['Name'] == selected_squad][0]

    # parameter names based on position_category
    categories = attribute_filters[selected_attribute_filter][5:]

    # parameter value
    scouting_attributes_values = []
    squad_attributes_values = []
    for attribute in categories:
        scouting_attributes_values.append(scouting_attributes_df.iloc[scouting_attributes_index][attribute])
    for attribute in categories:
        squad_attributes_values.append(squad_attributes_df.iloc[squad_attributes_index][attribute])

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=scouting_attributes_values,
        theta=categories,
        fill='toself',
        name=scouting_attributes_df.iloc[scouting_attributes_index].Name
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
