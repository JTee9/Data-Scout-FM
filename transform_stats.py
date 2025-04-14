import pandas as pd
import numpy as np
from warnings import simplefilter
from config import international_position_filters

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# Configure Pandas Settings
# pd.set_option('display.max_columns', 20)
pd.options.mode.chained_assignment = None

# Configure Numpy setting to show numerical values rather than np.float64()
np.set_printoptions(legacy='1.25')


def build_stats_dataframe(squad_stats_file, player_search_stats_file, language_preference):
    # Create the DataFrames
    squad_stats_df = squad_stats_file.copy()
    print('Pulling squad stats data into build stats dataframes function')
    squad_stats_df = squad_stats_df[0]
    # Remove zero width spaces
    squad_stats_df.columns = squad_stats_df.columns.str.replace('\u200b', '')
    print('Complete: Pulling squad stats data into build stats dataframes function')

    player_search_stats_df = player_search_stats_file.copy()
    print('Pulling player search stats data into build stats dataframes function')
    player_search_stats_df = player_search_stats_df[0]
    # Remove zero width spaces
    player_search_stats_df.columns = player_search_stats_df.columns.str.replace('\u200b', '')

    # Combine squad & player search stats dataframes
    stats_df = pd.concat([player_search_stats_df, squad_stats_df])
    print(f'Complete: stats_df combined dataframe created with shape: {stats_df.shape}')

    # Remove unnecessary columns
    def drop_columns_by_number(df, column_numbers):
        columns_to_drop = [df.columns[i] for i in column_numbers]
        return df.drop(columns=columns_to_drop)

    stats_df = drop_columns_by_number(stats_df, [1, 2])

    # Group columns based on processing type
    value_cols = [5, 6, 47]  # Columns that need currency/unit removal and numeric conversion
    # Transfer Value, Wage, Distance
    percentage_cols = [69, 20, 94, 37, 59, 76, 95, 52, 29, 32, 100, 116]  # Columns that need percentage processing
    numeric_cols = [1, 67, 66, 68, 17, 19, 18, 21, 82, 81, 16, 91, 92, 93,
                    39, 38, 61, 60, 63, 62, 64, 65, 34, 33, 36, 35, 54, 53,
                    56, 55, 58, 57, 103, 87, 71, 70, 41, 40, 78, 86, 85, 44,
                    73, 72, 77, 11, 22, 97, 96, 25, 46, 45, 49, 48, 50, 84,
                    83, 14, 15, 80, 79, 13, 75, 106, 23, 90, 110, 112, 111,
                    109, 109, 107, 108, 121, 32, 31, 98, 99, 30, 28, 27, 119,
                    10, 101, 9, 113, 120, 115, 114, 116, 104, 105, 24, 26,
                    43, 42, 102, 89, 88, 8, 12, 74] # Columns with straightforward numeric values

    # Clean the value columns.
    for col_num in value_cols:
        # Remove currency symbols
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('€', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('$', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('£', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('¥', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('₩', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('₺', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('₽', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('AED', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('BGN', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Br', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Bt', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('CHF', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('CNY', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('CRC', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Din', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('DKK', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Ft', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('HK', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('hrn', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('INR', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('ISK', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Kc', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('KM', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Kn', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Kr', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('kr', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('KWD', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('KZT', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Lek', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('MKD Den', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('NIS', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('PHP', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('QAR', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('R', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('RM', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('RON', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('RP.', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('S', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('SAR', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('TWD', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('VND', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('zl', '')

        # Annual/Monthly/Weekly
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/a', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/m', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/w', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/s', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/v', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('万/周', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('万/月', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('万/年', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('亿/年', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('/年', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('/月', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('/週', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('/周', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('연봉', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('월급', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('주급', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('yıllık', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('aylık', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('haftallık', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('/år', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('måned', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('uge', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('J.', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('M.', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('W.', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/jr', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/å', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('p/u', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mies.', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('tyg.', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('rocznie', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('α/ε', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('α/μ', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('α/βδ', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('в нед.', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('в мес', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('в год', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace(',', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('km', '')

        # values in thousands
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('tys.', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('m', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('t', 'K')
        if language_preference == 'Turkish':
            stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('B', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('χ', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('тыс.', 'K')

        # values in millions
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mio', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mio.', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Mio', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mln.', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mill', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mn', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('εκ.', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('млн', 'M')

        # values in billions
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mia.', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Mrd.', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Mld', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mld', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('MM', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('md', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('MR', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('δισ.', 'B')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('млрд', 'B')

        # Other values
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('亿', '億')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('억', '億')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('만', '万')

        # Handle values with both '.' and 'K'
        mask_k = stats_df.iloc[:, col_num].str.contains(r'\.(?=.*K)', na=False, regex=True)
        stats_df.loc[mask_k, stats_df.columns[col_num]] = stats_df.loc[mask_k, stats_df.columns[col_num]].str.replace(
            r'\.', '', regex=True)
        stats_df.loc[mask_k, stats_df.columns[col_num]] = stats_df.loc[mask_k, stats_df.columns[col_num]].str.replace(
            'K', '00', regex=False)
        # Handle values with both '.' and 'M'
        mask_m = stats_df.iloc[:, col_num].str.contains(r'\.(?=.*M)', na=False, regex=True)
        stats_df.loc[mask_m, stats_df.columns[col_num]] = stats_df.loc[mask_m, stats_df.columns[col_num]].str.replace(
            r'\.', '', regex=True)
        stats_df.loc[mask_m, stats_df.columns[col_num]] = stats_df.loc[mask_m, stats_df.columns[col_num]].str.replace(
            'M', '00000', regex=False)
        # Handle values with both '.' and 'B'
        mask_b = stats_df.iloc[:, col_num].str.contains(r'\.(?=.*B)', na=False, regex=True)
        stats_df.loc[mask_b, stats_df.columns[col_num]] = stats_df.loc[mask_b, stats_df.columns[col_num]].str.replace(
            r'\.', '', regex=True)
        stats_df.loc[mask_b, stats_df.columns[col_num]] = stats_df.loc[mask_b, stats_df.columns[col_num]].str.replace(
            'B', '00000000', regex=False)
        # Handle values with both '.' and '千'
        mask_sen = stats_df.iloc[:, col_num].str.contains(r'\.(?=.*千)', na=False, regex=True)
        stats_df.loc[mask_sen, stats_df.columns[col_num]] = stats_df.loc[
            mask_sen, stats_df.columns[col_num]].str.replace(
            r'\.', '', regex=True)
        stats_df.loc[mask_sen, stats_df.columns[col_num]] = stats_df.loc[
            mask_sen, stats_df.columns[col_num]].str.replace(
            '千', '00', regex=False)
        # Handle values with both '.' and '万'
        mask_man = stats_df.iloc[:, col_num].str.contains(r'\.(?=.*万)', na=False, regex=True)
        stats_df.loc[mask_man, stats_df.columns[col_num]] = stats_df.loc[mask_man, stats_df.columns[col_num]].str.replace(
            r'\.', '', regex=True)
        stats_df.loc[mask_man, stats_df.columns[col_num]] = stats_df.loc[mask_man, stats_df.columns[col_num]].str.replace(
            '万', '000', regex=False)
        # Handle values with both '.' and '億'
        mask_oku = stats_df.iloc[:, col_num].str.contains(r'\.(?=.*億)', na=False, regex=True)
        stats_df.loc[mask_oku, stats_df.columns[col_num]] = stats_df.loc[
            mask_oku, stats_df.columns[col_num]].str.replace(
            r'\.', '', regex=True)
        stats_df.loc[mask_oku, stats_df.columns[col_num]] = stats_df.loc[
            mask_oku, stats_df.columns[col_num]].str.replace(
            '億', '0000000', regex=False)

        # Handle values with only 'K'
        mask_only_k = stats_df.iloc[:, col_num].str.contains(r'K', na=False, regex=False) & (~mask_k)
        stats_df.loc[mask_only_k, stats_df.columns[col_num]] = stats_df.loc[mask_only_k, stats_df.columns[col_num]].str.replace(
            'K', '000', regex=False)
        # Handle values with only 'M'
        mask_only_m = stats_df.iloc[:, col_num].str.contains(r'M', na=False, regex=False) & (~mask_m)
        stats_df.loc[mask_only_m, stats_df.columns[col_num]] = stats_df.loc[mask_only_m, stats_df.columns[col_num]].str.replace(
            'M', '000000', regex=False)
        # Handle values with only 'B'
        mask_only_b = stats_df.iloc[:, col_num].str.contains(r'B', na=False, regex=False) & (~mask_b)
        stats_df.loc[mask_only_b, stats_df.columns[col_num]] = stats_df.loc[mask_only_b, stats_df.columns[col_num]].str.replace(
            'B', '000000000', regex=False)
        # Handle values with only '千'
        mask_only_sen = stats_df.iloc[:, col_num].str.contains(r'千', na=False, regex=False) & (~mask_sen)
        stats_df.loc[mask_only_sen, stats_df.columns[col_num]] = stats_df.loc[
            mask_only_sen, stats_df.columns[col_num]].str.replace(
            '千', '000', regex=False)
        # Handle values with only '万'
        mask_only_man = stats_df.iloc[:, col_num].str.contains(r'万', na=False, regex=False) & (~mask_man)
        stats_df.loc[mask_only_man, stats_df.columns[col_num]] = stats_df.loc[
            mask_only_man, stats_df.columns[col_num]].str.replace(
            '万', '0000', regex=False)
        # Handle values with only '億'
        mask_only_oku = stats_df.iloc[:, col_num].str.contains(r'億', na=False, regex=False) & (~mask_oku)
        stats_df.loc[mask_only_oku, stats_df.columns[col_num]] = stats_df.loc[
            mask_only_oku, stats_df.columns[col_num]].str.replace(
            '億', '00000000', regex=False)

        # Remove any remaining '.'
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('.', '')

        # Handle transfer value ranges
        range_mask = stats_df.iloc[:, col_num].str.contains('-', na=False, regex=False)
        if range_mask.any():  # only do this if there are actually ranges.
            def average_range(range_str):
                try:
                    start, end = map(int, range_str.split('-'))
                    return (start + end) / 2
                except ValueError:
                    return np.nan  # return nan if there is a problem.

            print('Applying average_range function to stats_df to remove transfer values with ranges.')
            print(
                f'stats_df.loc[range_mask, stats_df.columns[col_num]]: {stats_df.loc[range_mask, stats_df.columns[col_num]]}')
            stats_df.loc[range_mask, stats_df.columns[col_num]] = stats_df.loc[
                range_mask, stats_df.columns[col_num]].apply(average_range)
            print('Complete: Applying average_range function to stats_df to remove transfer values with ranges.')

        stats_df.iloc[:, col_num] = pd.to_numeric(stats_df.iloc[:, col_num], errors='coerce')

    for col_num in percentage_cols:
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('-', '0')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('%', '').astype(float, errors='ignore')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].multiply(.01)
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].round(2)

    for col_num in numeric_cols:
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].apply(str).str.replace('-', '0')
        stats_df.iloc[:, col_num] = pd.to_numeric(stats_df.iloc[:, col_num], errors='coerce')
        stats_df.iloc[:, col_num].astype(float).round(2)

    # # Create Distance/90 column (need to rearrange column order before adding this)
    # distance_col = stats_df.iloc[:, 47]
    # minutes_col = stats_df.iloc[:, 119]
    # dist_per_90 = str(stats_df.columns[47] + '/90')
    # stats_df[dist_per_90] = distance_col / minutes_col * 90
    # print(stats_df[dist_per_90])

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
    print('Initiating check_position_tag function')
    for position_tag, position_filter in international_position_filters[language_preference].items():
        # Create a new column in the dataframe for the position tag
        stats_df[position_tag] = stats_df.iloc[:, 2].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )
    print(stats_df.tail(14))

    # Create new column to fix 'Apps' parenthesis issue. Substitute appearances will be counted as 1 full appearance.
    # This number will be used to set a minimum 'total_apps' to exclude players with inflated stats in low # of Apps.

    stats_df.iloc[:, 117] = (
        stats_df.iloc[:, 117]
        .str.extractall(r"(\d+)")
        .astype(int)
        .groupby(level=0)
        .sum()
    )

    # Set minimum apps threshold (Unnecessary?)
    minimum_apps = 10
    stats_df = stats_df[stats_df.iloc[:, 117] >= minimum_apps]

    # Drop outliers with 0 Av Rat
    stats_df = stats_df[stats_df.iloc[:, 8] > 1]

    print('Complete: stats_df')

    return stats_df
