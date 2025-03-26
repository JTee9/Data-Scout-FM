import pandas as pd
import numpy as np
from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# Configure Pandas Settings
pd.set_option('display.max_columns', 20)
pd.options.mode.chained_assignment = None

# Configure Numpy setting to show numerical values rather than np.float64()
np.set_printoptions(legacy='1.25')


def build_stats_dataframe(squad_stats_file, player_search_stats_file):

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
    player_search_stats_df = player_search_stats_file.copy()
    player_search_stats_df = player_search_stats_df[0]

    # Add squad_stats_df into player_search_stats_df
    stats_df = pd.concat([player_search_stats_df, squad_stats_df])

    # Clean the dataframes ------------------------------

    # Remove unnecessary columns
    stats_df = stats_df.drop(columns=['Inf', 'Rec'])

    for column in ['Transfer Value', 'Wage', 'Distance']:
        # Remove currency symbols
        stats_df[column] = stats_df[column].str.replace('€', '')
        stats_df[column] = stats_df[column].str.replace('$', '')
        stats_df[column] = stats_df[column].str.replace('£', '')
        stats_df[column] = stats_df[column].str.replace('¥', '')
        stats_df[column] = stats_df[column].str.replace('₩', '')
        stats_df[column] = stats_df[column].str.replace('₺', '')
        stats_df[column] = stats_df[column].str.replace('₽', '')
        stats_df[column] = stats_df[column].str.replace('AED', '')
        stats_df[column] = stats_df[column].str.replace('BGN', '')
        stats_df[column] = stats_df[column].str.replace('Br', '')
        stats_df[column] = stats_df[column].str.replace('Bt', '')
        stats_df[column] = stats_df[column].str.replace('CHF', '')
        stats_df[column] = stats_df[column].str.replace('CNY', '')
        stats_df[column] = stats_df[column].str.replace('CRC', '')
        stats_df[column] = stats_df[column].str.replace('Din', '')
        stats_df[column] = stats_df[column].str.replace('DKK', '')
        stats_df[column] = stats_df[column].str.replace('Ft', '')
        stats_df[column] = stats_df[column].str.replace('HK', '')
        stats_df[column] = stats_df[column].str.replace('hrn', '')
        stats_df[column] = stats_df[column].str.replace('INR', '')
        stats_df[column] = stats_df[column].str.replace('ISK', '')
        stats_df[column] = stats_df[column].str.replace('Kc', '')
        stats_df[column] = stats_df[column].str.replace('KM', '')
        stats_df[column] = stats_df[column].str.replace('Kn', '')
        stats_df[column] = stats_df[column].str.replace('Kr', '')
        stats_df[column] = stats_df[column].str.replace('kr', '')
        stats_df[column] = stats_df[column].str.replace('KWD', '')
        stats_df[column] = stats_df[column].str.replace('KZT', '')
        stats_df[column] = stats_df[column].str.replace('Lek', '')
        stats_df[column] = stats_df[column].str.replace('MKD Den', '')
        stats_df[column] = stats_df[column].str.replace('NIS', '')
        stats_df[column] = stats_df[column].str.replace('PHP', '')
        stats_df[column] = stats_df[column].str.replace('QAR', '')
        stats_df[column] = stats_df[column].str.replace('R', '')
        stats_df[column] = stats_df[column].str.replace('RM', '')
        stats_df[column] = stats_df[column].str.replace('RON', '')
        stats_df[column] = stats_df[column].str.replace('RP.', '')
        stats_df[column] = stats_df[column].str.replace('S', '')
        stats_df[column] = stats_df[column].str.replace('SAR', '')
        stats_df[column] = stats_df[column].str.replace('TWD', '')
        stats_df[column] = stats_df[column].str.replace('VND', '')
        stats_df[column] = stats_df[column].str.replace('zl', '')

        stats_df[column] = stats_df[column].str.replace('p/a', '')
        stats_df[column] = stats_df[column].str.replace('p/m', '')
        stats_df[column] = stats_df[column].str.replace('p/w', '')
        stats_df[column] = stats_df[column].str.replace(',', '')
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
        # Handle values with both '.' and 'B'
        mask_b = stats_df[column].str.contains(r'\.(?=.*B)', na=False, regex=True)
        stats_df.loc[mask_b, column] = stats_df.loc[mask_b, column].str.replace(r'\.', '', regex=True)
        stats_df.loc[mask_b, column] = stats_df.loc[mask_b, column].str.replace('B', '00000000', regex=False)
        # Handle values with only 'B'
        mask_only_b = stats_df[column].str.contains(r'B', na=False, regex=False) & (~mask_b)
        stats_df.loc[mask_only_b, column] = stats_df.loc[mask_only_b, column].str.replace('B', '000000000', regex=False)
        # Remove any remaining '.'
        stats_df[column] = stats_df[column].str.replace('.', '')

        # Handle transfer value ranges

        def process_range_column(stats_df, column):
            """Processes a column containing range strings."""
            stats_df[column] = stats_df[column].astype(str).str.strip()
            range_mask = stats_df[column].str.contains('-', na=False, regex=False)

            if range_mask.any():
                def average_range(range_str):

                    try:
                        start, end = map(float, range_str.split('-'))
                        result = (start + end) / 2
                        return result
                    except ValueError as e:
                        return np.nan
                    except AttributeError as e:
                        return np.nan

                stats_df.loc[range_mask, column] = stats_df.loc[range_mask, column].apply(average_range)
            return stats_df

        stats_df = process_range_column(stats_df, 'Transfer Value')

        stats_df[column] = pd.to_numeric(stats_df[column], errors='coerce')

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
                   'Drb/90', 'Drb', 'Cr C/90', 'Cr C', 'Cr A', 'Crs A/90',
                   'Clr/90', 'Clear', 'CCC', 'Ch C/90', 'Blk/90', 'Blk', 'Asts/90',
                   'Aer A/90', 'Yel', 'xG', 'Saves/90', 'Tgls/90', 'Tcon/90', 'Tcon',
                   'Tgls', 'Red', 'Pts/Gm', 'PoM', 'Pen/R', 'Pens S', 'Pens Saved',
                   'Pens Faced', 'Pens', 'NP-xG/90', 'NP-xG', 'Mins', 'Starts',
                   'Gls/90', 'Conc', 'Gls', 'Won', 'G. Mis', 'Lost',
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
        if not isinstance(position, str):
            return False  # Return False for non-string values

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

    # Fix 'Apps' parenthesis issue. *Substitute appearances will be counted as 1 full appearance.
    # This number will be used to set a minimum Apps # to exclude players with no stats or inflated stats in low # of Apps.

    def process_apps_column(value):
        if isinstance(value, str):
            if '(' in value:
                # Case with parentheses
                extracted = pd.Series(value).str.extract(r"(\d+)\s*\(?(\d*)\)?")
                return extracted.fillna(0).astype(int).sum(axis=1).iloc[0]
            else:
                # Case without parentheses
                extracted = pd.Series(value).str.extract(r"(\d+)")
                if not extracted.empty:
                    return extracted.fillna(0).astype(int).sum(axis=1).iloc[0]
                else:
                    return 0  # return 0 if no value is found
        else:
            return value  # return value if it is already an integer rather than a string

    stats_df["Apps"] = stats_df["Apps"].apply(process_apps_column)

    # Set minimum apps threshold (Unnecessary?)
    minimum_apps = 10
    stats_df = stats_df[stats_df['Apps'] >= minimum_apps]

    # Drop outliers with 0 Av Rat
    stats_df = stats_df[stats_df['Av Rat'] > 1]

    return stats_df
