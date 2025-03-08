# Todo ----------------
# 1. Clean up dataframes: drop unnecessary stats columns, consider intuitive order of stats columns, fix bugged out names
# 2. Fix position scores, consider whether they are necessary.

import pandas as pd
import numpy as np
from warnings import simplefilter


def build_squad_attributes_dataframe(squad_attributes_file):
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

    # Configure Pandas Settings
    pd.set_option('display.max_columns', 20)
    pd.options.mode.chained_assignment = None

    # Configure Numpy setting to show numerical values rather than np.float64()
    np.set_printoptions(legacy='1.25')

    ## Create the DataFrames
    # Create squad attributes DataFrame from squad attributes view
    squad_attributes_df = squad_attributes_file.copy()
    squad_attributes_df = squad_attributes_df[0]

    # Create position filters dict
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

    # Create position tag columns -------------------------------
    # Function to check and tag positions correctly
    def check_position_tags(position, position_filter):
        # Split the position string by commas and strip any leading/trailing whitespace
        position_parts = [p.strip() for p in position.split(',')]

        # First, check for exact matches of each part in the position string
        for part in position_parts:
            # Check for exact match in the position filter list
            if part in position_filter:
                return True

        # Return False if no match is found
        return False

    # Loop over each position tag and its corresponding filter
    # Squad Attributes df
    for position_tag, position_filter in position_filters.items():
        # Create a new column in the dataframe for the position tag
        squad_attributes_df[position_tag] = squad_attributes_df['Position'].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )

    # Define attribute scores for each position
    squad_attributes_df['gk_score'] = (
            squad_attributes_df['Aer']
            + squad_attributes_df['Cmd']
            + squad_attributes_df['Com']
            + squad_attributes_df['Han']
            + squad_attributes_df['Fir']
            + squad_attributes_df['Kic']
            + squad_attributes_df['Ref']
            + squad_attributes_df['1v1']
            + squad_attributes_df['Thr']
    )

    squad_attributes_df['cb_score'] = (
            squad_attributes_df['Cnt']
            + squad_attributes_df['Pos']
            + squad_attributes_df['Bra']
            + squad_attributes_df['Hea']
            + squad_attributes_df['Mar']
            + squad_attributes_df['Tck']
            + squad_attributes_df['Jum']
            + squad_attributes_df['Acc']
    )

    squad_attributes_df['wb_score'] = (
            squad_attributes_df['Cnt']
            + squad_attributes_df['Pos']
            + squad_attributes_df['OtB']
            + squad_attributes_df['Wor']
            + squad_attributes_df['Mar']
            + squad_attributes_df['Tck']
            + squad_attributes_df['Sta']
            + squad_attributes_df['Acc']
    )

    squad_attributes_df['dm_score'] = (
            squad_attributes_df['Cnt']
            + squad_attributes_df['Pos']
            + squad_attributes_df['OtB']
            + squad_attributes_df['Wor']
            + squad_attributes_df['Fir']
            + squad_attributes_df['Tck']
            + squad_attributes_df['Sta']
            + squad_attributes_df['Dec']
    )

    squad_attributes_df['cm_score'] = (
            squad_attributes_df['Agi']
            + squad_attributes_df['Vis']
            + squad_attributes_df['OtB']
            + squad_attributes_df['Wor']
            + squad_attributes_df['Fir']
            + squad_attributes_df['Bal']
            + squad_attributes_df['Pas']
            + squad_attributes_df['Dec']
    )

    squad_attributes_df['wing_score'] = (
            squad_attributes_df['Acc']
            + squad_attributes_df['Pac']
            + squad_attributes_df['OtB']
            + squad_attributes_df['Tec']
            + squad_attributes_df['Fir']
            + squad_attributes_df['Dri']
            + squad_attributes_df['Agi']
            + squad_attributes_df['Fla']
    )

    squad_attributes_df['str_score'] = (
            squad_attributes_df['Acc']
            + squad_attributes_df['Com']
            + squad_attributes_df['OtB']
            + squad_attributes_df['Fin']
            + squad_attributes_df['Fir']
            + squad_attributes_df['Tec']
            + squad_attributes_df['Wor']
            + squad_attributes_df['Jum']
    )

    # Custom attributes for 'overall' radar
    # Squad df
    squad_attributes_df['Speed'] = squad_attributes_df[['Acc', 'Pac']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Vision'] = squad_attributes_df[['Pas', 'Fla', 'Vis']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Attacking'] = squad_attributes_df[['Fin', 'Cmp', 'OtB']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Technical'] = squad_attributes_df[['Dri', 'Fir', 'Tec']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Aerial'] = squad_attributes_df[['Hea', 'Jum']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Mental'] = squad_attributes_df[['Ant', 'Bra', 'Cnt', 'Dec', 'Det', 'Tea']].mean(axis=1).apply(
        np.floor)
    squad_attributes_df['Defending'] = squad_attributes_df[['Mar', 'Tck', 'Pos']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Physical'] = squad_attributes_df[['Agi', 'Bal', 'Sta', 'Str']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Aerial (GK)'] = squad_attributes_df[['Aer', 'Han']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Shot Stopping'] = squad_attributes_df[['1v1', 'Ref']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Distribution'] = squad_attributes_df[['Kic', 'Thr']].mean(axis=1).apply(np.floor)
    squad_attributes_df['Communication'] = squad_attributes_df[['Cmd', 'Com']].mean(axis=1).apply(np.floor)

    # Calculating position averages
    # Squad Attributes Averages

    # List to store the average rows for each position tag
    avg_attributes_rows = []

    # Iterate over each position tag in the position_filters
    for position_tag in position_filters.keys():
        # Filter the dataframe where the position tag is True
        tag_filtered_df = squad_attributes_df[squad_attributes_df[position_tag] == True]

        # Calculate the mean of the numeric columns for the filtered dataframe
        position_avg = tag_filtered_df.mean(numeric_only=True)

        # Create a new row for this position's average and set its 'Name'
        position_avg['Name'] = position_tag.replace(' Tag', '') + ' average'

        # Append this average row to the list
        avg_attributes_rows.append(position_avg)

    # Convert the list of average rows to a DataFrame
    squad_avg_per_position_tag = pd.DataFrame(avg_attributes_rows)

    # Append the calculated averages back to the original dataframe
    squad_attributes_df = pd.concat([squad_attributes_df, squad_avg_per_position_tag],
                                    ignore_index=True).round()

    return squad_attributes_df


def build_scouting_attributes_dataframe(scouting_attributes_file):
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

    # Configure Pandas Settings
    pd.set_option('display.max_columns', 20)
    pd.options.mode.chained_assignment = None

    # Configure Numpy setting to show numerical values rather than np.float64()
    np.set_printoptions(legacy='1.25')

    ## Create the DataFrames
    # Create scouting attributes DataFrame from Shortlist View
    scouting_attributes_df = scouting_attributes_file.copy()
    scouting_attributes_df = scouting_attributes_df[0]

    # Clean Scouting Attributes dataframe to remove range values
    for column in ['Acc', 'Wor', 'Vis', 'Thr', 'Tec', 'Tea', 'Tck', 'Str', 'Sta', 'TRO', 'Ref', 'Pun', 'Pos', 'Pen',
                   'Pas',
                   'Pac', '1v1', 'OtB', 'Nat', 'Mar', 'L Th', 'Lon', 'Ldr', 'Kic', 'Jum', 'Hea', 'Han', 'Fre', 'Fla',
                   'Fir',
                   'Fin', 'Ecc', 'Dri', 'Det', 'Dec', 'Cro', 'Cor', 'Cnt', 'Cmp', 'Com', 'Cmd', 'Bra', 'Bal', 'Ant',
                   'Agi',
                   'Agg', 'Aer']:
        scouting_attributes_df.loc[scouting_attributes_df[column].str.contains('-'), column] = ''
        scouting_attributes_df[column] = pd.to_numeric(scouting_attributes_df[column]).round()

    # Remove unnecessary columns from Scouting Attributes
    scouting_attributes_df = scouting_attributes_df.drop(columns=['Inf', 'Rec'])

    # Function to remove the nationality part of the name (split at the last hyphen)
    def remove_nationality(name):
        if '-' in name:  # Check if there is a hyphen in the name
            return name.rsplit('-', 1)[0]  # Split from the right and take the first part (player name)
        else:
            return name  # If no hyphen, return the name as is

    # Apply the function to the 'Name' column
    scouting_attributes_df['Name'] = scouting_attributes_df['Name'].apply(remove_nationality)

    # Create position filters dict
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

    # Custom attributes for 'overall' radar
    # Scouting df
    scouting_attributes_df['Speed'] = scouting_attributes_df[['Acc', 'Pac']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Vision'] = scouting_attributes_df[['Pas', 'Fla', 'Vis']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Attacking'] = scouting_attributes_df[['Fin', 'Cmp', 'OtB']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Technical'] = scouting_attributes_df[['Dri', 'Fir', 'Tec']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Aerial'] = scouting_attributes_df[['Hea', 'Jum']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Mental'] = scouting_attributes_df[['Ant', 'Bra', 'Cnt', 'Dec', 'Det', 'Tea']].mean(
        axis=1).apply(np.floor)
    scouting_attributes_df['Defending'] = scouting_attributes_df[['Mar', 'Tck', 'Pos']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Physical'] = scouting_attributes_df[['Agi', 'Bal', 'Sta', 'Str']].mean(axis=1).apply(
        np.floor)
    scouting_attributes_df['Aerial (GK)'] = scouting_attributes_df[['Aer', 'Han']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Shot Stopping'] = scouting_attributes_df[['1v1', 'Ref']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Distribution'] = scouting_attributes_df[['Kic', 'Thr']].mean(axis=1).apply(np.floor)
    scouting_attributes_df['Communication'] = scouting_attributes_df[['Cmd', 'Com']].mean(axis=1).apply(np.floor)

    # Create position tag columns -------------------------------
    # Function to check and tag positions correctly
    def check_position_tags(position, position_filter):
        # Split the position string by commas and strip any leading/trailing whitespace
        position_parts = [p.strip() for p in position.split(',')]

        # First, check for exact matches of each part in the position string
        for part in position_parts:
            # Check for exact match in the position filter list
            if part in position_filter:
                return True

        # Return False if no match is found
        return False

    # Loop over each position tag and its corresponding filter
    # Scouting Attributes df
    for position_tag, position_filter in position_filters.items():
        # Create a new column in the dataframe for the position tag
        scouting_attributes_df[position_tag] = scouting_attributes_df['Position'].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )

    # Replicate the squad attributes to assess shortlisted players
    scouting_attributes_df['gk_score'] = (
            scouting_attributes_df['Aer']
            + scouting_attributes_df['Cmd']
            + scouting_attributes_df['Com']
            + scouting_attributes_df['Han']
            + scouting_attributes_df['Fir']
            + scouting_attributes_df['Kic']
            + scouting_attributes_df['Ref']
            + scouting_attributes_df['1v1']
            + scouting_attributes_df['Thr']
    )

    scouting_attributes_df['cb_score'] = (
            scouting_attributes_df['Cnt']
            + scouting_attributes_df['Pos']
            + scouting_attributes_df['Bra']
            + scouting_attributes_df['Hea']
            + scouting_attributes_df['Mar']
            + scouting_attributes_df['Tck']
            + scouting_attributes_df['Jum']
            + scouting_attributes_df['Acc']
    )

    scouting_attributes_df['wb_score'] = (
            scouting_attributes_df['Cnt']
            + scouting_attributes_df['Pos']
            + scouting_attributes_df['OtB']
            + scouting_attributes_df['Wor']
            + scouting_attributes_df['Mar']
            + scouting_attributes_df['Tck']
            + scouting_attributes_df['Sta']
            + scouting_attributes_df['Acc']
    )

    scouting_attributes_df['dm_score'] = (
            scouting_attributes_df['Cnt']
            + scouting_attributes_df['Pos']
            + scouting_attributes_df['OtB']
            + scouting_attributes_df['Wor']
            + scouting_attributes_df['Fir']
            + scouting_attributes_df['Tck']
            + scouting_attributes_df['Sta']
            + scouting_attributes_df['Dec']
    )

    scouting_attributes_df['cm_score'] = (
            scouting_attributes_df['Agi']
            + scouting_attributes_df['Vis']
            + scouting_attributes_df['OtB']
            + scouting_attributes_df['Wor']
            + scouting_attributes_df['Fir']
            + scouting_attributes_df['Bal']
            + scouting_attributes_df['Pas']
            + scouting_attributes_df['Dec']
    )

    scouting_attributes_df['wing_score'] = (
            scouting_attributes_df['Acc']
            + scouting_attributes_df['Pac']
            + scouting_attributes_df['OtB']
            + scouting_attributes_df['Tec']
            + scouting_attributes_df['Fir']
            + scouting_attributes_df['Dri']
            + scouting_attributes_df['Agi']
            + scouting_attributes_df['Fla']
    )

    scouting_attributes_df['str_score'] = (
            scouting_attributes_df['Acc']
            + scouting_attributes_df['Com']
            + scouting_attributes_df['OtB']
            + scouting_attributes_df['Fin']
            + scouting_attributes_df['Fir']
            + scouting_attributes_df['Tec']
            + scouting_attributes_df['Wor']
            + scouting_attributes_df['Jum']
    )

    return scouting_attributes_df


def build_stats_dataframe(squad_stats_file, scouting_stats_file):

    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

    # Configure Pandas Settings
    pd.set_option('display.max_columns', 20)
    pd.options.mode.chained_assignment = None

    # Configure Numpy setting to show numerical values rather than np.float64()
    np.set_printoptions(legacy='1.25')

    ## Create the DataFrames
    # Create squad stats DataFrame from squad stats view
    squad_stats_df = squad_stats_file.copy()
    squad_stats_df = squad_stats_df[0]

    # Create scouting stats DataFrame from Player Search View
    scouting_stats_df = scouting_stats_file.copy()
    scouting_stats_df = scouting_stats_df[0]

    # Add squad_stats_df into scouting_stats_df
    stats_df = pd.concat([scouting_stats_df, squad_stats_df])

    # Clean the dataframes ------------------------------

    # Remove unnecessary columns
    stats_df = stats_df.drop(columns=['Inf', 'Rec'])

    # Clean stats_df values
    for column in ['Transfer Value', 'Wage', 'Distance']:
        stats_df[column] = stats_df[column].str.replace('€', '')
        stats_df[column] = stats_df[column].str.replace('p/a', '')
        stats_df[column] = stats_df[column].str.replace(',', '')
        stats_df[column] = stats_df[column].str.split('-', expand=True, )[0]
        stats_df[column] = stats_df[column].str.replace('-', '')
        stats_df[column] = stats_df[column].str.replace('km', '')
        stats_df[column] = stats_df[column].str.replace('Unknown', '')
        stats_df[column] = stats_df[column].str.replace('Not for Sale', '')
        # Handle values with both '.' and 'K'
        mask_k = stats_df[column].str.contains(r'\.(?=.*K)', na=False, regex=True)
        stats_df.loc[mask_k, column] = stats_df.loc[mask_k, column].str.replace(r'\.', '', regex=True)
        stats_df.loc[mask_k, column] = stats_df.loc[mask_k, column].str.replace('K', '00', regex=False)
        # Handle values with both '.' and 'M'
        mask_m = stats_df[column].str.contains(r'\.(?=.*M)', na=False, regex=True)
        stats_df.loc[mask_m, column] = stats_df.loc[mask_m, column].str.replace(r'\.', '', regex=True)
        stats_df.loc[mask_m, column] = stats_df.loc[mask_m, column].str.replace('M', '00000', regex=False)
        # Handle values with only 'K'
        mask_only_k = stats_df[column].str.contains(r'K', na=False, regex=False) & (~mask_k)
        stats_df.loc[mask_only_k, column] = stats_df.loc[mask_only_k, column].str.replace('K', '000', regex=False)
        # Handle values with only 'M'
        mask_only_m = stats_df[column].str.contains(r'M', na=False, regex=False) & (~mask_m)
        stats_df.loc[mask_only_m, column] = stats_df.loc[mask_only_m, column].str.replace('M', '000000', regex=False)

        stats_df[column] = pd.to_numeric(stats_df[column])

    for column in ['Tck R', 'Shot %', 'Sv %', 'Pas %',
                   'OP-Cr %', 'Hdr %', 'xSv %', 'Cr C/A',
                   'Conv %', 'Pen/R', 'Pens Saved Ratio', 'Gwin']:
        stats_df[column] = stats_df[column].str.replace('-', '0')
        stats_df[column] = stats_df[column].str.replace('%', '').astype(float, errors='ignore')
        stats_df[column] = stats_df[column].multiply(.01)
        stats_df[column] = stats_df[column].round(2)

    for column in ['Age', 'Tck/90', 'Tck C', 'Tck A', 'Shot/90', 'ShT/90', 'ShT',
                   'Shots Outside Box/90', 'Shts Blckd/90', 'Shts Blckd', 'Shots',
                   'Svt', 'Svp', 'Svh', 'Pr passes/90', 'Pr Passes', 'Pres C/90',
                   'Pres C', 'Pres A/90', 'Pres A', 'Poss Won/90', 'Poss Lost/90',
                   'Ps C/90', 'Ps C', 'Ps A/90', 'Pas A', 'OP-KP/90', 'OP-KP',
                   'OP-Crs C/90', 'OP-Crs C', 'OP-Crs A/90', 'OP-Crs A', 'Off',
                   'Gl Mst', 'K Tck/90', 'K Tck', 'K Ps/90', 'K Pas', 'K Hdrs/90',
                   'Int/90', 'Itc', 'Sprints/90', 'Hdrs W/90', 'Hdrs', 'Hdrs L/90',
                   'Goals Outside Box', 'FK Shots', 'xGP/90', 'xGP', 'xG/shot',
                   'Drb/90', 'Drb', 'Cr C/90', 'Cr C', 'Cr A',
                   'Clr/90', 'Clear', 'CCC', 'Ch C/90', 'Blk/90', 'Blk', 'Asts/90',
                   'Aer A/90', 'Yel', 'xG', 'Saves/90', 'Tgls/90', 'Tcon/90', 'Tcon',
                   'Tgls', 'Tgls', 'Red', 'Pts/Gm', 'PoM', 'Pen/R', 'Pens S', 'Pens Saved',
                   'Pens Faced', 'Pens', 'NP-xG/90', 'NP-xG', 'Last Gl', 'Last C',
                   'Mins/Gm', 'Mins', 'Gls/90', 'Conc', 'Gls', 'Won', 'G. Mis', 'Lost',
                   'D', 'Gwin', 'Fls', 'FA', 'xG/90', 'xG-OP', 'xA/90', 'xA', 'Con/90',
                   'Cln/90', 'Clean Sheets', 'Av Rat', 'Ast', 'Hdrs A']:
        stats_df[column] = stats_df[column].apply(str).str.replace('-', '0').astype(float).round(2)

    # Create position filters dict
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

    # Create position tag columns -------------------------------
    # Function to check and tag positions correctly
    def check_position_tags(position, position_filter):
        # Split the position string by commas and strip any leading/trailing whitespace
        position_parts = [p.strip() for p in position.split(',')]

        # First, check for exact matches of each part in the position string
        for part in position_parts:
            # Check for exact match in the position filter list
            if part in position_filter:
                return True

        # Return False if no match is found
        return False

    # Loop over each position tag and its corresponding filter
    for position_tag, position_filter in position_filters.items():
        # Create a new column in the dataframe for the position tag
        stats_df[position_tag] = stats_df['Position'].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )

    # Create new column to fix 'Apps' parenthesis issue. Substitute appearances will be counted as 1 full appearance.
    # This number will be used to set a minimum 'total_apps' to exclude players with inflated stats in low # of Apps.

    stats_df["total_apps"] = (
        stats_df["Apps"]
        .str.extractall(r"(\d+)")
        .astype(int)
        .groupby(level=0)
        .sum()
    )

    # Set minimum apps threshold (Unnecessary?)
    minimum_apps = 10
    stats_df = stats_df[stats_df['total_apps'] >= minimum_apps]

    # Drop outliers with 0 Av Rat
    stats_df = stats_df[stats_df['Av Rat'] > 1]

    return stats_df


# Save the data to CSV file
# squad_attributes_df.to_csv('squad_attributes.csv', index=False)
# scouting_attributes_df.to_csv('scouting_attributes.csv', index=False)
# stats_df.to_csv('stats.csv', index=False)