# Variables to share across app pages

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


# Attribute filters
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
    'Striker': ['Name', 'Age', 'Position', 'Club', 'Division', 'Dri', 'Fin', 'Fir', 'Tec', 'Cmp', 'OtB', 'Acc', 'Jum', 'Pac'],
    # Role Score Filters
    'Goalkeeper - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'goalkeeper_score', 'sweeper_keeper_de_score', 'sweeper_keeper_su_score', 'sweeper_keeper_at_score'
    ],
    'Central Defender - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'central_def_de_score', 'central_def_st_score', 'central_def_co_score', 'no_nonsense_cb_de_score',
        'no_nonsense_cb_st_score', 'no_nonsense_cb_co_score', 'wide_cb_de_score', 'wide_cb_su_score',
        'wide_cb_at_score', 'ball_playing_def_de_score', 'ball_playing_def_st_score', 'ball_playing_def_co_score',
        'libero_de_score', 'libero_su_score'
    ],
    'Full-back & Wing-back - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'fullback_de_score', 'fullback_su_score', 'fullback_at_score', 'fullback_au_score', 'no_nonsense_fb_score',
        'inverted_fb_score', 'wingback_de_score', 'wingback_su_score', 'wingback_at_score', 'wingback_au_score',
        'complete_wingback_su_score', 'complete_wingback_at_score', 'inverted_wb_de_score', 'inverted_wb_su_score',
        'inverted_wb_at_score'
    ],
    'Defensive Midfielder - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'anchor_score', 'half_back_score', 'defensive_midfielder_de_score', 'defensive_midfielder_su_score',
        'segundo_volante_su_score', 'segundo_volante_at_score', 'regista_score', 'ball_winning_midfielder_de_score',
        'ball_winning_midfielder_su_score', 'deep_lying_playmaker_de_score', 'deep_lying_playmaker_su_score',
        'roaming_playmaker_score'
    ],
    'Central Midfielder - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'ball_winning_midfielder_de_score', 'ball_winning_midfielder_su_score', 'deep_lying_playmaker_de_score',
        'deep_lying_playmaker_su_score', 'roaming_playmaker_score', 'carrilero_role_score', 'box_to_box_midfielder_score',
        'central_midfielder_de_score', 'central_midfielder_su_score', 'central_midfielder_at_score',
        'central_midfielder_au_score', 'mezzala_su_score', 'mezzala_at_score', 'advanced_playmaker_su_score',
        'advanced_playmaker_at_score'
    ],
    'Winger - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'defensive_winger_de_score', 'defensive_winger_su_score', 'wide_midfielder_de_score',
       'wide_midfielder_su_score', 'wide_midfielder_at_score', 'wide_midfielder_au_score',
       'wide_playmaker_su_score', 'wide_playmaker_at_score', 'inverted_winger_su_score',
       'inverted_winger_at_score', 'winger_su_score', 'winger_at_score', 'inside_forward_su_score',
       'inside_forward_at_score', 'raumdeuter_score', 'wide_target_forward_su_score',
       'wide_target_forward_at_score',
    ],
    'Attacking Midfielder - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'advanced_playmaker_su_score', 'advanced_playmaker_at_score', 'trequartista_score', 'enganche_score',
        'attacking_midfielder_su_score', 'attacking_midfielder_at_score', 'shadow_striker_score'
    ],
    'Striker - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'advanced_forward_score', 'poacher_score', 'false_nine_score', 'target_forward_su_score',
        'target_forward_at_score', 'deep_lying_forward_su_score', 'deep_lying_forward_at_score',
        'pressing_forward_de_score', 'pressing_forward_su_score', 'pressing_forward_at_score',
        'complete_forward_su_score', 'complete_forward_at_score'
    ]
}


# Negative stat categories
negative_stat_categories = ['Poss Lost/90', 'Hdrs L/90', 'Gl Mst', 'Conc', 'Con/90', 'Off', 'Fls', 'Yel', 'Red', 'Tcon', 'Tcon/90',
                            'Lost', 'G. Mis', 'Int Conc']


# Stats label dictionary to convert fm metric codenames to full names of the stat category

stats_label_dict = {'Name': 'Name', 'Age': 'Age', 'Position': 'Position', 'Club': 'Club', 'Division': 'Division',
                        'Transfer Value': 'Transfer Value', 'Wage': 'Wage', 'Transfer Status': 'Transfer Status',
                        'Av Rat': 'Average Rating', 'Gls': 'Goals', 'Gls/90': 'Goals per 90 minutes',
                        'Goals Outside Box': 'Goals from Outside the Box', 'Ast': 'Assists',
                        'Asts/90': 'Assists per 90 minutes', 'CCC': 'Overall number of chances created',
                        'Ch C/90': 'Chances Created per 90 minutes', 'Shots': 'Shots', 'Shot/90': 'Shots per 90 minutes',
                        'ShT': 'Shots on Target', 'ShT/90': 'Shots on Target per 90 minutes',
                        'Shot %': 'Shots On Target Ratio',
                        'Shots Outside Box/90': 'Shots from Outside the Box per 90 minutes',
                        'FK Shots': 'Free Kick Shots', 'xG': 'xG - Expected Goals',
                        'xG/90': 'xG/90 - Expected Goals per 90 minutes',
                        'xG/shot': 'xG/Shot - Expected Goals per Shot',
                        'xG-OP': 'xG OP - Expected Goals Overperformance',
                        'NP-xG': 'NP xG - Non Penalty Expected Goals',
                        'NP-xG/90': 'NP xG/90 - Non Penalty Expected Goals per 90 minutes',
                        'Conv %': 'Goal Conversion Rate', 'Pens': 'Penalties Taken', 'Pens S': 'Penalties Scored',
                        'Pen/R': 'Penalties Scored Ratio', 'Ps C': 'Passes Completed',
                        'Ps C/90': 'Passes Completed per 90 minutes', 'Pas A': 'Passes Attempted',
                        'Ps A/90': 'Passes Attempted per 90 minutes', 'Pas %': 'Pass Completion Ratio',
                        'Pr Passes': 'Progressive Passes', 'Pr passes/90': 'Progressive Passes per 90 minutes',
                        'K Pas': 'Key Passes', 'K Ps/90': 'Key Passes per 90 minutes', 'xA': 'xA - Expected Assists',
                        'xA/90': 'xA/90 - Expected Assists per 90 minutes', 'Sprints/90': 'Sprints per 90 minutes',
                        'Drb': 'Dribbles Made', 'Drb/90': 'Dribbles Made per 90 minutes',
                        'Distance': 'Distance Covered', 'Cr C': 'Crosses Completed',
                        'Cr C/90': 'Crosses Completed per 90 minutes', 'Cr A': 'Crosses Attempted',
                        'Crs A/90': 'Crosses Attempted per 90 minutes', 'Cr C/A': 'Cross Completion Ratio',
                        'OP-KP': 'Open Play Key Passes', 'OP-KP/90': 'Open Play Key Passes per 90 minutes',
                        'OP-Crs C': 'Open Play Crosses Completed',
                        'OP-Crs C/90': 'Open Play Crosses Completed per 90 minutes',
                        'OP-Crs A': 'Open Play Crosses Attempted',
                        'OP-Crs A/90': 'Open Play Crosses Attempted per 90 minutes',
                        'OP-Cr %': 'Open Play Cross Completion Ratio', 'Pres C': 'Pressures Completed',
                        'Pres C/90': 'Pressures Completed per 90 minutes', 'Pres A': 'Pressures Attempted',
                        'Pres A/90': 'Pressures Attempted per 90 minutes',
                        'Poss Won/90': 'Possessions Won per 90 minutes',
                        'Poss Lost/90': 'Possessions Lost per 90 minutes', 'Tck C': 'Tackles Completed',
                        'Tck/90': 'Tackles Completed per 90 minutes', 'Tck A': 'Tackles Attempted',
                        'Tck R': 'Tackle Completion Ratio', 'K Tck': 'Key Tackles',
                        'K Tck/90': 'Key Tackles per 90 minutes', 'Hdrs': 'Headers Won',
                        'Hdrs W/90': 'Headers Won per 90 minutes', 'Hdrs A': 'Headers Attempted',
                        'Aer A/90': 'Headers Attempted per 90 minutes', 'Hdr %': 'Headers Won Ratio',
                        'Hdrs L/90': 'Headers Lost per 90 minutes', 'K Hdrs/90': 'Key Headers per 90 minutes',
                        'Blk': 'Blocks', 'Blk/90': 'Blocks per 90 minutes', 'Shts Blckd': 'Shots Blocked',
                        'Shts Blckd/90': 'Shots Blocked per 90 minutes', 'Clear': 'Clearances',
                        'Clr/90': 'Clearances per 90 minutes', 'Itc': 'Interceptions',
                        'Int/90': 'Interceptions per 90 minutes', 'Gl Mst': 'Mistakes Leading to Goal',
                        'Clean Sheets': 'Clean Sheets', 'Cln/90': 'Clean Sheets per 90 minutes',
                        'Saves/90': 'Saves per 90 minutes', 'Svt': 'Saves Tipped', 'Svp': 'Saves Parried',
                        'Svh': 'Saves Held', 'Sv %': 'Save Ratio', 'xSv %': 'xSv Ratio - Expected Save Ratio',
                        'xGP': 'xGP - Expected Goals Prevented',
                        'xGP/90': 'xGP/90 - Expected Goals Prevented per 90 minutes', 'Pens Saved': 'Penalties Saved',
                        'Pens Faced': 'Penalties Faced', 'Pens Saved Ratio': 'Penalties Saved Ratio',
                        'Conc': 'Goals Conceded', 'Con/90': 'Goals Conceded per 90 minutes', 'Off': 'Offsides',
                        'Fls': 'Fouls Committed', 'FA': 'Fouls Against', 'Yel': 'Yellow Cards', 'Red': 'Red Cards',
                        'Pts/Gm': 'Points Won per Game', 'Tgls': 'Team Goals', 'Tgls/90': 'Team Goals per 90 minutes',
                        'Tcon': 'Team Goals Conceded', 'Tcon/90': 'Team Goals Conceded per 90 minutes',
                        'Won': 'Games Won', 'D': 'Games Drawn', 'Lost': 'Games Lost', 'Gwin': 'Game Win Ratio',
                        'Apps': 'Appearances', 'Starts': 'Starting Appearances', 'Mins': 'Minutes',
                        'G. Mis': 'Games Missed in a Row', 'PoM': 'Player of the Match',
                        'Int Apps': 'International Appearances (current season)',
                        'Int Ast': 'International Assists (current season)',
                        'Int Conc': 'International Goals Conceded (current season)',
                        'Int Av Rat': 'International Average Rating (current season)'}

# Preset Stats Radar Chart Values for users to toggle on dropdown menu
preset_radar_values = {
    'Goalkeeper': ['Apps', 'Av Rat', 'xSv %', 'xGP/90', 'Pens Saved Ratio', 'PoM', 'Saves/90', 'Clr/90', 'Pas %', 'Ps C/90', 'Sv %', 'Svh', 'Svp', 'Svt', 'Cln/90', 'Con/90'],
    'Central Defender': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Shts Blckd/90', 'Pr passes/90', 'Poss Won/90', 'Ps C/90', 'Pas %', 'Int/90', 'Hdrs W/90', 'Hdr %', 'Clr/90', 'Blk/90', 'Yel'],
    'Full-back': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Poss Won/90', 'Poss Lost/90', 'Ps C/90', 'Pas %', 'Int/90', 'Distance', 'Cr C/90', 'Cr C/A', 'Fls', 'Yel'],
    'Wing-Back': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Poss Won/90', 'Poss Lost/90', 'Pas %', 'Int/90', 'Distance', 'Cr C/90', 'Cr C/A', 'OP-Crs C/90', 'Ch C/90', 'Asts/90', 'Drb/90', 'Sprints/90'],
    'Defensive Midfielder': ['Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Pr passes/90', 'Poss Won/90', 'Poss Lost/90', 'Ps C/90', 'Pas %', 'K Ps/90', 'Int/90', 'Pres C/90', 'Hdrs W/90', 'Hdr %',],
    'Central Midfielder': ['Apps', 'Av Rat', 'Tck/90', 'Int/90', 'Pr passes/90', 'Poss Won/90', 'Poss Lost/90', 'Pas %', 'K Ps/90', 'Distance', 'Ch C/90', 'Asts/90', 'Pres C/90', 'ShT/90'],
    'Attacking Midfielder': ['Apps', 'Av Rat', 'Pas %', 'Ch C/90', 'Asts/90', 'xA/90', 'Poss Lost/90', 'K Ps/90', 'OP-KP/90', 'Drb/90', 'xG/shot', 'Gls/90', 'xG/90'],
    'Winger': ['Apps', 'Av Rat', 'Poss Lost/90', 'Pres C/90', 'Drb/90', 'Sprints/90', 'FA', 'Ch C/90', 'OP-KP/90', 'Cr C/90', 'Cr C/A', 'OP-Crs C/90', 'xG/shot', 'Gls/90', 'xG/90'],
    'Striker': ['Apps', 'Av Rat', 'Pres C/90', 'Poss Won/90', 'ShT/90', 'Shot %', 'Sprints/90', 'Hdrs W/90', 'Hdr %', 'xG/shot', 'Conv %', 'Asts/90', 'NP-xG/90', 'Gls/90', 'xG/90'],
    'Custom': []
}

# Sample charts for quick access to interesting data in the user's FM file
sample_charts = {
    'Top Strikers': {
        'Position': 'ST',
        'top10': ['Av Rat', 'Gls', 'Gls/90', 'xG/90', 'NP-xG/90', 'ShT/90'],
        'X': 'Gls',
        'Y': 'Av Rat'
    },
    'Top Wingers': {
        'Position': ['AM (R)', 'AM (L)'],
        'top10': ['Av Rat', 'Gls', 'Gls/90', 'xG/90', 'Ast', 'Asts/90', 'xA/90', 'Drb/90', 'Ch C/90', 'K Ps/90', 'Cr C/90', 'OP-KP/90', 'OP-Crs C/90'],
        'X': 'Sprints/90',
        'Y': 'Poss Lost/90'
    },
    'Top Attacking Midfielders': {
        'Position': 'AM (C)',
        'top10': ['Av Rat', 'Gls', 'Gls/90', 'Goals Outside Box', 'xG/90', 'Ast', 'Asts/90', 'xA/90', 'CCC', 'Ch C/90', 'K Ps/90', 'OP-KP/90'],
        'X': 'Ch C/90',
        'Y': 'Poss Lost/90'
    },
    'Top Central Midfielders': {
        'Position': 'M (C)',
        'top10': ['Av Rat', 'Ast', 'Asts/90', 'xA/90', 'CCC', 'Ch C/90', 'K Ps/90', 'OP-KP/90', 'Poss Won/90', 'Ps C/90', 'Pas %'],
        'X': 'Distance',
        'Y': 'ShT/90'
    },
    'Top Defensive Midfielders': {
        'Position': 'DM',
        'top10': ['Av Rat', 'K Ps/90', 'OP-KP/90', 'Poss Won/90', 'Pres C/90', 'Tck/90', 'Int/90', 'Ps C/90', 'Pas %'],
        'X': 'Poss Won/90',
        'Y': 'Pr passes/90'
    },
    'Top Wing-Backs': {
        'Position': ['WB (R)', 'WB (L)'],
        'top10': ['Av Rat', 'Ast', 'Asts/90', 'xA/90', 'Drb/90', 'CCC', 'Ch C/90', 'K Ps/90', 'Cr C/90', 'OP-KP/90', 'OP-Crs C/90', 'Poss Won/90', 'Tck/90', 'Int/90'],
        'X': 'Sprints/90',
        'Y': 'Cr C/90'
    },
    'Top Full-Backs': {
        'Position': ['D (R)', 'D (L)'],
        'top10': ['Av Rat', 'Cr C/90', 'OP-KP/90', 'OP-Crs C/90', 'Poss Won/90', 'Tck/90', 'K Tck/90', 'Int/90', 'Blk/90'],
        'X': 'Distance',
        'Y': 'Sprints/90'
    },
    'Top Central Defenders': {
        'Position': 'D (C)',
        'top10': ['Av Rat', 'Tck/90', 'K Tck/90', 'Int/90', 'Shts Blckd/90', 'Hdrs W/90', 'K Hdrs/90'],
        'X': 'Distance',
        'Y': 'Hdr %'
    },
    'Top Goalkeepers': {
        'Position': 'GK',
        'top10': ['Av Rat', 'Clean Sheets', 'Cln/90', 'Saves/90', 'Sv %'],
        'X': 'Clean Sheets',
        'Y': 'Saves/90'
    }
}