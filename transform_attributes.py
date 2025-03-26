# Todo ----------------
# 2. MAKE APP COMPATIBLE WITH ANY LANGUAGE (fix order of columns, address them by column # rather than column name, display in the user's language on the app)
# 3. Fix position scores, *Add Role Scores for attributes & stats (should be a more accurate representation than star ratings in game)

import pandas as pd
import numpy as np
from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# Configure Pandas Settings
pd.set_option('display.max_columns', 20)
pd.options.mode.chained_assignment = None

# Configure Numpy setting to show numerical values rather than np.float64()
np.set_printoptions(legacy='1.25')

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

    # Create role score columns
    def calculate_role_score(df, key_attributes, pref_attributes, column_title):
        key_attributes_total = df[key_attributes].sum(axis=1)
        pref_attributes_total = df[pref_attributes].sum(axis=1)
        role_total = (3 * key_attributes_total) + (2 * pref_attributes_total)
        role_max = (3 * (20 * len(key_attributes))) + (2 * (20 * len(pref_attributes)))
        role_score = (role_total / role_max).astype(float).round(2)
        df[column_title] = role_score
        return df

    # Goalkeeper role scores --------------------------------
    gk_key_attributes = ['Agi', 'Cnt', 'Pos', 'Aer', 'Cmd', 'Com', 'Han', 'Kic', 'Ref']
    gk_pref_attributes = ['Ant', 'Dec', '1v1', 'Thr']
    calculate_role_score(squad_attributes_df, gk_key_attributes, gk_pref_attributes,
                         'goalkeeper_score')

    sweeper_keeper_de_key_attributes = ['Agi', 'Ant', 'Cnt', 'Pos', 'Cmd', 'Kic', '1v1', 'Ref', ]
    sweeper_keeper_de_pref_attributes = ['Acc', 'Cmp', 'Dec', 'Vis', 'Aer', 'Com', 'Fir', 'Han', 'Pas', 'TRO', 'Thr']
    calculate_role_score(squad_attributes_df, sweeper_keeper_de_key_attributes, sweeper_keeper_de_pref_attributes,
                         'sweeper_keeper_de_score')

    sweeper_keeper_su_key_attributes = ['Agi', 'Ant', 'Cmp', 'Cnt', 'Pos', 'Cmd', 'Kic', '1v1', 'Ref', 'TRO']
    sweeper_keeper_su_pref_attributes = ['Acc', 'Dec', 'Vis', 'Aer', 'Com', 'Fir', 'Han', 'Pas', 'Thr']
    calculate_role_score(squad_attributes_df, sweeper_keeper_su_key_attributes, sweeper_keeper_su_pref_attributes,
                         'sweeper_keeper_su_score')

    sweeper_keeper_at_key_attributes = ['Agi', 'Ant', 'Cmp', 'Cnt', 'Pos', 'Cmd', 'Kic', '1v1', 'Ref', 'TRO']
    sweeper_keeper_at_pref_attributes = ['Acc', 'Dec', 'Vis', 'Aer', 'Com', 'Ecc', 'Fir', 'Han', 'Pas', 'Thr']
    calculate_role_score(squad_attributes_df, sweeper_keeper_at_key_attributes, sweeper_keeper_at_pref_attributes,
                         'sweeper_keeper_at_score')

    # Central Defender Role Scores ----------------------------------------
    central_def_de_key_attributes = ['Jum', 'Str', 'Pos', 'Hea', 'Mar', 'Tck']
    central_def_de_pref_attributes = ['Pac', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec']
    calculate_role_score(squad_attributes_df, central_def_de_key_attributes, central_def_de_pref_attributes,
                         'central_def_de_score')

    central_def_st_key_attributes = ['Jum', 'Str', 'Agg', 'Bra', 'Pos', 'Dec', 'Hea', 'Tck']
    central_def_st_pref_attributes = ['Mar', 'Ant', 'Cmp', 'Cnt']
    calculate_role_score(squad_attributes_df, central_def_st_key_attributes, central_def_st_pref_attributes,
                         'central_def_st_score')

    central_def_co_key_attributes = ['Pac', 'Ant', 'Cnt', 'Dec', 'Pos', 'Mar', 'Tck']
    central_def_co_pref_attributes = ['Jum', 'Str', 'Bra', 'Cmp', 'Hea']
    calculate_role_score(squad_attributes_df, central_def_co_key_attributes, central_def_co_pref_attributes,
                         'central_def_co_score')

    no_nonsense_cb_de_key_attributes = ['Jum', 'Str', 'Pos', 'Hea', 'Mar', 'Tck']
    no_nonsense_cb_de_pref_attributes = ['Pac', 'Agg', 'Ant', 'Bra', 'Cnt']
    calculate_role_score(squad_attributes_df, no_nonsense_cb_de_key_attributes, no_nonsense_cb_de_pref_attributes,
                         'no_nonsense_cb_de_score')

    no_nonsense_cb_st_key_attributes = ['Jum', 'Str', 'Agg', 'Bra', 'Pos', 'Hea', 'Tck']
    no_nonsense_cb_st_pref_attributes = ['Mar', 'Ant', 'Cnt']
    calculate_role_score(squad_attributes_df, no_nonsense_cb_st_key_attributes, no_nonsense_cb_st_pref_attributes,
                         'no_nonsense_cb_st_score')

    no_nonsense_cb_co_key_attributes = ['Pac', 'Ant', 'Cnt', 'Pos', 'Mar', 'Tck']
    no_nonsense_cb_co_pref_attributes = ['Jum', 'Str', 'Bra', 'Hea']
    calculate_role_score(squad_attributes_df, no_nonsense_cb_co_key_attributes, no_nonsense_cb_co_pref_attributes,
                         'no_nonsense_cb_co_score')

    wide_cb_de_key_attributes = ['Jum', 'Str', 'Pos', 'Hea', 'Mar', 'Tck']
    wide_cb_de_pref_attributes = ['Agi', 'Pac', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Wor', 'Dri', 'Fir', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, wide_cb_de_key_attributes, wide_cb_de_pref_attributes,
                         'wide_cb_de_score')

    wide_cb_su_key_attributes = ['Jum', 'Pac', 'Str', 'Pos', 'Dri', 'Hea', 'Mar', 'Tck']
    wide_cb_su_pref_attributes = ['Agi', 'Sta', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'OtB', 'Wor', 'Cro', 'Fir',
                                  'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, wide_cb_su_key_attributes, wide_cb_su_pref_attributes,
                         'wide_cb_su_score')

    wide_cb_at_key_attributes = ['Jum', 'Pac', 'Sta', 'Str', 'OtB', 'Cro', 'Dri', 'Hea', 'Mar', 'Tck']
    wide_cb_at_pref_attributes = ['Agi', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Wor', 'Fir', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, wide_cb_at_key_attributes, wide_cb_at_pref_attributes,
                         'wide_cb_at_score')

    ball_playing_def_de_key_attributes = ['Jum', 'Str', 'Cmp', 'Pos', 'Hea', 'Mar', 'Pas', 'Tck']
    ball_playing_def_de_pref_attributes = ['Pac', 'Agg', 'Ant', 'Bra', 'Cnt', 'Dec', 'Vis', 'Fir', 'Tec']
    calculate_role_score(squad_attributes_df, ball_playing_def_de_key_attributes, ball_playing_def_de_pref_attributes,
                         'ball_playing_def_de_score')

    ball_playing_def_st_key_attributes = ['Jum', 'Str', 'Agg', 'Bra', 'Cmp', 'Dec', 'Pos', 'Hea', 'Pas', 'Tck']
    ball_playing_def_st_pref_attributes = ['Ant', 'Cnt', 'Vis', 'Fir', 'Mar', 'Tec']
    calculate_role_score(squad_attributes_df, ball_playing_def_st_key_attributes, ball_playing_def_st_pref_attributes,
                         'ball_playing_def_st_score')

    ball_playing_def_co_key_attributes = ['Pac', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Mar', 'Pas', 'Tck']
    ball_playing_def_co_pref_attributes = ['Jum', 'Str', 'Bra', 'Vis', 'Fir', 'Hea', 'Tec']
    calculate_role_score(squad_attributes_df, ball_playing_def_co_key_attributes, ball_playing_def_co_pref_attributes,
                         'ball_playing_def_co_score')

    libero_de_key_attributes = ['Jum', 'Str', 'Cmp', 'Dec', 'Pos', 'Tea', 'Fir', 'Hea', 'Mar', 'Pas', 'Tck', 'Tec']
    libero_de_pref_attributes = ['Pac', 'Sta', 'Ant', 'Bra', 'Cnt']
    calculate_role_score(squad_attributes_df, libero_de_key_attributes, libero_de_pref_attributes,
                         'libero_de_score')

    libero_su_key_attributes = ['Jum', 'Str', 'Cmp', 'Dec', 'Pos', 'Tea', 'Fir', 'Hea', 'Mar', 'Pas', 'Tck', 'Tec']
    libero_su_pref_attributes = ['Pac', 'Sta', 'Ant', 'Bra', 'Cnt', 'Vis', 'Dri']
    calculate_role_score(squad_attributes_df, libero_su_key_attributes, libero_su_pref_attributes,
                         'libero_su_score')

    # Fullback/Wingback role scores ------------------------------------------
    inverted_fb_key_attributes = ['Str', 'Pos', 'Hea', 'Mar', 'Tck']
    inverted_fb_pref_attributes = ['Agi', 'Jum', 'Pac', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Wor', 'Dri', 'Fir',
                                   'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, inverted_fb_key_attributes, inverted_fb_pref_attributes,
                         'inverted_fb_score')

    inverted_wb_de_key_attributes = ['Ant', 'Dec', 'Pos', 'Tea', 'Pas', 'Tck']
    inverted_wb_de_pref_attributes = ['Acc', 'Agi', 'Sta', 'Cmp', 'Cnt', 'OtB', 'Wor', 'Fir', 'Mar', 'Tec']
    calculate_role_score(squad_attributes_df, inverted_wb_de_key_attributes, inverted_wb_de_pref_attributes,
                         'inverted_wb_de_score')

    inverted_wb_su_key_attributes = ['Cmp', 'Dec', 'Tea', 'Fir', 'Pas', 'Tck']
    inverted_wb_su_pref_attributes = ['Acc', 'Agi', 'Sta', 'Ant', 'Cnt', 'OtB', 'Pos', 'Vis', 'Wor', 'Mar', 'Tec']
    calculate_role_score(squad_attributes_df, inverted_wb_su_key_attributes, inverted_wb_su_pref_attributes,
                         'inverted_wb_su_score')

    inverted_wb_at_key_attributes = ['Acc', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tck', 'Tec']
    inverted_wb_at_pref_attributes = ['Agi', 'Pac', 'Sta', 'Ant', 'Cnt', 'Fla', 'Pos', 'Wor', 'Cro', 'Dri', 'Lon',
                                      'Mar']
    calculate_role_score(squad_attributes_df, inverted_wb_at_key_attributes, inverted_wb_at_pref_attributes,
                         'inverted_wb_at_score')

    fullback_de_key_attributes = ['Ant', 'Cnt', 'Pos', 'Mar', 'Tck']
    fullback_de_pref_attributes = ['Pac', 'Sta', 'Dec', 'Tea', 'Wor', 'Cro', 'Pas']
    calculate_role_score(squad_attributes_df, fullback_de_key_attributes, fullback_de_pref_attributes,
                         'fullback_de_score')

    fullback_su_key_attributes = ['Ant', 'Cnt', 'Pos', 'Mar', 'Tck']
    fullback_su_pref_attributes = ['Pac', 'Sta', 'Dec', 'Tea', 'Wor', 'Cro', 'Dri', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, fullback_su_key_attributes, fullback_su_pref_attributes,
                         'fullback_su_score')

    fullback_at_key_attributes = ['Ant', 'Pos', 'Tea', 'Cro', 'Mar', 'Tck']
    fullback_at_pref_attributes = ['Agi', 'Pac', 'Sta', 'Cnt', 'Dec', 'OtB', 'Wor', 'Dri', 'Fir', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, fullback_at_key_attributes, fullback_at_pref_attributes,
                         'fullback_at_score')

    fullback_au_key_attributes = ['Ant', 'Cnt', 'Pos', 'Tea', 'Mar', 'Tck']
    fullback_au_pref_attributes = ['Agi', 'Pac', 'Sta', 'Dec', 'Wor', 'Cro', 'Dri', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, fullback_au_key_attributes, fullback_au_pref_attributes,
                         'fullback_au_score')

    wingback_de_key_attributes = ['Acc', 'Sta', 'Ant', 'Pos', 'Tea', 'Wor', 'Mar', 'Tck']
    wingback_de_pref_attributes = ['Agi', 'Bal', 'Pac', 'Cnt', 'Dec', 'OtB', 'Cro', 'Dri', 'Fir', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, wingback_de_key_attributes, wingback_de_pref_attributes,
                         'wingback_de_score')

    wingback_su_key_attributes = ['Acc', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Mar', 'Tck']
    wingback_su_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Cnt', 'Dec', 'Pos', 'Fir', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, wingback_su_key_attributes, wingback_su_pref_attributes,
                         'wingback_su_score')

    wingback_at_key_attributes = ['Acc', 'Pac', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Tck', 'Tec']
    wingback_at_pref_attributes = ['Agi', 'Bal', 'Ant', 'Cnt', 'Dec', 'Fla', 'Pos', 'Fir', 'Mar', 'Pas']
    calculate_role_score(squad_attributes_df, wingback_at_key_attributes, wingback_at_pref_attributes,
                         'wingback_at_score')

    wingback_au_key_attributes = ['Acc', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Mar', 'Tck']
    wingback_au_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Cnt', 'Dec', 'Pos', 'Fir', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, wingback_au_key_attributes, wingback_au_pref_attributes,
                         'wingback_au_score')

    no_nonsense_fb_key_attributes = ['Str', 'Ant', 'Pos', 'Mar', 'Tck']
    no_nonsense_fb_pref_attributes = ['Agg', 'Bra', 'Cnt', 'Tea', 'Hea']
    calculate_role_score(squad_attributes_df, no_nonsense_fb_key_attributes, no_nonsense_fb_pref_attributes,
                         'no_nonsense_fb_score')

    complete_wingback_su_key_attributes = ['Acc', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Tec']
    complete_wingback_su_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Dec', 'Fla', 'Pos', 'Fir', 'Mar', 'Pas', 'Tck']
    calculate_role_score(squad_attributes_df, complete_wingback_su_key_attributes, complete_wingback_su_pref_attributes,
                         'complete_wingback_su_score')

    complete_wingback_at_key_attributes = ['Acc', 'Sta', 'Fla', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Tec']
    complete_wingback_at_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Dec', 'Pos', 'Fir', 'Mar', 'Pas', 'Tck']
    calculate_role_score(squad_attributes_df, complete_wingback_at_key_attributes, complete_wingback_at_pref_attributes,
                         'complete_wingback_at_score')

    # Defensive Midfielder role scores -------------------------------------------
    segundo_volante_su_key_attributes = ['Pac', 'Sta', 'OtB', 'Pos', 'Wor', 'Mar', 'Pas', 'Tck']
    segundo_volante_su_pref_attributes = ['Acc', 'Bal', 'Str', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Fin', 'Fir', 'Lon']
    calculate_role_score(squad_attributes_df, segundo_volante_su_key_attributes, segundo_volante_su_pref_attributes,
                         'segundo_volante_su_score')

    segundo_volante_at_key_attributes = ['Pac', 'Sta', 'Ant', 'OtB', 'Pos', 'Wor', 'Fin', 'Lon', 'Pas', 'Tck']
    segundo_volante_at_pref_attributes = ['Acc', 'Bal', 'Str', 'Cmp', 'Cnt', 'Dec', 'Fir', 'Mar']
    calculate_role_score(squad_attributes_df, segundo_volante_at_key_attributes, segundo_volante_at_pref_attributes,
                         'segundo_volante_at_score')

    half_back_key_attributes = ['Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Tea', 'Mar', 'Tck']
    half_back_pref_attributes = ['Jum', 'Sta', 'Str', 'Agg', 'Bra', 'Wor', 'Fir', 'Pas']
    calculate_role_score(squad_attributes_df, half_back_key_attributes, half_back_pref_attributes,
                         'half_back_score')

    defensive_midfielder_de_key_attributes = ['Ant', 'Cnt', 'Pos', 'Tea', 'Tck']
    defensive_midfielder_de_pref_attributes = ['Sta', 'Str', 'Agg', 'Cmp', 'Dec', 'Wor', 'Mar', 'Pas']
    calculate_role_score(squad_attributes_df, defensive_midfielder_de_key_attributes,
                         defensive_midfielder_de_pref_attributes,
                         'defensive_midfielder_de_score')

    defensive_midfielder_su_key_attributes = ['Ant', 'Cnt', 'Pos', 'Tea', 'Tck']
    defensive_midfielder_su_pref_attributes = ['Sta', 'Str', 'Agg', 'Cmp', 'Dec', 'Wor', 'Fir', 'Mar', 'Pas']
    calculate_role_score(squad_attributes_df, defensive_midfielder_su_key_attributes,
                         defensive_midfielder_su_pref_attributes,
                         'defensive_midfielder_su_score')

    anchor_key_attributes = ['Ant', 'Cnt', 'Dec', 'Pos', 'Mar', 'Tck']
    anchor_pref_attributes = ['Str', 'Cmp', 'Tea']
    calculate_role_score(squad_attributes_df, anchor_key_attributes, anchor_pref_attributes,
                         'anchor_score')

    regista_key_attributes = ['Cmp', 'Dec', 'Fla', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    regista_pref_attributes = ['Bal', 'Ant', 'Dri', 'Lon']
    calculate_role_score(squad_attributes_df, regista_key_attributes, regista_pref_attributes,
                         'regista_score')

    ball_winning_midfielder_de_key_attributes = ['Sta', 'Agg', 'Ant', 'Tea', 'Wor', 'Tck']
    ball_winning_midfielder_de_pref_attributes = ['Agi', 'Pac', 'Str', 'Bra', 'Cnt', 'Pos', 'Mar']
    calculate_role_score(squad_attributes_df, ball_winning_midfielder_de_key_attributes,
                         ball_winning_midfielder_de_pref_attributes,
                         'ball_winning_midfielder_de_score')

    ball_winning_midfielder_su_key_attributes = ['Sta', 'Agg', 'Ant', 'Tea', 'Wor', 'Tck']
    ball_winning_midfielder_su_pref_attributes = ['Agi', 'Pac', 'Str', 'Bra', 'Cnt', 'Mar', 'Pas']
    calculate_role_score(squad_attributes_df, ball_winning_midfielder_su_key_attributes,
                         ball_winning_midfielder_su_pref_attributes,
                         'ball_winning_midfielder_su_score')

    deep_lying_playmaker_de_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    deep_lying_playmaker_de_pref_attributes = ['Bal', 'Ant', 'Pos', 'Tck']
    calculate_role_score(squad_attributes_df, deep_lying_playmaker_de_key_attributes,
                         deep_lying_playmaker_de_pref_attributes,
                         'deep_lying_playmaker_de_score')

    deep_lying_playmaker_su_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    deep_lying_playmaker_su_pref_attributes = ['Bal', 'Ant', 'OtB', 'Pos']
    calculate_role_score(squad_attributes_df, deep_lying_playmaker_su_key_attributes,
                         deep_lying_playmaker_su_pref_attributes,
                         'deep_lying_playmaker_su_score')

    roaming_playmaker_key_attributes = ['Acc', 'Sta', 'Ant', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Wor', 'Fir', 'Pas',
                                        'Tec']
    roaming_playmaker_pref_attributes = ['Agi', 'Bal', 'Pac', 'Cnt', 'Pos', 'Dri', 'Lon']
    calculate_role_score(squad_attributes_df, roaming_playmaker_key_attributes, roaming_playmaker_pref_attributes,
                         'roaming_playmaker_score')

    # Central Midfielder role scores --------------------------------------------
    advanced_playmaker_su_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    advanced_playmaker_su_pref_attributes = ['Agi', 'Ant', 'Cnt', 'Fla', 'Dri']
    calculate_role_score(squad_attributes_df, advanced_playmaker_su_key_attributes,
                         advanced_playmaker_su_pref_attributes,
                         'advanced_playmaker_su_score')

    advanced_playmaker_at_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    advanced_playmaker_at_pref_attributes = ['Acc', 'Agi', 'Ant', 'Cnt', 'Fla', 'Dri']
    calculate_role_score(squad_attributes_df, advanced_playmaker_at_key_attributes,
                         advanced_playmaker_at_pref_attributes,
                         'advanced_playmaker_at_score')

    carrilero_key_attributes = ['Sta', 'Dec', 'Pos', 'Tea', 'Fir', 'Pas', 'Tck']
    carrilero_pref_attributes = ['Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor', 'Tec']
    calculate_role_score(squad_attributes_df, carrilero_key_attributes, carrilero_pref_attributes,
                         'carrilero_role_score')

    mezzala_su_key_attributes = ['Acc', 'Dec', 'OtB', 'Wor', 'Pas', 'Tec']
    mezzala_su_pref_attributes = ['Bal', 'Sta', 'Ant', 'Cmp', 'Vis', 'Dri', 'Fir', 'Lon', 'Tck']
    calculate_role_score(squad_attributes_df, mezzala_su_key_attributes, mezzala_su_pref_attributes,
                         'mezzala_su_score')

    mezzala_at_key_attributes = ['Acc', 'Dec', 'OtB', 'Vis', 'Wor', 'Dri', 'Pas', 'Tec']
    mezzala_at_pref_attributes = ['Bal', 'Sta', 'Ant', 'Cmp', 'Fla', 'Fin', 'Fir', 'Lon']
    calculate_role_score(squad_attributes_df, mezzala_at_key_attributes, mezzala_at_pref_attributes,
                         'mezzala_at_score')

    central_midfielder_de_key_attributes = ['Cnt', 'Dec', 'Pos', 'Tea', 'Tck']
    central_midfielder_de_pref_attributes = ['Sta', 'Agg', 'Ant', 'Cmp', 'Wor', 'Fir', 'Mar', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, central_midfielder_de_key_attributes,
                         central_midfielder_de_pref_attributes,
                         'central_midfielder_de_score')

    central_midfielder_su_key_attributes = ['Dec', 'Tea', 'Fir', 'Pas', 'Tck']
    central_midfielder_su_pref_attributes = ['Sta', 'Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor', 'Tec']
    calculate_role_score(squad_attributes_df, central_midfielder_su_key_attributes,
                         central_midfielder_su_pref_attributes,
                         'central_midfielder_su_score')

    central_midfielder_at_key_attributes = ['Dec', 'OtB', 'Fir', 'Pas']
    central_midfielder_at_pref_attributes = ['Acc', 'Sta', 'Ant', 'Cmp', 'Tea', 'Vis', 'Wor', 'Lon', 'Tck', 'Tec']
    calculate_role_score(squad_attributes_df, central_midfielder_at_key_attributes,
                         central_midfielder_at_pref_attributes,
                         'central_midfielder_at_score')

    central_midfielder_au_key_attributes = ['Dec', 'Tea', 'Fir', 'Pas', 'Tck']
    central_midfielder_au_pref_attributes = ['Sta', 'Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor', 'Tec']
    calculate_role_score(squad_attributes_df, central_midfielder_au_key_attributes,
                         central_midfielder_au_pref_attributes,
                         'central_midfielder_au_score')

    box_to_box_midfielder_key_attributes = ['Sta', 'OtB', 'Tea', 'Wor', 'Pas', 'Tck']
    box_to_box_midfielder_pref_attributes = ['Acc', 'Bal', 'Pac', 'Str', 'Agg', 'Ant', 'Cmp', 'Dec', 'Pos', 'Dri',
                                             'Fin', 'Fir', 'Lon', 'Tec']
    calculate_role_score(squad_attributes_df, box_to_box_midfielder_key_attributes,
                         box_to_box_midfielder_pref_attributes,
                         'box_to_box_midfielder_score')

    # Winger role scores --------------------------------------
    defensive_winger_de_key_attributes = ['Sta', 'Ant', 'OtB', 'Pos', 'Tea', 'Wor', 'Tec']
    defensive_winger_de_pref_attributes = ['Acc', 'Agg', 'Cnt', 'Dec', 'Cro', 'Dri', 'Fir', 'Mar', 'Tck']
    calculate_role_score(squad_attributes_df, defensive_winger_de_key_attributes, defensive_winger_de_pref_attributes,
                         'defensive_winger_de_score')

    defensive_winger_su_key_attributes = ['Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Tec']
    defensive_winger_su_pref_attributes = ['Acc', 'Agg', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Dri', 'Fir', 'Mar', 'Pas',
                                           'Tck']
    calculate_role_score(squad_attributes_df, defensive_winger_su_key_attributes, defensive_winger_su_pref_attributes,
                         'defensive_winger_su_score')

    wide_midfielder_de_key_attributes = ['Cnt', 'Dec', 'Pos', 'Tea', 'Wor', 'Pas', 'Tck']
    wide_midfielder_de_pref_attributes = ['Sta', 'Ant', 'Cmp', 'Cro', 'Fir', 'Mar', 'Tec']
    calculate_role_score(squad_attributes_df, wide_midfielder_de_key_attributes, wide_midfielder_de_pref_attributes,
                         'wide_midfielder_de_score')

    wide_midfielder_su_key_attributes = ['Sta', 'Dec', 'Tea', 'Wor', 'Pas', 'Tck']
    wide_midfielder_su_pref_attributes = ['Ant', 'Cmp', 'Cnt', 'OtB', 'Pos', 'Vis', 'Cro', 'Fir', 'Tec']
    calculate_role_score(squad_attributes_df, wide_midfielder_su_key_attributes, wide_midfielder_su_pref_attributes,
                         'wide_midfielder_su_score')

    wide_midfielder_at_key_attributes = ['Sta', 'Dec', 'Tea', 'Wor', 'Cro', 'Fir', 'Pas']
    wide_midfielder_at_pref_attributes = ['Ant', 'Cmp', 'OtB', 'Vis', 'Tck', 'Tec']
    calculate_role_score(squad_attributes_df, wide_midfielder_at_key_attributes, wide_midfielder_at_pref_attributes,
                         'wide_midfielder_at_score')

    wide_midfielder_au_key_attributes = ['Sta', 'Dec', 'Tea', 'Wor', 'Pas', 'Tck']
    wide_midfielder_au_pref_attributes = ['Ant', 'Cmp', 'Cnt', 'OtB', 'Pos', 'Vis', 'Cro', 'Fir', 'Tec']
    calculate_role_score(squad_attributes_df, wide_midfielder_au_key_attributes, wide_midfielder_au_pref_attributes,
                         'wide_midfielder_au_score')

    wide_playmaker_su_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    wide_playmaker_su_pref_attributes = ['Agi', 'OtB', 'Dri']
    calculate_role_score(squad_attributes_df, wide_playmaker_su_key_attributes, wide_playmaker_su_pref_attributes,
                         'wide_playmaker_su_score')

    wide_playmaker_at_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Dri', 'Fir', 'Pas', 'Tec']
    wide_playmaker_at_pref_attributes = ['Acc', 'Agi', 'Ant', 'Fla']
    calculate_role_score(squad_attributes_df, wide_playmaker_at_key_attributes, wide_playmaker_at_pref_attributes,
                         'wide_playmaker_at_score')

    inverted_winger_su_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Pas', 'Tec']
    inverted_winger_su_pref_attributes = ['Bal', 'Pac', 'Sta', 'Cmp', 'Dec', 'OtB', 'Vis', 'Wor', 'Fir', 'Lon']
    calculate_role_score(squad_attributes_df, inverted_winger_su_key_attributes, inverted_winger_su_pref_attributes,
                         'inverted_winger_su_score')

    inverted_winger_at_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Pas', 'Tec']
    inverted_winger_at_pref_attributes = ['Bal', 'Pac', 'Sta', 'Ant', 'Cmp', 'Dec', 'Fla', 'OtB', 'Vis', 'Wor', 'Fir',
                                          'Lon']
    calculate_role_score(squad_attributes_df, inverted_winger_at_key_attributes, inverted_winger_at_pref_attributes,
                         'inverted_winger_at_score')

    winger_su_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Tec']
    winger_su_pref_attributes = ['Bal', 'Pac', 'Sta', 'OtB', 'Wor', 'Fir', 'Pas']
    calculate_role_score(squad_attributes_df, winger_su_key_attributes, winger_su_pref_attributes,
                         'winger_su_score')

    winger_at_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Tec']
    winger_at_pref_attributes = ['Bal', 'Pac', 'Sta', 'Ant', 'Fla', 'OtB', 'Wor', 'Fir', 'Pas']
    calculate_role_score(squad_attributes_df, winger_at_key_attributes, winger_at_pref_attributes,
                         'winger_at_score')

    inside_forward_su_key_attributes = ['Acc', 'Agi', 'OtB', 'Dri', 'Fin', 'Fir', 'Tec']
    inside_forward_su_pref_attributes = ['Bal', 'Pac', 'Sta', 'Ant', 'Cmp', 'Fla', 'Vis', 'Wor', 'Lon', 'Pas']
    calculate_role_score(squad_attributes_df, inside_forward_su_key_attributes, inside_forward_su_pref_attributes,
                         'inside_forward_su_score')

    inside_forward_at_key_attributes = ['Acc', 'Agi', 'Ant', 'OtB', 'Dri', 'Fin', 'Fir', 'Tec']
    inside_forward_at_pref_attributes = ['Bal', 'Pac', 'Sta', 'Cmp', 'Fla', 'Wor', 'Lon', 'Pas']
    calculate_role_score(squad_attributes_df, inside_forward_at_key_attributes, inside_forward_at_pref_attributes,
                         'inside_forward_at_score')

    raumdeuter_key_attributes = ['Bal', 'Ant', 'Cmp', 'Cnt', 'Dec', 'OtB', 'Fin']
    raumdeuter_pref_attributes = ['Acc', 'Sta', 'Wor', 'Fir', 'Tec']
    calculate_role_score(squad_attributes_df, raumdeuter_key_attributes, raumdeuter_pref_attributes,
                         'raumdeuter_score')

    wide_target_forward_su_key_attributes = ['Jum', 'Str', 'Bra', 'Tea', 'Hea']
    wide_target_forward_su_pref_attributes = ['Bal', 'Sta', 'Ant', 'OtB', 'Wor', 'Cro', 'Fir']
    calculate_role_score(squad_attributes_df, wide_target_forward_su_key_attributes,
                         wide_target_forward_su_pref_attributes,
                         'wide_target_forward_su_score')

    wide_target_forward_at_key_attributes = ['Jum', 'Str', 'Bra', 'OtB', 'Hea']
    wide_target_forward_at_pref_attributes = ['Bal', 'Sta', 'Ant', 'Tea', 'Wor', 'Cro', 'Fin', 'Fir']
    calculate_role_score(squad_attributes_df, wide_target_forward_at_key_attributes,
                         wide_target_forward_at_pref_attributes,
                         'wide_target_forward_at_score')

    trequartista_key_attributes = ['Acc', 'Cmp', 'Dec', 'Fla', 'OtB', 'Vis', 'Dri', 'Fir', 'Pas', 'Tec']
    trequartista_pref_attributes = ['Agi', 'Bal', 'Ant', 'Fin']
    calculate_role_score(squad_attributes_df, trequartista_key_attributes, trequartista_pref_attributes,
                         'trequartista_score')

    enganche_key_attributes = ['Cmp', 'Dec', 'Vis', 'Fir', 'Pas', 'Tec']
    enganche_pref_attributes = ['Agi', 'Ant', 'Fla', 'OtB', 'Tea', 'Dri']
    calculate_role_score(squad_attributes_df, enganche_key_attributes, enganche_pref_attributes,
                         'enganche_score')

    attacking_midfielder_su_key_attributes = ['Ant', 'Dec', 'Fla', 'OtB', 'Fir', 'Lon', 'Pas', 'Tec']
    attacking_midfielder_su_pref_attributes = ['Agi', 'Cmp', 'Vis', 'Dri']
    calculate_role_score(squad_attributes_df, attacking_midfielder_su_key_attributes,
                         attacking_midfielder_su_pref_attributes,
                         'attacking_midfielder_su_score')

    attacking_midfielder_at_key_attributes = ['Ant', 'Dec', 'Fla', 'OtB', 'Fir', 'Lon', 'Pas', 'Tec', 'Dri']
    attacking_midfielder_at_pref_attributes = ['Agi', 'Cmp', 'Vis', 'Fin']
    calculate_role_score(squad_attributes_df, attacking_midfielder_at_key_attributes,
                         attacking_midfielder_at_pref_attributes,
                         'attacking_midfielder_at_score')

    shadow_striker_key_attributes = ['Acc', 'Ant', 'Cmp', 'OtB', 'Dri', 'Fin', 'Fir']
    shadow_striker_pref_attributes = ['Agi', 'Bal', 'Pac', 'Sta', 'Cnt', 'Dec', 'Wor', 'Pas', 'Tec']
    calculate_role_score(squad_attributes_df, shadow_striker_key_attributes, shadow_striker_pref_attributes,
                         'shadow_striker_score')

    advanced_forward_key_attributes = ['Acc', 'Cmp', 'OtB', 'Dri', 'Fin', 'Fir', 'Tec']
    advanced_forward_pref_attributes = ['Agi', 'Bal', 'Pac', 'Sta', 'Ant', 'Dec', 'Wor', 'Pas']
    calculate_role_score(squad_attributes_df, advanced_forward_key_attributes, advanced_forward_pref_attributes,
                         'advanced_forward_score')

    poacher_key_attributes = ['Ant', 'Cmp', 'OtB', 'Fin']
    poacher_pref_attributes = ['Acc', 'Dec', 'Fir', 'Hea', 'Tec']
    calculate_role_score(squad_attributes_df, poacher_key_attributes, poacher_pref_attributes,
                         'poacher_score')

    false_nine_key_attributes = ['Acc', 'Agi', 'Cmp', 'Dec', 'OtB', 'Vis', 'Dri', 'Fir', 'Pas', 'Tec']
    false_nine_pref_attributes = ['Bal', 'Ant', 'Fla', 'Tea', 'Fin']
    calculate_role_score(squad_attributes_df, false_nine_key_attributes, false_nine_pref_attributes,
                         'false_nine_score')

    target_forward_su_key_attributes = ['Bal', 'Jum', 'Str', 'Bra', 'Tea', 'Hea']
    target_forward_su_pref_attributes = ['Agg', 'Ant', 'Cmp', 'Dec', 'OtB', 'Fin', 'Fir']
    calculate_role_score(squad_attributes_df, target_forward_su_key_attributes, target_forward_su_pref_attributes,
                         'target_forward_su_score')

    target_forward_at_key_attributes = ['Bal', 'Jum', 'Str', 'Bra', 'Cmp', 'OtB', 'Fin', 'Hea']
    target_forward_at_pref_attributes = ['Agg', 'Ant', 'Dec', 'Tea', 'Fir']
    calculate_role_score(squad_attributes_df, target_forward_at_key_attributes, target_forward_at_pref_attributes,
                         'target_forward_at_score')

    deep_lying_forward_su_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Fir', 'Pas', 'Tec']
    deep_lying_forward_su_pref_attributes = ['Bal', 'Str', 'Ant', 'Fla', 'Vis', 'Fin']
    calculate_role_score(squad_attributes_df, deep_lying_forward_su_key_attributes,
                         deep_lying_forward_su_pref_attributes,
                         'deep_lying_forward_su_score')

    deep_lying_forward_at_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Fir', 'Pas', 'Tec']
    deep_lying_forward_at_pref_attributes = ['Bal', 'Str', 'Ant', 'Fla', 'Vis', 'Dri', 'Fin']
    calculate_role_score(squad_attributes_df, deep_lying_forward_at_key_attributes,
                         deep_lying_forward_at_pref_attributes,
                         'deep_lying_forward_at_score')

    pressing_forward_de_key_attributes = ['Acc', 'Pac', 'Sta', 'Agg', 'Ant', 'Bra', 'Dec', 'Tea', 'Wor']
    pressing_forward_de_pref_attributes = ['Agi', 'Bal', 'Str', 'Cmp', 'Cnt', 'Fir']
    calculate_role_score(squad_attributes_df, pressing_forward_de_key_attributes, pressing_forward_de_pref_attributes,
                         'pressing_forward_de_score')

    pressing_forward_su_key_attributes = ['Acc', 'Pac', 'Sta', 'Agg', 'Ant', 'Bra', 'Dec', 'Tea', 'Wor']
    pressing_forward_su_pref_attributes = ['Agi', 'Bal', 'Str', 'Cmp', 'Cnt', 'OtB', 'Fir', 'Pas']
    calculate_role_score(squad_attributes_df, pressing_forward_su_key_attributes, pressing_forward_su_pref_attributes,
                         'pressing_forward_su_score')

    pressing_forward_at_key_attributes = ['Acc', 'Pac', 'Sta', 'Agg', 'Ant', 'Bra', 'OtB', 'Tea', 'Wor']
    pressing_forward_at_pref_attributes = ['Agi', 'Bal', 'Str', 'Cmp', 'Cnt', 'Dec', 'Fin', 'Fir']
    calculate_role_score(squad_attributes_df, pressing_forward_at_key_attributes, pressing_forward_at_pref_attributes,
                         'pressing_forward_at_score')

    complete_forward_su_key_attributes = ['Acc', 'Agi', 'Str', 'Ant', 'Cmp', 'Dec', 'OtB', 'Vis', 'Dri', 'Fir', 'Hea',
                                          'Lon', 'Pas', 'Tec']
    complete_forward_su_pref_attributes = ['Bal', 'Jum', 'Pac', 'Sta', 'Tea', 'Wor', 'Fin']
    calculate_role_score(squad_attributes_df, complete_forward_su_key_attributes, complete_forward_su_pref_attributes,
                         'complete_forward_su_score')

    complete_forward_at_key_attributes = ['Acc', 'Agi', 'Str', 'Ant', 'Cmp', 'OtB', 'Dri', 'Fin', 'Fir', 'Hea', 'Tec']
    complete_forward_at_pref_attributes = ['Bal', 'Jum', 'Pac', 'Sta', 'Dec', 'Tea', 'Vis', 'Wor', 'Lon', 'Pas']
    calculate_role_score(squad_attributes_df, complete_forward_at_key_attributes, complete_forward_at_pref_attributes,
                         'complete_forward_at_score')

    # Custom attributes for 'overall' radar -----------------------------------------
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

    # Calculating position averages ----------------------------------
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


def build_shortlist_attributes_dataframe(shortlist_attributes_file):
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

    # Configure Pandas Settings
    pd.set_option('display.max_columns', 20)
    pd.options.mode.chained_assignment = None

    # Configure Numpy setting to show numerical values rather than np.float64()
    np.set_printoptions(legacy='1.25')

    ## Create the DataFrames
    # Create scouting attributes DataFrame from Shortlist View
    shortlist_attributes_df = shortlist_attributes_file.copy()
    shortlist_attributes_df = shortlist_attributes_df[0]

    # Clean Scouting Attributes dataframe to remove range values
    for column in ['Acc', 'Wor', 'Vis', 'Thr', 'Tec', 'Tea', 'Tck', 'Str', 'Sta', 'TRO', 'Ref', 'Pun', 'Pos', 'Pen',
                   'Pas',
                   'Pac', '1v1', 'OtB', 'Nat', 'Mar', 'L Th', 'Lon', 'Ldr', 'Kic', 'Jum', 'Hea', 'Han', 'Fre', 'Fla',
                   'Fir',
                   'Fin', 'Ecc', 'Dri', 'Det', 'Dec', 'Cro', 'Cor', 'Cnt', 'Cmp', 'Com', 'Cmd', 'Bra', 'Bal', 'Ant',
                   'Agi',
                   'Agg', 'Aer']:
        shortlist_attributes_df[column] = shortlist_attributes_df[column].astype(str)
        shortlist_attributes_df.loc[shortlist_attributes_df[column].str.contains('-'), column] = ''
        shortlist_attributes_df[column] = pd.to_numeric(shortlist_attributes_df[column]).round()

    # Remove unnecessary columns from Scouting Attributes
    shortlist_attributes_df = shortlist_attributes_df.drop(columns=['Inf', 'Rec'])

    # Function to remove the nationality part of the name (split at the last hyphen)
    def remove_nationality(name):
        if '-' in name:  # Check if there is a hyphen in the name
            return name.rsplit('-', 1)[0]  # Split from the right and take the first part (player name)
        else:
            return name  # If no hyphen, return the name as is

    # Apply the function to the 'Name' column
    shortlist_attributes_df['Name'] = shortlist_attributes_df['Name'].apply(remove_nationality)

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
    shortlist_attributes_df['Speed'] = shortlist_attributes_df[['Acc', 'Pac']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Vision'] = shortlist_attributes_df[['Pas', 'Fla', 'Vis']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Attacking'] = shortlist_attributes_df[['Fin', 'Cmp', 'OtB']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Technical'] = shortlist_attributes_df[['Dri', 'Fir', 'Tec']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Aerial'] = shortlist_attributes_df[['Hea', 'Jum']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Mental'] = shortlist_attributes_df[['Ant', 'Bra', 'Cnt', 'Dec', 'Det', 'Tea']].mean(
        axis=1).apply(np.floor)
    shortlist_attributes_df['Defending'] = shortlist_attributes_df[['Mar', 'Tck', 'Pos']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Physical'] = shortlist_attributes_df[['Agi', 'Bal', 'Sta', 'Str']].mean(axis=1).apply(
        np.floor)
    shortlist_attributes_df['Aerial (GK)'] = shortlist_attributes_df[['Aer', 'Han']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Shot Stopping'] = shortlist_attributes_df[['1v1', 'Ref']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Distribution'] = shortlist_attributes_df[['Kic', 'Thr']].mean(axis=1).apply(np.floor)
    shortlist_attributes_df['Communication'] = shortlist_attributes_df[['Cmd', 'Com']].mean(axis=1).apply(np.floor)

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
        shortlist_attributes_df[position_tag] = shortlist_attributes_df['Position'].apply(
            lambda pos: check_position_tags(pos, position_filter)
        )

    # Create role score columns
    def calculate_role_score(df, key_attributes, pref_attributes, column_title):
        key_attributes_total = df[key_attributes].sum(axis=1)
        pref_attributes_total = df[pref_attributes].sum(axis=1)
        role_total = (3 * key_attributes_total) + (2 * pref_attributes_total)
        role_max = (3 * (20 * len(key_attributes))) + (2 * (20 * len(pref_attributes)))
        role_score = (role_total / role_max).astype(float).round(2)
        df[column_title] = role_score
        return df

    # Goalkeeper role scores --------------------------------
    gk_key_attributes = ['Agi', 'Cnt', 'Pos', 'Aer', 'Cmd', 'Com', 'Han', 'Kic', 'Ref']
    gk_pref_attributes = ['Ant', 'Dec', '1v1', 'Thr']
    calculate_role_score(shortlist_attributes_df, gk_key_attributes, gk_pref_attributes,
                         'goalkeeper_score')

    sweeper_keeper_de_key_attributes = ['Agi', 'Ant', 'Cnt', 'Pos', 'Cmd', 'Kic', '1v1', 'Ref', ]
    sweeper_keeper_de_pref_attributes = ['Acc', 'Cmp', 'Dec', 'Vis', 'Aer', 'Com', 'Fir', 'Han', 'Pas', 'TRO', 'Thr']
    calculate_role_score(shortlist_attributes_df, sweeper_keeper_de_key_attributes, sweeper_keeper_de_pref_attributes,
                         'sweeper_keeper_de_score')

    sweeper_keeper_su_key_attributes = ['Agi', 'Ant', 'Cmp', 'Cnt', 'Pos', 'Cmd', 'Kic', '1v1', 'Ref', 'TRO']
    sweeper_keeper_su_pref_attributes = ['Acc', 'Dec', 'Vis', 'Aer', 'Com', 'Fir', 'Han', 'Pas', 'Thr']
    calculate_role_score(shortlist_attributes_df, sweeper_keeper_su_key_attributes, sweeper_keeper_su_pref_attributes,
                         'sweeper_keeper_su_score')

    sweeper_keeper_at_key_attributes = ['Agi', 'Ant', 'Cmp', 'Cnt', 'Pos', 'Cmd', 'Kic', '1v1', 'Ref', 'TRO']
    sweeper_keeper_at_pref_attributes = ['Acc', 'Dec', 'Vis', 'Aer', 'Com', 'Ecc', 'Fir', 'Han', 'Pas', 'Thr']
    calculate_role_score(shortlist_attributes_df, sweeper_keeper_at_key_attributes, sweeper_keeper_at_pref_attributes,
                         'sweeper_keeper_at_score')

    # Central Defender Role Scores ----------------------------------------
    central_def_de_key_attributes = ['Jum', 'Str', 'Pos', 'Hea', 'Mar', 'Tck']
    central_def_de_pref_attributes = ['Pac', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec']
    calculate_role_score(shortlist_attributes_df, central_def_de_key_attributes, central_def_de_pref_attributes,
                         'central_def_de_score')

    central_def_st_key_attributes = ['Jum', 'Str', 'Agg', 'Bra', 'Pos', 'Dec', 'Hea', 'Tck']
    central_def_st_pref_attributes = ['Mar', 'Ant', 'Cmp', 'Cnt']
    calculate_role_score(shortlist_attributes_df, central_def_st_key_attributes, central_def_st_pref_attributes,
                         'central_def_st_score')

    central_def_co_key_attributes = ['Pac', 'Ant', 'Cnt', 'Dec', 'Pos', 'Mar', 'Tck']
    central_def_co_pref_attributes = ['Jum', 'Str', 'Bra', 'Cmp', 'Hea']
    calculate_role_score(shortlist_attributes_df, central_def_co_key_attributes, central_def_co_pref_attributes,
                         'central_def_co_score')

    no_nonsense_cb_de_key_attributes = ['Jum', 'Str', 'Pos', 'Hea', 'Mar', 'Tck']
    no_nonsense_cb_de_pref_attributes = ['Pac', 'Agg', 'Ant', 'Bra', 'Cnt']
    calculate_role_score(shortlist_attributes_df, no_nonsense_cb_de_key_attributes, no_nonsense_cb_de_pref_attributes,
                         'no_nonsense_cb_de_score')

    no_nonsense_cb_st_key_attributes = ['Jum', 'Str', 'Agg', 'Bra', 'Pos', 'Hea', 'Tck']
    no_nonsense_cb_st_pref_attributes = ['Mar', 'Ant', 'Cnt']
    calculate_role_score(shortlist_attributes_df, no_nonsense_cb_st_key_attributes, no_nonsense_cb_st_pref_attributes,
                         'no_nonsense_cb_st_score')

    no_nonsense_cb_co_key_attributes = ['Pac', 'Ant', 'Cnt', 'Pos', 'Mar', 'Tck']
    no_nonsense_cb_co_pref_attributes = ['Jum', 'Str', 'Bra', 'Hea']
    calculate_role_score(shortlist_attributes_df, no_nonsense_cb_co_key_attributes, no_nonsense_cb_co_pref_attributes,
                         'no_nonsense_cb_co_score')

    wide_cb_de_key_attributes = ['Jum', 'Str', 'Pos', 'Hea', 'Mar', 'Tck']
    wide_cb_de_pref_attributes = ['Agi', 'Pac', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Wor', 'Dri', 'Fir', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, wide_cb_de_key_attributes, wide_cb_de_pref_attributes,
                         'wide_cb_de_score')

    wide_cb_su_key_attributes = ['Jum', 'Pac', 'Str', 'Pos', 'Dri', 'Hea', 'Mar', 'Tck']
    wide_cb_su_pref_attributes = ['Agi', 'Sta', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'OtB', 'Wor', 'Cro', 'Fir',
                                  'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, wide_cb_su_key_attributes, wide_cb_su_pref_attributes,
                         'wide_cb_su_score')

    wide_cb_at_key_attributes = ['Jum', 'Pac', 'Sta', 'Str', 'OtB', 'Cro', 'Dri', 'Hea', 'Mar', 'Tck']
    wide_cb_at_pref_attributes = ['Agi', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Wor', 'Fir', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, wide_cb_at_key_attributes, wide_cb_at_pref_attributes,
                         'wide_cb_at_score')

    ball_playing_def_de_key_attributes = ['Jum', 'Str', 'Cmp', 'Pos', 'Hea', 'Mar', 'Pas', 'Tck']
    ball_playing_def_de_pref_attributes = ['Pac', 'Agg', 'Ant', 'Bra', 'Cnt', 'Dec', 'Vis', 'Fir', 'Tec']
    calculate_role_score(shortlist_attributes_df, ball_playing_def_de_key_attributes,
                         ball_playing_def_de_pref_attributes,
                         'ball_playing_def_de_score')

    ball_playing_def_st_key_attributes = ['Jum', 'Str', 'Agg', 'Bra', 'Cmp', 'Dec', 'Pos', 'Hea', 'Pas', 'Tck']
    ball_playing_def_st_pref_attributes = ['Ant', 'Cnt', 'Vis', 'Fir', 'Mar', 'Tec']
    calculate_role_score(shortlist_attributes_df, ball_playing_def_st_key_attributes,
                         ball_playing_def_st_pref_attributes,
                         'ball_playing_def_st_score')

    ball_playing_def_co_key_attributes = ['Pac', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Mar', 'Pas', 'Tck']
    ball_playing_def_co_pref_attributes = ['Jum', 'Str', 'Bra', 'Vis', 'Fir', 'Hea', 'Tec']
    calculate_role_score(shortlist_attributes_df, ball_playing_def_co_key_attributes,
                         ball_playing_def_co_pref_attributes,
                         'ball_playing_def_co_score')

    libero_de_key_attributes = ['Jum', 'Str', 'Cmp', 'Dec', 'Pos', 'Tea', 'Fir', 'Hea', 'Mar', 'Pas', 'Tck', 'Tec']
    libero_de_pref_attributes = ['Pac', 'Sta', 'Ant', 'Bra', 'Cnt']
    calculate_role_score(shortlist_attributes_df, libero_de_key_attributes, libero_de_pref_attributes,
                         'libero_de_score')

    libero_su_key_attributes = ['Jum', 'Str', 'Cmp', 'Dec', 'Pos', 'Tea', 'Fir', 'Hea', 'Mar', 'Pas', 'Tck', 'Tec']
    libero_su_pref_attributes = ['Pac', 'Sta', 'Ant', 'Bra', 'Cnt', 'Vis', 'Dri']
    calculate_role_score(shortlist_attributes_df, libero_su_key_attributes, libero_su_pref_attributes,
                         'libero_su_score')

    # Fullback/Wingback role scores ------------------------------------------
    inverted_fb_key_attributes = ['Str', 'Pos', 'Hea', 'Mar', 'Tck']
    inverted_fb_pref_attributes = ['Agi', 'Jum', 'Pac', 'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Wor', 'Dri', 'Fir',
                                   'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, inverted_fb_key_attributes, inverted_fb_pref_attributes,
                         'inverted_fb_score')

    inverted_wb_de_key_attributes = ['Ant', 'Dec', 'Pos', 'Tea', 'Pas', 'Tck']
    inverted_wb_de_pref_attributes = ['Acc', 'Agi', 'Sta', 'Cmp', 'Cnt', 'OtB', 'Wor', 'Fir', 'Mar', 'Tec']
    calculate_role_score(shortlist_attributes_df, inverted_wb_de_key_attributes, inverted_wb_de_pref_attributes,
                         'inverted_wb_de_score')

    inverted_wb_su_key_attributes = ['Cmp', 'Dec', 'Tea', 'Fir', 'Pas', 'Tck']
    inverted_wb_su_pref_attributes = ['Acc', 'Agi', 'Sta', 'Ant', 'Cnt', 'OtB', 'Pos', 'Vis', 'Wor', 'Mar', 'Tec']
    calculate_role_score(shortlist_attributes_df, inverted_wb_su_key_attributes, inverted_wb_su_pref_attributes,
                         'inverted_wb_su_score')

    inverted_wb_at_key_attributes = ['Acc', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tck', 'Tec']
    inverted_wb_at_pref_attributes = ['Agi', 'Pac', 'Sta', 'Ant', 'Cnt', 'Fla', 'Pos', 'Wor', 'Cro', 'Dri', 'Lon',
                                      'Mar']
    calculate_role_score(shortlist_attributes_df, inverted_wb_at_key_attributes, inverted_wb_at_pref_attributes,
                         'inverted_wb_at_score')

    fullback_de_key_attributes = ['Ant', 'Cnt', 'Pos', 'Mar', 'Tck']
    fullback_de_pref_attributes = ['Pac', 'Sta', 'Dec', 'Tea', 'Wor', 'Cro', 'Pas']
    calculate_role_score(shortlist_attributes_df, fullback_de_key_attributes, fullback_de_pref_attributes,
                         'fullback_de_score')

    fullback_su_key_attributes = ['Ant', 'Cnt', 'Pos', 'Mar', 'Tck']
    fullback_su_pref_attributes = ['Pac', 'Sta', 'Dec', 'Tea', 'Wor', 'Cro', 'Dri', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, fullback_su_key_attributes, fullback_su_pref_attributes,
                         'fullback_su_score')

    fullback_at_key_attributes = ['Ant', 'Pos', 'Tea', 'Cro', 'Mar', 'Tck']
    fullback_at_pref_attributes = ['Agi', 'Pac', 'Sta', 'Cnt', 'Dec', 'OtB', 'Wor', 'Dri', 'Fir', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, fullback_at_key_attributes, fullback_at_pref_attributes,
                         'fullback_at_score')

    fullback_au_key_attributes = ['Ant', 'Cnt', 'Pos', 'Tea', 'Mar', 'Tck']
    fullback_au_pref_attributes = ['Agi', 'Pac', 'Sta', 'Dec', 'Wor', 'Cro', 'Dri', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, fullback_au_key_attributes, fullback_au_pref_attributes,
                         'fullback_au_score')

    wingback_de_key_attributes = ['Acc', 'Sta', 'Ant', 'Pos', 'Tea', 'Wor', 'Mar', 'Tck']
    wingback_de_pref_attributes = ['Agi', 'Bal', 'Pac', 'Cnt', 'Dec', 'OtB', 'Cro', 'Dri', 'Fir', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, wingback_de_key_attributes, wingback_de_pref_attributes,
                         'wingback_de_score')

    wingback_su_key_attributes = ['Acc', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Mar', 'Tck']
    wingback_su_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Cnt', 'Dec', 'Pos', 'Fir', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, wingback_su_key_attributes, wingback_su_pref_attributes,
                         'wingback_su_score')

    wingback_at_key_attributes = ['Acc', 'Pac', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Tck', 'Tec']
    wingback_at_pref_attributes = ['Agi', 'Bal', 'Ant', 'Cnt', 'Dec', 'Fla', 'Pos', 'Fir', 'Mar', 'Pas']
    calculate_role_score(shortlist_attributes_df, wingback_at_key_attributes, wingback_at_pref_attributes,
                         'wingback_at_score')

    wingback_au_key_attributes = ['Acc', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Mar', 'Tck']
    wingback_au_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Cnt', 'Dec', 'Pos', 'Fir', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, wingback_au_key_attributes, wingback_au_pref_attributes,
                         'wingback_au_score')

    no_nonsense_fb_key_attributes = ['Str', 'Ant', 'Pos', 'Mar', 'Tck']
    no_nonsense_fb_pref_attributes = ['Agg', 'Bra', 'Cnt', 'Tea', 'Hea']
    calculate_role_score(shortlist_attributes_df, no_nonsense_fb_key_attributes, no_nonsense_fb_pref_attributes,
                         'no_nonsense_fb_score')

    complete_wingback_su_key_attributes = ['Acc', 'Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Tec']
    complete_wingback_su_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Dec', 'Fla', 'Pos', 'Fir', 'Mar', 'Pas', 'Tck']
    calculate_role_score(shortlist_attributes_df, complete_wingback_su_key_attributes,
                         complete_wingback_su_pref_attributes,
                         'complete_wingback_su_score')

    complete_wingback_at_key_attributes = ['Acc', 'Sta', 'Fla', 'OtB', 'Tea', 'Wor', 'Cro', 'Dri', 'Tec']
    complete_wingback_at_pref_attributes = ['Agi', 'Bal', 'Pac', 'Ant', 'Dec', 'Pos', 'Fir', 'Mar', 'Pas', 'Tck']
    calculate_role_score(shortlist_attributes_df, complete_wingback_at_key_attributes,
                         complete_wingback_at_pref_attributes,
                         'complete_wingback_at_score')

    # Defensive Midfielder role scores -------------------------------------------
    segundo_volante_su_key_attributes = ['Pac', 'Sta', 'OtB', 'Pos', 'Wor', 'Mar', 'Pas', 'Tck']
    segundo_volante_su_pref_attributes = ['Acc', 'Bal', 'Str', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Fin', 'Fir', 'Lon']
    calculate_role_score(shortlist_attributes_df, segundo_volante_su_key_attributes, segundo_volante_su_pref_attributes,
                         'segundo_volante_su_score')

    segundo_volante_at_key_attributes = ['Pac', 'Sta', 'Ant', 'OtB', 'Pos', 'Wor', 'Fin', 'Lon', 'Pas', 'Tck']
    segundo_volante_at_pref_attributes = ['Acc', 'Bal', 'Str', 'Cmp', 'Cnt', 'Dec', 'Fir', 'Mar']
    calculate_role_score(shortlist_attributes_df, segundo_volante_at_key_attributes, segundo_volante_at_pref_attributes,
                         'segundo_volante_at_score')

    half_back_key_attributes = ['Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Tea', 'Mar', 'Tck']
    half_back_pref_attributes = ['Jum', 'Sta', 'Str', 'Agg', 'Bra', 'Wor', 'Fir', 'Pas']
    calculate_role_score(shortlist_attributes_df, half_back_key_attributes, half_back_pref_attributes,
                         'half_back_score')

    defensive_midfielder_de_key_attributes = ['Ant', 'Cnt', 'Pos', 'Tea', 'Tck']
    defensive_midfielder_de_pref_attributes = ['Sta', 'Str', 'Agg', 'Cmp', 'Dec', 'Wor', 'Mar', 'Pas']
    calculate_role_score(shortlist_attributes_df, defensive_midfielder_de_key_attributes,
                         defensive_midfielder_de_pref_attributes,
                         'defensive_midfielder_de_score')

    defensive_midfielder_su_key_attributes = ['Ant', 'Cnt', 'Pos', 'Tea', 'Tck']
    defensive_midfielder_su_pref_attributes = ['Sta', 'Str', 'Agg', 'Cmp', 'Dec', 'Wor', 'Fir', 'Mar', 'Pas']
    calculate_role_score(shortlist_attributes_df, defensive_midfielder_su_key_attributes,
                         defensive_midfielder_su_pref_attributes,
                         'defensive_midfielder_su_score')

    anchor_key_attributes = ['Ant', 'Cnt', 'Dec', 'Pos', 'Mar', 'Tck']
    anchor_pref_attributes = ['Str', 'Cmp', 'Tea']
    calculate_role_score(shortlist_attributes_df, anchor_key_attributes, anchor_pref_attributes,
                         'anchor_score')

    regista_key_attributes = ['Cmp', 'Dec', 'Fla', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    regista_pref_attributes = ['Bal', 'Ant', 'Dri', 'Lon']
    calculate_role_score(shortlist_attributes_df, regista_key_attributes, regista_pref_attributes,
                         'regista_score')

    ball_winning_midfielder_de_key_attributes = ['Sta', 'Agg', 'Ant', 'Tea', 'Wor', 'Tck']
    ball_winning_midfielder_de_pref_attributes = ['Agi', 'Pac', 'Str', 'Bra', 'Cnt', 'Pos', 'Mar']
    calculate_role_score(shortlist_attributes_df, ball_winning_midfielder_de_key_attributes,
                         ball_winning_midfielder_de_pref_attributes,
                         'ball_winning_midfielder_de_score')

    ball_winning_midfielder_su_key_attributes = ['Sta', 'Agg', 'Ant', 'Tea', 'Wor', 'Tck']
    ball_winning_midfielder_su_pref_attributes = ['Agi', 'Pac', 'Str', 'Bra', 'Cnt', 'Mar', 'Pas']
    calculate_role_score(shortlist_attributes_df, ball_winning_midfielder_su_key_attributes,
                         ball_winning_midfielder_su_pref_attributes,
                         'ball_winning_midfielder_su_score')

    deep_lying_playmaker_de_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    deep_lying_playmaker_de_pref_attributes = ['Bal', 'Ant', 'Pos', 'Tck']
    calculate_role_score(shortlist_attributes_df, deep_lying_playmaker_de_key_attributes,
                         deep_lying_playmaker_de_pref_attributes,
                         'deep_lying_playmaker_de_score')

    deep_lying_playmaker_su_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    deep_lying_playmaker_su_pref_attributes = ['Bal', 'Ant', 'OtB', 'Pos']
    calculate_role_score(shortlist_attributes_df, deep_lying_playmaker_su_key_attributes,
                         deep_lying_playmaker_su_pref_attributes,
                         'deep_lying_playmaker_su_score')

    roaming_playmaker_key_attributes = ['Acc', 'Sta', 'Ant', 'Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Wor', 'Fir', 'Pas',
                                        'Tec']
    roaming_playmaker_pref_attributes = ['Agi', 'Bal', 'Pac', 'Cnt', 'Pos', 'Dri', 'Lon']
    calculate_role_score(shortlist_attributes_df, roaming_playmaker_key_attributes, roaming_playmaker_pref_attributes,
                         'roaming_playmaker_score')

    # Central Midfielder role scores --------------------------------------------
    advanced_playmaker_su_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    advanced_playmaker_su_pref_attributes = ['Agi', 'Ant', 'Cnt', 'Fla', 'Dri']
    calculate_role_score(shortlist_attributes_df, advanced_playmaker_su_key_attributes,
                         advanced_playmaker_su_pref_attributes,
                         'advanced_playmaker_su_score')

    advanced_playmaker_at_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    advanced_playmaker_at_pref_attributes = ['Acc', 'Agi', 'Ant', 'Cnt', 'Fla', 'Dri']
    calculate_role_score(shortlist_attributes_df, advanced_playmaker_at_key_attributes,
                         advanced_playmaker_at_pref_attributes,
                         'advanced_playmaker_at_score')

    carrilero_key_attributes = ['Sta', 'Dec', 'Pos', 'Tea', 'Fir', 'Pas', 'Tck']
    carrilero_pref_attributes = ['Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor', 'Tec']
    calculate_role_score(shortlist_attributes_df, carrilero_key_attributes, carrilero_pref_attributes,
                         'carrilero_role_score')

    mezzala_su_key_attributes = ['Acc', 'Dec', 'OtB', 'Wor', 'Pas', 'Tec']
    mezzala_su_pref_attributes = ['Bal', 'Sta', 'Ant', 'Cmp', 'Vis', 'Dri', 'Fir', 'Lon', 'Tck']
    calculate_role_score(shortlist_attributes_df, mezzala_su_key_attributes, mezzala_su_pref_attributes,
                         'mezzala_su_score')

    mezzala_at_key_attributes = ['Acc', 'Dec', 'OtB', 'Vis', 'Wor', 'Dri', 'Pas', 'Tec']
    mezzala_at_pref_attributes = ['Bal', 'Sta', 'Ant', 'Cmp', 'Fla', 'Fin', 'Fir', 'Lon']
    calculate_role_score(shortlist_attributes_df, mezzala_at_key_attributes, mezzala_at_pref_attributes,
                         'mezzala_at_score')

    central_midfielder_de_key_attributes = ['Cnt', 'Dec', 'Pos', 'Tea', 'Tck']
    central_midfielder_de_pref_attributes = ['Sta', 'Agg', 'Ant', 'Cmp', 'Wor', 'Fir', 'Mar', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, central_midfielder_de_key_attributes,
                         central_midfielder_de_pref_attributes,
                         'central_midfielder_de_score')

    central_midfielder_su_key_attributes = ['Dec', 'Tea', 'Fir', 'Pas', 'Tck']
    central_midfielder_su_pref_attributes = ['Sta', 'Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor', 'Tec']
    calculate_role_score(shortlist_attributes_df, central_midfielder_su_key_attributes,
                         central_midfielder_su_pref_attributes,
                         'central_midfielder_su_score')

    central_midfielder_at_key_attributes = ['Dec', 'OtB', 'Fir', 'Pas']
    central_midfielder_at_pref_attributes = ['Acc', 'Sta', 'Ant', 'Cmp', 'Tea', 'Vis', 'Wor', 'Lon', 'Tck', 'Tec']
    calculate_role_score(shortlist_attributes_df, central_midfielder_at_key_attributes,
                         central_midfielder_at_pref_attributes,
                         'central_midfielder_at_score')

    central_midfielder_au_key_attributes = ['Dec', 'Tea', 'Fir', 'Pas', 'Tck']
    central_midfielder_au_pref_attributes = ['Sta', 'Ant', 'Cmp', 'Cnt', 'OtB', 'Vis', 'Wor', 'Tec']
    calculate_role_score(shortlist_attributes_df, central_midfielder_au_key_attributes,
                         central_midfielder_au_pref_attributes,
                         'central_midfielder_au_score')

    box_to_box_midfielder_key_attributes = ['Sta', 'OtB', 'Tea', 'Wor', 'Pas', 'Tck']
    box_to_box_midfielder_pref_attributes = ['Acc', 'Bal', 'Pac', 'Str', 'Agg', 'Ant', 'Cmp', 'Dec', 'Pos', 'Dri',
                                             'Fin', 'Fir', 'Lon', 'Tec']
    calculate_role_score(shortlist_attributes_df, box_to_box_midfielder_key_attributes,
                         box_to_box_midfielder_pref_attributes,
                         'box_to_box_midfielder_score')

    # Winger role scores --------------------------------------
    defensive_winger_de_key_attributes = ['Sta', 'Ant', 'OtB', 'Pos', 'Tea', 'Wor', 'Tec']
    defensive_winger_de_pref_attributes = ['Acc', 'Agg', 'Cnt', 'Dec', 'Cro', 'Dri', 'Fir', 'Mar', 'Tck']
    calculate_role_score(shortlist_attributes_df, defensive_winger_de_key_attributes,
                         defensive_winger_de_pref_attributes,
                         'defensive_winger_de_score')

    defensive_winger_su_key_attributes = ['Sta', 'OtB', 'Tea', 'Wor', 'Cro', 'Tec']
    defensive_winger_su_pref_attributes = ['Acc', 'Agg', 'Ant', 'Cmp', 'Cnt', 'Dec', 'Pos', 'Dri', 'Fir', 'Mar', 'Pas',
                                           'Tck']
    calculate_role_score(shortlist_attributes_df, defensive_winger_su_key_attributes,
                         defensive_winger_su_pref_attributes,
                         'defensive_winger_su_score')

    wide_midfielder_de_key_attributes = ['Cnt', 'Dec', 'Pos', 'Tea', 'Wor', 'Pas', 'Tck']
    wide_midfielder_de_pref_attributes = ['Sta', 'Ant', 'Cmp', 'Cro', 'Fir', 'Mar', 'Tec']
    calculate_role_score(shortlist_attributes_df, wide_midfielder_de_key_attributes, wide_midfielder_de_pref_attributes,
                         'wide_midfielder_de_score')

    wide_midfielder_su_key_attributes = ['Sta', 'Dec', 'Tea', 'Wor', 'Pas', 'Tck']
    wide_midfielder_su_pref_attributes = ['Ant', 'Cmp', 'Cnt', 'OtB', 'Pos', 'Vis', 'Cro', 'Fir', 'Tec']
    calculate_role_score(shortlist_attributes_df, wide_midfielder_su_key_attributes, wide_midfielder_su_pref_attributes,
                         'wide_midfielder_su_score')

    wide_midfielder_at_key_attributes = ['Sta', 'Dec', 'Tea', 'Wor', 'Cro', 'Fir', 'Pas']
    wide_midfielder_at_pref_attributes = ['Ant', 'Cmp', 'OtB', 'Vis', 'Tck', 'Tec']
    calculate_role_score(shortlist_attributes_df, wide_midfielder_at_key_attributes, wide_midfielder_at_pref_attributes,
                         'wide_midfielder_at_score')

    wide_midfielder_au_key_attributes = ['Sta', 'Dec', 'Tea', 'Wor', 'Pas', 'Tck']
    wide_midfielder_au_pref_attributes = ['Ant', 'Cmp', 'Cnt', 'OtB', 'Pos', 'Vis', 'Cro', 'Fir', 'Tec']
    calculate_role_score(shortlist_attributes_df, wide_midfielder_au_key_attributes, wide_midfielder_au_pref_attributes,
                         'wide_midfielder_au_score')

    wide_playmaker_su_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Fir', 'Pas', 'Tec']
    wide_playmaker_su_pref_attributes = ['Agi', 'OtB', 'Dri']
    calculate_role_score(shortlist_attributes_df, wide_playmaker_su_key_attributes, wide_playmaker_su_pref_attributes,
                         'wide_playmaker_su_score')

    wide_playmaker_at_key_attributes = ['Cmp', 'Dec', 'Tea', 'Vis', 'Dri', 'Fir', 'Pas', 'Tec']
    wide_playmaker_at_pref_attributes = ['Acc', 'Agi', 'Ant', 'Fla']
    calculate_role_score(shortlist_attributes_df, wide_playmaker_at_key_attributes, wide_playmaker_at_pref_attributes,
                         'wide_playmaker_at_score')

    inverted_winger_su_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Pas', 'Tec']
    inverted_winger_su_pref_attributes = ['Bal', 'Pac', 'Sta', 'Cmp', 'Dec', 'OtB', 'Vis', 'Wor', 'Fir', 'Lon']
    calculate_role_score(shortlist_attributes_df, inverted_winger_su_key_attributes, inverted_winger_su_pref_attributes,
                         'inverted_winger_su_score')

    inverted_winger_at_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Pas', 'Tec']
    inverted_winger_at_pref_attributes = ['Bal', 'Pac', 'Sta', 'Ant', 'Cmp', 'Dec', 'Fla', 'OtB', 'Vis', 'Wor', 'Fir',
                                          'Lon']
    calculate_role_score(shortlist_attributes_df, inverted_winger_at_key_attributes, inverted_winger_at_pref_attributes,
                         'inverted_winger_at_score')

    winger_su_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Tec']
    winger_su_pref_attributes = ['Bal', 'Pac', 'Sta', 'OtB', 'Wor', 'Fir', 'Pas']
    calculate_role_score(shortlist_attributes_df, winger_su_key_attributes, winger_su_pref_attributes,
                         'winger_su_score')

    winger_at_key_attributes = ['Acc', 'Agi', 'Cro', 'Dri', 'Tec']
    winger_at_pref_attributes = ['Bal', 'Pac', 'Sta', 'Ant', 'Fla', 'OtB', 'Wor', 'Fir', 'Pas']
    calculate_role_score(shortlist_attributes_df, winger_at_key_attributes, winger_at_pref_attributes,
                         'winger_at_score')

    inside_forward_su_key_attributes = ['Acc', 'Agi', 'OtB', 'Dri', 'Fin', 'Fir', 'Tec']
    inside_forward_su_pref_attributes = ['Bal', 'Pac', 'Sta', 'Ant', 'Cmp', 'Fla', 'Vis', 'Wor', 'Lon', 'Pas']
    calculate_role_score(shortlist_attributes_df, inside_forward_su_key_attributes, inside_forward_su_pref_attributes,
                         'inside_forward_su_score')

    inside_forward_at_key_attributes = ['Acc', 'Agi', 'Ant', 'OtB', 'Dri', 'Fin', 'Fir', 'Tec']
    inside_forward_at_pref_attributes = ['Bal', 'Pac', 'Sta', 'Cmp', 'Fla', 'Wor', 'Lon', 'Pas']
    calculate_role_score(shortlist_attributes_df, inside_forward_at_key_attributes, inside_forward_at_pref_attributes,
                         'inside_forward_at_score')

    raumdeuter_key_attributes = ['Bal', 'Ant', 'Cmp', 'Cnt', 'Dec', 'OtB', 'Fin']
    raumdeuter_pref_attributes = ['Acc', 'Sta', 'Wor', 'Fir', 'Tec']
    calculate_role_score(shortlist_attributes_df, raumdeuter_key_attributes, raumdeuter_pref_attributes,
                         'raumdeuter_score')

    wide_target_forward_su_key_attributes = ['Jum', 'Str', 'Bra', 'Tea', 'Hea']
    wide_target_forward_su_pref_attributes = ['Bal', 'Sta', 'Ant', 'OtB', 'Wor', 'Cro', 'Fir']
    calculate_role_score(shortlist_attributes_df, wide_target_forward_su_key_attributes,
                         wide_target_forward_su_pref_attributes,
                         'wide_target_forward_su_score')

    wide_target_forward_at_key_attributes = ['Jum', 'Str', 'Bra', 'OtB', 'Hea']
    wide_target_forward_at_pref_attributes = ['Bal', 'Sta', 'Ant', 'Tea', 'Wor', 'Cro', 'Fin', 'Fir']
    calculate_role_score(shortlist_attributes_df, wide_target_forward_at_key_attributes,
                         wide_target_forward_at_pref_attributes,
                         'wide_target_forward_at_score')

    trequartista_key_attributes = ['Acc', 'Cmp', 'Dec', 'Fla', 'OtB', 'Vis', 'Dri', 'Fir', 'Pas', 'Tec']
    trequartista_pref_attributes = ['Agi', 'Bal', 'Ant', 'Fin']
    calculate_role_score(shortlist_attributes_df, trequartista_key_attributes, trequartista_pref_attributes,
                         'trequartista_score')

    enganche_key_attributes = ['Cmp', 'Dec', 'Vis', 'Fir', 'Pas', 'Tec']
    enganche_pref_attributes = ['Agi', 'Ant', 'Fla', 'OtB', 'Tea', 'Dri']
    calculate_role_score(shortlist_attributes_df, enganche_key_attributes, enganche_pref_attributes,
                         'enganche_score')

    attacking_midfielder_su_key_attributes = ['Ant', 'Dec', 'Fla', 'OtB', 'Fir', 'Lon', 'Pas', 'Tec']
    attacking_midfielder_su_pref_attributes = ['Agi', 'Cmp', 'Vis', 'Dri']
    calculate_role_score(shortlist_attributes_df, attacking_midfielder_su_key_attributes,
                         attacking_midfielder_su_pref_attributes,
                         'attacking_midfielder_su_score')

    attacking_midfielder_at_key_attributes = ['Ant', 'Dec', 'Fla', 'OtB', 'Fir', 'Lon', 'Pas', 'Tec', 'Dri']
    attacking_midfielder_at_pref_attributes = ['Agi', 'Cmp', 'Vis', 'Fin']
    calculate_role_score(shortlist_attributes_df, attacking_midfielder_at_key_attributes,
                         attacking_midfielder_at_pref_attributes,
                         'attacking_midfielder_at_score')

    shadow_striker_key_attributes = ['Acc', 'Ant', 'Cmp', 'OtB', 'Dri', 'Fin', 'Fir']
    shadow_striker_pref_attributes = ['Agi', 'Bal', 'Pac', 'Sta', 'Cnt', 'Dec', 'Wor', 'Pas', 'Tec']
    calculate_role_score(shortlist_attributes_df, shadow_striker_key_attributes, shadow_striker_pref_attributes,
                         'shadow_striker_score')

    advanced_forward_key_attributes = ['Acc', 'Cmp', 'OtB', 'Dri', 'Fin', 'Fir', 'Tec']
    advanced_forward_pref_attributes = ['Agi', 'Bal', 'Pac', 'Sta', 'Ant', 'Dec', 'Wor', 'Pas']
    calculate_role_score(shortlist_attributes_df, advanced_forward_key_attributes, advanced_forward_pref_attributes,
                         'advanced_forward_score')

    poacher_key_attributes = ['Ant', 'Cmp', 'OtB', 'Fin']
    poacher_pref_attributes = ['Acc', 'Dec', 'Fir', 'Hea', 'Tec']
    calculate_role_score(shortlist_attributes_df, poacher_key_attributes, poacher_pref_attributes,
                         'poacher_score')

    false_nine_key_attributes = ['Acc', 'Agi', 'Cmp', 'Dec', 'OtB', 'Vis', 'Dri', 'Fir', 'Pas', 'Tec']
    false_nine_pref_attributes = ['Bal', 'Ant', 'Fla', 'Tea', 'Fin']
    calculate_role_score(shortlist_attributes_df, false_nine_key_attributes, false_nine_pref_attributes,
                         'false_nine_score')

    target_forward_su_key_attributes = ['Bal', 'Jum', 'Str', 'Bra', 'Tea', 'Hea']
    target_forward_su_pref_attributes = ['Agg', 'Ant', 'Cmp', 'Dec', 'OtB', 'Fin', 'Fir']
    calculate_role_score(shortlist_attributes_df, target_forward_su_key_attributes, target_forward_su_pref_attributes,
                         'target_forward_su_score')

    target_forward_at_key_attributes = ['Bal', 'Jum', 'Str', 'Bra', 'Cmp', 'OtB', 'Fin', 'Hea']
    target_forward_at_pref_attributes = ['Agg', 'Ant', 'Dec', 'Tea', 'Fir']
    calculate_role_score(shortlist_attributes_df, target_forward_at_key_attributes, target_forward_at_pref_attributes,
                         'target_forward_at_score')

    deep_lying_forward_su_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Fir', 'Pas', 'Tec']
    deep_lying_forward_su_pref_attributes = ['Bal', 'Str', 'Ant', 'Fla', 'Vis', 'Fin']
    calculate_role_score(shortlist_attributes_df, deep_lying_forward_su_key_attributes,
                         deep_lying_forward_su_pref_attributes,
                         'deep_lying_forward_su_score')

    deep_lying_forward_at_key_attributes = ['Cmp', 'Dec', 'OtB', 'Tea', 'Fir', 'Pas', 'Tec']
    deep_lying_forward_at_pref_attributes = ['Bal', 'Str', 'Ant', 'Fla', 'Vis', 'Dri', 'Fin']
    calculate_role_score(shortlist_attributes_df, deep_lying_forward_at_key_attributes,
                         deep_lying_forward_at_pref_attributes,
                         'deep_lying_forward_at_score')

    pressing_forward_de_key_attributes = ['Acc', 'Pac', 'Sta', 'Agg', 'Ant', 'Bra', 'Dec', 'Tea', 'Wor']
    pressing_forward_de_pref_attributes = ['Agi', 'Bal', 'Str', 'Cmp', 'Cnt', 'Fir']
    calculate_role_score(shortlist_attributes_df, pressing_forward_de_key_attributes,
                         pressing_forward_de_pref_attributes,
                         'pressing_forward_de_score')

    pressing_forward_su_key_attributes = ['Acc', 'Pac', 'Sta', 'Agg', 'Ant', 'Bra', 'Dec', 'Tea', 'Wor']
    pressing_forward_su_pref_attributes = ['Agi', 'Bal', 'Str', 'Cmp', 'Cnt', 'OtB', 'Fir', 'Pas']
    calculate_role_score(shortlist_attributes_df, pressing_forward_su_key_attributes,
                         pressing_forward_su_pref_attributes,
                         'pressing_forward_su_score')

    pressing_forward_at_key_attributes = ['Acc', 'Pac', 'Sta', 'Agg', 'Ant', 'Bra', 'OtB', 'Tea', 'Wor']
    pressing_forward_at_pref_attributes = ['Agi', 'Bal', 'Str', 'Cmp', 'Cnt', 'Dec', 'Fin', 'Fir']
    calculate_role_score(shortlist_attributes_df, pressing_forward_at_key_attributes,
                         pressing_forward_at_pref_attributes,
                         'pressing_forward_at_score')

    complete_forward_su_key_attributes = ['Acc', 'Agi', 'Str', 'Ant', 'Cmp', 'Dec', 'OtB', 'Vis', 'Dri', 'Fir', 'Hea',
                                          'Lon', 'Pas', 'Tec']
    complete_forward_su_pref_attributes = ['Bal', 'Jum', 'Pac', 'Sta', 'Tea', 'Wor', 'Fin']
    calculate_role_score(shortlist_attributes_df, complete_forward_su_key_attributes,
                         complete_forward_su_pref_attributes,
                         'complete_forward_su_score')

    complete_forward_at_key_attributes = ['Acc', 'Agi', 'Str', 'Ant', 'Cmp', 'OtB', 'Dri', 'Fin', 'Fir', 'Hea', 'Tec']
    complete_forward_at_pref_attributes = ['Bal', 'Jum', 'Pac', 'Sta', 'Dec', 'Tea', 'Vis', 'Wor', 'Lon', 'Pas']
    calculate_role_score(shortlist_attributes_df, complete_forward_at_key_attributes,
                         complete_forward_at_pref_attributes,
                         'complete_forward_at_score')

    return shortlist_attributes_df
