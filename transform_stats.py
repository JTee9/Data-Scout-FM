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
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('χλμ', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('公里', '')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('км', '')

        # values in thousands
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('tys.', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('m', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('t', 'K')
        if language_preference == 'Turkish':
            stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('B', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('χ.', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('тыс.', 'K')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('千', 'K')

        # values in millions
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mio', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mio.', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('Mio', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mln.', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mill', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('mn', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('εκ.', 'M')
        stats_df.iloc[:, col_num] = stats_df.iloc[:, col_num].str.replace('млн.', 'M')

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

        # Process rows containing 'K'
        mask_k = stats_df.iloc[:, col_num].str.contains('K', na=False)
        for index in stats_df.index[mask_k]:
            value = stats_df.at[index, stats_df.columns[col_num]]
            if ' - ' in value:
                part1, part2 = value.split(' - ')

                def process_part_k(part):
                    if 'K' in part:
                        if '.' in part:
                            integer_part, decimal_part = part.split('.')
                            num_decimals = len(decimal_part.replace('K', ''))
                            k_removed = part.replace('K', '')
                            decimal_removed = k_removed.replace('.', '')
                            num_zeros = 3 - num_decimals
                            cleaned_part = decimal_removed + '0' * num_zeros
                        else:
                            cleaned_part = part.replace('K', '000')
                        return cleaned_part
                    return part

                part1_cleaned = process_part_k(part1)
                part2_cleaned = process_part_k(part2)
                stats_df.at[index, stats_df.columns[col_num]] = f"{part1_cleaned} - {part2_cleaned}"

            else:  # Handle single values with 'K'
                if '.' in value:
                    integer_part, decimal_part = value.split('.')
                    num_decimals = len(decimal_part.replace('K', ''))
                    k_removed = value.replace('K', '')
                    decimal_removed = k_removed.replace('.', '')
                    num_zeros = 3 - num_decimals
                    cleaned_value = decimal_removed + '0' * num_zeros
                else:
                    cleaned_value = value.replace('K', '000')
                stats_df.at[index, stats_df.columns[col_num]] = cleaned_value

        # Process rows containing 'M'
        mask_m = stats_df.iloc[:, col_num].str.contains('M', na=False)
        for index in stats_df.index[mask_m]:
            value = stats_df.at[index, stats_df.columns[col_num]]
            if ' - ' in value:
                part1, part2 = value.split(' - ')

                def process_part_m(part):
                    if 'M' in part:
                        if '.' in part:
                            integer_part, decimal_part = part.split('.')
                            num_decimals = len(decimal_part.replace('M', ''))
                            m_removed = part.replace('M', '')
                            decimal_removed = m_removed.replace('.', '')
                            num_zeros = 6 - num_decimals
                            cleaned_part = decimal_removed + '0' * num_zeros
                        else:
                            cleaned_part = part.replace('M', '000000')
                        return cleaned_part
                    return part

                part1_cleaned = process_part_m(part1)
                part2_cleaned = process_part_m(part2)
                stats_df.at[index, stats_df.columns[col_num]] = f"{part1_cleaned} - {part2_cleaned}"

            else:  # Handle single values with 'M'
                if '.' in value:
                    integer_part, decimal_part = value.split('.')
                    num_decimals = len(decimal_part.replace('M', ''))
                    m_removed = value.replace('M', '')
                    decimal_removed = m_removed.replace('.', '')
                    num_zeros = 6 - num_decimals
                    cleaned_value = decimal_removed + '0' * num_zeros
                else:
                    cleaned_value = value.replace('M', '000000')
                stats_df.at[index, stats_df.columns[col_num]] = cleaned_value

        # Process rows containing 'B'
        mask_b = stats_df.iloc[:, col_num].str.contains('B', na=False)
        for index in stats_df.index[mask_b]:
            value = stats_df.at[index, stats_df.columns[col_num]]
            if ' - ' in value:
                part1, part2 = value.split(' - ')

                def process_part_b(part):
                    if 'B' in part:
                        if '.' in part:
                            integer_part, decimal_part = part.split('.')
                            num_decimals = len(decimal_part.replace('B', ''))
                            b_removed = part.replace('B', '')
                            decimal_removed = b_removed.replace('.', '')
                            num_zeros = 9 - num_decimals
                            cleaned_part = decimal_removed + '0' * num_zeros
                        else:
                            cleaned_part = part.replace('B', '000000000')
                        return cleaned_part
                    return part

                part1_cleaned = process_part_b(part1)
                part2_cleaned = process_part_b(part2)
                stats_df.at[index, stats_df.columns[col_num]] = f"{part1_cleaned} - {part2_cleaned}"

            else:  # Handle single values with 'B'
                if '.' in value:
                    integer_part, decimal_part = value.split('.')
                    num_decimals = len(decimal_part.replace('B', ''))
                    b_removed = value.replace('B', '')
                    decimal_removed = b_removed.replace('.', '')
                    num_zeros = 9 - num_decimals
                    cleaned_value = decimal_removed + '0' * num_zeros
                else:
                    cleaned_value = value.replace('B', '000000000')
                stats_df.at[index, stats_df.columns[col_num]] = cleaned_value

        # Process rows containing '万'
        mask_man = stats_df.iloc[:, col_num].str.contains('万', na=False)
        for index in stats_df.index[mask_man]:
            value = stats_df.at[index, stats_df.columns[col_num]]
            if ' - ' in value:
                part1, part2 = value.split(' - ')

                def process_part_man(part):
                    if '万' in part:
                        if '.' in part:
                            integer_part, decimal_part = part.split('.')
                            num_decimals = len(decimal_part.replace('万', ''))
                            man_removed = part.replace('万', '')
                            decimal_removed = man_removed.replace('.', '')
                            num_zeros = 4 - num_decimals
                            cleaned_part = decimal_removed + '0' * num_zeros
                        else:
                            cleaned_part = part.replace('万', '0000')
                        return cleaned_part
                    return part

                part1_cleaned = process_part_man(part1)
                part2_cleaned = process_part_man(part2)
                stats_df.at[index, stats_df.columns[col_num]] = f"{part1_cleaned} - {part2_cleaned}"

            else:  # Handle single values with '万'
                if '.' in value:
                    integer_part, decimal_part = value.split('.')
                    num_decimals = len(decimal_part.replace('万', ''))
                    man_removed = value.replace('万', '')
                    decimal_removed = man_removed.replace('.', '')
                    num_zeros = 4 - num_decimals
                    cleaned_value = decimal_removed + '0' * num_zeros
                else:
                    cleaned_value = value.replace('万', '0000')
                stats_df.at[index, stats_df.columns[col_num]] = cleaned_value

        # Process rows containing '億'
        mask_oku = stats_df.iloc[:, col_num].str.contains('億', na=False)
        for index in stats_df.index[mask_oku]:
            value = stats_df.at[index, stats_df.columns[col_num]]
            if ' - ' in value:
                part1, part2 = value.split(' - ')

                def process_part_oku(part):
                    if '億' in part:
                        if '.' in part:
                            integer_part, decimal_part = part.split('.')
                            num_decimals = len(decimal_part.replace('億', ''))
                            oku_removed = part.replace('億', '')
                            decimal_removed = oku_removed.replace('.', '')
                            num_zeros = 8 - num_decimals
                            cleaned_part = decimal_removed + '0' * num_zeros
                        else:
                            cleaned_part = part.replace('億', '00000000')
                        return cleaned_part
                    return part

                part1_cleaned = process_part_oku(part1)
                part2_cleaned = process_part_oku(part2)
                stats_df.at[index, stats_df.columns[col_num]] = f"{part1_cleaned} - {part2_cleaned}"

            else:  # Handle single values with '億'
                if '.' in value:
                    integer_part, decimal_part = value.split('.')
                    num_decimals = len(decimal_part.replace('億', ''))
                    oku_removed = value.replace('億', '')
                    decimal_removed = oku_removed.replace('.', '')
                    num_zeros = 8 - num_decimals
                    cleaned_value = decimal_removed + '0' * num_zeros
                else:
                    cleaned_value = value.replace('億', '00000000')
                stats_df.at[index, stats_df.columns[col_num]] = cleaned_value

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

            stats_df.loc[range_mask, stats_df.columns[col_num]] = stats_df.loc[
                range_mask, stats_df.columns[col_num]].apply(average_range)

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
    new_columns = {}
    for position_tag, position_filter in international_position_filters[language_preference].items():
        # Create a new column in the dataframe for the position tag
        new_columns[position_tag] = stats_df.iloc[:, 2].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )
    new_df = pd.DataFrame(new_columns)
    stats_df = pd.concat([stats_df, new_df], axis=1)


    # Configure 'Apps' columns to solve parenthesis issue. Substitute appearances will be counted as 1 full appearance.
    # This number will be used to set a minimum total apps to exclude players with inflated stats in low # of Apps.

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
