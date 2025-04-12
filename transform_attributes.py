import pandas as pd
import numpy as np
from warnings import simplefilter
from config import international_position_filters, international_role_name_dict, overall_radar_columns_dict

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# Configure Pandas Settings
pd.set_option('display.max_columns', 20)
pd.options.mode.chained_assignment = None

# Configure Numpy setting to show numerical values rather than np.float64()
np.set_printoptions(legacy='1.25')


# Function to transform user's squad_attributes file into the correct format for the app
def build_squad_attributes_dataframe(squad_attributes_file, language_preference):
    # Create squad attributes DataFrame from squad attributes view
    squad_attributes_df = squad_attributes_file.copy()
    print('Pulling squad attributes data into build attributes dataframes function')
    squad_attributes_df = squad_attributes_df[0]
    print('Complete: Pulling squad stats data into build stats dataframes function')

    # Remove zero width spaces
    squad_attributes_df.columns = squad_attributes_df.columns.str.replace('\u200b', '')

    # Create new columns for 'Overall' and 'GK Overall' radar chart
    overall_radar_columns = overall_radar_columns_dict[language_preference]

    def create_overall_radar_column(df, new_column_name_base, column_indices):
        """
        Creates a new column in the DataFrame by calculating the mean of specified columns.
        If a column with the same base name already exists, it appends '(Overall)' to the new column name.

        Args:
            df (pd.DataFrame): The input DataFrame.
            new_column_name_base (str): The base name for the new column.
            column_indices (list): A list of integer indices of the columns to average.

        Returns:
            pd.DataFrame: The DataFrame with the new column added.
        """
        new_column_name = new_column_name_base
        if new_column_name in df.columns:
            new_column_name += ' (Overall)'

        df[new_column_name] = df.iloc[:, column_indices].mean(axis=1).round(0)
        return df

    # Calculate the average of the columns for each category on the 'Overall' charts
    print('Creating overall radar columns for squad attributes.')
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[0], [5, 20])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[1], [19, 33, 7])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[2], [35, 43, 22])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[3], [37, 34, 9])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[4], [30, 29])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[5],
                                                      [48, 46, 42, 39, 38, 10])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[6], [24, 11, 17])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[7], [49, 47, 13, 12])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[8], [51, 31])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[9], [21, 15])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[10], [28, 8])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[11], [45, 44])
    squad_attributes_df = create_overall_radar_column(squad_attributes_df, overall_radar_columns[12], [36])

    # # Calculate the average of the columns for each category on the 'Overall' charts
    # print('Creating overall radar columns for squad attributes.')
    # squad_attributes_df[overall_radar_columns[0]] = squad_attributes_df.iloc[:, [5, 20]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[1]] = squad_attributes_df.iloc[:, [19, 33, 7]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[2]] = squad_attributes_df.iloc[:, [35, 43, 22]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[3]] = squad_attributes_df.iloc[:, [37, 34, 9]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[4]] = squad_attributes_df.iloc[:, [30, 29]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[5]] = squad_attributes_df.iloc[:, [48, 46, 42, 39, 38, 10]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[6]] = squad_attributes_df.iloc[:, [24, 11, 17]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[7]] = squad_attributes_df.iloc[:, [49, 47, 13, 12]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[8]] = squad_attributes_df.iloc[:, [51, 31]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[9]] = squad_attributes_df.iloc[:, [21, 15]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[10]] = squad_attributes_df.iloc[:, [28, 8]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[11]] = squad_attributes_df.iloc[:, [45, 44]].mean(axis=1).round(0)
    # squad_attributes_df[overall_radar_columns[12]] = squad_attributes_df.iloc[:, 36].round(0)

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
    for position_tag, position_filter in international_position_filters[language_preference].items():
        # Create a new column in the dataframe for the position tag
        squad_attributes_df[position_tag] = squad_attributes_df.iloc[:, 1].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )

    # Function to create role score columns
    def calculate_role_score(df, key_attributes, pref_attributes, column_title):
        key_attributes_total = df.iloc[:, key_attributes].sum(axis=1)
        pref_attributes_total = df.iloc[:, pref_attributes].sum(axis=1)
        role_total = (3 * key_attributes_total) + (2 * pref_attributes_total)
        role_max = (3 * (20 * len(key_attributes))) + (2 * (20 * len(pref_attributes)))
        role_score = (role_total / role_max) * 100
        df[column_title] = role_score.round(0).astype(int)
        return df

    # Pull role name list in user's language
    role_list = international_role_name_dict[language_preference]

    # Goalkeeper role scores --------------------------------
    gk_key_attributes = [49, 42, 17, 51, 45, 44, 31, 28, 15]
    gk_pref_attributes = [48, 39, 21, 8]
    calculate_role_score(squad_attributes_df, gk_key_attributes, gk_pref_attributes,
                         role_list[0])

    sweeper_keeper_de_key_attributes = [49, 48, 42, 17, 45, 28, 21, 15]
    sweeper_keeper_de_pref_attributes = [5, 43, 39, 7, 51, 44, 34, 31, 19, 14, 8]
    calculate_role_score(squad_attributes_df, sweeper_keeper_de_key_attributes, sweeper_keeper_de_pref_attributes,
                         role_list[1])

    sweeper_keeper_su_key_attributes = [49, 48, 43, 42, 17, 45, 28, 21, 15, 14]
    sweeper_keeper_su_pref_attributes = [5, 39, 7, 51, 44, 34, 31, 19, 8]
    calculate_role_score(squad_attributes_df, sweeper_keeper_su_key_attributes, sweeper_keeper_su_pref_attributes,
                         role_list[2])

    sweeper_keeper_at_key_attributes = [49, 48, 43, 42, 17, 45, 28, 21, 15, 14]
    sweeper_keeper_at_pref_attributes = [5, 39, 7, 51, 44, 36, 34, 31, 19, 8]
    calculate_role_score(squad_attributes_df, sweeper_keeper_at_key_attributes, sweeper_keeper_at_pref_attributes,
                         role_list[3])

    # Central Defender Role Scores ----------------------------------------
    central_def_de_key_attributes = [29, 12, 17, 30, 24, 11]
    central_def_de_pref_attributes = [20, 50, 48, 46, 43, 42, 39]
    calculate_role_score(squad_attributes_df, central_def_de_key_attributes, central_def_de_pref_attributes,
                         role_list[4])

    central_def_st_key_attributes = [29, 12, 50, 46, 17, 39, 30, 11]
    central_def_st_pref_attributes = [24, 48, 43, 42]
    calculate_role_score(squad_attributes_df, central_def_st_key_attributes, central_def_st_pref_attributes,
                         role_list[5])

    central_def_co_key_attributes = [20, 48, 42, 39, 17, 24, 11]
    central_def_co_pref_attributes = [29, 12, 46, 43, 30]
    calculate_role_score(squad_attributes_df, central_def_co_key_attributes, central_def_co_pref_attributes,
                         role_list[6])

    no_nonsense_cb_de_key_attributes = [29, 12, 17, 30, 24, 11]
    no_nonsense_cb_de_pref_attributes = [20, 50, 48, 46, 42]
    calculate_role_score(squad_attributes_df, no_nonsense_cb_de_key_attributes, no_nonsense_cb_de_pref_attributes,
                         role_list[7])

    no_nonsense_cb_st_key_attributes = [29, 12, 50, 46, 17, 30, 11]
    no_nonsense_cb_st_pref_attributes = [24, 48, 42]
    calculate_role_score(squad_attributes_df, no_nonsense_cb_st_key_attributes, no_nonsense_cb_st_pref_attributes,
                         role_list[8])

    no_nonsense_cb_co_key_attributes = [20, 48, 42, 39, 17, 24, 11]
    no_nonsense_cb_co_pref_attributes = [29, 12, 46, 30]
    calculate_role_score(squad_attributes_df, no_nonsense_cb_co_key_attributes, no_nonsense_cb_co_pref_attributes,
                         role_list[9])

    wide_cb_de_key_attributes = [29, 12, 17, 30, 24, 11]
    wide_cb_de_pref_attributes = [49, 20, 50, 48, 46, 43, 42, 6, 37, 34, 19, 9]
    calculate_role_score(squad_attributes_df, wide_cb_de_key_attributes, wide_cb_de_pref_attributes,
                         role_list[10])

    wide_cb_su_key_attributes = [29, 20, 12, 17, 37, 30, 24, 11]
    wide_cb_su_pref_attributes = [49, 13, 50, 48, 46, 43, 42, 39, 22, 6, 40, 34, 19, 9]
    calculate_role_score(squad_attributes_df, wide_cb_su_key_attributes, wide_cb_su_pref_attributes,
                         role_list[11])

    wide_cb_at_key_attributes = [29, 20, 13, 12, 22, 40, 37, 30, 24, 11]
    wide_cb_at_pref_attributes = [49, 50, 48, 46, 43, 42, 39, 17, 6, 34, 19, 9]
    calculate_role_score(squad_attributes_df, wide_cb_at_key_attributes, wide_cb_at_pref_attributes,
                         role_list[12])

    ball_playing_def_de_key_attributes = [29, 12, 43, 17, 30, 24, 19, 11]
    ball_playing_def_de_pref_attributes = [20, 50, 48, 46, 42, 39, 7, 34, 9]
    calculate_role_score(squad_attributes_df, ball_playing_def_de_key_attributes,
                         ball_playing_def_de_pref_attributes,
                         role_list[13])

    ball_playing_def_st_key_attributes = [29, 12, 50, 46, 43, 39, 17, 30, 19, 11]
    ball_playing_def_st_pref_attributes = [48, 42, 7, 34, 24, 9]
    calculate_role_score(squad_attributes_df, ball_playing_def_st_key_attributes,
                         ball_playing_def_st_pref_attributes,
                         role_list[14])

    ball_playing_def_co_key_attributes = [20, 48, 43, 42, 39, 17, 24, 19, 11]
    ball_playing_def_co_pref_attributes = [29, 12, 46, 7, 34, 30, 9]
    calculate_role_score(squad_attributes_df, ball_playing_def_co_key_attributes,
                         ball_playing_def_co_pref_attributes,
                         role_list[15])

    libero_de_key_attributes = [29, 12, 43, 39, 17, 10, 34, 30, 24, 19, 11, 9]
    libero_de_pref_attributes = [20, 13, 48, 46, 42]
    calculate_role_score(squad_attributes_df, libero_de_key_attributes, libero_de_pref_attributes,
                         role_list[16])

    libero_su_key_attributes = [29, 12, 43, 39, 17, 10, 34, 30, 24, 19, 11, 9]
    libero_su_pref_attributes = [20, 13, 48, 46, 42, 7, 37]
    calculate_role_score(squad_attributes_df, libero_su_key_attributes, libero_su_pref_attributes,
                         role_list[17])

    # Fullback/Wingback role scores ------------------------------------------
    fullback_de_key_attributes = [48, 42, 17, 24, 11]
    fullback_de_pref_attributes = [20, 13, 39, 10, 6, 40, 19]
    calculate_role_score(squad_attributes_df, fullback_de_key_attributes, fullback_de_pref_attributes,
                         role_list[18])

    fullback_su_key_attributes = [48, 42, 17, 24, 11]
    fullback_su_pref_attributes = [20, 13, 39, 10, 6, 40, 37, 19, 9]
    calculate_role_score(squad_attributes_df, fullback_su_key_attributes, fullback_su_pref_attributes,
                         role_list[19])

    fullback_at_key_attributes = [48, 17, 10, 40, 24, 11]
    fullback_at_pref_attributes = [49, 20, 13, 42, 39, 22, 6, 37, 34, 19, 9]
    calculate_role_score(squad_attributes_df, fullback_at_key_attributes, fullback_at_pref_attributes,
                         role_list[20])

    fullback_au_key_attributes = [48, 42, 17, 10, 24, 11]
    fullback_au_pref_attributes = [49, 20, 13, 39, 6, 40, 37, 19, 9]
    calculate_role_score(squad_attributes_df, fullback_au_key_attributes, fullback_au_pref_attributes,
                         role_list[21])

    no_nonsense_fb_key_attributes = [12, 48, 17, 24, 11]
    no_nonsense_fb_pref_attributes = [50, 46, 42, 10, 30]
    calculate_role_score(squad_attributes_df, no_nonsense_fb_key_attributes, no_nonsense_fb_pref_attributes,
                         role_list[22])

    inverted_fb_key_attributes = [12, 17, 30, 24, 11]
    inverted_fb_pref_attributes = [49, 29, 20, 50, 48, 46, 43, 42, 39, 6, 37, 34, 19, 9]
    calculate_role_score(squad_attributes_df, inverted_fb_key_attributes, inverted_fb_pref_attributes,
                         role_list[23])

    wingback_de_key_attributes = [5, 13, 48, 17, 10, 6, 24, 11]
    wingback_de_pref_attributes = [49, 47, 20, 42, 39, 22, 40, 37, 34, 19, 9]
    calculate_role_score(squad_attributes_df, wingback_de_key_attributes, wingback_de_pref_attributes,
                         role_list[24])

    wingback_su_key_attributes = [5, 13, 22, 10, 6, 40, 37, 24, 11]
    wingback_su_pref_attributes = [49, 47, 20, 48, 42, 39, 17, 34, 19, 9]
    calculate_role_score(squad_attributes_df, wingback_su_key_attributes, wingback_su_pref_attributes,
                         role_list[25])

    wingback_at_key_attributes = [5, 20, 13, 22, 10, 6, 40, 37, 11, 9]
    wingback_at_pref_attributes = [49, 47, 48, 42, 39, 33, 17, 34, 24, 19]
    calculate_role_score(squad_attributes_df, wingback_at_key_attributes, wingback_at_pref_attributes,
                         role_list[26])

    wingback_au_key_attributes = [5, 13, 22, 10, 6, 40, 37, 24, 11]
    wingback_au_pref_attributes = [49, 47, 20, 48, 42, 39, 17, 34, 19, 9]
    calculate_role_score(squad_attributes_df, wingback_au_key_attributes, wingback_au_pref_attributes,
                         role_list[27])

    complete_wingback_su_key_attributes = [5, 13, 22, 10, 6, 40, 37, 9]
    complete_wingback_su_pref_attributes = [49, 47, 20, 48, 39, 33, 17, 34, 24, 19, 11]
    calculate_role_score(squad_attributes_df, complete_wingback_su_key_attributes,
                         complete_wingback_su_pref_attributes,
                         role_list[28])

    complete_wingback_at_key_attributes = [5, 13, 33, 22, 10, 6, 40, 37, 9]
    complete_wingback_at_pref_attributes = [49, 47, 20, 48, 39, 17, 34, 24, 19, 11]
    calculate_role_score(squad_attributes_df, complete_wingback_at_key_attributes,
                         complete_wingback_at_pref_attributes,
                         role_list[29])

    inverted_wb_de_key_attributes = [48, 39, 17, 10, 19, 11]
    inverted_wb_de_pref_attributes = [5, 49, 13, 43, 42, 22, 6, 34, 24, 9]
    calculate_role_score(squad_attributes_df, inverted_wb_de_key_attributes, inverted_wb_de_pref_attributes,
                         role_list[30])

    inverted_wb_su_key_attributes = [43, 39, 10, 34, 19, 11]
    inverted_wb_su_pref_attributes = [5, 49, 13, 48, 42, 22, 17, 7, 6, 24, 9]
    calculate_role_score(squad_attributes_df, inverted_wb_su_key_attributes, inverted_wb_su_pref_attributes,
                         role_list[31])

    inverted_wb_at_key_attributes = [5, 43, 39, 22, 10, 7, 34, 19, 11, 9]
    inverted_wb_at_pref_attributes = [49, 20, 13, 48, 42, 33, 17, 6, 40, 37, 26, 24]
    calculate_role_score(squad_attributes_df, inverted_wb_at_key_attributes, inverted_wb_at_pref_attributes,
                         role_list[32])

    # Defensive Midfielder role scores -------------------------------------------
    anchor_key_attributes = [48, 42, 39, 17, 24, 11]
    anchor_pref_attributes = [12, 43, 10]
    calculate_role_score(squad_attributes_df, anchor_key_attributes, anchor_pref_attributes,
                         role_list[33])

    half_back_key_attributes = [48, 43, 42, 39, 17, 10, 24, 11]
    half_back_pref_attributes = [29, 13, 12, 50, 46, 6, 34, 19]
    calculate_role_score(squad_attributes_df, half_back_key_attributes, half_back_pref_attributes,
                         role_list[34])

    defensive_midfielder_de_key_attributes = [48, 42, 17, 10, 11]
    defensive_midfielder_de_pref_attributes = [13, 12, 50, 43, 39, 6, 24, 19]
    calculate_role_score(squad_attributes_df, defensive_midfielder_de_key_attributes,
                         defensive_midfielder_de_pref_attributes,
                         role_list[35])

    defensive_midfielder_su_key_attributes = [48, 42, 17, 10, 11]
    defensive_midfielder_su_pref_attributes = [13, 12, 50, 43, 39, 6, 34, 24, 19]
    calculate_role_score(squad_attributes_df, defensive_midfielder_su_key_attributes,
                         defensive_midfielder_su_pref_attributes,
                         role_list[36])

    segundo_volante_su_key_attributes = [20, 13, 22, 17, 6, 24, 19, 11]
    segundo_volante_su_pref_attributes = [5, 47, 12, 48, 43, 42, 39, 35, 34, 26]
    calculate_role_score(squad_attributes_df, segundo_volante_su_key_attributes, segundo_volante_su_pref_attributes,
                         role_list[37])

    segundo_volante_at_key_attributes = [20, 13, 48, 22, 17, 6, 35, 26, 19, 11]
    segundo_volante_at_pref_attributes = [5, 47, 12, 43, 42, 39, 34, 24]
    calculate_role_score(squad_attributes_df, segundo_volante_at_key_attributes, segundo_volante_at_pref_attributes,
                         role_list[38])

    regista_key_attributes = [43, 39, 33, 22, 10, 7, 34, 19, 9]
    regista_pref_attributes = [47, 48, 37, 26]
    calculate_role_score(squad_attributes_df, regista_key_attributes, regista_pref_attributes,
                         role_list[39])

    ball_winning_midfielder_de_key_attributes = [13, 50, 48, 10, 6, 11]
    ball_winning_midfielder_de_pref_attributes = [49, 20, 12, 46, 42, 17, 24]
    calculate_role_score(squad_attributes_df, ball_winning_midfielder_de_key_attributes,
                         ball_winning_midfielder_de_pref_attributes,
                         role_list[40])

    ball_winning_midfielder_su_key_attributes = [13, 50, 48, 10, 6, 11]
    ball_winning_midfielder_su_pref_attributes = [49, 20, 12, 46, 42, 24, 19]
    calculate_role_score(squad_attributes_df, ball_winning_midfielder_su_key_attributes,
                         ball_winning_midfielder_su_pref_attributes,
                         role_list[41])

    deep_lying_playmaker_de_key_attributes = [43, 39, 10, 7, 34, 19, 9]
    deep_lying_playmaker_de_pref_attributes = [47, 48, 17, 11]
    calculate_role_score(squad_attributes_df, deep_lying_playmaker_de_key_attributes,
                         deep_lying_playmaker_de_pref_attributes,
                         role_list[42])

    deep_lying_playmaker_su_key_attributes = [43, 39, 10, 7, 34, 19, 9]
    deep_lying_playmaker_su_pref_attributes = [47, 48, 22, 17]
    calculate_role_score(squad_attributes_df, deep_lying_playmaker_su_key_attributes,
                         deep_lying_playmaker_su_pref_attributes,
                         role_list[43])

    roaming_playmaker_key_attributes = [5, 13, 48, 43, 39, 22, 10, 7, 6, 34, 19, 9]
    roaming_playmaker_pref_attributes = [49, 47, 20, 42, 17, 37, 26]
    calculate_role_score(squad_attributes_df, roaming_playmaker_key_attributes, roaming_playmaker_pref_attributes,
                         role_list[44])

    # Central Midfielder role scores --------------------------------------------
    carrilero_key_attributes = [13, 39, 17, 10, 34, 19, 11]
    carrilero_pref_attributes = [48, 43, 42, 22, 7, 6, 9]
    calculate_role_score(squad_attributes_df, carrilero_key_attributes, carrilero_pref_attributes,
                         role_list[45])

    box_to_box_midfielder_key_attributes = [13, 22, 10, 6, 19, 11]
    box_to_box_midfielder_pref_attributes = [5, 47, 20, 12, 50, 48, 43, 39, 17, 37, 35, 34, 26, 9]
    calculate_role_score(squad_attributes_df, box_to_box_midfielder_key_attributes,
                         box_to_box_midfielder_pref_attributes,
                         role_list[46])

    central_midfielder_de_key_attributes = [42, 39, 17, 10, 11]
    central_midfielder_de_pref_attributes = [13, 50, 48, 43, 6, 34, 24, 19, 9]
    calculate_role_score(squad_attributes_df, central_midfielder_de_key_attributes,
                         central_midfielder_de_pref_attributes,
                         role_list[47])

    central_midfielder_su_key_attributes = [39, 10, 34, 19, 11]
    central_midfielder_su_pref_attributes = [13, 48, 43, 42, 22, 7, 6, 9]
    calculate_role_score(squad_attributes_df, central_midfielder_su_key_attributes,
                         central_midfielder_su_pref_attributes,
                         role_list[48])

    central_midfielder_at_key_attributes = [39, 22, 34, 19]
    central_midfielder_at_pref_attributes = [5, 13, 48, 43, 10, 7, 6, 26, 11, 9]
    calculate_role_score(squad_attributes_df, central_midfielder_at_key_attributes,
                         central_midfielder_at_pref_attributes,
                         role_list[49])

    central_midfielder_au_key_attributes = [39, 10, 34, 19, 11]
    central_midfielder_au_pref_attributes = [13, 48, 43, 42, 22, 7, 6, 9]
    calculate_role_score(squad_attributes_df, central_midfielder_au_key_attributes,
                         central_midfielder_au_pref_attributes,
                         role_list[50])

    mezzala_su_key_attributes = [5, 39, 22, 6, 19, 9]
    mezzala_su_pref_attributes = [47, 13, 48, 43, 7, 37, 34, 26, 11]
    calculate_role_score(squad_attributes_df, mezzala_su_key_attributes, mezzala_su_pref_attributes,
                         role_list[51])

    mezzala_at_key_attributes = [5, 39, 22, 7, 6, 37, 19, 9]
    mezzala_at_pref_attributes = [47, 13, 48, 43, 33, 35, 34, 26]
    calculate_role_score(squad_attributes_df, mezzala_at_key_attributes, mezzala_at_pref_attributes,
                         role_list[52])

    advanced_playmaker_su_key_attributes = [43, 39, 22, 10, 7, 34, 19, 9]
    advanced_playmaker_su_pref_attributes = [49, 48, 42, 33, 37]
    calculate_role_score(squad_attributes_df, advanced_playmaker_su_key_attributes,
                         advanced_playmaker_su_pref_attributes,
                         role_list[53])

    advanced_playmaker_at_key_attributes = [43, 39, 22, 10, 7, 34, 19, 9]
    advanced_playmaker_at_pref_attributes = [5, 49, 48, 42, 33, 37]
    calculate_role_score(squad_attributes_df, advanced_playmaker_at_key_attributes,
                         advanced_playmaker_at_pref_attributes,
                         role_list[54])

    # Winger role scores --------------------------------------
    defensive_winger_de_key_attributes = [13, 48, 22, 17, 10, 6, 9]
    defensive_winger_de_pref_attributes = [5, 50, 42, 39, 40, 37, 34, 24, 11]
    calculate_role_score(squad_attributes_df, defensive_winger_de_key_attributes,
                         defensive_winger_de_pref_attributes,
                         role_list[55])

    defensive_winger_su_key_attributes = [13, 22, 10, 6, 40, 9]
    defensive_winger_su_pref_attributes = [5, 50, 48, 43, 42, 39, 17, 37, 34, 24, 19, 11]
    calculate_role_score(squad_attributes_df, defensive_winger_su_key_attributes,
                         defensive_winger_su_pref_attributes,
                         role_list[56])

    wide_midfielder_de_key_attributes = [42, 39, 17, 10, 6, 19, 11]
    wide_midfielder_de_pref_attributes = [13, 48, 43, 40, 34, 24, 9]
    calculate_role_score(squad_attributes_df, wide_midfielder_de_key_attributes, wide_midfielder_de_pref_attributes,
                         role_list[57])

    wide_midfielder_su_key_attributes = [13, 39, 10, 6, 19, 11]
    wide_midfielder_su_pref_attributes = [48, 43, 42, 22, 17, 7, 40, 34, 9]
    calculate_role_score(squad_attributes_df, wide_midfielder_su_key_attributes, wide_midfielder_su_pref_attributes,
                         role_list[58])

    wide_midfielder_at_key_attributes = [13, 39, 10, 6, 40, 34, 19]
    wide_midfielder_at_pref_attributes = [48, 43, 22, 7, 11, 9]
    calculate_role_score(squad_attributes_df, wide_midfielder_at_key_attributes, wide_midfielder_at_pref_attributes,
                         role_list[59])

    wide_midfielder_au_key_attributes = [13, 39, 10, 6, 19, 11]
    wide_midfielder_au_pref_attributes = [48, 43, 42, 22, 17, 7, 40, 34, 9]
    calculate_role_score(squad_attributes_df, wide_midfielder_au_key_attributes, wide_midfielder_au_pref_attributes,
                         role_list[60])

    wide_playmaker_su_key_attributes = [43, 39, 10, 7, 34, 19, 9]
    wide_playmaker_su_pref_attributes = [49, 22, 37]
    calculate_role_score(squad_attributes_df, wide_playmaker_su_key_attributes, wide_playmaker_su_pref_attributes,
                         role_list[61])

    wide_playmaker_at_key_attributes = [43, 39, 10, 7, 37, 34, 19, 9]
    wide_playmaker_at_pref_attributes = [5, 49, 48, 33]
    calculate_role_score(squad_attributes_df, wide_playmaker_at_key_attributes, wide_playmaker_at_pref_attributes,
                         role_list[62])

    inverted_winger_su_key_attributes = [5, 49, 40, 37, 19, 9]
    inverted_winger_su_pref_attributes = [47, 20, 13, 43, 39, 22, 7, 6, 34, 26]
    calculate_role_score(squad_attributes_df, inverted_winger_su_key_attributes, inverted_winger_su_pref_attributes,
                         role_list[63])

    inverted_winger_at_key_attributes = [5, 49, 40, 37, 19, 9]
    inverted_winger_at_pref_attributes = [47, 20, 13, 48, 43, 39, 33, 22, 7, 6, 34, 26]
    calculate_role_score(squad_attributes_df, inverted_winger_at_key_attributes, inverted_winger_at_pref_attributes,
                         role_list[64])

    winger_su_key_attributes = [5, 49, 40, 37, 9]
    winger_su_pref_attributes = [47, 20, 13, 22, 6, 34, 19]
    calculate_role_score(squad_attributes_df, winger_su_key_attributes, winger_su_pref_attributes,
                         role_list[65])

    winger_at_key_attributes = [5, 49, 40, 37, 9]
    winger_at_pref_attributes = [47, 20, 13, 48, 33, 22, 6, 34, 19]
    calculate_role_score(squad_attributes_df, winger_at_key_attributes, winger_at_pref_attributes,
                         role_list[66])

    inside_forward_su_key_attributes = [5, 49, 22, 37, 35, 34, 9]
    inside_forward_su_pref_attributes = [47, 20, 13, 48, 43, 33, 7, 6, 26, 19]
    calculate_role_score(squad_attributes_df, inside_forward_su_key_attributes, inside_forward_su_pref_attributes,
                         role_list[67])

    inside_forward_at_key_attributes = [5, 49, 48, 22, 37, 35, 34, 9]
    inside_forward_at_pref_attributes = [47, 20, 13, 43, 33, 6, 26, 19]
    calculate_role_score(squad_attributes_df, inside_forward_at_key_attributes, inside_forward_at_pref_attributes,
                         role_list[68])

    raumdeuter_key_attributes = [47, 48, 43, 42, 39, 22, 35]
    raumdeuter_pref_attributes = [5, 13, 6, 34, 9]
    calculate_role_score(squad_attributes_df, raumdeuter_key_attributes, raumdeuter_pref_attributes,
                         role_list[69])

    wide_target_forward_su_key_attributes = [29, 12, 46, 10, 30]
    wide_target_forward_su_pref_attributes = [47, 13, 48, 22, 6, 40, 34]
    calculate_role_score(squad_attributes_df, wide_target_forward_su_key_attributes,
                         wide_target_forward_su_pref_attributes,
                         role_list[70])

    wide_target_forward_at_key_attributes = [29, 12, 46, 22, 30]
    wide_target_forward_at_pref_attributes = [47, 13, 48, 10, 6, 40, 35, 34]
    calculate_role_score(squad_attributes_df, wide_target_forward_at_key_attributes,
                         wide_target_forward_at_pref_attributes,
                         role_list[71])

    # Attacking Midfielder role scores
    trequartista_key_attributes = [5, 43, 39, 33, 22, 7, 37, 34, 19, 9]
    trequartista_pref_attributes = [49, 47, 48, 35]
    calculate_role_score(squad_attributes_df, trequartista_key_attributes, trequartista_pref_attributes,
                         role_list[72])

    enganche_key_attributes = [43, 39, 7, 34, 19, 9]
    enganche_pref_attributes = [49, 48, 33, 22, 10, 37]
    calculate_role_score(squad_attributes_df, enganche_key_attributes, enganche_pref_attributes,
                         role_list[73])

    attacking_midfielder_su_key_attributes = [48, 39, 33, 22, 34, 26, 19, 9]
    attacking_midfielder_su_pref_attributes = [49, 43, 7, 37]
    calculate_role_score(squad_attributes_df, attacking_midfielder_su_key_attributes,
                         attacking_midfielder_su_pref_attributes,
                         role_list[74])

    attacking_midfielder_at_key_attributes = [48, 39, 33, 22, 34, 26, 19, 9, 37]
    attacking_midfielder_at_pref_attributes = [49, 43, 7, 35]
    calculate_role_score(squad_attributes_df, attacking_midfielder_at_key_attributes,
                         attacking_midfielder_at_pref_attributes,
                         role_list[75])

    shadow_striker_key_attributes = [5, 48, 43, 22, 37, 35, 34]
    shadow_striker_pref_attributes = [49, 47, 20, 13, 42, 39, 6, 19, 9]
    calculate_role_score(squad_attributes_df, shadow_striker_key_attributes, shadow_striker_pref_attributes,
                         role_list[76])

    # Striker role scores
    advanced_forward_key_attributes = [5, 43, 22, 37, 35, 34, 9]
    advanced_forward_pref_attributes = [49, 47, 20, 13, 48, 39, 6, 19]
    calculate_role_score(squad_attributes_df, advanced_forward_key_attributes, advanced_forward_pref_attributes,
                         role_list[77])

    poacher_key_attributes = [48, 43, 22, 35]
    poacher_pref_attributes = [5, 39, 34, 30, 9]
    calculate_role_score(squad_attributes_df, poacher_key_attributes, poacher_pref_attributes,
                         role_list[78])

    false_nine_key_attributes = [5, 49, 43, 39, 22, 7, 37, 34, 19, 9]
    false_nine_pref_attributes = [47, 48, 33, 10, 35]
    calculate_role_score(squad_attributes_df, false_nine_key_attributes, false_nine_pref_attributes,
                         role_list[79])

    target_forward_su_key_attributes = [47, 29, 12, 46, 10, 30]
    target_forward_su_pref_attributes = [50, 48, 43, 39, 22, 35, 34]
    calculate_role_score(squad_attributes_df, target_forward_su_key_attributes, target_forward_su_pref_attributes,
                         role_list[80])

    target_forward_at_key_attributes = [47, 29, 12, 46, 43, 22, 35, 30]
    target_forward_at_pref_attributes = [50, 48, 39, 10, 34]
    calculate_role_score(squad_attributes_df, target_forward_at_key_attributes, target_forward_at_pref_attributes,
                         role_list[81])

    deep_lying_forward_su_key_attributes = [43, 39, 22, 10, 34, 19, 9]
    deep_lying_forward_su_pref_attributes = [47, 12, 48, 33, 7, 35]
    calculate_role_score(squad_attributes_df, deep_lying_forward_su_key_attributes,
                         deep_lying_forward_su_pref_attributes,
                         role_list[82])

    deep_lying_forward_at_key_attributes = [43, 39, 22, 10, 34, 19, 9]
    deep_lying_forward_at_pref_attributes = [47, 12, 48, 33, 7, 37, 35]
    calculate_role_score(squad_attributes_df, deep_lying_forward_at_key_attributes,
                         deep_lying_forward_at_pref_attributes,
                         role_list[83])

    pressing_forward_de_key_attributes = [5, 20, 13, 50, 48, 46, 39, 10, 6]
    pressing_forward_de_pref_attributes = [49, 47, 12, 43, 42, 34]
    calculate_role_score(squad_attributes_df, pressing_forward_de_key_attributes,
                         pressing_forward_de_pref_attributes,
                         role_list[84])

    pressing_forward_su_key_attributes = [5, 20, 13, 50, 48, 46, 39, 10, 6]
    pressing_forward_su_pref_attributes = [49, 47, 12, 43, 42, 22, 34, 19]
    calculate_role_score(squad_attributes_df, pressing_forward_su_key_attributes,
                         pressing_forward_su_pref_attributes,
                         role_list[85])

    pressing_forward_at_key_attributes = [5, 20, 13, 50, 48, 46, 22, 10, 6]
    pressing_forward_at_pref_attributes = [49, 47, 12, 43, 42, 39, 35, 34]
    calculate_role_score(squad_attributes_df, pressing_forward_at_key_attributes,
                         pressing_forward_at_pref_attributes,
                         role_list[86])

    complete_forward_su_key_attributes = [5, 49, 12, 48, 43, 39, 22, 7, 37, 34, 30, 26, 19, 9]
    complete_forward_su_pref_attributes = [47, 29, 20, 13, 10, 6, 35]
    calculate_role_score(squad_attributes_df, complete_forward_su_key_attributes,
                         complete_forward_su_pref_attributes,
                         role_list[87])

    complete_forward_at_key_attributes = [5, 49, 12, 48, 43, 22, 37, 35, 34, 30, 9]
    complete_forward_at_pref_attributes = [47, 29, 20, 13, 39, 10, 7, 6, 26, 19]
    calculate_role_score(squad_attributes_df, complete_forward_at_key_attributes,
                         complete_forward_at_pref_attributes,
                         role_list[88])
    print('Complete: squad_attributes_df')

    squad_attributes_df.to_csv('squad_attributes.csv', encoding='utf-8', index=False)

    return squad_attributes_df


# Function to transform user's shortlist_attributes file into the correct format for the app
def build_shortlist_attributes_dataframe(shortlist_attributes_file, language_preference):
    # Create shortlist attributes dataframe
    shortlist_attributes_df = shortlist_attributes_file.copy()
    shortlist_attributes_df = shortlist_attributes_df[0]

    # Remove zero width spaces
    shortlist_attributes_df.columns = shortlist_attributes_df.columns.str.replace('\u200b', '')

    # Remove unnecessary columns from Shortlist Attributes
    def drop_columns_by_number(df, column_numbers):
        columns_to_drop = [df.columns[i] for i in column_numbers]
        return df.drop(columns=columns_to_drop)

    # Remove unnecessary columns 'Inf', 'Rec'
    shortlist_attributes_df = drop_columns_by_number(shortlist_attributes_df, [0, 2])
    shortlist_attributes_df.reset_index()

    # Clean Shortlist Attributes dataframe to convert range values to average
    for col_num in range(5, 52):

        column_name = shortlist_attributes_df.columns[col_num]
        shortlist_attributes_df.iloc[:, col_num] = shortlist_attributes_df.iloc[:, col_num].astype(str)

        def process_range_column(df, column_number):
            """Processes a column containing range strings."""
            range_mask = df.iloc[:, column_number].str.contains('-', na=False, regex=False)

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

                df.loc[range_mask, column_name] = df.loc[range_mask, column_name].apply(average_range)
            return df
        shortlist_attributes_df = process_range_column(shortlist_attributes_df, col_num)
        shortlist_attributes_df.iloc[:, col_num] = pd.to_numeric(shortlist_attributes_df.iloc[:, col_num]).round()

    # Function to remove the nationality part of the name (split at the last hyphen)
    def remove_nationality(name):
        if '-' in name:  # Check if there is a hyphen in the name
            return name.rsplit('-', 1)[0]  # Split from the right and take the first part (player name)
        else:
            return name  # If no hyphen, return the name as is

    # Apply the function to the 'Name' column
    shortlist_attributes_df.iloc[:, 0] = shortlist_attributes_df.iloc[:, 0].apply(remove_nationality)

    # Create new columns for 'Overall' and 'GK Overall' radar chart
    def mean_floor_if_no_nan(row, column_list):
        '''Checks if the row has any NaN values in the defined column list. Returns NaN if any of the values are NaN, else returns the average'''
        if row.iloc[column_list].isnull().any():
            return np.nan
        else:
            return np.floor(row.iloc[column_list].mean())

    # Pull the overall radar column names in the user's language
    overall_radar_columns = overall_radar_columns_dict[language_preference]

    def create_overall_radar_column_nan_check(df, new_column_name_base, column_indices):
        """
        Creates a new column in the DataFrame by applying a function that handles NaN values.
        If a column with the same base name already exists, it appends '(Overall)' to the new column name.

        Args:
            df (pd.DataFrame): The input DataFrame.
            new_column_name_base (str): The base name for the new column.
            column_indices (list): A list of integer indices of the columns to process.

        Returns:
            pd.DataFrame: The DataFrame with the new column added.
        """
        new_column_name = new_column_name_base
        if new_column_name in df.columns:
            new_column_name += ' (Overall)'

        df[new_column_name] = df.apply(
            lambda row: mean_floor_if_no_nan(row, column_indices), axis=1).round(0)
        return df

    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[0],
                                                                    [5, 20])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[1],
                                                                    [19, 33, 7])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[2],
                                                                    [35, 43, 22])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[3],
                                                                    [37, 34, 9])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[4],
                                                                    [31, 30])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[5],
                                                                    [47, 45, 41, 38, 37, 9])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[6],
                                                                    [24, 11, 17])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[7],
                                                                    [49, 47, 13, 12])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[8],
                                                                    [51, 31])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[9],
                                                                    [21, 15])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[10],
                                                                    [28, 8])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[11],
                                                                    [45, 44])
    shortlist_attributes_df = create_overall_radar_column_nan_check(shortlist_attributes_df, overall_radar_columns[12],
                                                                    [36])


    # # Calculate the average of the columns for each category on the 'Overall' charts
    # shortlist_attributes_df[overall_radar_columns[0]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [5, 20]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[1]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [19, 33, 7]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[2]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [35, 43, 22]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[3]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [37, 34, 9]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[4]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [31, 30]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[5]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [47, 45, 41, 38, 37, 9]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[6]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [24, 11, 17]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[7]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [49, 47, 13, 12]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[8]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [51, 31]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[9]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [21, 15]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[10]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [28, 8]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[11]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [45, 44]), axis=1).round(0)
    # shortlist_attributes_df[overall_radar_columns[12]] = shortlist_attributes_df.apply(
    #     lambda row: mean_floor_if_no_nan(row, [36]), axis=1).round(0)

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

    # Loop over each position tag and its corresponding filter in the user's language
    # Scouting Attributes df
    for position_tag, position_filter in international_position_filters[language_preference].items():
        # Create a new column in the dataframe for the position tag
        shortlist_attributes_df[position_tag] = shortlist_attributes_df.iloc[:, 1].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )

    # Function to create role score columns
    def calculate_role_score(df, key_attributes, pref_attributes, column_title):
        key_attributes_total = df.iloc[:, key_attributes].sum(axis=1)
        pref_attributes_total = df.iloc[:, pref_attributes].sum(axis=1)
        role_total = (3 * key_attributes_total) + (2 * pref_attributes_total)
        role_max = (3 * (20 * len(key_attributes))) + (2 * (20 * len(pref_attributes)))
        role_score = (role_total / role_max) * 100
        df[column_title] = role_score.round(0).astype(int)
        return df

    # Pull role name list in the user's language
    role_list = international_role_name_dict[language_preference]

    # Goalkeeper role scores --------------------------------
    gk_key_attributes = [49, 42, 17, 51, 45, 44, 31, 28, 15]
    gk_pref_attributes = [48, 39, 21, 8]
    calculate_role_score(shortlist_attributes_df, gk_key_attributes, gk_pref_attributes,
                         role_list[0])

    sweeper_keeper_de_key_attributes = [49, 48, 42, 17, 45, 28, 21, 15]
    sweeper_keeper_de_pref_attributes = [5, 43, 39, 7, 51, 44, 34, 31, 19, 14, 8]
    calculate_role_score(shortlist_attributes_df, sweeper_keeper_de_key_attributes, sweeper_keeper_de_pref_attributes,
                         role_list[1])

    sweeper_keeper_su_key_attributes = [49, 48, 43, 42, 17, 45, 28, 21, 15, 14]
    sweeper_keeper_su_pref_attributes = [5, 39, 7, 51, 44, 34, 31, 19, 8]
    calculate_role_score(shortlist_attributes_df, sweeper_keeper_su_key_attributes, sweeper_keeper_su_pref_attributes,
                         role_list[2])

    sweeper_keeper_at_key_attributes = [49, 48, 43, 42, 17, 45, 28, 21, 15, 14]
    sweeper_keeper_at_pref_attributes = [5, 39, 7, 51, 44, 36, 34, 31, 19, 8]
    calculate_role_score(shortlist_attributes_df, sweeper_keeper_at_key_attributes, sweeper_keeper_at_pref_attributes,
                         role_list[3])

    # Central Defender Role Scores ----------------------------------------
    central_def_de_key_attributes = [29, 12, 17, 30, 24, 11]
    central_def_de_pref_attributes = [20, 50, 48, 46, 43, 42, 39]
    calculate_role_score(shortlist_attributes_df, central_def_de_key_attributes, central_def_de_pref_attributes,
                         role_list[4])

    central_def_st_key_attributes = [29, 12, 50, 46, 17, 39, 30, 11]
    central_def_st_pref_attributes = [24, 48, 43, 42]
    calculate_role_score(shortlist_attributes_df, central_def_st_key_attributes, central_def_st_pref_attributes,
                         role_list[5])

    central_def_co_key_attributes = [20, 48, 42, 39, 17, 24, 11]
    central_def_co_pref_attributes = [29, 12, 46, 43, 30]
    calculate_role_score(shortlist_attributes_df, central_def_co_key_attributes, central_def_co_pref_attributes,
                         role_list[6])

    no_nonsense_cb_de_key_attributes = [29, 12, 17, 30, 24, 11]
    no_nonsense_cb_de_pref_attributes = [20, 50, 48, 46, 42]
    calculate_role_score(shortlist_attributes_df, no_nonsense_cb_de_key_attributes, no_nonsense_cb_de_pref_attributes,
                         role_list[7])

    no_nonsense_cb_st_key_attributes = [29, 12, 50, 46, 17, 30, 11]
    no_nonsense_cb_st_pref_attributes = [24, 48, 42]
    calculate_role_score(shortlist_attributes_df, no_nonsense_cb_st_key_attributes, no_nonsense_cb_st_pref_attributes,
                         role_list[8])

    no_nonsense_cb_co_key_attributes = [20, 48, 42, 39, 17, 24, 11]
    no_nonsense_cb_co_pref_attributes = [29, 12, 46, 30]
    calculate_role_score(shortlist_attributes_df, no_nonsense_cb_co_key_attributes, no_nonsense_cb_co_pref_attributes,
                         role_list[9])

    wide_cb_de_key_attributes = [29, 12, 17, 30, 24, 11]
    wide_cb_de_pref_attributes = [49, 20, 50, 48, 46, 43, 42, 6, 37, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, wide_cb_de_key_attributes, wide_cb_de_pref_attributes,
                         role_list[10])

    wide_cb_su_key_attributes = [29, 20, 12, 17, 37, 30, 24, 11]
    wide_cb_su_pref_attributes = [49, 13, 50, 48, 46, 43, 42, 39, 22, 6, 40, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, wide_cb_su_key_attributes, wide_cb_su_pref_attributes,
                         role_list[11])

    wide_cb_at_key_attributes = [29, 20, 13, 12, 22, 40, 37, 30, 24, 11]
    wide_cb_at_pref_attributes = [49, 50, 48, 46, 43, 42, 39, 17, 6, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, wide_cb_at_key_attributes, wide_cb_at_pref_attributes,
                         role_list[12])

    ball_playing_def_de_key_attributes = [29, 12, 43, 17, 30, 24, 19, 11]
    ball_playing_def_de_pref_attributes = [20, 50, 48, 46, 42, 39, 7, 34, 9]
    calculate_role_score(shortlist_attributes_df, ball_playing_def_de_key_attributes,
                         ball_playing_def_de_pref_attributes,
                         role_list[13])

    ball_playing_def_st_key_attributes = [29, 12, 50, 46, 43, 39, 17, 30, 19, 11]
    ball_playing_def_st_pref_attributes = [48, 42, 7, 34, 24, 9]
    calculate_role_score(shortlist_attributes_df, ball_playing_def_st_key_attributes,
                         ball_playing_def_st_pref_attributes,
                         role_list[14])

    ball_playing_def_co_key_attributes = [20, 48, 43, 42, 39, 17, 24, 19, 11]
    ball_playing_def_co_pref_attributes = [29, 12, 46, 7, 34, 30, 9]
    calculate_role_score(shortlist_attributes_df, ball_playing_def_co_key_attributes,
                         ball_playing_def_co_pref_attributes,
                         role_list[15])

    libero_de_key_attributes = [29, 12, 43, 39, 17, 10, 34, 30, 24, 19, 11, 9]
    libero_de_pref_attributes = [20, 13, 48, 46, 42]
    calculate_role_score(shortlist_attributes_df, libero_de_key_attributes, libero_de_pref_attributes,
                         role_list[16])

    libero_su_key_attributes = [29, 12, 43, 39, 17, 10, 34, 30, 24, 19, 11, 9]
    libero_su_pref_attributes = [20, 13, 48, 46, 42, 7, 37]
    calculate_role_score(shortlist_attributes_df, libero_su_key_attributes, libero_su_pref_attributes,
                         role_list[17])

    # Fullback/Wingback role scores ------------------------------------------
    fullback_de_key_attributes = [48, 42, 17, 24, 11]
    fullback_de_pref_attributes = [20, 13, 39, 10, 6, 40, 19]
    calculate_role_score(shortlist_attributes_df, fullback_de_key_attributes, fullback_de_pref_attributes,
                         role_list[18])

    fullback_su_key_attributes = [48, 42, 17, 24, 11]
    fullback_su_pref_attributes = [20, 13, 39, 10, 6, 40, 37, 19, 9]
    calculate_role_score(shortlist_attributes_df, fullback_su_key_attributes, fullback_su_pref_attributes,
                         role_list[19])

    fullback_at_key_attributes = [48, 17, 10, 40, 24, 11]
    fullback_at_pref_attributes = [49, 20, 13, 42, 39, 22, 6, 37, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, fullback_at_key_attributes, fullback_at_pref_attributes,
                         role_list[20])

    fullback_au_key_attributes = [48, 42, 17, 10, 24, 11]
    fullback_au_pref_attributes = [49, 20, 13, 39, 6, 40, 37, 19, 9]
    calculate_role_score(shortlist_attributes_df, fullback_au_key_attributes, fullback_au_pref_attributes,
                         role_list[21])

    no_nonsense_fb_key_attributes = [12, 48, 17, 24, 11]
    no_nonsense_fb_pref_attributes = [50, 46, 42, 10, 30]
    calculate_role_score(shortlist_attributes_df, no_nonsense_fb_key_attributes, no_nonsense_fb_pref_attributes,
                         role_list[22])

    inverted_fb_key_attributes = [12, 17, 30, 24, 11]
    inverted_fb_pref_attributes = [49, 29, 20, 50, 48, 46, 43, 42, 39, 6, 37, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, inverted_fb_key_attributes, inverted_fb_pref_attributes,
                         role_list[23])

    wingback_de_key_attributes = [5, 13, 48, 17, 10, 6, 24, 11]
    wingback_de_pref_attributes = [49, 47, 20, 42, 39, 22, 40, 37, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, wingback_de_key_attributes, wingback_de_pref_attributes,
                         role_list[24])

    wingback_su_key_attributes = [5, 13, 22, 10, 6, 40, 37, 24, 11]
    wingback_su_pref_attributes = [49, 47, 20, 48, 42, 39, 17, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, wingback_su_key_attributes, wingback_su_pref_attributes,
                         role_list[25])

    wingback_at_key_attributes = [5, 20, 13, 22, 10, 6, 40, 37, 11, 9]
    wingback_at_pref_attributes = [49, 47, 48, 42, 39, 33, 17, 34, 24, 19]
    calculate_role_score(shortlist_attributes_df, wingback_at_key_attributes, wingback_at_pref_attributes,
                         role_list[26])

    wingback_au_key_attributes = [5, 13, 22, 10, 6, 40, 37, 24, 11]
    wingback_au_pref_attributes = [49, 47, 20, 48, 42, 39, 17, 34, 19, 9]
    calculate_role_score(shortlist_attributes_df, wingback_au_key_attributes, wingback_au_pref_attributes,
                         role_list[27])

    complete_wingback_su_key_attributes = [5, 13, 22, 10, 6, 40, 37, 9]
    complete_wingback_su_pref_attributes = [49, 47, 20, 48, 39, 33, 17, 34, 24, 19, 11]
    calculate_role_score(shortlist_attributes_df, complete_wingback_su_key_attributes,
                         complete_wingback_su_pref_attributes,
                         role_list[28])

    complete_wingback_at_key_attributes = [5, 13, 33, 22, 10, 6, 40, 37, 9]
    complete_wingback_at_pref_attributes = [49, 47, 20, 48, 39, 17, 34, 24, 19, 11]
    calculate_role_score(shortlist_attributes_df, complete_wingback_at_key_attributes,
                         complete_wingback_at_pref_attributes,
                         role_list[29])

    inverted_wb_de_key_attributes = [48, 39, 17, 10, 19, 11]
    inverted_wb_de_pref_attributes = [5, 49, 13, 43, 42, 22, 6, 34, 24, 9]
    calculate_role_score(shortlist_attributes_df, inverted_wb_de_key_attributes, inverted_wb_de_pref_attributes,
                         role_list[30])

    inverted_wb_su_key_attributes = [43, 39, 10, 34, 19, 11]
    inverted_wb_su_pref_attributes = [5, 49, 13, 48, 42, 22, 17, 7, 6, 24, 9]
    calculate_role_score(shortlist_attributes_df, inverted_wb_su_key_attributes, inverted_wb_su_pref_attributes,
                         role_list[31])

    inverted_wb_at_key_attributes = [5, 43, 39, 22, 10, 7, 34, 19, 11, 9]
    inverted_wb_at_pref_attributes = [49, 20, 13, 48, 42, 33, 17, 6, 40, 37, 26, 24]
    calculate_role_score(shortlist_attributes_df, inverted_wb_at_key_attributes, inverted_wb_at_pref_attributes,
                         role_list[32])

    # Defensive Midfielder role scores -------------------------------------------
    anchor_key_attributes = [48, 42, 39, 17, 24, 11]
    anchor_pref_attributes = [12, 43, 10]
    calculate_role_score(shortlist_attributes_df, anchor_key_attributes, anchor_pref_attributes,
                         role_list[33])

    half_back_key_attributes = [48, 43, 42, 39, 17, 10, 24, 11]
    half_back_pref_attributes = [29, 13, 12, 50, 46, 6, 34, 19]
    calculate_role_score(shortlist_attributes_df, half_back_key_attributes, half_back_pref_attributes,
                         role_list[34])

    defensive_midfielder_de_key_attributes = [48, 42, 17, 10, 11]
    defensive_midfielder_de_pref_attributes = [13, 12, 50, 43, 39, 6, 24, 19]
    calculate_role_score(shortlist_attributes_df, defensive_midfielder_de_key_attributes,
                         defensive_midfielder_de_pref_attributes,
                         role_list[35])

    defensive_midfielder_su_key_attributes = [48, 42, 17, 10, 11]
    defensive_midfielder_su_pref_attributes = [13, 12, 50, 43, 39, 6, 34, 24, 19]
    calculate_role_score(shortlist_attributes_df, defensive_midfielder_su_key_attributes,
                         defensive_midfielder_su_pref_attributes,
                         role_list[36])

    segundo_volante_su_key_attributes = [20, 13, 22, 17, 6, 24, 19, 11]
    segundo_volante_su_pref_attributes = [5, 47, 12, 48, 43, 42, 39, 35, 34, 26]
    calculate_role_score(shortlist_attributes_df, segundo_volante_su_key_attributes, segundo_volante_su_pref_attributes,
                         role_list[37])

    segundo_volante_at_key_attributes = [20, 13, 48, 22, 17, 6, 35, 26, 19, 11]
    segundo_volante_at_pref_attributes = [5, 47, 12, 43, 42, 39, 34, 24]
    calculate_role_score(shortlist_attributes_df, segundo_volante_at_key_attributes, segundo_volante_at_pref_attributes,
                         role_list[38])

    regista_key_attributes = [43, 39, 33, 22, 10, 7, 34, 19, 9]
    regista_pref_attributes = [47, 48, 37, 26]
    calculate_role_score(shortlist_attributes_df, regista_key_attributes, regista_pref_attributes,
                         role_list[39])

    ball_winning_midfielder_de_key_attributes = [13, 50, 48, 10, 6, 11]
    ball_winning_midfielder_de_pref_attributes = [49, 20, 12, 46, 42, 17, 24]
    calculate_role_score(shortlist_attributes_df, ball_winning_midfielder_de_key_attributes,
                         ball_winning_midfielder_de_pref_attributes,
                         role_list[40])

    ball_winning_midfielder_su_key_attributes = [13, 50, 48, 10, 6, 11]
    ball_winning_midfielder_su_pref_attributes = [49, 20, 12, 46, 42, 24, 19]
    calculate_role_score(shortlist_attributes_df, ball_winning_midfielder_su_key_attributes,
                         ball_winning_midfielder_su_pref_attributes,
                         role_list[41])

    deep_lying_playmaker_de_key_attributes = [43, 39, 10, 7, 34, 19, 9]
    deep_lying_playmaker_de_pref_attributes = [47, 48, 17, 11]
    calculate_role_score(shortlist_attributes_df, deep_lying_playmaker_de_key_attributes,
                         deep_lying_playmaker_de_pref_attributes,
                         role_list[42])

    deep_lying_playmaker_su_key_attributes = [43, 39, 10, 7, 34, 19, 9]
    deep_lying_playmaker_su_pref_attributes = [47, 48, 22, 17]
    calculate_role_score(shortlist_attributes_df, deep_lying_playmaker_su_key_attributes,
                         deep_lying_playmaker_su_pref_attributes,
                         role_list[43])

    roaming_playmaker_key_attributes = [5, 13, 48, 43, 39, 22, 10, 7, 6, 34, 19, 9]
    roaming_playmaker_pref_attributes = [49, 47, 20, 42, 17, 37, 26]
    calculate_role_score(shortlist_attributes_df, roaming_playmaker_key_attributes, roaming_playmaker_pref_attributes,
                         role_list[44])

    # Central Midfielder role scores --------------------------------------------
    carrilero_key_attributes = [13, 39, 17, 10, 34, 19, 11]
    carrilero_pref_attributes = [48, 43, 42, 22, 7, 6, 9]
    calculate_role_score(shortlist_attributes_df, carrilero_key_attributes, carrilero_pref_attributes,
                         role_list[45])

    box_to_box_midfielder_key_attributes = [13, 22, 10, 6, 19, 11]
    box_to_box_midfielder_pref_attributes = [5, 47, 20, 12, 50, 48, 43, 39, 17, 37, 35, 34, 26, 9]
    calculate_role_score(shortlist_attributes_df, box_to_box_midfielder_key_attributes,
                         box_to_box_midfielder_pref_attributes,
                         role_list[46])

    central_midfielder_de_key_attributes = [42, 39, 17, 10, 11]
    central_midfielder_de_pref_attributes = [13, 50, 48, 43, 6, 34, 24, 19, 9]
    calculate_role_score(shortlist_attributes_df, central_midfielder_de_key_attributes,
                         central_midfielder_de_pref_attributes,
                         role_list[47])

    central_midfielder_su_key_attributes = [39, 10, 34, 19, 11]
    central_midfielder_su_pref_attributes = [13, 48, 43, 42, 22, 7, 6, 9]
    calculate_role_score(shortlist_attributes_df, central_midfielder_su_key_attributes,
                         central_midfielder_su_pref_attributes,
                         role_list[48])

    central_midfielder_at_key_attributes = [39, 22, 34, 19]
    central_midfielder_at_pref_attributes = [5, 13, 48, 43, 10, 7, 6, 26, 11, 9]
    calculate_role_score(shortlist_attributes_df, central_midfielder_at_key_attributes,
                         central_midfielder_at_pref_attributes,
                         role_list[49])

    central_midfielder_au_key_attributes = [39, 10, 34, 19, 11]
    central_midfielder_au_pref_attributes = [13, 48, 43, 42, 22, 7, 6, 9]
    calculate_role_score(shortlist_attributes_df, central_midfielder_au_key_attributes,
                         central_midfielder_au_pref_attributes,
                         role_list[50])

    mezzala_su_key_attributes = [5, 39, 22, 6, 19, 9]
    mezzala_su_pref_attributes = [47, 13, 48, 43, 7, 37, 34, 26, 11]
    calculate_role_score(shortlist_attributes_df, mezzala_su_key_attributes, mezzala_su_pref_attributes,
                         role_list[51])

    mezzala_at_key_attributes = [5, 39, 22, 7, 6, 37, 19, 9]
    mezzala_at_pref_attributes = [47, 13, 48, 43, 33, 35, 34, 26]
    calculate_role_score(shortlist_attributes_df, mezzala_at_key_attributes, mezzala_at_pref_attributes,
                         role_list[52])

    advanced_playmaker_su_key_attributes = [43, 39, 22, 10, 7, 34, 19, 9]
    advanced_playmaker_su_pref_attributes = [49, 48, 42, 33, 37]
    calculate_role_score(shortlist_attributes_df, advanced_playmaker_su_key_attributes,
                         advanced_playmaker_su_pref_attributes,
                         role_list[53])

    advanced_playmaker_at_key_attributes = [43, 39, 22, 10, 7, 34, 19, 9]
    advanced_playmaker_at_pref_attributes = [5, 49, 48, 42, 33, 37]
    calculate_role_score(shortlist_attributes_df, advanced_playmaker_at_key_attributes,
                         advanced_playmaker_at_pref_attributes,
                         role_list[54])

    # Winger role scores --------------------------------------
    defensive_winger_de_key_attributes = [13, 48, 22, 17, 10, 6, 9]
    defensive_winger_de_pref_attributes = [5, 50, 42, 39, 40, 37, 34, 24, 11]
    calculate_role_score(shortlist_attributes_df, defensive_winger_de_key_attributes,
                         defensive_winger_de_pref_attributes,
                         role_list[55])

    defensive_winger_su_key_attributes = [13, 22, 10, 6, 40, 9]
    defensive_winger_su_pref_attributes = [5, 50, 48, 43, 42, 39, 17, 37, 34, 24, 19, 11]
    calculate_role_score(shortlist_attributes_df, defensive_winger_su_key_attributes,
                         defensive_winger_su_pref_attributes,
                         role_list[56])

    wide_midfielder_de_key_attributes = [42, 39, 17, 10, 6, 19, 11]
    wide_midfielder_de_pref_attributes = [13, 48, 43, 40, 34, 24, 9]
    calculate_role_score(shortlist_attributes_df, wide_midfielder_de_key_attributes, wide_midfielder_de_pref_attributes,
                         role_list[57])

    wide_midfielder_su_key_attributes = [13, 39, 10, 6, 19, 11]
    wide_midfielder_su_pref_attributes = [48, 43, 42, 22, 17, 7, 40, 34, 9]
    calculate_role_score(shortlist_attributes_df, wide_midfielder_su_key_attributes, wide_midfielder_su_pref_attributes,
                         role_list[58])

    wide_midfielder_at_key_attributes = [13, 39, 10, 6, 40, 34, 19]
    wide_midfielder_at_pref_attributes = [48, 43, 22, 7, 11, 9]
    calculate_role_score(shortlist_attributes_df, wide_midfielder_at_key_attributes, wide_midfielder_at_pref_attributes,
                         role_list[59])

    wide_midfielder_au_key_attributes = [13, 39, 10, 6, 19, 11]
    wide_midfielder_au_pref_attributes = [48, 43, 42, 22, 17, 7, 40, 34, 9]
    calculate_role_score(shortlist_attributes_df, wide_midfielder_au_key_attributes, wide_midfielder_au_pref_attributes,
                         role_list[60])

    wide_playmaker_su_key_attributes = [43, 39, 10, 7, 34, 19, 9]
    wide_playmaker_su_pref_attributes = [49, 22, 37]
    calculate_role_score(shortlist_attributes_df, wide_playmaker_su_key_attributes, wide_playmaker_su_pref_attributes,
                         role_list[61])

    wide_playmaker_at_key_attributes = [43, 39, 10, 7, 37, 34, 19, 9]
    wide_playmaker_at_pref_attributes = [5, 49, 48, 33]
    calculate_role_score(shortlist_attributes_df, wide_playmaker_at_key_attributes, wide_playmaker_at_pref_attributes,
                         role_list[62])

    inverted_winger_su_key_attributes = [5, 49, 40, 37, 19, 9]
    inverted_winger_su_pref_attributes = [47, 20, 13, 43, 39, 22, 7, 6, 34, 26]
    calculate_role_score(shortlist_attributes_df, inverted_winger_su_key_attributes, inverted_winger_su_pref_attributes,
                         role_list[63])

    inverted_winger_at_key_attributes = [5, 49, 40, 37, 19, 9]
    inverted_winger_at_pref_attributes = [47, 20, 13, 48, 43, 39, 33, 22, 7, 6, 34, 26]
    calculate_role_score(shortlist_attributes_df, inverted_winger_at_key_attributes, inverted_winger_at_pref_attributes,
                         role_list[64])

    winger_su_key_attributes = [5, 49, 40, 37, 9]
    winger_su_pref_attributes = [47, 20, 13, 22, 6, 34, 19]
    calculate_role_score(shortlist_attributes_df, winger_su_key_attributes, winger_su_pref_attributes,
                         role_list[65])

    winger_at_key_attributes = [5, 49, 40, 37, 9]
    winger_at_pref_attributes = [47, 20, 13, 48, 33, 22, 6, 34, 19]
    calculate_role_score(shortlist_attributes_df, winger_at_key_attributes, winger_at_pref_attributes,
                         role_list[66])

    inside_forward_su_key_attributes = [5, 49, 22, 37, 35, 34, 9]
    inside_forward_su_pref_attributes = [47, 20, 13, 48, 43, 33, 7, 6, 26, 19]
    calculate_role_score(shortlist_attributes_df, inside_forward_su_key_attributes, inside_forward_su_pref_attributes,
                         role_list[67])

    inside_forward_at_key_attributes = [5, 49, 48, 22, 37, 35, 34, 9]
    inside_forward_at_pref_attributes = [47, 20, 13, 43, 33, 6, 26, 19]
    calculate_role_score(shortlist_attributes_df, inside_forward_at_key_attributes, inside_forward_at_pref_attributes,
                         role_list[68])

    raumdeuter_key_attributes = [47, 48, 43, 42, 39, 22, 35]
    raumdeuter_pref_attributes = [5, 13, 6, 34, 9]
    calculate_role_score(shortlist_attributes_df, raumdeuter_key_attributes, raumdeuter_pref_attributes,
                         role_list[69])

    wide_target_forward_su_key_attributes = [29, 12, 46, 10, 30]
    wide_target_forward_su_pref_attributes = [47, 13, 48, 22, 6, 40, 34]
    calculate_role_score(shortlist_attributes_df, wide_target_forward_su_key_attributes,
                         wide_target_forward_su_pref_attributes,
                         role_list[70])

    wide_target_forward_at_key_attributes = [29, 12, 46, 22, 30]
    wide_target_forward_at_pref_attributes = [47, 13, 48, 10, 6, 40, 35, 34]
    calculate_role_score(shortlist_attributes_df, wide_target_forward_at_key_attributes,
                         wide_target_forward_at_pref_attributes,
                         role_list[71])

    # Attacking Midfielder role scores
    trequartista_key_attributes = [5, 43, 39, 33, 22, 7, 37, 34, 19, 9]
    trequartista_pref_attributes = [49, 47, 48, 35]
    calculate_role_score(shortlist_attributes_df, trequartista_key_attributes, trequartista_pref_attributes,
                         role_list[72])

    enganche_key_attributes = [43, 39, 7, 34, 19, 9]
    enganche_pref_attributes = [49, 48, 33, 22, 10, 37]
    calculate_role_score(shortlist_attributes_df, enganche_key_attributes, enganche_pref_attributes,
                         role_list[73])

    attacking_midfielder_su_key_attributes = [48, 39, 33, 22, 34, 26, 19, 9]
    attacking_midfielder_su_pref_attributes = [49, 43, 7, 37]
    calculate_role_score(shortlist_attributes_df, attacking_midfielder_su_key_attributes,
                         attacking_midfielder_su_pref_attributes,
                         role_list[74])

    attacking_midfielder_at_key_attributes = [48, 39, 33, 22, 34, 26, 19, 9, 37]
    attacking_midfielder_at_pref_attributes = [49, 43, 7, 35]
    calculate_role_score(shortlist_attributes_df, attacking_midfielder_at_key_attributes,
                         attacking_midfielder_at_pref_attributes,
                         role_list[75])

    shadow_striker_key_attributes = [5, 48, 43, 22, 37, 35, 34]
    shadow_striker_pref_attributes = [49, 47, 20, 13, 42, 39, 6, 19, 9]
    calculate_role_score(shortlist_attributes_df, shadow_striker_key_attributes, shadow_striker_pref_attributes,
                         role_list[76])

    # Striker role scores
    advanced_forward_key_attributes = [5, 43, 22, 37, 35, 34, 9]
    advanced_forward_pref_attributes = [49, 47, 20, 13, 48, 39, 6, 19]
    calculate_role_score(shortlist_attributes_df, advanced_forward_key_attributes, advanced_forward_pref_attributes,
                         role_list[77])

    poacher_key_attributes = [48, 43, 22, 35]
    poacher_pref_attributes = [5, 39, 34, 30, 9]
    calculate_role_score(shortlist_attributes_df, poacher_key_attributes, poacher_pref_attributes,
                         role_list[78])

    false_nine_key_attributes = [5, 49, 43, 39, 22, 7, 37, 34, 19, 9]
    false_nine_pref_attributes = [47, 48, 33, 10, 35]
    calculate_role_score(shortlist_attributes_df, false_nine_key_attributes, false_nine_pref_attributes,
                         role_list[79])

    target_forward_su_key_attributes = [47, 29, 12, 46, 10, 30]
    target_forward_su_pref_attributes = [50, 48, 43, 39, 22, 35, 34]
    calculate_role_score(shortlist_attributes_df, target_forward_su_key_attributes, target_forward_su_pref_attributes,
                         role_list[80])

    target_forward_at_key_attributes = [47, 29, 12, 46, 43, 22, 35, 30]
    target_forward_at_pref_attributes = [50, 48, 39, 10, 34]
    calculate_role_score(shortlist_attributes_df, target_forward_at_key_attributes, target_forward_at_pref_attributes,
                         role_list[81])

    deep_lying_forward_su_key_attributes = [43, 39, 22, 10, 34, 19, 9]
    deep_lying_forward_su_pref_attributes = [47, 12, 48, 33, 7, 35]
    calculate_role_score(shortlist_attributes_df, deep_lying_forward_su_key_attributes,
                         deep_lying_forward_su_pref_attributes,
                         role_list[82])

    deep_lying_forward_at_key_attributes = [43, 39, 22, 10, 34, 19, 9]
    deep_lying_forward_at_pref_attributes = [47, 12, 48, 33, 7, 37, 35]
    calculate_role_score(shortlist_attributes_df, deep_lying_forward_at_key_attributes,
                         deep_lying_forward_at_pref_attributes,
                         role_list[83])

    pressing_forward_de_key_attributes = [5, 20, 13, 50, 48, 46, 39, 10, 6]
    pressing_forward_de_pref_attributes = [49, 47, 12, 43, 42, 34]
    calculate_role_score(shortlist_attributes_df, pressing_forward_de_key_attributes,
                         pressing_forward_de_pref_attributes,
                         role_list[84])

    pressing_forward_su_key_attributes = [5, 20, 13, 50, 48, 46, 39, 10, 6]
    pressing_forward_su_pref_attributes = [49, 47, 12, 43, 42, 22, 34, 19]
    calculate_role_score(shortlist_attributes_df, pressing_forward_su_key_attributes,
                         pressing_forward_su_pref_attributes,
                         role_list[85])

    pressing_forward_at_key_attributes = [5, 20, 13, 50, 48, 46, 22, 10, 6]
    pressing_forward_at_pref_attributes = [49, 47, 12, 43, 42, 39, 35, 34]
    calculate_role_score(shortlist_attributes_df, pressing_forward_at_key_attributes,
                         pressing_forward_at_pref_attributes,
                         role_list[86])

    complete_forward_su_key_attributes = [5, 49, 12, 48, 43, 39, 22, 7, 37, 34, 30, 26, 19, 9]
    complete_forward_su_pref_attributes = [47, 29, 20, 13, 10, 6, 35]
    calculate_role_score(shortlist_attributes_df, complete_forward_su_key_attributes,
                         complete_forward_su_pref_attributes,
                         role_list[87])

    complete_forward_at_key_attributes = [5, 49, 12, 48, 43, 22, 37, 35, 34, 30, 9]
    complete_forward_at_pref_attributes = [47, 29, 20, 13, 39, 10, 7, 6, 26, 19]
    calculate_role_score(shortlist_attributes_df, complete_forward_at_key_attributes,
                         complete_forward_at_pref_attributes,
                         role_list[88])

    print('Complete: shortlist_attributes_df')

    return shortlist_attributes_df
