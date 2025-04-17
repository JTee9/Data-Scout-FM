# Todo -----------------------------------
# 1. Complete position filter updates for all languages
# 2. Expand stats_label_dict to include other languages

# Variables to share across app pages

# Dictionary to check user's language preference with language_key('Wage' in the user's language)
language_dict = {
    'Wage': 'English',
    'Salary': 'English (US)',
    '給与': 'Japanese',
    '급료': 'Korean',
    'Sueldo': 'Spanish',
    'Stipendio': 'Italian',
    'Salaire': 'French',
    'Gehalt': 'German',
    'Salário': 'Portuguese',
    'Salaris': 'Dutch',
    'Løn': 'Danish',
    'Lønn': 'Norwegian',
    'Lön': 'Swedish',
    '工资': 'Chinese',
    'Płaca': 'Polish',
    'Maaş': 'Turkish',
    'Απολαβές': 'Greek',
    'Зарплата': 'Russian'
}

# Position filters
international_position_filters = {
        'English': {
            'GK': ['GK'],
            'D (C)': ['D (C)', 'D (RC)', 'D (LC)', 'D (RLC)'],
            'D (R)': ['D (R)', 'D (RL)', 'D (RC)', 'D (RLC)',
                      'D/WB (R)', 'D/WB (RL)',
                      'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)'],
            'D (L)': ['D (L)', 'D (RL)', 'D (LC)', 'D (RLC)',
                      'D/WB (L)', 'D/WB (RL)',
                      'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)'],
            'WB (R)': ['D/WB (R)', 'D/WB (RL)',
                       'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                       'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'WB (R)', 'WB (RL)',
                       'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'],
            'WB (L)': ['D/WB (L)', 'D/WB (RL)',
                       'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                       'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'WB (L)', 'WB (RL)',
                       'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'],
            'M (R)': ['D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                      'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                      'M (R)', 'M (RL)', 'M (RC)', 'M (RLC)',
                      'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)'],
            'M (L)': ['D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                      'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                      'M (L)', 'M (RL)', 'M (LC)', 'M (RLC)',
                      'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)'],
            'DM': ['DM'],
            'M (C)': ['M (C)', 'M (RC)', 'M (LC)', 'M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)'],
            'AM (C)': ['M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (C)', 'AM (RC)', 'AM (LC)', 'AM (RLC)'],
            'AM (R)': ['D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                       'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'
                       'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)',
                       'AM (R)', 'AM (RL)', 'AM (RC)', 'AM (RLC)'],
            'AM (L)': ['D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                       'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'
                       'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (L)', 'AM (RL)', 'AM (LC)', 'AM (RLC)'],
            'ST': ['ST (C)']
        },
        'English (US)': {
            'GK': ['GK'],
            'D (C)': ['D (C)', 'D (RC)', 'D (LC)', 'D (RLC)'],
            'D (R)': ['D (R)', 'D (RL)', 'D (RC)', 'D (RLC)',
                      'D/WB (R)', 'D/WB (RL)',
                      'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)'],
            'D (L)': ['D (L)', 'D (RL)', 'D (LC)', 'D (RLC)',
                      'D/WB (L)', 'D/WB (RL)',
                      'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)'],
            'WB (R)': ['D/WB (R)', 'D/WB (RL)',
                       'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                       'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'WB (R)', 'WB (RL)',
                       'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'],
            'WB (L)': ['D/WB (L)', 'D/WB (RL)',
                       'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                       'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'WB (L)', 'WB (RL)',
                       'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'],
            'M (R)': ['D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                      'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                      'M (R)', 'M (RL)', 'M (RC)', 'M (RLC)',
                      'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)'],
            'M (L)': ['D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                      'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                      'M (L)', 'M (RL)', 'M (LC)', 'M (RLC)',
                      'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)'],
            'DM': ['DM'],
            'M (C)': ['M (C)', 'M (RC)', 'M (LC)', 'M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)'],
            'AM (C)': ['M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (C)', 'AM (RC)', 'AM (LC)', 'AM (RLC)'],
            'AM (R)': ['D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                       'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'
                       'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)',
                       'AM (R)', 'AM (RL)', 'AM (RC)', 'AM (RLC)'],
            'AM (L)': ['D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                       'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'
                       'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (L)', 'AM (RL)', 'AM (LC)', 'AM (RLC)'],
            'ST': ['ST (C)']
        },
        'Japanese': {
            'GK': ['GK'],
            'DF (C)': ['DF (C)', 'DF (RC)', 'DF (LC)', 'DF (RLC)'],
            'DF (R)': ['DF (R)', 'DF (RL)', 'DF (RC)', 'DF (RLC)',
                       'DF/WB (R)', 'DF/WB (RL)',
                       'DF/WB/MF (R)', 'DF/WB/MF (RL)', 'DF/WB/MF (RC)', 'DF/WB/MF (RLC)',
                       'DF/WB/AM (R)', 'DF/WB/AM (RL)', 'DF/WB/AM (RC)', 'DF/WB/AM (RLC)',
                       'DF/WB/MF/AM (R)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (RC)', 'DF/WB/MF/AM (RLC)',
                       'DF/MF (R)', 'DF/MF (RL)', 'DF/MF (RC)', 'DF/MF (RLC)',
                       'DF/MF/AM (R)', 'DF/MF/AM (RL)', 'DF/MF/AM (RC)', 'DF/MF/AM (RLC)',
                       'DF/AM (R)', 'DF/AM (RL)', 'DF/AM (RC)', 'DF/AM (RLC)'],
            'DF (L)': ['DF (L)', 'DF (RL)', 'DF (LC)', 'DF (RLC)',
                       'DF/WB (L)', 'DF/WB (RL)',
                       'DF/WB/MF (L)', 'DF/WB/MF (RL)', 'DF/WB/MF (LC)', 'DF/WB/MF (RLC)',
                       'DF/WB/AM (L)', 'DF/WB/AM (RL)', 'DF/WB/AM (LC)', 'DF/WB/AM (RLC)',
                       'DF/WB/MF/AM (L)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (LC)', 'DF/WB/MF/AM (RLC)',
                       'DF/MF (L)', 'DF/MF (RL)', 'DF/MF (LC)', 'DF/MF (RLC)',
                       'DF/MF/AM (L)', 'DF/MF/AM (RL)', 'DF/MF/AM (LC)', 'DF/MF/AM (RLC)',
                       'DF/AM (L)', 'DF/AM (RL)', 'DF/AM (LC)', 'DF/AM (RLC)'],
            'WB (R)': ['DF/WB (R)', 'DF/WB (RL)',
                       'DF/WB/MF (R)', 'DF/WB/MF (RL)', 'DF/WB/MF (RC)', 'DF/WB/MF (RLC)',
                       'DF/WB/AM (R)', 'DF/WB/AM (RL)', 'DF/WB/AM (RC)', 'DF/WB/AM (RLC)',
                       'DF/WB/MF/AM (R)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (RC)', 'DF/WB/MF/AM (RLC)',
                       'WB (R)', 'WB (RL)',
                       'WB/MF (R)', 'WB/MF (RL)', 'WB/MF (RC)', 'WB/MF (RLC)',
                       'WB/MF/AM (R)', 'WB/MF/AM (RL)', 'WB/MF/AM (RC)', 'WB/MF/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'],
            'WB (L)': ['DF/WB (L)', 'DF/WB (RL)',
                       'DF/WB/MF (L)', 'DF/WB/MF (RL)', 'DF/WB/MF (LC)', 'DF/WB/MF (RLC)',
                       'DF/WB/AM (L)', 'DF/WB/AM (RL)', 'DF/WB/AM (LC)', 'DF/WB/AM (RLC)',
                       'DF/WB/MF/AM (L)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (LC)', 'DF/WB/MF/AM (RLC)',
                       'WB (L)', 'WB (RL)',
                       'WB/MF (L)', 'WB/MF (RL)', 'WB/MF (LC)', 'WB/MF (RLC)',
                       'WB/MF/AM (L)', 'WB/MF/AM (RL)', 'WB/MF/AM (LC)', 'WB/MF/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'],
            'M (R)': ['DF/WB/MF (R)', 'DF/WB/MF (RL)', 'DF/WB/MF (RC)', 'DF/WB/MF (RLC)',
                      'DF/WB/AM (R)', 'DF/WB/AM (RL)', 'DF/WB/AM (RC)', 'DF/WB/AM (RLC)',
                      'DF/WB/MF/AM (R)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (RC)', 'DF/WB/MF/AM (RLC)',
                      'DF/MF (R)', 'DF/MF (RL)', 'DF/MF (RC)', 'DF/MF (RLC)',
                      'DF/MF/AM (R)', 'DF/MF/AM (RL)', 'DF/MF/AM (RC)', 'DF/MF/AM (RLC)',
                      'WB/MF (R)', 'WB/MF (RL)', 'WB/MF (RC)', 'WB/MF (RLC)',
                      'WB/MF/AM (R)', 'WB/MF/AM (RL)', 'WB/MF/AM (RC)', 'WB/MF/AM (RLC)',
                      'M (R)', 'M (RL)', 'M (RC)', 'M (RLC)',
                      'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)'],
            'M (L)': ['DF/WB/MF (L)', 'DF/WB/MF (RL)', 'DF/WB/MF (LC)', 'DF/WB/MF (RLC)',
                      'DF/WB/AM (L)', 'DF/WB/AM (RL)', 'DF/WB/AM (LC)', 'DF/WB/AM (RLC)',
                      'DF/WB/MF/AM (L)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (LC)', 'DF/WB/MF/AM (RLC)',
                      'DF/MF (L)', 'DF/MF (RL)', 'DF/MF (LC)', 'DF/MF (RLC)',
                      'DF/MF/AM (L)', 'DF/MF/AM (RL)', 'DF/MF/AM (LC)', 'DF/MF/AM (RLC)',
                      'WB/MF (L)', 'WB/MF (RL)', 'WB/MF (LC)', 'WB/MF (RLC)',
                      'WB/MF/AM (L)', 'WB/MF/AM (RL)', 'WB/MF/AM (LC)', 'WB/MF/AM (RLC)',
                      'M (L)', 'M (RL)', 'M (LC)', 'M (RLC)',
                      'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)'],
            'DM': ['DM'],
            'M (C)': ['M (C)', 'M (RC)', 'M (LC)', 'M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)'],
            'AM (C)': ['M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (C)', 'AM (RC)', 'AM (LC)', 'AM (RLC)'],
            'AM (R)': ['DF/WB/AM (R)', 'DF/WB/AM (RL)', 'DF/WB/AM (RC)', 'DF/WB/AM (RLC)',
                       'DF/WB/MF/AM (R)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (RC)', 'DF/WB/MF/AM (RLC)',
                       'DF/MF/AM (R)', 'DF/MF/AM (RL)', 'DF/MF/AM (RC)', 'DF/MF/AM (RLC)',
                       'DF/AM (R)', 'DF/AM (RL)', 'DF/AM (RC)', 'DF/AM (RLC)',
                       'WB/MF/AM (R)', 'WB/MF/AM (RL)', 'WB/MF/AM (RC)', 'WB/MF/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'
                       'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)',
                       'AM (R)', 'AM (RL)', 'AM (RC)', 'AM (RLC)'],
            'AM (L)': ['DF/WB/AM (L)', 'DF/WB/AM (RL)', 'DF/WB/AM (LC)', 'DF/WB/AM (RLC)',
                       'DF/WB/MF/AM (L)', 'DF/WB/MF/AM (RL)', 'DF/WB/MF/AM (LC)', 'DF/WB/MF/AM (RLC)',
                       'DF/MF/AM (L)', 'DF/MF/AM (RL)', 'DF/MF/AM (LC)', 'DF/MF/AM (RLC)',
                       'DF/AM (L)', 'DF/AM (RL)', 'DF/AM (LC)', 'DF/AM (RLC)',
                       'WB/MF/AM (L)', 'WB/MF/AM (RL)', 'WB/MF/AM (LC)', 'WB/MF/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'
                       'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (L)', 'AM (RL)', 'AM (LC)', 'AM (RLC)'],
            'ST': ['ST (C)']
        },
        'Korean': {
            'GK': ['GK'],
            'D (C)': ['D (C)', 'D (RC)', 'D (LC)', 'D (RLC)'],
            'D (R)': ['D (R)', 'D (RL)', 'D (RC)', 'D (RLC)',
                      'D/WB (R)', 'D/WB (RL)',
                      'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)'],
            'D (L)': ['D (L)', 'D (RL)', 'D (LC)', 'D (RLC)',
                      'D/WB (L)', 'D/WB (RL)',
                      'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)'],
            'WB (R)': ['D/WB (R)', 'D/WB (RL)',
                       'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                       'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'WB (R)', 'WB (RL)',
                       'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'],
            'WB (L)': ['D/WB (L)', 'D/WB (RL)',
                       'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                       'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'WB (L)', 'WB (RL)',
                       'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'],
            'M (R)': ['D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                      'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                      'M (R)', 'M (RL)', 'M (RC)', 'M (RLC)',
                      'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)'],
            'M (L)': ['D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                      'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                      'M (L)', 'M (RL)', 'M (LC)', 'M (RLC)',
                      'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)'],
            'DM': ['DM'],
            'M (C)': ['M (C)', 'M (RC)', 'M (LC)', 'M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)'],
            'AM (C)': ['M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (C)', 'AM (RC)', 'AM (LC)', 'AM (RLC)'],
            'AM (R)': ['D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                       'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'
                       'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)',
                       'AM (R)', 'AM (RL)', 'AM (RC)', 'AM (RLC)'],
            'AM (L)': ['D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                       'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'
                       'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (L)', 'AM (RL)', 'AM (LC)', 'AM (RLC)'],
            'ST': ['ST (C)']
        },
        'Chinese': {
            'GK': ['GK'],
            'D (C)': ['D (C)', 'D (RC)', 'D (LC)', 'D (RLC)'],
            'D (R)': ['D (R)', 'D (RL)', 'D (RC)', 'D (RLC)',
                      'D/WB (R)', 'D/WB (RL)',
                      'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)'],
            'D (L)': ['D (L)', 'D (RL)', 'D (LC)', 'D (RLC)',
                      'D/WB (L)', 'D/WB (RL)',
                      'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)'],
            'WB (R)': ['D/WB (R)', 'D/WB (RL)',
                       'D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                       'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'WB (R)', 'WB (RL)',
                       'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'],
            'WB (L)': ['D/WB (L)', 'D/WB (RL)',
                       'D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                       'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'WB (L)', 'WB (RL)',
                       'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'],
            'M (R)': ['D/WB/M (R)', 'D/WB/M (RL)', 'D/WB/M (RC)', 'D/WB/M (RLC)',
                      'D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                      'D/M (R)', 'D/M (RL)', 'D/M (RC)', 'D/M (RLC)',
                      'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                      'WB/M (R)', 'WB/M (RL)', 'WB/M (RC)', 'WB/M (RLC)',
                      'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                      'M (R)', 'M (RL)', 'M (RC)', 'M (RLC)',
                      'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)'],
            'M (L)': ['D/WB/M (L)', 'D/WB/M (RL)', 'D/WB/M (LC)', 'D/WB/M (RLC)',
                      'D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                      'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                      'D/M (L)', 'D/M (RL)', 'D/M (LC)', 'D/M (RLC)',
                      'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                      'WB/M (L)', 'WB/M (RL)', 'WB/M (LC)', 'WB/M (RLC)',
                      'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                      'M (L)', 'M (RL)', 'M (LC)', 'M (RLC)',
                      'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)'],
            'DM': ['DM'],
            'M (C)': ['M (C)', 'M (RC)', 'M (LC)', 'M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)'],
            'AM (C)': ['M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (C)', 'AM (RC)', 'AM (LC)', 'AM (RLC)'],
            'AM (R)': ['D/WB/AM (R)', 'D/WB/AM (RL)', 'D/WB/AM (RC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (R)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (RC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (R)', 'D/M/AM (RL)', 'D/M/AM (RC)', 'D/M/AM (RLC)',
                       'D/AM (R)', 'D/AM (RL)', 'D/AM (RC)', 'D/AM (RLC)',
                       'WB/M/AM (R)', 'WB/M/AM (RL)', 'WB/M/AM (RC)', 'WB/M/AM (RLC)',
                       'WB/AM (R)', 'WB/AM (RL)', 'WB/AM (RC)', 'WB/AM (RLC)'
                       'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)',
                       'AM (R)', 'AM (RL)', 'AM (RC)', 'AM (RLC)'],
            'AM (L)': ['D/WB/AM (L)', 'D/WB/AM (RL)', 'D/WB/AM (LC)', 'D/WB/AM (RLC)',
                       'D/WB/M/AM (L)', 'D/WB/M/AM (RL)', 'D/WB/M/AM (LC)', 'D/WB/M/AM (RLC)',
                       'D/M/AM (L)', 'D/M/AM (RL)', 'D/M/AM (LC)', 'D/M/AM (RLC)',
                       'D/AM (L)', 'D/AM (RL)', 'D/AM (LC)', 'D/AM (RLC)',
                       'WB/M/AM (L)', 'WB/M/AM (RL)', 'WB/M/AM (LC)', 'WB/M/AM (RLC)',
                       'WB/AM (L)', 'WB/AM (RL)', 'WB/AM (LC)', 'WB/AM (RLC)'
                       'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (L)', 'AM (RL)', 'AM (LC)', 'AM (RLC)'],
            'ST': ['ST (C)']
        },
        'German': {
            'TW': ['TW'],
            'V (Z)': ['V (Z)', 'V (RZ)', 'V (LZ)', 'V (RLZ)'],
            'V (R)': ['V (R)', 'V (RL)', 'V (RZ)', 'V (RLZ)', 'V/FV (R)', 'V/FV (RL)',
                      'V/FV/M (R)', 'V/FV/M (RL)', 'V/FV/M/OM (R)', 'V/FV/M/OM (RL)',
                      'V/FV/M/OM (RZ)', 'V/FV/M/OM (RLZ)', 'V/M (R)', 'V/M (RL)'],
            'V (L)': ['V (L)', 'V (RL)', 'V (LZ)', 'V (RLZ)', 'V/FV (L)', 'V/FV (RL)',
                      'V/FV/M (L)', 'V/FV/M (RL)', 'V/FV/M/OM (L)', 'V/FV/M/OM (RL)', 'V/M (L)', 'V/M (RL)'],
            'FV (R)': ['V/FV (R)', 'V/FV (RL)', 'V/FV/M (R)', 'V/FV/M (RL)', 'V/FV/M (RZ)',
                       'V/FV/M (RLZ)', 'V/FV/M/OM (R)', 'V/FV/M/OM (RL)', 'V/FV/M/OM (RZ)',
                       'V/FV/M/OM (RLZ)', 'FV (R)', 'FV (RL)', 'FV/M (R)', 'FV/M (RL)',
                       'FV/M (RZ)', 'FV/M (RLZ)', 'FV/M/OM (R)', 'FV/M/OM (RL)'],
            'FV (L)': ['V/FV (L)', 'V/FV (RL)', 'V/FV/M (L)', 'V/FV/M (RL)', 'V/FV/M (LZ)',
                       'V/FV/M (RLZ)', 'V/FV/M/OM (L)', 'V/FV/M/OM (RL)', 'V/FV/M/OM (LZ)',
                       'V/FV/M/OM (RLZ)', 'FV (L)', 'FV (RL)', 'FV/M (L)', 'FV/M (RL)',
                       'FV/M (LZ)', 'FV/M (RLZ)', 'FV/M/OM (L)', 'FV/M/OM (RL)'],
            'M (R)': ['V/FV/M (R)', 'V/FV/M (RL)', 'V/FV/M (RZ)', 'V/FV/M (RLZ)', 'V/FV/M/OM (R)',
                      'V/FV/M/OM (RL)', 'V/FV/M/OM (RZ)', 'V/FV/M/OM (RLZ)', 'FV/M (R)', 'FV/M (RL)',
                      'FV/M (RZ)', 'FV/M (RLZ)', 'FV/M/OM (R)', 'FV/M/OM (RL)', 'FV/M/OM (RZ)',
                      'FV/M/OM (RLZ)', 'M (R)', 'M (RL)', 'M (RZ)', 'M (RLZ)', 'M/OM (R)', 'M/OM (RL)',
                      'M/OM (RZ)', 'M/OM (RLZ)'],
            'M (L)': ['V/FV/M (L)', 'V/FV/M (RL)', 'V/FV/M (LZ)', 'V/FV/M (RLZ)', 'V/FV/M/OM (L)',
                      'V/FV/M/OM (RL)', 'V/FV/M/OM (LZ)', 'V/FV/M/OM (RLZ)', 'FV/M (L)', 'FV/M (RL)',
                      'FV/M (LZ)', 'FV/M (RLZ)', 'FV/M/OM (L)', 'FV/M/OM (RL)', 'FV/M/OM (LZ)',
                      'FV/M/OM (RLZ)', 'M (L)', 'M (RL)', 'M (LZ)', 'M (RLZ)', 'M/OM (L)', 'M/OM (RL)',
                      'M/OM (LZ)', 'M/OM (RLZ)'],
            'DM': ['DM'],
            'M (Z)': ['M (Z)', 'M (RZ)', 'M (LZ)', 'M (RLZ)', 'M/OM (Z)', 'M/OM (RZ)', 'M/OM (LZ)', 'M/OM (RLZ)'],
            'OM (Z)': ['M/OM (Z)', 'M/OM (RZ)', 'M/OM (LZ)', 'M/OM (RLZ)',
                       'OM (Z)', 'OM (RZ)', 'OM (LZ)', 'OM (RLZ)'],
            'OM (R)': ['V/FV/M/OM (R)', 'V/FV/M/OM (RL)', 'V/FV/M/OM (RZ)', 'V/FV/M/OM (RLZ)',
                       'FV/M/OM (R)', 'FV/M/OM (RL)', 'FV/M/OM (RZ)', 'FV/M/OM (RLZ)',
                       'M/OM (R)', 'M/OM (RL)', 'M/OM (RZ)', 'M/OM (RLZ)',
                       'OM (R)', 'OM (RL)', 'OM (RZ)', 'OM (RLZ)'],
            'OM (L)': ['V/FV/M/OM (L)', 'V/FV/M/OM (RL)', 'V/FV/M/OM (LZ)', 'V/FV/M/OM (RLZ)',
                       'FV/M/OM (L)', 'FV/M/OM (RL)', 'FV/M/OM (LZ)', 'FV/M/OM (RLZ)',
                       'M/OM (L)', 'M/OM (RL)', 'M/OM (LZ)', 'M/OM (RLZ)',
                       'OM (L)', 'OM (RL)', 'OM (LZ)', 'OM (RLZ)'],
            'ST': ['ST (Z)']
        },
        'Danish': {
            'Mm': ['Mm'],
            'F (C)': ['F (C)', 'F (HC)', 'F (VC)', 'F (HVC)'],
            'F (H)': ['F (H)', 'F (HV)', 'F (HC)', 'F (HVC)', 'F/WB (H)', 'F/WB (HV)',
                      'F/WB/M (H)', 'F/WB/M (HV)', 'F/WB/M/OM (H)', 'F/WB/M/OM (HV)',
                      'F/WB/M/OM (HC)', 'F/WB/M/OM (HVC)', 'F/M (H)', 'F/M (HV)'],
            'F (V)': ['F (V)', 'F (HV)', 'F (VC)', 'F (HVC)', 'F/WB (V)', 'F/WB (HV)',
                      'F/WB/M (V)', 'F/WB/M (HV)', 'F/WB/M/OM (V)', 'F/WB/M/OM (HV)', 'F/M (V)', 'F/M (HV)'],
            'WB (H)': ['F/WB (H)', 'F/WB (HV)', 'F/WB/M (H)', 'F/WB/M (HV)', 'F/WB/M (HC)',
                       'F/WB/M (HVC)', 'F/WB/M/OM (H)', 'F/WB/M/OM (HV)', 'F/WB/M/OM (HC)',
                       'F/WB/M/OM (HVC)', 'WB (H)', 'WB (HV)', 'WB/M (H)', 'WB/M (HV)',
                       'WB/M (HC)', 'WB/M (HVC)', 'WB/M/OM (H)', 'WB/M/OM (HV)'],
            'WB (V)': ['F/WB (V)', 'F/WB (HV)', 'F/WB/M (V)', 'F/WB/M (HV)', 'F/WB/M (VC)',
                       'F/WB/M (HVC)', 'F/WB/M/OM (V)', 'F/WB/M/OM (HV)', 'F/WB/M/OM (VC)',
                       'F/WB/M/OM (HVC)', 'WB (V)', 'WB (HV)', 'WB/M (V)', 'WB/M (HV)',
                       'WB/M (VC)', 'WB/M (HVC)', 'WB/M/OM (V)', 'WB/M/OM (HV)'],
            'M (H)': ['F/WB/M (H)', 'F/WB/M (HV)', 'F/WB/M (HC)', 'F/WB/M (HVC)', 'F/WB/M/OM (H)',
                      'F/WB/M/OM (HV)', 'F/WB/M/OM (HC)', 'F/WB/M/OM (HVC)', 'WB/M (H)', 'WB/M (HV)',
                      'WB/M (HC)', 'WB/M (HVC)', 'WB/M/OM (H)', 'WB/M/OM (HV)', 'WB/M/OM (HC)',
                      'WB/M/OM (HVC)', 'M (H)', 'M (HV)', 'M (HC)', 'M (HVC)', 'M/OM (H)', 'M/OM (HV)',
                      'M/OM (HC)', 'M/OM (HVC)'],
            'M (V)': ['F/WB/M (V)', 'F/WB/M (HV)', 'F/WB/M (VC)', 'F/WB/M (HVC)', 'F/WB/M/OM (V)',
                      'F/WB/M/OM (HV)', 'F/WB/M/OM (VC)', 'F/WB/M/OM (HVC)', 'WB/M (V)', 'WB/M (HV)',
                      'WB/M (VC)', 'WB/M (HVC)', 'WB/M/OM (V)', 'WB/M/OM (HV)', 'WB/M/OM (VC)',
                      'WB/M/OM (HVC)', 'M (V)', 'M (HV)', 'M (VC)', 'M (HVC)', 'M/OM (V)', 'M/OM (HV)',
                      'M/OM (VC)', 'M/OM (HVC)'],
            'DM': ['DM'],
            'M (C)': ['M (C)', 'M (HC)', 'M (VC)', 'M (HVC)', 'M/OM (C)', 'M/OM (HC)', 'M/OM (VC)', 'M/OM (HVC)'],
            'OM (C)': ['M/OM (C)', 'M/OM (HC)', 'M/OM (VC)', 'M/OM (HVC)',
                       'OM (C)', 'OM (HC)', 'OM (VC)', 'OM (HVC)'],
            'OM (H)': ['F/WB/M/OM (H)', 'F/WB/M/OM (HV)', 'F/WB/M/OM (HC)', 'F/WB/M/OM (HVC)',
                       'WB/M/OM (H)', 'WB/M/OM (HV)', 'WB/M/OM (HC)', 'WB/M/OM (HVC)',
                       'M/OM (H)', 'M/OM (HV)', 'M/OM (HC)', 'M/OM (HVC)',
                       'OM (H)', 'OM (HV)', 'OM (HC)', 'OM (HVC)'],
            'OM (V)': ['F/WB/M/OM (V)', 'F/WB/M/OM (HV)', 'F/WB/M/OM (VC)', 'F/WB/M/OM (HVC)',
                       'WB/M/OM (V)', 'WB/M/OM (HV)', 'WB/M/OM (VC)', 'WB/M/OM (HVC)',
                       'M/OM (V)', 'M/OM (HV)', 'M/OM (VC)', 'M/OM (HVC)',
                       'OM (V)', 'OM (HV)', 'OM (VC)', 'OM (HVC)'],
            'An': ['An (C)']
        },
        'Norwegian': {
            'Kee': ['Kee'],
            'F (S)': ['F (S)', 'F (HS)', 'F (VS)', 'F (HVS)'],
            'F (H)': ['F (H)', 'F (HV)', 'F (HS)', 'F (HVS)', 'F/VB (H)', 'F/VB (HV)',
                      'F/VB/M (H)', 'F/VB/M (HV)', 'F/VB/M/OM (H)', 'F/VB/M/OM (HV)',
                      'F/VB/M/OM (HS)', 'F/VB/M/OM (HVS)', 'F/M (H)', 'F/M (HV)'],
            'F (V)': ['F (V)', 'F (HV)', 'F (VS)', 'F (HVS)', 'F/VB (V)', 'F/VB (HV)',
                      'F/VB/M (V)', 'F/VB/M (HV)', 'F/VB/M/OM (V)', 'F/VB/M/OM (HV)', 'F/M (V)', 'F/M (HV)'],
            'VB (H)': ['F/VB (H)', 'F/VB (HV)', 'F/VB/M (H)', 'F/VB/M (HV)', 'F/VB/M (HS)',
                       'F/VB/M (HVS)', 'F/VB/M/OM (H)', 'F/VB/M/OM (HV)', 'F/VB/M/OM (HS)',
                       'F/VB/M/OM (HVS)', 'VB (H)', 'VB (HV)', 'VB/M (H)', 'VB/M (HV)',
                       'VB/M (HS)', 'VB/M (HVS)', 'VB/M/OM (H)', 'VB/M/OM (HV)'],
            'VB (V)': ['F/VB (V)', 'F/VB (HV)', 'F/VB/M (V)', 'F/VB/M (HV)', 'F/VB/M (VS)',
                       'F/VB/M (HVS)', 'F/VB/M/OM (V)', 'F/VB/M/OM (HV)', 'F/VB/M/OM (VS)',
                       'F/VB/M/OM (HVS)', 'VB (V)', 'VB (HV)', 'VB/M (V)', 'VB/M (HV)',
                       'VB/M (VS)', 'VB/M (HVS)', 'VB/M/OM (V)', 'VB/M/OM (HV)'],
            'M (H)': ['F/VB/M (H)', 'F/VB/M (HV)', 'F/VB/M (HS)', 'F/VB/M (HVS)', 'F/VB/M/OM (H)',
                      'F/VB/M/OM (HV)', 'F/VB/M/OM (HS)', 'F/VB/M/OM (HVS)', 'VB/M (H)', 'VB/M (HV)',
                      'VB/M (HS)', 'VB/M (HVS)', 'VB/M/OM (H)', 'VB/M/OM (HV)', 'VB/M/OM (HS)',
                      'VB/M/OM (HVS)', 'M (H)', 'M (HV)', 'M (HS)', 'M (HVS)', 'M/OM (H)', 'M/OM (HV)',
                      'M/OM (HS)', 'M/OM (HVS)'],
            'M (V)': ['F/VB/M (V)', 'F/VB/M (HV)', 'F/VB/M (VS)', 'F/VB/M (HVS)', 'F/VB/M/OM (V)',
                      'F/VB/M/OM (HV)', 'F/VB/M/OM (VS)', 'F/VB/M/OM (HVS)', 'VB/M (V)', 'VB/M (HV)',
                      'VB/M (VS)', 'VB/M (HVS)', 'VB/M/OM (V)', 'VB/M/OM (HV)', 'VB/M/OM (VS)',
                      'VB/M/OM (HVS)', 'M (V)', 'M (HV)', 'M (VS)', 'M (HVS)', 'M/OM (V)', 'M/OM (HV)',
                      'M/OM (VS)', 'M/OM (HVS)'],
            'DM': ['DM'],
            'M (S)': ['M (S)', 'M (HS)', 'M (VS)', 'M (HVS)', 'M/OM (S)', 'M/OM (HS)', 'M/OM (VS)', 'M/OM (HVS)'],
            'OM (S)': ['M/OM (S)', 'M/OM (HS)', 'M/OM (VS)', 'M/OM (HVS)',
                       'OM (S)', 'OM (HS)', 'OM (VS)', 'OM (HVS)'],
            'OM (H)': ['F/VB/M/OM (H)', 'F/VB/M/OM (HV)', 'F/VB/M/OM (HS)', 'F/VB/M/OM (HVS)',
                       'VB/M/OM (H)', 'VB/M/OM (HV)', 'VB/M/OM (HS)', 'VB/M/OM (HVS)',
                       'M/OM (H)', 'M/OM (HV)', 'M/OM (HS)', 'M/OM (HVS)',
                       'OM (H)', 'OM (HV)', 'OM (HS)', 'OM (HVS)'],
            'OM (V)': ['F/VB/M/OM (V)', 'F/VB/M/OM (HV)', 'F/VB/M/OM (VS)', 'F/VB/M/OM (HVS)',
                       'VB/M/OM (V)', 'VB/M/OM (HV)', 'VB/M/OM (VS)', 'VB/M/OM (HVS)',
                       'M/OM (V)', 'M/OM (HV)', 'M/OM (VS)', 'M/OM (HVS)',
                       'OM (V)', 'OM (HV)', 'OM (VS)', 'OM (HVS)'],
            'SP': ['SP (S)']
        },
        'Swedish': {
            'Mål': ['Mål'],
            'B (C)': ['B (C)', 'B (HC)', 'B (VC)', 'B (HVC)'],
            'B (H)': ['B (H)', 'B (HV)', 'B (HC)', 'B (HVC)', 'B/YB (H)', 'B/YB (HV)',
                      'B/YB/M (H)', 'B/YB/M (HV)', 'B/YB/M/OM (H)', 'B/YB/M/OM (HV)',
                      'B/YB/M/OM (HC)', 'B/YB/M/OM (HVC)', 'B/M (H)', 'B/M (HV)'],
            'B (V)': ['B (V)', 'B (HV)', 'B (VC)', 'B (HVC)', 'B/YB (V)', 'B/YB (HV)',
                      'B/YB/M (V)', 'B/YB/M (HV)', 'B/YB/M/OM (V)', 'B/YB/M/OM (HV)', 'B/M (V)', 'B/M (HV)'],
            'YB (H)': ['B/YB (H)', 'B/YB (HV)', 'B/YB/M (H)', 'B/YB/M (HV)', 'B/YB/M (HC)',
                       'B/YB/M (HVC)', 'B/YB/M/OM (H)', 'B/YB/M/OM (HV)', 'B/YB/M/OM (HC)',
                       'B/YB/M/OM (HVC)', 'YB (H)', 'YB (HV)', 'YB/M (H)', 'YB/M (HV)',
                       'YB/M (HC)', 'YB/M (HVC)', 'YB/M/OM (H)', 'YB/M/OM (HV)'],
            'YB (V)': ['B/YB (V)', 'B/YB (HV)', 'B/YB/M (V)', 'B/YB/M (HV)', 'B/YB/M (VC)',
                       'B/YB/M (HVC)', 'B/YB/M/OM (V)', 'B/YB/M/OM (HV)', 'B/YB/M/OM (VC)',
                       'B/YB/M/OM (HVC)', 'YB (V)', 'YB (HV)', 'YB/M (V)', 'YB/M (HV)',
                       'YB/M (VC)', 'YB/M (HVC)', 'YB/M/OM (V)', 'YB/M/OM (HV)'],
            'M (H)': ['B/YB/M (H)', 'B/YB/M (HV)', 'B/YB/M (HC)', 'B/YB/M (HVC)', 'B/YB/M/OM (H)',
                      'B/YB/M/OM (HV)', 'B/YB/M/OM (HC)', 'B/YB/M/OM (HVC)', 'YB/M (H)', 'YB/M (HV)',
                      'YB/M (HC)', 'YB/M (HVC)', 'YB/M/OM (H)', 'YB/M/OM (HV)', 'YB/M/OM (HC)',
                      'YB/M/OM (HVC)', 'M (H)', 'M (HV)', 'M (HC)', 'M (HVC)', 'M/OM (H)', 'M/OM (HV)',
                      'M/OM (HC)', 'M/OM (HVC)'],
            'M (V)': ['B/YB/M (V)', 'B/YB/M (HV)', 'B/YB/M (VC)', 'B/YB/M (HVC)', 'B/YB/M/OM (V)',
                      'B/YB/M/OM (HV)', 'B/YB/M/OM (VC)', 'B/YB/M/OM (HVC)', 'YB/M (V)', 'YB/M (HV)',
                      'YB/M (VC)', 'YB/M (HVC)', 'YB/M/OM (V)', 'YB/M/OM (HV)', 'YB/M/OM (VC)',
                      'YB/M/OM (HVC)', 'M (V)', 'M (HV)', 'M (VC)', 'M (HVC)', 'M/OM (V)', 'M/OM (HV)',
                      'M/OM (VC)', 'M/OM (HVC)'],
            'DM': ['DM'],
            'M (C)': ['M (C)', 'M (HC)', 'M (VC)', 'M (HVC)', 'M/OM (C)', 'M/OM (HC)', 'M/OM (VC)', 'M/OM (HVC)'],
            'OM (C)': ['M/OM (C)', 'M/OM (HC)', 'M/OM (VC)', 'M/OM (HVC)',
                       'OM (C)', 'OM (HC)', 'OM (VC)', 'OM (HVC)'],
            'OM (H)': ['B/YB/M/OM (H)', 'B/YB/M/OM (HV)', 'B/YB/M/OM (HC)', 'B/YB/M/OM (HVC)',
                       'YB/M/OM (H)', 'YB/M/OM (HV)', 'YB/M/OM (HC)', 'YB/M/OM (HVC)',
                       'M/OM (H)', 'M/OM (HV)', 'M/OM (HC)', 'M/OM (HVC)',
                       'OM (H)', 'OM (HV)', 'OM (HC)', 'OM (HVC)'],
            'OM (V)': ['B/YB/M/OM (V)', 'B/YB/M/OM (HV)', 'B/YB/M/OM (VC)', 'B/YB/M/OM (HVC)',
                       'YB/M/OM (V)', 'YB/M/OM (HV)', 'YB/M/OM (VC)', 'YB/M/OM (HVC)',
                       'M/OM (V)', 'M/OM (HV)', 'M/OM (VC)', 'M/OM (HVC)',
                       'OM (V)', 'OM (HV)', 'OM (VC)', 'OM (HVC)'],
            'A': ['A (C)']
        },
        'Dutch': {
            'DM': ['DM'],
            'V (C)': ['V (C)', 'V (RC)', 'V (LC)', 'V (RLC)'],
            'V (R)': ['V (R)', 'V (RL)', 'V (RC)', 'V (RLC)', 'V/VV (R)', 'V/VV (RL)',
                      'V/VV/M (R)', 'V/VV/M (RL)', 'V/VV/M/AM (R)', 'V/VV/M/AM (RL)',
                      'V/VV/M/AM (RC)', 'V/VV/M/AM (RLC)', 'V/M (R)', 'V/M (RL)'],
            'V (L)': ['V (L)', 'V (RL)', 'V (LC)', 'V (RLC)', 'V/VV (L)', 'V/VV (RL)',
                      'V/VV/M (L)', 'V/VV/M (RL)', 'V/VV/M/AM (L)', 'V/VV/M/AM (RL)', 'V/M (L)', 'V/M (RL)'],
            'VV (R)': ['V/VV (R)', 'V/VV (RL)', 'V/VV/M (R)', 'V/VV/M (RL)', 'V/VV/M (RC)',
                       'V/VV/M (RLC)', 'V/VV/M/AM (R)', 'V/VV/M/AM (RL)', 'V/VV/M/AM (RC)',
                       'V/VV/M/AM (RLC)', 'VV (R)', 'VV (RL)', 'VV/M (R)', 'VV/M (RL)',
                       'VV/M (RC)', 'VV/M (RLC)', 'VV/M/AM (R)', 'VV/M/AM (RL)'],
            'VV (L)': ['V/VV (L)', 'V/VV (RL)', 'V/VV/M (L)', 'V/VV/M (RL)', 'V/VV/M (LC)',
                       'V/VV/M (RLC)', 'V/VV/M/AM (L)', 'V/VV/M/AM (RL)', 'V/VV/M/AM (LC)',
                       'V/VV/M/AM (RLC)', 'VV (L)', 'VV (RL)', 'VV/M (L)', 'VV/M (RL)',
                       'VV/M (LC)', 'VV/M (RLC)', 'VV/M/AM (L)', 'VV/M/AM (RL)'],
            'M (R)': ['V/VV/M (R)', 'V/VV/M (RL)', 'V/VV/M (RC)', 'V/VV/M (RLC)', 'V/VV/M/AM (R)',
                      'V/VV/M/AM (RL)', 'V/VV/M/AM (RC)', 'V/VV/M/AM (RLC)', 'VV/M (R)', 'VV/M (RL)',
                      'VV/M (RC)', 'VV/M (RLC)', 'VV/M/AM (R)', 'VV/M/AM (RL)', 'VV/M/AM (RC)',
                      'VV/M/AM (RLC)', 'M (R)', 'M (RL)', 'M (RC)', 'M (RLC)', 'M/AM (R)', 'M/AM (RL)',
                      'M/AM (RC)', 'M/AM (RLC)'],
            'M (L)': ['V/VV/M (L)', 'V/VV/M (RL)', 'V/VV/M (LC)', 'V/VV/M (RLC)', 'V/VV/M/AM (L)',
                      'V/VV/M/AM (RL)', 'V/VV/M/AM (LC)', 'V/VV/M/AM (RLC)', 'VV/M (L)', 'VV/M (RL)',
                      'VV/M (LC)', 'VV/M (RLC)', 'VV/M/AM (L)', 'VV/M/AM (RL)', 'VV/M/AM (LC)',
                      'VV/M/AM (RLC)', 'M (L)', 'M (RL)', 'M (LC)', 'M (RLC)', 'M/AM (L)', 'M/AM (RL)',
                      'M/AM (LC)', 'M/AM (RLC)'],
            'VM': ['VM'],
            'M (C)': ['M (C)', 'M (RC)', 'M (LC)', 'M (RLC)', 'M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)'],
            'AM (C)': ['M/AM (C)', 'M/AM (RC)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (C)', 'AM (RC)', 'AM (LC)', 'AM (RLC)'],
            'AM (R)': ['V/VV/M/AM (R)', 'V/VV/M/AM (RL)', 'V/VV/M/AM (RC)', 'V/VV/M/AM (RLC)',
                       'VV/M/AM (R)', 'VV/M/AM (RL)', 'VV/M/AM (RC)', 'VV/M/AM (RLC)',
                       'M/AM (R)', 'M/AM (RL)', 'M/AM (RC)', 'M/AM (RLC)',
                       'AM (R)', 'AM (RL)', 'AM (RC)', 'AM (RLC)'],
            'AM (L)': ['V/VV/M/AM (L)', 'V/VV/M/AM (RL)', 'V/VV/M/AM (LC)', 'V/VV/M/AM (RLC)',
                       'VV/M/AM (L)', 'VV/M/AM (RL)', 'VV/M/AM (LC)', 'VV/M/AM (RLC)',
                       'M/AM (L)', 'M/AM (RL)', 'M/AM (LC)', 'M/AM (RLC)',
                       'AM (L)', 'AM (RL)', 'AM (LC)', 'AM (RLC)'],
            'S': ['S (C)']
        },
        'Spanish': {
            'POR': ['POR'],
            'DF (C)': ['DF (C)', 'DF (DC)', 'DF (IC)', 'DF (DIC)'],
            'DF (D)': ['DF (D)', 'DF (DI)', 'DF (DC)', 'DF (DIC)', 'DF/CR (D)', 'DF/CR (DI)',
                      'DF/CR/ME (D)', 'DF/CR/ME (DI)', 'DF/CR/ME/MP (D)', 'DF/CR/ME/MP (DI)',
                      'DF/CR/ME/MP (DC)', 'DF/CR/ME/MP (DIC)', 'DF/ME (D)', 'DF/ME (DI)'],
            'DF (I)': ['DF (I)', 'DF (DI)', 'DF (IC)', 'DF (DIC)', 'DF/CR (I)', 'DF/CR (DI)',
                      'DF/CR/ME (I)', 'DF/CR/ME (DI)', 'DF/CR/ME/MP (I)', 'DF/CR/ME/MP (DI)', 'DF/ME (I)', 'DF/ME (DI)'],
            'CR (D)': ['DF/CR (D)', 'DF/CR (DI)', 'DF/CR/ME (D)', 'DF/CR/ME (DI)', 'DF/CR/ME (DC)',
                       'DF/CR/ME (DIC)', 'DF/CR/ME/MP (D)', 'DF/CR/ME/MP (DI)', 'DF/CR/ME/MP (DC)',
                       'DF/CR/ME/MP (DIC)', 'CR (D)', 'CR (DI)', 'CR/ME (D)', 'CR/ME (DI)',
                       'CR/ME (DC)', 'CR/ME (DIC)', 'CR/ME/MP (D)', 'CR/ME/MP (DI)'],
            'CR (I)': ['DF/CR (I)', 'DF/CR (DI)', 'DF/CR/ME (I)', 'DF/CR/ME (DI)', 'DF/CR/ME (IC)',
                       'DF/CR/ME (DIC)', 'DF/CR/ME/MP (I)', 'DF/CR/ME/MP (DI)', 'DF/CR/ME/MP (IC)',
                       'DF/CR/ME/MP (DIC)', 'CR (I)', 'CR (DI)', 'CR/ME (I)', 'CR/ME (DI)',
                       'CR/ME (IC)', 'CR/ME (DIC)', 'CR/ME/MP (I)', 'CR/ME/MP (DI)'],
            'ME (D)': ['DF/CR/ME (D)', 'DF/CR/ME (DI)', 'DF/CR/ME (DC)', 'DF/CR/ME (DIC)', 'DF/CR/ME/MP (D)',
                      'DF/CR/ME/MP (DI)', 'DF/CR/ME/MP (DC)', 'DF/CR/ME/MP (DIC)', 'CR/ME (D)', 'CR/ME (DI)',
                      'CR/ME (DC)', 'CR/ME (DIC)', 'CR/ME/MP (D)', 'CR/ME/MP (DI)', 'CR/ME/MP (DC)',
                      'CR/ME/MP (DIC)', 'ME (D)', 'ME (DI)', 'ME (DC)', 'ME (DIC)', 'ME/MP (D)', 'ME/MP (DI)',
                      'ME/MP (DC)', 'ME/MP (DIC)'],
            'ME (I)': ['DF/CR/ME (I)', 'DF/CR/ME (DI)', 'DF/CR/ME (IC)', 'DF/CR/ME (DIC)', 'DF/CR/ME/MP (I)',
                      'DF/CR/ME/MP (DI)', 'DF/CR/ME/MP (IC)', 'DF/CR/ME/MP (DIC)', 'CR/ME (I)', 'CR/ME (DI)',
                      'CR/ME (IC)', 'CR/ME (DIC)', 'CR/ME/MP (I)', 'CR/ME/MP (DI)', 'CR/ME/MP (IC)',
                      'CR/ME/MP (DIC)', 'ME (I)', 'ME (DI)', 'ME (IC)', 'ME (DIC)', 'ME/MP (I)', 'ME/MP (DI)',
                      'ME/MP (IC)', 'ME/MP (DIC)'],
            'MC': ['MC'],
            'ME (C)': ['ME (C)', 'ME (DC)', 'ME (IC)', 'ME (DIC)', 'ME/MP (C)', 'ME/MP (DC)', 'ME/MP (IC)', 'ME/MP (DIC)'],
            'MP (C)': ['ME/MP (C)', 'ME/MP (DC)', 'ME/MP (IC)', 'ME/MP (DIC)',
                       'MP (C)', 'MP (DC)', 'MP (IC)', 'MP (DIC)'],
            'MP (D)': ['D/CR/ME/MP (D)', 'D/CR/ME/MP (DI)', 'D/CR/ME/MP (DC)', 'D/CR/ME/MP (DIC)',
                       'CR/ME/MP (D)', 'CR/ME/MP (DI)', 'CR/ME/MP (DC)', 'CR/ME/MP (DIC)',
                       'ME/MP (D)', 'ME/MP (DI)', 'ME/MP (DC)', 'ME/MP (DIC)',
                       'MP (D)', 'MP (DI)', 'MP (DC)', 'MP (DIC)'],
            'MP (I)': ['D/CR/ME/MP (I)', 'D/CR/ME/MP (DI)', 'D/CR/ME/MP (IC)', 'D/CR/ME/MP (DIC)',
                       'CR/ME/MP (I)', 'CR/ME/MP (DI)', 'CR/ME/MP (IC)', 'CR/ME/MP (DIC)',
                       'ME/MP (I)', 'ME/MP (DI)', 'ME/MP (IC)', 'ME/MP (DIC)',
                       'MP (I)', 'MP (DI)', 'MP (IC)', 'MP (DIC)'],
            'DL': ['DL (C)']
        },
        'French': {
            'GB': ['GB'],
            'D (C)': ['D (C)', 'D (DC)', 'D (GC)', 'D (DGC)'],
            'D (D)': ['D (D)', 'D (DG)', 'D (DC)', 'D (DGC)', 'D/AL (D)', 'D/AL (DG)',
                      'D/AL/M (D)', 'D/AL/M (DG)', 'D/AL/M/MO (D)', 'D/AL/M/MO (DG)',
                      'D/AL/M/MO (DC)', 'D/AL/M/MO (DGC)', 'D/M (D)', 'D/M (DG)'],
            'D (G)': ['D (G)', 'D (DG)', 'D (GC)', 'D (DGC)', 'D/AL (G)', 'D/AL (DG)',
                      'D/AL/M (G)', 'D/AL/M (DG)', 'D/AL/M/MO (G)', 'D/AL/M/MO (DG)', 'D/M (G)', 'D/M (DG)'],
            'AL (D)': ['D/AL (D)', 'D/AL (DG)', 'D/AL/M (D)', 'D/AL/M (DG)', 'D/AL/M (DC)',
                       'D/AL/M (DGC)', 'D/AL/M/MO (D)', 'D/AL/M/MO (DG)', 'D/AL/M/MO (DC)',
                       'D/AL/M/MO (DGC)', 'AL (D)', 'AL (DG)', 'AL/M (D)', 'AL/M (DG)',
                       'AL/M (DC)', 'AL/M (DGC)', 'AL/M/MO (D)', 'AL/M/MO (DG)'],
            'AL (G)': ['D/AL (G)', 'D/AL (DG)', 'D/AL/M (G)', 'D/AL/M (DG)', 'D/AL/M (GC)',
                       'D/AL/M (DGC)', 'D/AL/M/MO (G)', 'D/AL/M/MO (DG)', 'D/AL/M/MO (GC)',
                       'D/AL/M/MO (DGC)', 'AL (G)', 'AL (DG)', 'AL/M (G)', 'AL/M (DG)',
                       'AL/M (GC)', 'AL/M (DGC)', 'AL/M/MO (G)', 'AL/M/MO (DG)'],
            'M (D)': ['D/AL/M (D)', 'D/AL/M (DG)', 'D/AL/M (DC)', 'D/AL/M (DGC)', 'D/AL/M/MO (D)',
                      'D/AL/M/MO (DG)', 'D/AL/M/MO (DC)', 'D/AL/M/MO (DGC)', 'AL/M (D)', 'AL/M (DG)',
                      'AL/M (DC)', 'AL/M (DGC)', 'AL/M/MO (D)', 'AL/M/MO (DG)', 'AL/M/MO (DC)',
                      'AL/M/MO (DGC)', 'M (D)', 'M (DG)', 'M (DC)', 'M (DGC)', 'M/MO (D)', 'M/MO (DG)',
                      'M/MO (DC)', 'M/MO (DGC)'],
            'M (G)': ['D/AL/M (G)', 'D/AL/M (DG)', 'D/AL/M (GC)', 'D/AL/M (DGC)', 'D/AL/M/MO (G)',
                      'D/AL/M/MO (DG)', 'D/AL/M/MO (GC)', 'D/AL/M/MO (DGC)', 'AL/M (G)', 'AL/M (DG)',
                      'AL/M (GC)', 'AL/M (DGC)', 'AL/M/MO (G)', 'AL/M/MO (DG)', 'AL/M/MO (GC)',
                      'AL/M/MO (DGC)', 'M (G)', 'M (DG)', 'M (GC)', 'M (DGC)', 'M/MO (G)', 'M/MO (DG)',
                      'M/MO (GC)', 'M/MO (DGC)'],
            'MD': ['MD'],
            'M (C)': ['M (C)', 'M (DC)', 'M (GC)', 'M (DGC)', 'M/MO (C)', 'M/MO (DC)', 'M/MO (GC)', 'M/MO (DGC)'],
            'MO (C)': ['M/MO (C)', 'M/MO (DC)', 'M/MO (GC)', 'M/MO (DGC)',
                       'MO (C)', 'MO (DC)', 'MO (GC)', 'MO (DGC)'],
            'MO (D)': ['D/AL/M/MO (D)', 'D/AL/M/MO (DG)', 'D/AL/M/MO (DC)', 'D/AL/M/MO (DGC)',
                       'AL/M/MO (D)', 'AL/M/MO (DG)', 'AL/M/MO (DC)', 'AL/M/MO (DGC)',
                       'M/MO (D)', 'M/MO (DG)', 'M/MO (DC)', 'M/MO (DGC)',
                       'MO (D)', 'MO (DG)', 'MO (DC)', 'MO (DGC)'],
            'MO (G)': ['D/AL/M/MO (G)', 'D/AL/M/MO (DG)', 'D/AL/M/MO (GC)', 'D/AL/M/MO (DGC)',
                       'AL/M/MO (G)', 'AL/M/MO (DG)', 'AL/M/MO (GC)', 'AL/M/MO (DGC)',
                       'M/MO (G)', 'M/MO (DG)', 'M/MO (GC)', 'M/MO (DGC)',
                       'MO (G)', 'MO (DG)', 'MO (GC)', 'MO (DGC)'],
            'BT': ['BT (C)']
        },
        'Italian': {
            'Por': ['Por'],
            'D (C)': ['D (C)', 'D (DC)', 'D (SC)', 'D (DSC)'],
            'D (D)': ['D (D)', 'D (DS)', 'D (DC)', 'D (DSC)', 'D/TF (D)', 'D/TF (DS)',
                      'D/TF/C (D)', 'D/TF/C (DS)', 'D/TF/C/T (D)', 'D/TF/C/T (DS)',
                      'D/TF/C/T (DC)', 'D/TF/C/T (DSC)', 'D/C (D)', 'D/C (DS)'],
            'D (S)': ['D (S)', 'D (DS)', 'D (SC)', 'D (DSC)', 'D/TF (S)', 'D/TF (DS)',
                      'D/TF/C (S)', 'D/TF/C (DS)', 'D/TF/C/T (S)', 'D/TF/C/T (DS)', 'D/C (S)', 'D/C (DS)'],
            'TF (D)': ['D/TF (D)', 'D/TF (DS)', 'D/TF/C (D)', 'D/TF/C (DS)', 'D/TF/C (DC)',
                       'D/TF/C (DSC)', 'D/TF/C/T (D)', 'D/TF/C/T (DS)', 'D/TF/C/T (DC)',
                       'D/TF/C/T (DSC)', 'TF (D)', 'TF (DS)', 'TF/C (D)', 'TF/C (DS)',
                       'TF/C (DC)', 'TF/C (DSC)', 'TF/C/T (D)', 'TF/C/T (DS)'],
            'TF (S)': ['D/TF (S)', 'D/TF (DS)', 'D/TF/C (S)', 'D/TF/C (DS)', 'D/TF/C (SC)',
                       'D/TF/C (DSC)', 'D/TF/C/T (S)', 'D/TF/C/T (DS)', 'D/TF/C/T (SC)',
                       'D/TF/C/T (DSC)', 'TF (S)', 'TF (DS)', 'TF/C (S)', 'TF/C (DS)',
                       'TF/C (SC)', 'TF/C (DSC)', 'TF/C/T (S)', 'TF/C/T (DS)'],
            'C (D)': ['D/TF/C (D)', 'D/TF/C (DS)', 'D/TF/C (DC)', 'D/TF/C (DSC)', 'D/TF/C/T (D)',
                      'D/TF/C/T (DS)', 'D/TF/C/T (DC)', 'D/TF/C/T (DSC)', 'TF/C (D)', 'TF/C (DS)',
                      'TF/C (DC)', 'TF/C (DSC)', 'TF/C/T (D)', 'TF/C/T (DS)', 'TF/C/T (DC)',
                      'TF/C/T (DSC)', 'C (D)', 'C (DS)', 'C (DC)', 'C (DSC)', 'C/T (D)', 'C/T (DS)',
                      'C/T (DC)', 'C/T (DSC)'],
            'C (S)': ['D/TF/C (S)', 'D/TF/C (DS)', 'D/TF/C (SC)', 'D/TF/C (DSC)', 'D/TF/C/T (S)',
                      'D/TF/C/T (DS)', 'D/TF/C/T (SC)', 'D/TF/C/T (DSC)', 'TF/C (S)', 'TF/C (DS)',
                      'TF/C (SC)', 'TF/C (DSC)', 'TF/C/T (S)', 'TF/C/T (DS)', 'TF/C/T (SC)',
                      'TF/C/T (DSC)', 'C (S)', 'C (DS)', 'C (SC)', 'C (DSC)', 'C/T (S)', 'C/T (DS)',
                      'C/T (SC)', 'C/T (DSC)'],
            'M': ['M'],
            'C (C)': ['C (C)', 'C (DC)', 'C (SC)', 'C (DSC)', 'C/T (C)', 'C/T (DC)', 'C/T (SC)', 'C/T (DSC)'],
            'T (C)': ['C/T (C)', 'C/T (DC)', 'C/T (SC)', 'C/T (DSC)',
                       'T (C)', 'T (DC)', 'T (SC)', 'T (DSC)'],
            'T (D)': ['D/TF/C/T (D)', 'D/TF/C/T (DS)', 'D/TF/C/T (DC)', 'D/TF/C/T (DSC)',
                       'TF/C/T (D)', 'TF/C/T (DS)', 'TF/C/T (DC)', 'TF/C/T (DSC)',
                       'C/T (D)', 'C/T (DS)', 'C/T (DC)', 'C/T (DSC)',
                       'T (D)', 'T (DS)', 'T (DC)', 'T (DSC)'],
            'T (S)': ['D/TF/C/T (S)', 'D/TF/C/T (DS)', 'D/TF/C/T (SC)', 'D/TF/C/T (DSC)',
                       'TF/C/T (S)', 'TF/C/T (DS)', 'TF/C/T (SC)', 'TF/C/T (DSC)',
                       'C/T (S)', 'C/T (DS)', 'C/T (SC)', 'C/T (DSC)',
                       'T (S)', 'T (DS)', 'T (SC)', 'T (DSC)'],
            'DL': ['DL (C)']
        },
        'Portuguese': {
            'GR': ['GR'],
            'D (C)': ['D (C)', 'D (DC)', 'D (EC)', 'D (DEC)'],
            'D (D)': ['D (D)', 'D (DE)', 'D (DC)', 'D (DEC)', 'D/DA (D)', 'D/DA (DE)',
                      'D/DA/M (D)', 'D/DA/M (DE)', 'D/DA/M/T (D)', 'D/DA/M/MO (DE)',
                      'D/DA/M/MO (DC)', 'D/DA/M/MO (DEC)', 'D/M (D)', 'D/M (DE)'],
            'D (E)': ['D (E)', 'D (DE)', 'D (EC)', 'D (DEC)', 'D/DA (E)', 'D/DA (DE)',
                      'D/DA/M (E)', 'D/DA/M (DE)', 'D/DA/M/MO (E)', 'D/DA/M/MO (DE)', 'D/M (E)', 'D/M (DE)'],
            'DA (D)': ['D/DA (D)', 'D/DA (DE)', 'D/DA/M (D)', 'D/DA/M (DE)', 'D/DA/M (DC)',
                       'D/DA/M (DEC)', 'D/DA/M/MO (D)', 'D/DA/M/MO (DE)', 'D/DA/M/MO (DC)',
                       'D/DA/M/MO (DEC)', 'DA (D)', 'DA (DE)', 'DA/M (D)', 'DA/M (DE)',
                       'DA/M (DC)', 'DA/M (DEC)', 'DA/M/MO (D)', 'DA/M/MO (DE)'],
            'DA (E)': ['D/DA (E)', 'D/DA (DE)', 'D/DA/M (E)', 'D/DA/M (DE)', 'D/DA/M (EC)',
                       'D/DA/M (DEC)', 'D/DA/M/MO (E)', 'D/DA/M/MO (DE)', 'D/DA/M/MO (EC)',
                       'D/DA/M/MO (DEC)', 'DA (E)', 'DA (DE)', 'DA/M (E)', 'DA/M (DE)',
                       'DA/M (EC)', 'DA/M (DEC)', 'DA/M/MO (E)', 'DA/M/MO (DE)'],
            'M (D)': ['D/DA/M (D)', 'D/DA/M (DE)', 'D/DA/M (DC)', 'D/DA/M (DEC)', 'D/DA/M/MO (D)',
                      'D/DA/M/MO (DE)', 'D/DA/M/MO (DC)', 'D/DA/M/MO (DEC)', 'DA/M (D)', 'DA/M (DE)',
                      'DA/M (DC)', 'DA/M (DEC)', 'DA/M/MO (D)', 'DA/M/MO (DE)', 'DA/M/MO (DC)',
                      'DA/M/MO (DEC)', 'M (D)', 'M (DE)', 'M (DC)', 'M (DEC)', 'M/MO (D)', 'M/MO (DE)',
                      'M/MO (DC)', 'M/MO (DEC)'],
            'M (E)': ['D/DA/M (E)', 'D/DA/M (DE)', 'D/DA/M (EC)', 'D/DA/M (DEC)', 'D/DA/M/MO (E)',
                      'D/DA/M/MO (DE)', 'D/DA/M/MO (EC)', 'D/DA/M/MO (DEC)', 'DA/M (E)', 'DA/M (DE)',
                      'DA/M (EC)', 'DA/M (DEC)', 'DA/M/MO (E)', 'DA/M/MO (DE)', 'DA/M/MO (EC)',
                      'DA/M/MO (DEC)', 'M (E)', 'M (DE)', 'M (EC)', 'M (DEC)', 'M/MO (E)', 'M/MO (DE)',
                      'M/MO (EC)', 'M/MO (DEC)'],
            'MD': ['MD'],
            'M (C)': ['M (C)', 'M (DC)', 'M (EC)', 'M (DEC)', 'M/MO (C)', 'M/MO (DC)', 'M/MO (EC)', 'M/MO (DEC)'],
            'MO (C)': ['M/MO (C)', 'M/MO (DC)', 'M/MO (EC)', 'M/MO (DEC)',
                       'MO (C)', 'MO (DC)', 'MO (EC)', 'MO (DEC)'],
            'MO (D)': ['D/DA/M/MO (D)', 'D/DA/M/MO (DE)', 'D/DA/M/MO (DC)', 'D/DA/M/MO (DEC)',
                       'DA/M/MO (D)', 'DA/M/MO (DE)', 'DA/M/MO (DC)', 'DA/M/MO (DEC)',
                       'M/MO (D)', 'M/MO (DE)', 'M/MO (DC)', 'M/MO (DEC)',
                       'MO (D)', 'MO (DE)', 'MO (DC)', 'MO (DEC)'],
            'MO (E)': ['D/DA/M/MO (E)', 'D/DA/M/MO (DE)', 'D/DA/M/MO (EC)', 'D/DA/M/MO (DEC)',
                       'DA/M/MO (E)', 'DA/M/MO (DE)', 'DA/M/MO (EC)', 'DA/M/MO (DEC)',
                       'M/MO (E)', 'M/MO (DE)', 'M/MO (EC)', 'M/MO (DEC)',
                       'MO (E)', 'MO (DE)', 'MO (EC)', 'MO (DEC)'],
            'PL': ['PL (C)']
        },
        'Polish': {
            'BR': ['BR'],
            'O (Ś)': ['O (Ś)', 'O (PŚ)', 'O (LŚ)', 'O (PLŚ)'],
            'O (P)': ['O (P)', 'O (PL)', 'O (PŚ)', 'O (PLŚ)', 'O/WO (P)', 'O/WO (PL)',
                      'O/WO/P (P)', 'O/WO/P (PL)', 'O/WO/P/OP (P)', 'O/WO/P/OP (PL)',
                      'O/WO/P/OP (PŚ)', 'O/WO/P/OP (PLŚ)', 'O/P (P)', 'O/P (PL)'],
            'O (L)': ['O (L)', 'O (PL)', 'O (LŚ)', 'O (PLŚ)', 'O/WO (L)', 'O/WO (PL)',
                      'O/WO/P (L)', 'O/WO/P (PL)', 'O/WO/P/OP (L)', 'O/WO/P/OP (PL)', 'O/P (L)', 'O/P (PL)'],
            'WO (P)': ['O/WO (P)', 'O/WO (PL)', 'O/WO/P (P)', 'O/WO/P (PL)', 'O/WO/P (PŚ)',
                       'O/WO/P (PLŚ)', 'O/WO/P/OP (P)', 'O/WO/P/OP (PL)', 'O/WO/P/OP (PŚ)',
                       'O/WO/P/OP (PLŚ)', 'WO (P)', 'WO (PL)', 'WO/P (P)', 'WO/P (PL)',
                       'WO/P (PŚ)', 'WO/P (PLŚ)', 'WO/P/OP (P)', 'WO/P/OP (PL)'],
            'WO (L)': ['O/WO (L)', 'O/WO (PL)', 'O/WO/P (L)', 'O/WO/P (PL)', 'O/WO/P (LŚ)',
                       'O/WO/P (PLŚ)', 'O/WO/P/OP (L)', 'O/WO/P/OP (PL)', 'O/WO/P/OP (LŚ)',
                       'O/WO/P/OP (PLŚ)', 'WO (L)', 'WO (PL)', 'WO/P (L)', 'WO/P (PL)',
                       'WO/P (LŚ)', 'WO/P (PLŚ)', 'WO/P/OP (L)', 'WO/P/OP (PL)'],
            'P (P)': ['O/WO/P (P)', 'O/WO/P (PL)', 'O/WO/P (PŚ)', 'O/WO/P (PLŚ)', 'O/WO/P/OP (P)',
                      'O/WO/P/OP (PL)', 'O/WO/P/OP (PŚ)', 'O/WO/P/OP (PLŚ)', 'WO/P (P)', 'WO/P (PL)',
                      'WO/P (PŚ)', 'WO/P (PLŚ)', 'WO/P/OP (P)', 'WO/P/OP (PL)', 'WO/P/OP (PŚ)',
                      'WO/P/OP (PLŚ)', 'P (P)', 'P (PL)', 'P (PŚ)', 'P (PLŚ)', 'P/OP (P)', 'P/OP (PL)',
                      'P/OP (PŚ)', 'P/OP (PLŚ)'],
            'P (L)': ['O/WO/P (L)', 'O/WO/P (PL)', 'O/WO/P (LŚ)', 'O/WO/P (PLŚ)', 'O/WO/P/OP (L)',
                      'O/WO/P/OP (PL)', 'O/WO/P/OP (LŚ)', 'O/WO/P/OP (PLŚ)', 'WO/P (L)', 'WO/P (PL)',
                      'WO/P (LŚ)', 'WO/P (PLŚ)', 'WO/P/OP (L)', 'WO/P/OP (PL)', 'WO/P/OP (LŚ)',
                      'WO/P/OP (PLŚ)', 'P (L)', 'P (PL)', 'P (LŚ)', 'P (PLŚ)', 'P/OP (L)', 'P/OP (PL)',
                      'P/OP (LŚ)', 'P/OP (PLŚ)'],
            'DP': ['DP'],
            'P (Ś)': ['P (Ś)', 'P (PŚ)', 'P (LŚ)', 'P (PLŚ)', 'P/OP (Ś)', 'P/OP (PŚ)', 'P/OP (LŚ)', 'P/OP (PLŚ)'],
            'OP (Ś)': ['P/OP (Ś)', 'P/OP (PŚ)', 'P/OP (LŚ)', 'P/OP (PLŚ)',
                       'OP (Ś)', 'OP (PŚ)', 'OP (LŚ)', 'OP (PLŚ)'],
            'OP (P)': ['P/WO/P/OP (P)', 'P/WO/P/OP (PL)', 'P/WO/P/OP (PŚ)', 'P/WO/P/OP (PLŚ)',
                       'WO/P/OP (P)', 'WO/P/OP (PL)', 'WO/P/OP (PŚ)', 'WO/P/OP (PLŚ)',
                       'P/OP (P)', 'P/OP (PL)', 'P/OP (PŚ)', 'P/OP (PLŚ)',
                       'OP (P)', 'OP (PL)', 'OP (PŚ)', 'OP (PLŚ)'],
            'OP (L)': ['P/WO/P/OP (L)', 'P/WO/P/OP (PL)', 'P/WO/P/OP (LŚ)', 'P/WO/P/OP (PLŚ)',
                       'WO/P/OP (L)', 'WO/P/OP (PL)', 'WO/P/OP (LŚ)', 'WO/P/OP (PLŚ)',
                       'P/OP (L)', 'P/OP (PL)', 'P/OP (LŚ)', 'P/OP (PLŚ)',
                       'OP (L)', 'OP (PL)', 'OP (LŚ)', 'OP (PLŚ)'],
            'N': ['N (Ś)']
        },
        'Turkish': {
            'K': ['K'],
            'D (M)': ['D (M)', 'D (SğM)', 'D (SlM)', 'D (SğSlM)'],
            'D (Sğ)': ['D (Sğ)', 'D (SğSl)', 'D (SğM)', 'D (SğSlM)', 'D/KB (Sğ)', 'D/KB (SğSl)',
                      'D/KB/OS (Sğ)', 'D/KB/OS (SğSl)', 'D/KB/OS/OOS (Sğ)', 'D/KB/OS/OOS (SğSl)',
                      'D/KB/OS/OOS (SğM)', 'D/KB/OS/OOS (SğSlM)', 'D/OS (Sğ)', 'D/OS (SğSl)'],
            'D (Sl)': ['D (Sl)', 'D (SğSl)', 'D (SlM)', 'D (SğSlM)', 'D/KB (Sl)', 'D/KB (SğSl)',
                      'D/KB/OS (SI)', 'D/KB/OS (SğSl)', 'D/KB/OS/OOS (Sl)', 'D/KB/OS/OOS (SğSl)', 'D/OS (Sl)', 'D/OS (SğSl)'],
            'KB (Sğ)': ['D/KB (Sğ)', 'D/KB (SğSl)', 'D/KB/OS (Sğ)', 'D/KB/OS (SğSl)', 'D/KB/OS (SğM)',
                       'D/KB/OS (SğSlM)', 'D/KB/OS/OOS (Sğ)', 'D/KB/OS/OOS (SğSl)', 'D/KB/OS/OOS (SğM)',
                       'D/KB/OS/OOS (SğSlM)', 'KB (Sğ)', 'KB (SğSl)', 'KB/OS (Sğ)', 'KB/OS (SğSl)',
                       'KB/OS (SğM)', 'KB/OS (SğSlM)', 'KB/OS/OOS (Sğ)', 'KB/OS/OOS (SğSl)'],
            'KB (Sl)': ['D/KB (Sl)', 'D/KB (SğSl)', 'D/KB/OS (Sl)', 'D/KB/OS (SğSl)', 'D/KB/OS (SlM)',
                       'D/KB/OS (SğSlM)', 'D/KB/OS/OOS (Sl)', 'D/KB/OS/OOS (SğSl)', 'D/KB/OS/OOS (SlM)',
                       'D/KB/OS/OOS (SğSlM)', 'KB (Sl)', 'KB (SğSl)', 'KB/OS (Sl)', 'KB/OS (SğSl)',
                       'KB/OS (SlM)', 'KB/OS (SğSlM)', 'KB/OS/OOS (Sl)', 'KB/OS/OOS (SğSl)'],
            'OS (Sğ)': ['D/KB/OS (Sğ)', 'D/KB/OS (SğSl)', 'D/KB/OS (SğM)', 'D/KB/OS (SğSlM)', 'D/KB/OS/OOS (Sğ)',
                      'D/KB/OS/OOS (SğSl)', 'D/KB/OS/OOS (SğM)', 'D/KB/OS/OOS (SğSlM)', 'KB/OS (Sğ)', 'KB/OS (SğSl)',
                      'KB/OS (SğM)', 'KB/OS (SğSlM)', 'KB/OS/OOS (Sğ)', 'KB/OS/OOS (SğSl)', 'KB/OS/OOS (SğM)',
                      'KB/OS/OOS (SğSlM)', 'OS (Sğ)', 'OS (SğSl)', 'OS (SğM)', 'OS (SğSlM)', 'OS/OOS (Sğ)', 'OS/OOS (SğSl)',
                      'OS/OOS (SğM)', 'OS/OOS (SğSlM)'],
            'OS (Sl)': ['D/KB/OS (Sl)', 'D/KB/OS (SğSl)', 'D/KB/OS (SlM)', 'D/KB/OS (SğSlM)', 'D/KB/OS/OOS (Sl)',
                      'D/KB/OS/OOS (SğSl)', 'D/KB/OS/OOS (SlM)', 'D/KB/OS/OOS (SğSlM)', 'KB/OS (Sl)', 'KB/OS (SğSl)',
                      'KB/OS (SlM)', 'KB/OS (SğSlM)', 'KB/OS/OOS (Sl)', 'KB/OS/OOS (SğSl)', 'KB/OS/OOS (SlM)',
                      'KB/OS/OOS (SğSlM)', 'OS (Sl)', 'OS (SğSl)', 'OS (SlM)', 'OS (SğSlM)', 'OS/OOS (Sl)', 'OS/OOS (SğSl)',
                      'OS/OOS (SlM)', 'OS/OOS (SğSlM)'],
            'DOS': ['DOS'],
            'OS (M)': ['OS (M)', 'OS (SğM)', 'OS (SlM)', 'OS (SğSlM)', 'OS/OOS (M)', 'OS/OOS (SğM)', 'OS/OOS (SlM)', 'OS/OOS (SğSlM)'],
            'OOS (M)': ['OS/OOS (M)', 'OS/OOS (SğM)', 'OS/OOS (SlM)', 'OS/OOS (SğSlM)',
                       'OOS (M)', 'OOS (SğM)', 'OOS (SlM)', 'OOS (SğSlM)'],
            'OOS (Sğ)': ['OS/KB/OS/OOS (Sğ)', 'OS/KB/OS/OOS (SğSl)', 'OS/KB/OS/OOS (SğM)', 'OS/KB/OS/OOS (SğSlM)',
                       'KB/OS/OOS (Sğ)', 'KB/OS/OOS (SğSl)', 'KB/OS/OOS (SğM)', 'KB/OS/OOS (SğSlM)',
                       'OS/OOS (Sğ)', 'OS/OOS (SğSl)', 'OS/OOS (SğM)', 'OS/OOS (SğSlM)',
                       'OOS (Sğ)', 'OOS (SğSl)', 'OOS (SğM)', 'OOS (SğSlM)'],
            'OOS (Sl)': ['OS/KB/OS/OOS (Sl)', 'OS/KB/OS/OOS (SğSl)', 'OS/KB/OS/OOS (SlM)', 'OS/KB/OS/OOS (SğSlM)',
                       'KB/OS/OOS (Sl)', 'KB/OS/OOS (SğSl)', 'KB/OS/OOS (SlM)', 'KB/OS/OOS (SğSlM)',
                       'OS/OOS (Sl)', 'OS/OOS (SğSl)', 'OS/OOS (SlM)', 'OS/OOS (SğSlM)',
                       'OOS (Sl)', 'OOS (SğSl)', 'OOS (SlM)', 'OOS (SğSlM)'],
            'ST': ['ST (M)']
        },
        'Greek': {
            'ΤΦ': ['ΤΦ'],
            'Α (Κ)': ['Α (Κ)', 'Α (ΔΚ)', 'Α (ΑΚ)', 'Α (ΔΑΚ)'],
            'Α (Δ)': ['Α (Δ)', 'Α (ΔΑ)', 'Α (ΔΚ)', 'Α (ΔΑΚ)', 'Α/ΜΧ (Δ)', 'Α/ΜΧ (ΔΑ)',
                      'Α/ΜΧ/Μ (Δ)', 'Α/ΜΧ/Μ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (Δ)', 'Α/ΜΧ/Μ/EΜ (ΔΑ)',
                      'Α/ΜΧ/Μ/EΜ (ΔΚ)', 'Α/ΜΧ/Μ/EΜ (ΔΑΚ)', 'Α/Μ (Δ)', 'Α/Μ (ΔΑ)'],
            'Α (Α)': ['Α (Α)', 'Α (ΔΑ)', 'Α (ΑΚ)', 'Α (ΔΑΚ)', 'Α/ΜΧ (Α)', 'Α/ΜΧ (ΔΑ)',
                      'Α/ΜΧ/Μ (Α)', 'Α/ΜΧ/Μ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (Α)', 'Α/ΜΧ/Μ/EΜ (ΔΑ)', 'Α/Μ (Α)', 'Α/Μ (ΔΑ)'],
            'ΜΧ (Δ)': ['Α/ΜΧ (Δ)', 'Α/ΜΧ (ΔΑ)', 'Α/ΜΧ/Μ (Δ)', 'Α/ΜΧ/Μ (ΔΑ)', 'Α/ΜΧ/Μ (ΔΚ)',
                       'Α/ΜΧ/Μ (ΔΑΚ)', 'Α/ΜΧ/Μ/EΜ (Δ)', 'Α/ΜΧ/Μ/EΜ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (ΔΚ)',
                       'Α/ΜΧ/Μ/EΜ (ΔΑΚ)', 'ΜΧ (Δ)', 'ΜΧ (ΔΑ)', 'ΜΧ/Μ (Δ)', 'ΜΧ/Μ (ΔΑ)',
                       'ΜΧ/Μ (ΔΚ)', 'ΜΧ/Μ (ΔΑΚ)', 'ΜΧ/Μ/EΜ (Δ)', 'ΜΧ/Μ/EΜ (ΔΑ)'],
            'ΜΧ (Α)': ['Α/ΜΧ (Α)', 'Α/ΜΧ (ΔΑ)', 'Α/ΜΧ/Μ (Α)', 'Α/ΜΧ/Μ (ΔΑ)', 'Α/ΜΧ/Μ (ΑΚ)',
                       'Α/ΜΧ/Μ (ΔΑΚ)', 'Α/ΜΧ/Μ/EΜ (Α)', 'Α/ΜΧ/Μ/EΜ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (ΑΚ)',
                       'Α/ΜΧ/Μ/EΜ (ΔΑΚ)', 'ΜΧ (Α)', 'ΜΧ (ΔΑ)', 'ΜΧ/Μ (Α)', 'ΜΧ/Μ (ΔΑ)',
                       'ΜΧ/Μ (ΑΚ)', 'ΜΧ/Μ (ΔΑΚ)', 'ΜΧ/Μ/EΜ (Α)', 'ΜΧ/Μ/EΜ (ΔΑ)'],
            'Μ (Δ)': ['Α/ΜΧ/Μ (Δ)', 'Α/ΜΧ/Μ (ΔΑ)', 'Α/ΜΧ/Μ (ΔΚ)', 'Α/ΜΧ/Μ (ΔΑΚ)', 'Α/ΜΧ/Μ/EΜ (Δ)',
                      'Α/ΜΧ/Μ/EΜ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (ΔΚ)', 'Α/ΜΧ/Μ/EΜ (ΔΑΚ)', 'ΜΧ/Μ (Δ)', 'ΜΧ/Μ (ΔΑ)',
                      'ΜΧ/Μ (ΔΚ)', 'ΜΧ/Μ (ΔΑΚ)', 'ΜΧ/Μ/EΜ (Δ)', 'ΜΧ/Μ/EΜ (ΔΑ)', 'ΜΧ/Μ/EΜ (ΔΚ)',
                      'ΜΧ/Μ/EΜ (ΔΑΚ)', 'Μ (Δ)', 'Μ (ΔΑ)', 'Μ (ΔΚ)', 'Μ (ΔΑΚ)', 'Μ/EΜ (Δ)', 'Μ/EΜ (ΔΑ)',
                      'Μ/ΕΜ (ΔΚ)', 'Μ/ΕΜ (ΔΑΚ)'],
            'Μ (Α)': ['Α/ΜΧ/Μ (Α)', 'Α/ΜΧ/Μ (ΔΑ)', 'Α/ΜΧ/Μ (ΑΚ)', 'Α/ΜΧ/Μ (ΔΑΚ)', 'Α/ΜΧ/Μ/EΜ (Α)',
                      'Α/ΜΧ/Μ/EΜ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (ΑΚ)', 'Α/ΜΧ/Μ/EΜ (ΔΑΚ)', 'ΜΧ/Μ (Α)', 'ΜΧ/Μ (ΔΑ)',
                      'ΜΧ/Μ (ΑΚ)', 'ΜΧ/Μ (ΔΑΚ)', 'ΜΧ/Μ/EΜ (Α)', 'ΜΧ/Μ/EΜ (ΔΑ)', 'ΜΧ/Μ/EΜ (ΑΚ)',
                      'ΜΧ/Μ/EΜ (ΔΑΚ)', 'Μ (Α)', 'Μ (ΔΑ)', 'Μ (ΑΚ)', 'Μ (ΔΑΚ)', 'Μ/EΜ (Α)', 'Μ/EΜ (ΔΑ)',
                      'Μ/EΜ (ΑΚ)', 'Μ/ΕΜ (ΔΑΚ)'],
            'ΑΜ': ['ΑΜ'],
            'Μ (Κ)': ['Μ (Κ)', 'Μ (ΔΚ)', 'Μ (ΑΚ)', 'Μ (ΔΑΚ)', 'Μ/ΕΜ (Κ)', 'Μ/ΕΜ (ΔΚ)', 'Μ/EΜ (ΑΚ)', 'Μ/EΜ (ΔΑΚ)'],
            'ΕΜ (Κ)': ['Μ/ΕΜ (Κ)', 'Μ/EΜ (ΔΚ)', 'Μ/EΜ (ΑΚ)', 'Μ/ΕΜ (ΔΑΚ)',
                       'EΜ (Κ)', 'EΜ (ΔΚ)', 'EΜ (ΑΚ)', 'EΜ (ΔΑΚ)'],
            'EΜ (Δ)': ['Α/ΜΧ/Μ/EΜ (Δ)', 'Α/ΜΧ/Μ/EΜ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (ΔΚ)', 'Α/ΜΧ/Μ/EΜ (ΔΑΚ)',
                       'ΜΧ/Μ/EΜ (Δ)', 'ΜΧ/Μ/EΜ (ΔΑ)', 'ΜΧ/Μ/EΜ (ΔΚ)', 'ΜΧ/Μ/EΜ (ΔΑΚ)',
                       'Μ/EΜ (Δ)', 'Μ/EΜ (ΔΑ)', 'Μ/EΜ (ΔΚ)', 'Μ/ΕΜ (ΔΑΚ)',
                       'EΜ (Δ)', 'ΕΜ (ΔΑ)', 'EΜ (ΔΚ)', 'ΕΜ (ΔΑΚ)'],
            'ΕΜ (Α)': ['Α/ΜΧ/Μ/EΜ (Α)', 'Α/ΜΧ/Μ/EΜ (ΔΑ)', 'Α/ΜΧ/Μ/EΜ (ΑΚ)', 'Α/ΜΧ/Μ/EΜ (ΔΑΚ)',
                       'ΜΧ/Μ/EΜ (Α)', 'ΜΧ/Μ/EΜ (ΔΑ)', 'ΜΧ/Μ/EΜ (ΑΚ)', 'ΜΧ/Μ/EΜ (ΔΑΚ)',
                       'Μ/EΜ (Α)', 'Μ/EΜ (ΔΑ)', 'Μ/EΜ (ΑΚ)', 'Μ/ΕΜ (ΔΑΚ)',
                       'EΜ (Α)', 'ΕΜ (ΔΑ)', 'EΜ (ΑΚ)', 'EΜ (ΔΑΚ)'],
            'ΕΠ': ['ΕΠ (Κ)']
        },
        'Russian': {
            'В': ['В'],
            'З (Ц)': ['З (Ц)', 'З (ПЦ)', 'З (ЛЦ)', 'З (ПЛЦ)'],
            'З (П)': ['З (П)', 'З (ПЛ)', 'З (ПЦ)', 'З (ПЛЦ)', 'З/KЗ (П)', 'З/KЗ (ПЛ)',
                      'З/KЗ/П (П)', 'З/KЗ/П (ПЛ)', 'З/KЗ/П/АП (П)', 'З/KЗ/П/АП (ПЛ)',
                      'З/KЗ/П/АП (ПЦ)', 'З/KЗ/П/АП (ПЛЦ)', 'З/П (П)', 'З/П (ПЛ)'],
            'З (Л)': ['З (Л)', 'З (ПЛ)', 'З (ЛЦ)', 'З (ПЛЦ)', 'З/KЗ (Л)', 'З/KЗ (ПЛ)',
                      'З/KЗ/П (Л)', 'З/KЗ/П (ПЛ)', 'З/KЗ/П/АП (Л)', 'З/KЗ/П/АП (ПЛ)', 'З/П (Л)', 'З/П (ПЛ)'],
            'KЗ (П)': ['З/KЗ (П)', 'З/KЗ (ПЛ)', 'З/KЗ/П (П)', 'З/KЗ/П (ПЛ)', 'З/KЗ/П (ПЦ)',
                       'З/KЗ/П (ПЛЦ)', 'З/KЗ/П/АП (П)', 'З/KЗ/П/АП (ПЛ)', 'З/KЗ/П/АП (ПЦ)',
                       'З/KЗ/П/АП (ПЛЦ)', 'KЗ (П)', 'KЗ (ПЛ)', 'KЗ/П (П)', 'KЗ/П (ПЛ)',
                       'KЗ/П (ПЦ)', 'KЗ/П (ПЛЦ)', 'KЗ/П/АП (П)', 'KЗ/П/АП (ПЛ)'],
            'KЗ (Л)': ['З/KЗ (Л)', 'З/KЗ (ПЛ)', 'З/KЗ/П (Л)', 'З/KЗ/П (ПЛ)', 'З/KЗ/П (ЛЦ)',
                       'З/KЗ/П (ПЛЦ)', 'З/KЗ/П/АП (Л)', 'З/KЗ/П/АП (ПЛ)', 'З/KЗ/П/АП (ЛЦ)',
                       'З/KЗ/П/АП (ПЛЦ)', 'KЗ (Л)', 'KЗ (ПЛ)', 'KЗ/П (Л)', 'KЗ/П (ПЛ)',
                       'KЗ/П (ЛЦ)', 'KЗ/П (ПЛЦ)', 'KЗ/П/АП (Л)', 'KЗ/П/АП (ПЛ)'],
            'П (П)': ['З/KЗ/П (П)', 'З/KЗ/П (ПЛ)', 'З/KЗ/П (ПЦ)', 'З/KЗ/П (ПЛЦ)', 'З/KЗ/П/АП (П)',
                      'З/KЗ/П/АП (ПЛ)', 'З/KЗ/П/АП (ПЦ)', 'З/KЗ/П/АП (ПЛЦ)', 'KЗ/П (П)', 'KЗ/П (ПЛ)',
                      'KЗ/П (ПЦ)', 'KЗ/П (ПЛЦ)', 'KЗ/П/АП (П)', 'KЗ/П/АП (ПЛ)', 'KЗ/П/АП (ПЦ)',
                      'KЗ/П/АП (ПЛЦ)', 'П (П)', 'П (ПЛ)', 'П (ПЦ)', 'П (ПЛЦ)', 'П/АП (П)', 'П/АП (ПЛ)',
                      'П/АП (ПЦ)', 'П/АП (ПЛЦ)'],
            'П (Л)': ['З/KЗ/П (Л)', 'З/KЗ/П (ПЛ)', 'З/KЗ/П (ЛЦ)', 'З/KЗ/П (ПЛЦ)', 'З/KЗ/П/АП (Л)',
                      'З/KЗ/П/АП (ПЛ)', 'З/KЗ/П/АП (ЛЦ)', 'З/KЗ/П/АП (ПЛЦ)', 'KЗ/П (Л)', 'KЗ/П (ПЛ)',
                      'KЗ/П (ЛЦ)', 'KЗ/П (ПЛЦ)', 'KЗ/П/АП (Л)', 'KЗ/П/АП (ПЛ)', 'KЗ/П/АП (ЛЦ)',
                      'KЗ/П/АП (ПЛЦ)', 'П (Л)', 'П (ПЛ)', 'П (ЛЦ)', 'П (ПЛЦ)', 'П/АП (Л)', 'П/АП (ПЛ)',
                      'П/АП (ЛЦ)', 'П/АП (ПЛЦ)'],
            'ОП': ['ОП'],
            'П (Ц)': ['П (Ц)', 'П (ПЦ)', 'П (ЛЦ)', 'П (ПЛЦ)', 'П/АП (Ц)', 'П/АП (ПЦ)', 'П/АП (ЛЦ)', 'П/АП (ПЛЦ)'],
            'АП (Ц)': ['П/АП (Ц)', 'П/АП (ПЦ)', 'П/АП (ЛЦ)', 'П/АП (ПЛЦ)',
                       'АП (Ц)', 'АП (ПЦ)', 'АП (ЛЦ)', 'АП (ПЛЦ)'],
            'АП (П)': ['D/KЗ/П/АП (П)', 'D/KЗ/П/АП (ПЛ)', 'D/KЗ/П/АП (ПЦ)', 'D/KЗ/П/АП (ПЛЦ)',
                       'KЗ/П/АП (П)', 'KЗ/П/АП (ПЛ)', 'KЗ/П/АП (ПЦ)', 'KЗ/П/АП (ПЛЦ)',
                       'П/АП (П)', 'П/АП (ПЛ)', 'П/АП (ПЦ)', 'П/АП (ПЛЦ)',
                       'АП (П)', 'АП (ПЛ)', 'АП (ПЦ)', 'АП (ПЛЦ)'],
            'АП (Л)': ['D/KЗ/П/АП (Л)', 'D/KЗ/П/АП (ПЛ)', 'D/KЗ/П/АП (ЛЦ)', 'D/KЗ/П/АП (ПЛЦ)',
                       'KЗ/П/АП (Л)', 'KЗ/П/АП (ПЛ)', 'KЗ/П/АП (ЛЦ)', 'KЗ/П/АП (ПЛЦ)',
                       'П/АП (Л)', 'П/АП (ПЛ)', 'П/АП (ЛЦ)', 'П/АП (ПЛЦ)',
                       'АП (Л)', 'АП (ПЛ)', 'АП (ЛЦ)', 'АП (ПЛЦ)'],
            'НП': ['НП (Ц)']
        }
    }

# Attribute filters (make this international)
attribute_filters = {
    'Overall': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Speed', 'Physical', 'Defending', 'Mental', 'Aerial', 'Technical', 'Attacking', 'Vision'
    ],
    'GK Overall': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Speed', 'Physical', 'Shot Stopping', 'Distribution', 'Aerial (GK)', 'Eccentricity', 'Communication', 'Mental'
    ],
    'Technical': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Cor', 'Cro', 'Dri', 'Fin', 'Fir', 'Fre', 'Hea', 'Lon', 'L Th', 'Mar', 'Pas', 'Pen', 'Tck', 'Tec'
    ],
    'Mental': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Det', 'Fla', 'Ldr', 'OtB', 'Pos', 'Tea', 'Vis', 'Wor'
    ],
    'Physical': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Acc', 'Agi', 'Bal', 'Jum', 'Nat', 'Pac', 'Sta', 'Str'
    ],
    'Goalkeeper': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Aer', 'Agi', 'Ant', 'Cnt', 'Pos', 'Cmd', 'Com', 'Han', 'Kic', '1v1', 'Ref'
    ],
    'Central Defender': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Jum', 'Str', 'Agg', 'Bra', 'Cnt', 'Dec', 'Pos', 'Hea', 'Mar', 'Tck'
    ],
    'Full-back': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Ant', 'Cnt', 'Pos', 'Tea', 'Cro', 'Mar', 'Tck'
    ],
    'Wing-Back': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Acc', 'Pac', 'Sta', 'Ant', 'OtB', 'Pos', 'Tea', 'Wor', 'Cro', 'Dri', 'Mar', 'Tck', 'Tec'
    ],
    'Defensive Midfielder': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Pac', 'Sta', 'Ant', 'Cnt', 'Dec', 'Pos', 'Tea', 'Wor', 'Mar', 'Tck'
    ],
    'Central Midfielder': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Acc', 'Sta', 'Cmp', 'Cnt', 'Dec', 'OtB', 'Tea', 'Fir', 'Pas', 'Tck'
    ],
    'Attacking Midfielder': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Acc', 'Ant', 'Cmp', 'Dec', 'Fla', 'OtB', 'Vis', 'Dri', 'Fir', 'Lon', 'Pas', 'Tec'
    ],
    'Winger': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Acc', 'Agi', 'Sta', 'Dec', 'Wor', 'Cro', 'Dri', 'Pas', 'Tec'
    ],
    'Striker': [
        'Name', 'Age', 'Position', 'Club', 'Division',
        'Acc', 'Agi', 'Str', 'Ant', 'Cmp', 'Dec', 'OtB', 'Fir', 'Fin', 'Hea', 'Lon', 'Tec'
    ],
    # Role Score Filters
    'Goalkeeper - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'G-De', 'SK-De', 'SK-Su', 'SK-At'
    ],
    'Central Defender - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'CD-De', 'CD-St', 'CD-Co', 'NCB-De', 'NCB-St', 'NCB-Co',
        'WCB-De', 'WCB-Su', 'WCB-At', 'BPD-De', 'BPD-St', 'BPD-Co', 'L-De', 'L-Su'
    ],
    'Full-back & Wing-back - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'FB-De', 'FB-Su', 'FB-At', 'FB-Au', 'NFB-De', 'IFB-De',
        'WB-De', 'WB-Su', 'WB-At', 'WB-Au', 'CWB-Su', 'CWB-At', 'IWB-De', 'IWB-Su', 'IWB-At'
    ],
    'Defensive Midfielder - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'A-De', 'HB-De', 'DM-De', 'DM-Su', 'VOL-Su', 'VOL-At',
        'RGA-Su', 'BWM-De', 'BWM-Su', 'DLP-De', 'DLP-Su', 'RPM-Su'
    ],
    'Central Midfielder - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'BWM-De', 'BWM-Su', 'DLP-De', 'DLP-Su', 'RPM-Su', 'CAR-Su',
        'BBM-Su', 'CM-De', 'CM-Su', 'CM-At', 'CM-Au', 'MEZ-Su', 'MEZ-At', 'AP-Su', 'AP-At'
    ],
    'Winger - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'DW-De', 'DW-Su', 'WM-De', 'WM-Su', 'WM-At', 'WM-Au',
        'WP-Su', 'WP-At', 'IW-Su', 'IW-At', 'W-Su', 'W-At', 'IF-Su', 'IF-At', 'RMD-At', 'WT-Su', 'WT-At',
    ],
    'Attacking Midfielder - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'AP-Su', 'AP-At', 'T-At', 'EG-Su', 'AM-Su', 'AM-At', 'SS-At'
    ],
    'Striker - Role Scores': [
        'Name', 'Age', 'Position', 'Club', 'Division', 'AF-At', 'P-At', 'F9-Su', 'TF-Su', 'TF-At', 'DLF-Su',
        'DLF-At', 'PF-De', 'PF-Su', 'PF-At', 'CF-Su', 'CF-At'
    ]
}

attributes_filters_by_index = {
        'Overall': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            53, 60, 59, 58, 57, 56, 55, 54 #'Speed', 'Physical', 'Defending', 'Mental', 'Aerial', 'Technical', 'Attacking', 'Vision'
        ],
        'GK Overall': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            53, 60, 62, 63, 61, 65, 64, 58 #'Speed', 'Physical', 'Shot Stopping', 'Distribution', 'Aerial (GK)', 'Eccentricity', 'Communication', 'Mental'
        ],
        'Technical': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            41, 40, 37, 35, 34, 32, 30, 26, 25, 24, 19, 18, 11, 9 #'Cor', 'Cro', 'Dri', 'Fin', 'Fir', 'Fre', 'Hea', 'Lon', 'L Th', 'Mar', 'Pas', 'Pen', 'Tck', 'Tec'
        ],
        'Mental': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            50, 48, 46, 43, 42, 39, 38, 33, 27, 22, 17, 10, 7, 6 #'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Det', 'Fla', 'Ldr', 'OtB', 'Pos', 'Tea', 'Vis', 'Wor'
        ],
        'Physical': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            5, 49, 47, 29, 23, 20, 13, 12 #'Acc', 'Agi', 'Bal', 'Jum', 'Nat', 'Pac', 'Sta', 'Str'
        ],
        'Goalkeeper': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            51, 49, 48, 42, 17, 45, 44, 31, 28, 21, 15 #'Aer', 'Agi', 'Ant', 'Cnt', 'Pos', 'Cmd', 'Com', 'Han', 'Kic', '1v1', 'Ref'
        ],
        'Central Defender': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            29, 12, 50, 46, 42, 39, 17, 30, 24, 11 #'Jum', 'Str', 'Agg', 'Bra', 'Cnt', 'Dec', 'Pos', 'Hea', 'Mar', 'Tck'
        ],
        'Full-back': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            48, 42, 17, 10, 40, 24, 11 #'Ant', 'Cnt', 'Pos', 'Tea', 'Cro', 'Mar', 'Tck'
        ],
        'Wing-Back': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            5, 20, 13, 48, 22, 17, 10, 6, 40, 37, 24, 11, 9 #'Acc', 'Pac', 'Sta', 'Ant', 'OtB', 'Pos', 'Tea', 'Wor', 'Cro', 'Dri', 'Mar', 'Tck', 'Tec'
        ],
        'Defensive Midfielder': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            20, 13, 48, 42, 39, 17, 10, 6, 24, 11 #'Pac', 'Sta', 'Ant', 'Cnt', 'Dec', 'Pos', 'Tea', 'Wor', 'Mar', 'Tck'
        ],
        'Central Midfielder': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            5, 13, 43, 42, 39, 22, 10, 34, 19, 11 #'Acc', 'Sta', 'Cmp', 'Cnt', 'Dec', 'OtB', 'Tea', 'Fir', 'Pas', 'Tck'
        ],
        'Attacking Midfielder': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            5, 48, 43, 39, 33, 22, 7, 37, 34, 26, 19, 9 #'Acc', 'Ant', 'Cmp', 'Dec', 'Fla', 'OtB', 'Vis', 'Dri', 'Fir', 'Lon', 'Pas', 'Tec'
        ],
        'Winger': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            5, 49, 13, 39, 6, 40, 37, 19, 9 #'Acc', 'Agi', 'Sta', 'Dec', 'Wor', 'Cro', 'Dri', 'Pas', 'Tec'
        ],
        'Striker': [
            0, 2, 1, 3, 4, #'Name', 'Age', 'Position', 'Club', 'Division',
            5, 49, 12, 48, 43, 39, 22, 34, 35, 30, 26, 9 #'Acc', 'Agi', 'Str', 'Ant', 'Cmp', 'Dec', 'OtB', 'Fir', 'Fin', 'Hea', 'Lon', 'Tec'
        ],
        # Role Score Filters
        'Goalkeeper - Role Scores': [
            0, 2, 1, 3, 4, 80, 81, 82, 83 #'G-De', 'SK-De', 'SK-Su', 'SK-At'
        ],
        'Central Defender - Role Scores': [
            0, 2, 1, 3, 4, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97
            #'CD-De', 'CD-St', 'CD-Co', 'NCB-De', 'NCB-St', 'NCB-Co', 'WCB-De', 'WCB-Su', 'WCB-At', 'BPD-De', 'BPD-St',
            #'BPD-Co', 'L-De', 'L-Su'
        ],
        'Full-back & Wing-back - Role Scores': [
            0, 2, 1, 3, 4, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112
            #'FB-De', 'FB-Su', 'FB-At', 'FB-Au', 'NFB-De', 'IFB-De', 'WB-De', 'WB-Su', 'WB-At', 'WB-Au', 'CWB-Su', 'CWB-At', 'IWB-De', 'IWB-Su', 'IWB-At'
        ],
        'Defensive Midfielder - Role Scores': [
            0, 2, 1, 3, 4, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124
            #'A-De', 'HB-De', 'DM-De', 'DM-Su', 'VOL-Su', 'VOL-At', 'RGA-Su', 'BWM-De', 'BWM-Su', 'DLP-De', 'DLP-Su', 'RPM-Su'
        ],
        'Central Midfielder - Role Scores': [
            0, 2, 1, 3, 4, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134
            #'BWM-De', 'BWM-Su', 'DLP-De', 'DLP-Su', 'RPM-Su', 'CAR-Su', 'BBM-Su', 'CM-De', 'CM-Su', 'CM-At', 'CM-Au', 'MEZ-Su', 'MEZ-At', 'AP-Su', 'AP-At'
        ],
        'Winger - Role Scores': [
            0, 2, 1, 3, 4, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151
            #'DW-De', 'DW-Su', 'WM-De', 'WM-Su', 'WM-At', 'WM-Au', 'WP-Su', 'WP-At', 'IW-Su', 'IW-At', 'W-Su', 'W-At', 'IF-Su', 'IF-At', 'RMD-At', 'WT-Su', 'WT-At',
        ],
        'Attacking Midfielder - Role Scores': [
            0, 2, 1, 3, 4, 133, 134, 152, 153, 154, 155, 156
            #'AP-Su', 'AP-At', 'T-At', 'EG-Su', 'AM-Su', 'AM-At', 'SS-At'
        ],
        'Striker - Role Scores': [
            0, 2, 1, 3, 4, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168
            #'AF-At', 'P-At', 'F9-Su', 'TF-Su', 'TF-At', 'DLF-Su', 'DLF-At', 'PF-De', 'PF-Su', 'PF-At', 'CF-Su', 'CF-At'
        ]
}

# Role name dictionaries
international_role_name_dict = {
    'English': [
        'G-De', 'SK-De', 'SK-Su', 'SK-At',

        'CD-De', 'CD-St', 'CD-Co', 'NCB-De', 'NCB-St', 'NCB-Co',
        'WCB-De', 'WCB-Su', 'WCB-At', 'BPD-De', 'BPD-St', 'BPD-Co', 'L-De', 'L-Su',

        'FB-De', 'FB-Su', 'FB-At', 'FB-Au', 'NFB-De', 'IFB-De',
        'WB-De', 'WB-Su', 'WB-At', 'WB-Au', 'CWB-Su', 'CWB-At', 'IWB-De', 'IWB-Su', 'IWB-At',

        'A-De', 'HB-De', 'DM-De', 'DM-Su', 'VOL-Su', 'VOL-At',
        'RGA-Su', 'BWM-De', 'BWM-Su', 'DLP-De', 'DLP-Su', 'RPM-Su',

        'CAR-Su', 'BBM-Su', 'CM-De', 'CM-Su', 'CM-At', 'CM-Au', 'MEZ-Su', 'MEZ-At', 'AP-Su', 'AP-At',

        'DW-De', 'DW-Su', 'WM-De', 'WM-Su', 'WM-At', 'WM-Au',
        'WP-Su', 'WP-At', 'IW-Su', 'IW-At', 'W-Su', 'W-At', 'IF-Su', 'IF-At', 'RMD-At', 'WT-Su', 'WT-At',

        'T-At', 'EG-Su', 'AM-Su', 'AM-At', 'SS-At',

        'AF-At', 'P-At', 'F9-Su', 'TF-Su', 'TF-At', 'DLF-Su',
        'DLF-At', 'PF-De', 'PF-Su', 'PF-At', 'CF-Su', 'CF-At'
        ],
    'English (US)': [
        'G-De', 'SK-De', 'SK-Su', 'SK-At',

        'CD-De', 'CD-St', 'CD-Co', 'NCB-De', 'NCB-St', 'NCB-Co',
        'WCB-De', 'WCB-Su', 'WCB-At', 'BPD-De', 'BPD-St', 'BPD-Co', 'L-De', 'L-Su',

        'FB-De', 'FB-Su', 'FB-At', 'FB-Au', 'NFB-De', 'IFB-De',
        'WB-De', 'WB-Su', 'WB-At', 'WB-Au', 'CWB-Su', 'CWB-At', 'IWB-De', 'IWB-Su', 'IWB-At',

        'A-De', 'HB-De', 'DM-De', 'DM-Su', 'VOL-Su', 'VOL-At',
        'RGA-Su', 'BWM-De', 'BWM-Su', 'DLP-De', 'DLP-Su', 'RPM-Su',

        'CAR-Su', 'BBM-Su', 'CM-De', 'CM-Su', 'CM-At', 'CM-Au', 'MEZ-Su', 'MEZ-At', 'AP-Su', 'AP-At',

        'DW-De', 'DW-Su', 'WM-De', 'WM-Su', 'WM-At', 'WM-Au',
        'WP-Su', 'WP-At', 'IW-Su', 'IW-At', 'W-Su', 'W-At', 'IF-Su', 'IF-At', 'RMD-At', 'WT-Su', 'WT-At',

        'T-At', 'EG-Su', 'AM-Su', 'AM-At', 'SS-At',

        'AF-At', 'P-At', 'F9-Su', 'TF-Su', 'TF-At', 'DLF-Su',
        'DLF-At', 'PF-De', 'PF-Su', 'PF-At', 'CF-Su', 'CF-At'
        ],
    'Japanese': [
        'G-守', 'SK-守', 'SK-サ', 'SK-攻',

        'CD-守', 'CD-ス', 'CD-カ', 'NCB-守', 'NCB-ス', 'NCB-カ',
        'WCB-守', 'WCB-サ', 'WCB-攻', 'BPD-守', 'BPD-ス', 'BPD-カ', 'L-守', 'L-サ',

        'FB-守', 'FB-サ', 'FB-攻', 'FB-自', 'NSB-守', 'IFB-守',
        'WB-守', 'WB-サ', 'WB-攻', 'WB-自', 'CWB-サ', 'CWB-攻', 'IWB-守', 'IWB-サ', 'IWB-攻',

        'A-守', 'HB-守', 'DM-守', 'DM-サ', 'VOL-サ', 'VOL-攻',
        'RGA-サ', 'BWM-守', 'BWM-サ', 'DLP-守', 'DLP-サ', 'RPM-サ',

        'CAR-サ', 'BBM-サ', 'CM-守', 'CM-サ', 'CM-攻', 'CM-自', 'MEZ-サ', 'MEZ-攻', 'AP-サ', 'AP-攻',

        'DW-守', 'DW-サ', 'WM-守', 'WM-サ', 'WM-攻', 'WM-自',
        'WP-サ', 'WP-攻', 'IW-サ', 'IW-攻', 'W-サ', 'W-攻', 'IF-サ', 'IF-攻', 'RMD-攻', 'WT-サ', 'WT-攻',

        'T-攻', 'EG-サ', 'AM-サ', 'AM-攻', 'SS-攻',

        'AF-攻', 'P-攻', 'F9-サ', 'TF-サ', 'TF-攻', 'DLF-サ',
        'DLF-攻', 'PF-守', 'PF-サ', 'PF-攻', 'CF-サ', 'CF-攻'
        ],
    'Korean': [
        'G-De', 'Sk-De', 'Sk-Su', 'Sk-At',

        'CD-De', 'CD-St', 'CD-Co', 'NCB-De', 'NCB-St', 'NCB-Co',
        'WCB-De', 'WCB-Su', 'WCB-At', 'BPD-De', 'BPD-St', 'BPD-Co', 'L-De', 'L-Su',

        'FB-De', 'FB-Su', 'FB-At', 'FB-Au', 'NFB-De', 'IFB-De',
        'WB-De', 'WB-Su', 'WB-At', 'WB-Au', 'CWB-Su', 'CWB-At', 'IWB-De', 'IWB-Su', 'IWB-At',

        'A-De', 'HB-De', 'DM-De', 'DM-Su', 'VOL-Su', 'VOL-At',
        'RGA-Su', 'BWM-De', 'BWM-Su', 'DLP-De', 'DLP-Su', 'RPM-Su',

        'CAR-Su', 'BBM-Su', 'CM-De', 'CM-Su', 'CM-At', 'CM-Au', 'MEZ-Su', 'MEZ-At', 'AP-Su', 'AP-At',

        'DW-De', 'DW-Su', 'WM-De', 'WM-Su', 'WM-At', 'WM-Au',
        'WP-Su', 'WP-At', 'IW-Su', 'IW-At', 'W-Su', 'W-At', 'IF-Su', 'IF-At', 'RMD-At', 'WT-Su', 'WT-At',

        'T-At', 'EG-Su', 'AM-Su', 'AM-At', 'SS-At',

        'AF-At', 'P-At', 'F9-Su', 'TF-Su', 'TF-At', 'DLF-Su',
        'DLF-At', 'PF-De', 'PF-Su', 'PF-At', 'CF-Su', 'CF-At'
        ],
    'Spanish': [
        'POR-De', 'PCI-De', 'PCI-Ap', 'PCI-At',

        'DFC-De', 'DFC-Ta', 'DFC-Co', 'DPr-De', 'DPr-Ta', 'DPr-Co',
        'CLT-De', 'CLT-Ap', 'CLT-At', 'DCT-De', 'DCT-Ta', 'DCT-Co', 'LIB-De', 'LIB-Ap',

        'LAT-De', 'LAT-Ap', 'LAT-At', 'LAT-Au', 'LP-De', 'LPC-De',
        'CAR-De', 'CAR-Ap', 'CAR-At', 'CAR-Au', 'CRC-Ap', 'CRC-At', 'CIN-De', 'CIN-Ap', 'CIN-At',

        'PVD-De', 'MCI-De', 'MC-De', 'MC-Ap', 'VOL-Ap', 'VOL-At',
        'REG-Ap', 'CRP-De', 'CRP-Ap', 'PVO-De', 'PVO-Ap', 'OIT-Ap',

        'INM-Ap', 'CTT-Ap', 'CM-De', 'CM-Ap', 'CM-At', 'CM-Au', 'MEZ-Ap', 'MEZ-At', 'OAD-Ap', 'OAD-At',

        'IDF-De', 'IDF-Ap', 'INT-De', 'INT-Ap', 'INT-At', 'INT-Au',
        'OES-Ap', 'OES-At', 'II-Ap', 'II-At', 'EXT-Ap', 'EXT-At', 'DLI-Ap', 'DLI-At', 'BDE-At', 'OE-Ap', 'OE-At',

        'TRE-At', 'ENG-Ap', 'MP-Ap', 'MP-At', 'DLS-At',

        'DLA-At', 'ARI-At', 'F9-Ap', 'DO-Ap', 'DO-At', '2°D-Ap',
        '2°D-At', 'DP-De', 'DP-Ap', 'DP-At', 'DLC-Ap', 'DLC-At'
    ],
    'Italian': [
        'Por-Df', 'PLb-Df', 'PLb-So', 'PLb-At',

        'CD-Df', 'CD-St', 'CD-Cp', 'DSF-Df', 'DSF-St', 'DSF-Cp',
        'BDf-Df', 'BDf-So', 'BDf-At', 'DIm-Df', 'DIm-St', 'DIm-Cp', 'LAv-Df', 'LAv-So',

        'Ter-Df', 'Ter-So', 'Ter-At', 'Ter-Ca', 'TsF-Df', 'TI-Df',
        'TF-Df', 'TF-So', 'TF-At', 'TF-Ca', 'EsC-So', 'EsC-At', 'EsI-Df', 'EsI-So', 'EsI-At',

        'MIn-Df', 'CmM-Df', 'M-Df', 'M-So', 'SM-So', 'SM-At',
        'Reg-So', 'Inc-Df', 'Inc-So', 'RAr-Df', 'RAr-So', 'RMo-So',

        'Car-So', 'CQn-So', 'CCn-Df', 'CCn-So', 'CCn-At', 'CCn-Ca', 'Mez-So', 'Mez-At', 'RAv-So', 'RAv-At',

        'Apr-Df', 'Apr-So', 'CLt-Df', 'CLt-So', 'CLt-At', 'CLt-Ca',
        'RLg-So', 'RLg-At', 'Ain-So', 'Ain-At', 'Ala-So', 'Ala-At', 'AtE-So', 'AtE-At', 'TSp-At', 'FGL-So', 'FGL-At',

        'Trq-At', 'Rif-So', 'COf-So', 'COf-At', 'AdS-At',

        'CA-At', 'UA-At', 'F9-So', 'FG-So', 'FG-At', 'SP-So',
        'SP-At', 'AcP-Df', 'AcP-So', 'AcP-At', 'PCo-So', 'PCo-At'
    ],
    'French': [
        'GB-Dé', 'GL-Dé', 'GL-So', 'GL-At',

        'CD-Dé', 'CD-St', 'CD-Co', 'DCS-Dé', 'DCS-St', 'DCS-Co',
        'DCE-Dé', 'DCE-So', 'DCE-At', 'DéR-Dé', 'DéR-St', 'DéR-Co', 'Lib-Dé', 'Lib-So',

        'DL-Dé', 'DL-So', 'DL-At', 'DL-Au', 'ALS-Dé', 'ALI-Dé',
        'LOf-Dé', 'LOf-So', 'LOf-At', 'LOf-Au', 'LOC-So', 'LOC-At', 'LI-Dé', 'LI-So', 'LI-At',

        'MS-Dé', '½D-Dé', 'MD-Dé', 'MD-So', 'VOL-So', 'VOL-At',
        'RGA-So', 'MRé-Dé', 'MRé-So', 'MJR-Dé', 'MJR-So', 'MJL-So',

        'CAR-So', 'B2B-So', 'MA-Dé', 'MA-So', 'MA-At', 'MA-Au', 'MEZ-So', 'MEZ-At', 'MJA-So', 'MJA-At',

        'AiD-Dé', 'AiD-So', 'ML-Dé', 'ML-So', 'ML-At', 'ML-Au',
        'MJE-So', 'MJE-At', 'AI-So', 'AI-At', 'Ail-So', 'Ail-At', 'AtI-So', 'AtI-At', 'RMD-At', 'APE-So', 'APE-At',

        'AtS-At', 'EG-So', 'MO-So', 'MO-At', '9½-At',

        'AtA-At', 'RS-At', 'F9-So', 'AtP-So', 'AtP-At', 'AeR-So',
        'AeR-At', 'AP-Dé', 'AP-So', 'AP-At', 'AtC-So', 'AtC-At'
    ],
    'German': [
        'TW-Ve', 'MTW-Ve', 'MTW-Un', 'MTW-An',

        'IV-Ve', 'IV-Vo', 'IV-Rü', 'KIV-Ve', 'KIV-Vo', 'KIV-Rü',
        'HRV-Ve', 'HRV-Un', 'HRV-An', 'BsV-Ve', 'BsV-Vo', 'BsV-Rü', 'LI-Ve', 'LI-Un',

        'AV-Ve', 'AV-Un', 'AV-An', 'AV-Au', 'KIA-Ve', 'IAv-Ve',
        'FV-Ve', 'FV-Un', 'FV-An', 'FV-Au', 'KFV-Un', 'KFV-An', 'IFV-Ve', 'IFV-Un', 'IFV-An',

        'Abr-Ve', 'TS-Ve', 'DM-Ve', 'DM-Un', 'VOL-Un', 'VOL-An',
        'REG-Un', 'BeM-Ve', 'BeM-Un', 'ZSm-Ve', 'ZSm-Un', 'VeSm-Un',

        'CAR-Un', 'BBM-Un', 'ZM-Ve', 'ZM-Un', 'ZM-An', 'ZM-Au', 'MEZ-Un', 'MEZ-An', 'VoSm-Un', 'VoSm-An',

        'DFI-Ve', 'DFI-Un', 'AM-Ve', 'AM-Un', 'AM-An', 'AM-Au',
        'ASm-Un', 'ASm-An', 'IFl-Un', 'IFl-An', 'Flg-Un', 'Flg-An', 'IAS-Un', 'IAS-An', 'RMD-An', 'ÄZS-Un', 'ÄZS-An',

        'T-An', 'ENG-Un', 'OM-Un', 'OM-An', 'SnS-An',

        'StS-An', 'Kni-An', 'F9-Un', 'ZS-Un', 'ZS-An', 'HäS-Un',
        'HäS-An', 'PSt-Ve', 'PSt-Un', 'PSt-An', 'KoS-Un', 'KoS-An'
    ],
    'Portuguese': [
        'GR-De', 'GRL-De', 'GRL-Ap', 'GRL-At',

        'DC-De', 'DC-Bl', 'DC-Co', 'DCE-De', 'DCE-Bl', 'DCE-Co',
        'CD-De', 'CD-Ap', 'CD-At', 'DBl-De', 'DBl-Bl', 'DBl-Co', 'LOf-De', 'LOf-Ap',

        'DL-De', 'DL-Ap', 'DL-At', 'DL-Au', 'DLE-De', 'LTI-De',
        'Al-De', 'Al-Ap', 'Al-At', 'Al-Au', 'AlC-Ap', 'AlC-At', 'DAI-De', 'DAI-Ap', 'DAI-At',

        'Tri-De', 'PD-De', 'MD-De', 'MD-Ap', 'VOL-Ap', 'VOL-At',
        'RGA-Ap', 'MRB-De', 'MRB-Ap', 'CJ-De', 'CJ-Ap', 'OV-Ap',

        'CAR-Ap', 'MAA-Ap', 'MC-De', 'MC-Ap', 'MC-At', 'MC-Au', 'MEZ-Ap', 'MEZ-At', 'CJA-Ap', 'CJA-At',

        'ExD-De', 'ExD-Ap', 'MAl-De', 'MAl-Ap', 'MAl-At', 'MAl-Au',
        'OA-Ap', 'OA-At', 'EI-Ap', 'EI-At', 'Ex-Ap', 'Ex-At', 'AI-Ap', 'AI-At', 'PLA-At', 'ARA-Ap', 'ARA-At',

        'N10-At', 'PO-Ap', 'MO-Ap', 'MO-At', 'AS-At',

        'PL-At', 'PLF-At', 'F9-Ap', 'AR-Ap', 'AR-At', 'AvR-Ap',
        'AvR-At', 'AT-De', 'AT-Ap', 'AT-At', 'AC-Ap', 'AC-At'
    ],
    'Dutch': [
        'DM-Ve', 'MVK-Ve', 'MVK-On', 'MVK-Aa',

        'VC-Ve', 'VC-St', 'VC-Co', 'RCV-Ve', 'RCV-St', 'RCV-Co',
        'WCV-Ve', 'WCV-On', 'WCV-Aa', 'VBV-Ve', 'VBV-St', 'VBV-Co', 'L-Ve', 'L-On',

        'VV-Ve', 'VV-On', 'VV-Aa', 'VV-Au', 'RVV-Ve', 'NBKV-Ve',
        'AVV-Ve', 'AVV-On', 'AVV-Aa', 'AVV-Au', 'CVV-On', 'CVV-Aa', 'NBV-Ve', 'NBV-On', 'NBV-Aa',

        'BA-Ve', 'HM-Ve', 'VM-Ve', 'VM-On', 'VOL-On', 'VOL-Aa',
        'RGA-On', 'BVM-Ve', 'BVM-On', 'SVD-Ve', 'SVD-On', 'ZS-On',

        'CAR-On', 'DYM-On', 'CM-Ve', 'CM-On', 'CM-Aa', 'CM-Au', 'MEZ-On', 'MEZ-Aa', 'VSM-On', 'VSM-Aa',

        'VSV-Ve', 'VSV-On', 'BM-Ve', 'BM-On', 'BM-Aa', 'BM-Au',
        'SvV-On', 'SvV-Aa', 'NBV-On', 'NBV-Aa', 'VS-On', 'VS-Aa', 'HVS-On', 'HVS-Aa', 'RMD-Aa', 'WT-On', 'WT-Aa',

        '10-Aa', 'ENG-On', 'AM-On', 'AM-Aa', 'SS-Aa',

        'DS-Aa', 'A-Aa', 'VN9-On', 'TF-On', 'TF-Aa', 'HS-On',
        'HS-Aa', 'DR-Ve', 'DR-On', 'DR-Aa', 'CS-On', 'CS-Aa'
    ],
    'Danish': [
        'Mm-Fo', 'SMM-Fo', 'SMM-St', 'SMM-At',

        'CF-Fo', 'CF-St', 'CF-Co', 'KMF-Fo', 'KMF-St', 'KMF-Co',
        'BPM-Fo', 'BPM-St', 'BPM-At', 'BSF-Fo', 'BSF-St', 'BSF-Co', 'L-Fo', 'L-St',

        'B-Fo', 'B-St', 'B-At', 'B-Au', 'KB-Fo', 'IFB-Fo',
        'WB-Fo', 'WB-St', 'WB-At', 'WB-Au', 'KWB-St', 'KWB-At', 'OWB-Fo', 'OWB-St', 'OWB-At',

        'Ank-Fo', 'HB-Fo', 'DM-Fo', 'DM-St', 'VOL-St', 'VOL-At',
        'RGA-St', 'BVM-Fo', 'BVM-St', 'DLP-Fo', 'DLP-St', 'FPM-St',

        'OVS-St', 'FFM-St', 'CM-Fo', 'CM-St', 'CM-At', 'CM-Au', 'MEZ-St', 'MEZ-At', 'FP-St', 'FP-At',

        'DW-Fo', 'DW-St', 'BM-Fo', 'BM-St', 'BM-At', 'BM-Au',
        'BP-St', 'BP-At', 'OK-St', 'OK-At', 'W-St', 'W-At', 'IA-St', 'IA-At', 'RTY-At', 'WT-St', 'WT-At',

        'Trq-At', 'EG-St', 'OM-St', 'OM-At', 'SA-At',

        'FA-At', 'S-At', 'F9-St', 'TF-St', 'TF-At', 'DLA-St',
        'DLA-At', 'PA-Fo', 'PA-St', 'PA-At', 'KA-St', 'KA-At'
    ],
    'Norwegian': [
        'M-De', 'SK-De', 'SK-St', 'SK-An',

        'MS-De', 'MS-St', 'MS-Dk', 'SFS-De', 'SFS-St', 'SFS-Dk',
        'SMS-De', 'SMS-St', 'SMS-An', 'BSF-De', 'BSF-St', 'BSF-Dk', 'L-De', 'L-St',

        'B-De', 'B-St', 'B-An', 'B-Au', 'SSB-De', 'IVB-De',
        'VB-De', 'VB-St', 'VB-An', 'VB-Au', 'KVB-St', 'KVB-An', 'IVB-De', 'IVB-St', 'IVB-An',

        'ANK-De', 'HB-De', 'DM-De', 'DM-St', 'VOL-St', 'VOL-An',
        'RGA-St', 'BVM-De', 'BVM-St', 'DLP-De', 'DLP-St', 'VPM-St',

        'CAR-St', 'IL-St', 'SM-De', 'SM-St', 'SM-An', 'SM-Au', 'MEZ-St', 'MEZ-An', 'FP-St', 'FP-An',

        'DV-De', 'DV-St', 'SM-De', 'SM-St', 'SM-An', 'SM-Au',
        'BP-St', 'BP-An', 'IK-St', 'IK-An', 'V-St', 'V-An', 'BS-St', 'BS-An', 'RMD-An', 'BOP-St', 'BOP-An',

        'T-An', 'EG-St', 'OM-St', 'OM-An', 'SS-An',

        'FS-An', 'MT-An', 'F9-St', 'OP-St', 'OP-An', 'DLS-St',
        'DLS-An', 'PS-De', 'PS-St', 'PS-An', 'KS-St', 'KS-An'
    ],
    'Swedish': [
        'Mv-FÖ', 'MLi-FÖ', 'MLi-Us', 'MLi-AT',

        'MB-FÖ', 'MB-Mk', 'MB-UN', 'KMB-FÖ', 'KMB-Mk', 'KMB-UN',
        'BMB-FÖ', 'BMB-Us', 'BMB-AT', 'SSF-FÖ', 'SSF-Mk', 'SSF-UN', 'L-FÖ', 'L-Us',

        'YB-FÖ', 'YB-Us', 'YB-AT', 'YB-Au', 'KYB-FÖ', 'IYB-FÖ',
        'OYB-FÖ', 'OYB-Us', 'OYB-AT', 'OYB-Au', 'KOY-Us', 'KOY-AT', 'IYB-FÖ', 'IYB-Us', 'IYB-AT',

        'Bls-FÖ', 'HB-FÖ', 'DM-FÖ', 'DM-Us', 'VOL-Us', 'VOL-AT',
        'RGA-Us', 'BMF-FÖ', 'BMF-Us', 'DSF-FÖ', 'DSF-Us', 'FSF-Us',

        'CAR-Us', 'LM-Us', 'IM-FÖ', 'IM-Us', 'IM-AT', 'IM-Au', 'MEZ-Us', 'MEZ-AT', 'OSF-Us', 'OSF-AT',

        'DYT-FÖ', 'DYT-Us', 'YM-FÖ', 'YM-Us', 'YM-AT', 'YM-Au',
        'BSF-Us', 'BSF-AT', 'IY-Us', 'IY-AT', 'YT-Us', 'YT-AT', 'IF-Us', 'IF-AT', 'RMD-AT', 'BBM-Us', 'BBM-AT',

        'T-AT', 'EG-Us', 'OM-Us', 'OM-AT', 'SA-AT',

        'OF-AT', 'MT-AT', 'F9-Us', 'BM-Us', 'BM-AT', 'DLF-Us',
        'DLF-AT', 'PF-FÖ', 'PF-Us', 'PF-AT', 'KF-Us', 'KF-AT'
    ],
    'Chinese': [
        'G-防守', 'SK-防守', 'SK-策应 ', 'SK-进攻',

        'CD-防守', 'CD-St', 'CD-Co', 'NCB-防守', 'NCB-St', 'NCB-Co',
        'WCB-防守', 'WCB-策应 ', 'WCB-进攻', 'BPD-防守', 'BPD-St', 'BPD-Co', 'L-防守', 'L-策应 ',

        'FB-防守', 'FB-策应 ', 'FB-进攻', 'FB-自动', 'NFB-防守', 'IFB-防守',
        'WB-防守', 'WB-策应 ', 'WB-进攻', 'WB-自动', 'CWB-策应 ', 'CWB-进攻', 'IWB-防守', 'IWB-策应 ', 'IWB-进攻',

        'A-防守', 'HB-防守', 'DM-防守', 'DM-策应 ', 'VOL-策应 ', 'VOL-进攻',
        'RGA-策应 ', 'BWM-防守', 'BWM-策应 ', 'DLP-防守', 'DLP-策应 ', 'RPM-策应 ',

        'CAR-策应 ', 'BBM-策应 ', 'CM-防守', 'CM-策应 ', 'CM-进攻', 'CM-自动', 'MEZ-策应 ', 'MEZ-进攻', 'AP-策应 ', 'AP-进攻',

        'DW-防守', 'DW-策应 ', 'WM-防守', 'WM-策应 ', 'WM-进攻', 'WM-自动',
        'WP-策应 ', 'WP-进攻', 'IW-策应 ', 'IW-进攻', 'W-策应 ', 'W-进攻', 'IF-策应 ', 'IF-进攻', 'RMD-进攻', 'WT-策应 ', 'WT-进攻',

        'T-进攻', 'EG-策应 ', 'AM-策应 ', 'AM-进攻', 'SS-进攻',

        'AF-进攻', 'P-进攻', 'F9-策应 ', 'TF-策应 ', 'TF-进攻', 'DLF-策应 ',
        'DLF-进攻', 'PF-防守', 'PF-策应 ', 'PF-进攻', 'CF-策应 ', 'CF-进攻'
    ],
    'Polish': [
        'BR-Ob', 'BL-Ob', 'BL-W', 'BL-At',

        'ŚO-Ob', 'ŚO-St', 'ŚO-Zb', 'TŚO-Ob', 'TŚO-St', 'TŚO-Zb',
        'BŚO-Ob', 'BŚO-W', 'BŚO-At', 'OGP-Ob', 'OGP-St', 'OGP-Zb', 'LB-Ob', 'LB-W',

        'BO-Ob', 'BO-W', 'BO-At', 'BO-Au', 'TBO-Ob', 'OBO-Ob',
        'BWO-Ob', 'BWO-W', 'BWO-At', 'BWO-Au', 'KBO-W', 'KBO-At', 'OCS-Ob', 'OCS-W', 'OCS-At',

        'RD-Ob', 'ŁD-Ob', 'DP-Ob', 'DP-W', 'VOL-W', 'VOL-At',
        'RGA-W', 'POP-Ob', 'POP-W', 'CR-Ob', 'CR-W', 'SwR-W',

        'CAR-W', 'PD-W', 'ŚP-Ob', 'ŚP-W', 'ŚP-At', 'ŚP-Au', 'MEZ-W', 'MEZ-At', 'WR-W', 'WR-At',

        'DS-Ob', 'DS-W', 'BP-Ob', 'BP-W', 'BP-At', 'BP-Au',
        'BoR-W', 'BoR-At', 'OS-W', 'OS-At', 'S-W', 'S-At', 'SN-W', 'SN-At', 'RmD-At', 'BOd-W', 'BOd-At',

        'K10-At', 'ENG-W', 'OP-W', 'OP-At', 'FN-At',

        'WN-At', 'LPK-At', 'F9-W', 'O-W', 'O-At', 'CN-W',
        'CN-At', 'NN-Ob', 'NN-W', 'NN-At', 'KN-W', 'KN-At'
    ],
    'Turkish': [
        'K-Sv', 'LK-Sv', 'LK-De', 'LK-Hü',

        'SS-Sv', 'SS-Ks', 'SS-To', 'ÇS-Sv', 'ÇS-Ks', 'ÇS-To',
        'KS-Sv', 'KS-De', 'KS-Hü', 'PS-Sv', 'PS-Ks', 'PS-To', 'LB-Sv', 'LB-De',

        'SB-Sv', 'SB-De', 'SB-Hü', 'SB-Og', 'ÇB-Sv', 'SİB-Sv',
        'KB-Sv', 'KB-De', 'KB-Hü', 'KB-Og', 'İYB-De', 'İYB-Hü', 'SHB-Sv', 'SHB-De', 'SHB-Hü',

        'ÖL-Sv', 'GL-Sv', 'DOS-Sv', 'DOS-De', 'VOL-De', 'VOL-Hü',
        'REG-De', 'SO-Sv', 'SO-De', 'DOK-Sv', 'DOK-De', 'GOK-De',

        'DNM-De', 'İYO-De', 'MO-Sv', 'MO-De', 'MO-Hü', 'MO-Og', 'MEZ-De', 'MEZ-Hü', 'OOK-De', 'OOK-Hü',

        'DK-Sv', 'DK-De', 'ÇKO-Sv', 'ÇKO-De', 'ÇKO-Hü', 'ÇKO-Og',
        'KOK-De', 'KOK-Hü', 'TAK-De', 'TAK-Hü', 'K-De', 'K-Hü', 'KF-De', 'KF-Hü', 'RMD-Hü', 'HKO-De', 'HKO-Hü',

        'ON-Hü', 'EG-De', 'OOS-De', 'OOS-Hü', 'GF-Hü',

        'YF-Hü', 'FG-Hü', 'SF-De', 'PS-De', 'PS-Hü', 'YRD-De',
        'YRD-Hü', 'ÇF-Sv', 'ÇF-De', 'ÇF-Hü', 'KOF-De', 'KOF-Hü'
    ],
    'Greek': [
        'ΤΦ-A', 'TΛ-A', 'TΛ-Υπ', 'TΛ-Επ',

        'KA-A', 'KA-Στ', 'KA-K', 'ΣKA-A', 'ΣKA-Στ', 'ΣKA-K',
        'AΣτ-A', 'AΣτ-Υπ', 'AΣτ-Επ', 'ΔA-A', 'ΔA-Στ', 'ΔA-K', 'Λμπ-A', 'Λμπ-Υπ',

        'ΠM-A', 'ΠM-Υπ', 'ΠM-Επ', 'ΠM-Aυ', 'ΣΠA-A', 'AΠM-A',
        'MX-A', 'MX-Υπ', 'MX-Επ', 'MX-Aυ', 'OMX-Υπ', 'OMX-Επ', 'AMX-A', 'AMX-Υπ', 'AMX-Επ',

        'AMK-A', 'XM-A', 'AM-A', 'AM-Υπ', 'VOL-Υπ', 'VOL-Επ',
        'RGA-Υπ', 'KK-A', 'KK-Υπ', 'O-A', 'O-Υπ', 'EO-Υπ',

        'CAR-Υπ', 'BBM-Υπ', 'KM-A', 'KM-Υπ', 'KM-Επ', 'KM-Aυ', 'MEZ-Υπ', 'MEZ-Επ', 'ΠO-Υπ', 'ΠO-Επ',

        'AE-A', 'AE-Υπ', 'AκM-A', 'AκM-Υπ', 'AκM-Επ', 'AκM-Aυ',
        'AO-Υπ', 'AO-Επ', 'AνE-Υπ', 'AνE-Επ', 'Ε-Υπ', 'Ε-Επ', 'EE-Υπ', 'EE-Επ', 'RMD-Επ', 'AEΣ-Υπ', 'AEΣ-Επ',

        'T-Επ', 'EG-Υπ', 'EM-Υπ', 'EM-Επ', 'KρE-Επ',

        'ΠE-Επ', 'K-Επ', 'Ψ9-Υπ', 'EΣ-Υπ', 'EΣ-Επ', 'EμB-Υπ',
        'EμB-Επ', 'EΠ-A', 'EΠ-Υπ', 'EΠ-Επ', 'OE-Υπ', 'OE-Επ'
    ],
    'Russian': [
        'В-Зщ', 'ВЧ-Зщ', 'ВЧ-Пo', 'ВЧ-Aт',

        'ЦЗ-Зщ', 'ЦЗ-Бл', 'ЦЗ-Пс', 'ЧЦЗ-Зщ', 'ЧЦЗ-Бл', 'ЧЦЗ-Пс',
        'КЦЗ-Зщ', 'КЦЗ-Пo', 'КЦЗ-Aт', 'СЗ-Зщ', 'СЗ-Бл', 'СЗ-Пс', 'Л-Зщ', 'Л-Пo',

        'ФЗ-Зщ', 'ФЗ-Пo', 'ФЗ-Aт', 'ФЗ-Aр', 'ЧФЗ-Зщ', 'ПКЗ-Зщ',
        'КЗ-Зщ', 'КЗ-Пo', 'КЗ-Aт', 'КЗ-Aр', 'AКЗ-Пo', 'AКЗ-Aт', 'ПКЗ-Зщ', 'ПКЗ-Пo', 'ПКЗ-Aт',

        'ЧОП-Зщ', 'Хб-Зщ', 'ОП-Зщ', 'ОП-Пo', 'Вол-Пo', 'Вол-Aт',
        'Рдж-Пo', 'ПР-Зщ', 'ПР-Пo', 'ОПл-Зщ', 'ОПл-Пo', 'БПл-Пo',

        'Кар-Пo', 'БТБ-Пo', 'ЦП-Зщ', 'ЦП-Пo', 'ЦП-Aт', 'ЦП-Aр', 'Мец-Пo', 'Мец-Aт', 'ВПл-Пo', 'ВПл-Aт',

        'КПО-Зщ', 'КПО-Пo', 'ФП-Зщ', 'ФП-Пo', 'ФП-Aт', 'ФП-Aр',
        'ФПл-Пo', 'ФПл-Aт', 'ПКП-Пo', 'ПКП-Aт', 'КП-Пo', 'КП-Aт', 'И-Пo', 'И-Aт', 'Рмд-Aт', 'ФT-Пo', 'ФT-Aт',

        'T-Aт', 'Энг-Пo', 'AП-Пo', 'AП-Aт', 'ТН-Aт',

        'ВФ-Aт', 'ЧФ-Aт', 'Л9-Пo', 'Tм-Пo', 'Tм-Aт', 'ОФ-Пo',
        'ОФ-Aт', 'ПФ-Зщ', 'ПФ-Пo', 'ПФ-Aт', 'УФ-Пo', 'УФ-Aт'
    ]
}

# Column names for 'Overall' radar charts
overall_radar_columns_dict = {
        'English': ['Speed', 'Vision', 'Attacking', 'Technical', 'Aerial', 'Mental', 'Defending', 'Physical',
                    'Aerial (GK)', 'Shot Stopping', 'Distribution', 'Communication', 'Eccentricity'],
        'English (US)': ['Speed', 'Vision', 'Attacking', 'Technical', 'Aerial', 'Mental', 'Defending', 'Physical',
                    'Aerial (GK)', 'Shot Stopping', 'Distribution', 'Communication', 'Eccentricity'],
        'Japanese': ['スピード', '視野 (Overall)', '攻撃力', 'テクニカル', '空中', 'メンタル', '守備力', 'フィジカル', '空中（GK)',
                     'シュートストップ', '配球', 'コミュニケーション能力', '奇抜さ'],
        'Korean': ['스피드', '시야', '공격', '기술적 능력', '공중볼 처리', '정신력', '수비', '신체적 능력',
                   '공중볼 처리 (GK)', '슈팅 방어', '볼 배급', '수비 ', '기행 조율'],
        'Spanish': ['Velocidad', 'Visión', 'Ataque', 'Técnica', 'Aéreo', 'Mental', 'Defensa', 'Físico',
                    'Aéreo (POR)', 'Paradas', 'Distribución', 'Comunicación', 'Excentricidad'],
        'Italian': ['Velocità', 'Visione di gioco', 'Attacco', 'Tecnica', 'Aereo', 'Mentale', 'Difesa', 'Fisico',
                    'Aereo (Por)', 'Parate', 'Distribuzione', 'Comunicazione', 'Eccentricità'],
        'French': ['Vitesse', 'Vision du jeu', 'Attaque', 'Technique', 'Jeu aérien', 'Mental', 'Défense', 'Physique',
                   'Jeu aérien (GB)', 'Arréts sur la ligne', 'Distribution', 'Communication', 'Excentricité'],
        'German': ['Geschwindigkeit', 'Übersicht', 'Offensive', 'Technik', 'In der Luft', 'Mentalität', 'Defensive', 'Physische Stärke',
                   'In der Luft (TW)', 'Schüsse abwehren', 'Ballverteilung', 'Kommunikation', 'Exzentrizität'],
        'Portuguese': ['Velocidade', 'Visão de Jogo', 'Attacar', 'Técnica', 'Jogo Aéreo', 'Mental', 'Defesa', 'Físico',
                       'Jogo Aéreo (GR)', 'Defesa de Remates', 'Distribuição', 'Comunicação', 'Excentricidade'],
        'Dutch': ['Snelheid', 'Inzicht', 'Aanvallend', 'Techniek', 'In de lucht', 'Mentaal', 'Verdedigend', 'Fysiek',
                  'In de lucht (DM)', 'Schoten tegenhouden', 'Verdeling', 'Communicatie', 'Excentriciteit'],
        'Danish': ['Fart', 'Overblik', 'Offensiv', 'Teknisk', 'Luftspil', 'Mental', 'Forsvar', 'Fysisk',
                   'Luftspil (Mm)', 'Skudstopning', 'Distribution', 'Kommunikation', 'Excentricitet'],
        'Norwegian': ['Hurtighet', 'Overblikk', 'Offensivt', 'Teknisk', 'Luftstyrke', 'Mentalt', 'Defensivt', 'Fysisk',
                      'Luftstyrke (Kee)', 'Stoppe skudd', 'Distribusjon', 'Kommunikasjon', 'Eksentrisitet'],
        'Swedish': ['Snabbhet', 'Speluppfattning', 'Anfallsspel', 'Teknik', 'Huvudspel', 'Psyke', 'Försvarsspel', 'Fysiskt',
                    'Huvudspel (Mål)', 'Blockering av skott', 'Fördelning', 'Kommunikation', 'Originalitet'],
        'Chinese': ['速度', '视野', '进攻', '技术', '制空', '精神', '防守', '身体',
                    '制空 (GK)', '拦截射门', '大脚开球', '指挥防守', '意外性'],
        'Polish': ['Szybkość', 'Przegląd sytuacji', 'Ofensywa', 'Techniczne', 'Górne pilki', 'Psychiczne', 'Defensywa', 'Fizyczne',
                   'Górne pilki (BR)', 'Obrona strzalów', 'Wyprowadzanie pilki', 'Komunikacja', 'Ekscentryczność'],
        'Turkish': ['Hız', 'Vizyon', 'Hücum', 'Teknik', 'Hava', 'Zihinsel', 'Savunma', 'Fiziksel',
                    'Hava (K)', 'Şut Karşılama', 'Dağıtım', 'İletişim', 'Eksantriklik'],
        'Greek': ['Ταχύτητα', 'Δημιουργικδτητα', 'Επίθεση', 'Τεχνική', 'Εναέρια', 'Ψυχίκά', 'Αμυνα', 'Σωματικά/Φυσικά',
                  'Εναέρια (TΦ)', 'Σταμάτημα Σουτ', 'Μοίρασμα', 'Επικοινωνία', 'Εκκεντρικότητα'],
        'Russian': ['Скорость', 'Видение поля', 'Атакующие', 'Технические', 'Игра в воздухе', 'Психологические', 'Навыки Защиты', 'Физические',
                    'Игра в воздухе (В)', 'Парирование ударов', 'Ввод мяча', 'Взаимодействие', 'Эксцентричность']
    }

# Negative stat categories
negative_stat_categories = [65, 77, 87, 101, 102, 103, 104, 106, 107, 111, 112, 115, 120, 124]
#'Poss Lost/90', 'Hdrs L/90', 'Gl Mst', 'Conc', 'Con/90', 'Off', 'Fls', 'Yel', 'Red', 'Tcon', 'Tcon/90', 'Lost', 'G. Mis', 'Int Conc'


# Stats label dictionary to convert fm metric codenames to full names of the stat category
international_stats_label_dict = {
    'English': {
        'Name': 'Name', 'Age': 'Age', 'Position': 'Position', 'Club': 'Club', 'Division': 'Division',
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
        'Int Av Rat': 'International Average Rating (current season)',
        'Media Description': 'Media Description', 'Home-Grown Status': 'Home-Grown Status'
    },
    'English (US)': {
        'Name': 'Name', 'Age': 'Age', 'Position': 'Position', 'Club': 'Club', 'Division': 'Division',
        'Transfer Value': 'Transfer Value', 'Salary': 'Salary', 'Transfer Status': 'Transfer Status',
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
        'Shutouts': 'Shutouts', 'Cln/90': 'Clean Sheets per 90 minutes',
        'Saves/90': 'Saves per 90 minutes', 'Svt': 'Saves Tipped', 'Svp': 'Saves Parried',
        'Svh': 'Saves Held', 'Sv %': 'Save Ratio', 'xSv %': 'xSv Ratio - Expected Save Ratio',
        'xGP': 'xGP - Expected Goals Prevented',
        'xGP/90': 'xGP/90 - Expected Goals Prevented per 90 minutes', 'Pens Saved': 'Penalties Saved',
        'Pens Faced': 'Penalties Faced', 'Pens Saved Ratio': 'Penalties Saved Ratio',
        'Conc': 'Goals Allowed', 'All/90': 'Goals Allowed per 90 minutes', 'Off': 'Offsides',
        'Fls': 'Fouls Committed', 'FA': 'Fouls Against', 'Yel': 'Yellow Cards', 'Red': 'Red Cards',
        'Pts/Gm': 'Points Won per Game', 'Tgls': 'Team Goals', 'Tgls/90': 'Team Goals per 90 minutes',
        'Tall': 'Team Goals Allowed', 'Tcon/90': 'Team Goals Allowed per 90 minutes',
        'Won': 'Games Won', 'D': 'Games Drawn', 'Lost': 'Games Lost', 'Gwin': 'Game Win Ratio',
        'Apps': 'Appearances', 'Starts': 'Starting Appearances', 'Mins': 'Minutes',
        'G. Mis': 'Games Missed in a Row', 'PoM': 'Player of the Match',
        'Int Apps': 'International Appearances (current season)',
        'Int Ast': 'International Assists (current season)',
        'Int Conc': 'International Goals Conceded (current season)',
        'Int Av Rat': 'International Average Rating (current season)',
        'Media Description': 'Media Description', 'Home-Grown Status': 'Home-Grown Status'
    }
}

# Preset Stats Radar Chart Values for users to toggle on dropdown menu
preset_radar_values_by_index = {
    'Goalkeeper': [117, 8, 95, 97, 100, 121, 90, 84, 37, 34, 94, 93, 92, 91, 89, 102],
    #'Apps', 'Av Rat', 'xSv %', 'xGP/90', 'Pens Saved Ratio', 'PoM', 'Saves/90', 'Clr/90', 'Pas %', 'Ps C/90', 'Sv %', 'Svh', 'Svp', 'Svt', 'Cln/90', 'Con/90'
    'Central Defender': [117, 8, 67, 69, 82, 39, 64, 34, 37, 86, 73, 76, 84, 80, 106],
    #'Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Shts Blckd/90', 'Pr passes/90', 'Poss Won/90', 'Ps C/90', 'Pas %', 'Int/90', 'Hdrs W/90', 'Hdr %', 'Clr/90', 'Blk/90', 'Yel'
    'Full-back': [117, 8, 67, 69, 64, 65, 34, 37, 86, 47, 49, 52, 104, 106],
    #'Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Poss Won/90', 'Poss Lost/90', 'Ps C/90', 'Pas %', 'Int/90', 'Distance', 'Cr C/90', 'Cr C/A', 'Fls', 'Yel'
    'Wing-Back': [117, 8, 67, 69, 64, 65, 37, 86, 47, 49, 52, 56, 15, 13, 46, 44],
    #'Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Poss Won/90', 'Poss Lost/90', 'Pas %', 'Int/90', 'Distance', 'Cr C/90', 'Cr C/A', 'OP-Crs C/90', 'Ch C/90', 'Asts/90', 'Drb/90', 'Sprints/90'
    'Defensive Midfielder': [117, 8, 67, 69, 39, 64, 65, 34, 37, 41, 86, 61, 73, 76],
    #'Apps', 'Av Rat', 'Tck/90', 'Tck R', 'Pr passes/90', 'Poss Won/90', 'Poss Lost/90', 'Ps C/90', 'Pas %', 'K Ps/90', 'Int/90', 'Pres C/90', 'Hdrs W/90', 'Hdr %'
    'Central Midfielder': [117, 8, 67, 86, 39, 64, 65, 37, 41, 47, 15, 13, 61, 19],
    #'Apps', 'Av Rat', 'Tck/90', 'Int/90', 'Pr passes/90', 'Poss Won/90', 'Poss Lost/90', 'Pas %', 'K Ps/90', 'Distance', 'Ch C/90', 'Asts/90', 'Pres C/90', 'ShT/90'
    'Attacking Midfielder': [117, 8, 37, 15, 13, 43, 65, 41, 54, 46, 25, 10, 24],
    #'Apps', 'Av Rat', 'Pas %', 'Ch C/90', 'Asts/90', 'xA/90', 'Poss Lost/90', 'K Ps/90', 'OP-KP/90', 'Drb/90', 'xG/shot', 'Gls/90', 'xG/90'
    'Winger': [117, 8, 65, 61, 46, 44, 105, 15, 54, 49, 52, 56, 25, 10, 24],
    #'Apps', 'Av Rat', 'Poss Lost/90', 'Pres C/90', 'Drb/90', 'Sprints/90', 'FA', 'Ch C/90', 'OP-KP/90', 'Cr C/90', 'Cr C/A', 'OP-Crs C/90', 'xG/shot', 'Gls/90', 'xG/90'
    'Striker': [117, 8, 61, 64, 19, 20, 44, 73, 76, 25, 29, 13, 28, 10, 24],
    #'Apps', 'Av Rat', 'Pres C/90', 'Poss Won/90', 'ShT/90', 'Shot %', 'Sprints/90', 'Hdrs W/90', 'Hdr %', 'xG/shot', 'Conv %', 'Asts/90', 'NP-xG/90', 'Gls/90', 'xG/90'
    'Custom': []
}

# Sample charts for quick access to interesting data in the user's FM file
sample_filters_by_index = {
    'Top Strikers': {
        'Position': 141,
        #'ST'
        'top10': [8, 9, 10, 24, 28, 19],
        #['Av Rat', 'Gls', 'Gls/90', 'xG/90', 'NP-xG/90', 'ShT/90'],
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Explosive', 'Powerful', 'Rangy',
                              'Towering', 'Strong', 'Pacy', 'goalscorer'],
        'X': 9,
        #'Gls'
        'Y': 8,
        #'Av Rat'
    },
    'Top Wingers': {
        'Position': [134, 135, 139, 140],
        #'AM (R)', 'AM (L)'
        'top10': [8, 9, 10, 24, 12, 13, 43, 46, 15, 41, 49, 54, 56],
        #'Av Rat', 'Gls', 'Gls/90', 'xG/90', 'Ast', 'Asts/90', 'xA/90', 'Drb/90', 'Ch C/90', 'K Ps/90', 'Cr C/90', 'OP-KP/90', 'OP-Crs C/90'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Explosive', 'Confident', 'Dynamic'],
        'X': 44,
        #'Sprints/90',
        'Y': 65,
        #'Poss Lost/90'
    },
    'Top Attacking Midfielders': {
        'Position': 138,
        #'AM (C)',
        'top10': [8, 9, 10, 11, 24, 12, 13, 43, 14, 15, 41, 54],
        #'Av Rat', 'Gls', 'Gls/90', 'Goals Outside Box', 'xG/90', 'Ast', 'Asts/90', 'xA/90', 'CCC', 'Ch C/90', 'K Ps/90', 'OP-KP/90'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'entertainer', 'orchestrator'],
        'X': 15,
        #'Ch C/90',
        'Y': 65,
        #'Poss Lost/90'
    },
    'Top Central Midfielders': {
        'Position': 137,
        #'M (C)',
        'top10': [8, 12, 13, 43, 14, 15, 41, 54, 64, 34, 37],
        #'Av Rat', 'Ast', 'Asts/90', 'xA/90', 'CCC', 'Ch C/90', 'K Ps/90', 'OP-KP/90', 'Poss Won/90', 'Ps C/90', 'Pas %'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Industrious', 'orchestrator',
                              'Tireless', 'Tenacious', 'Strong'],
        'X': 47,
        #'Distance',
        'Y': 19
        #'ShT/90'
    },
    'Top Defensive Midfielders': {
        'Position': 136,
        #'DM',
        'top10': [8, 41, 54, 64, 61, 67, 86, 34, 37],
        #'Av Rat', 'K Ps/90', 'OP-KP/90', 'Poss Won/90', 'Pres C/90', 'Tck/90', 'Int/90', 'Ps C/90', 'Pas %'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Industrious', 'orchestrator',
                              'Tireless', 'Tenacious', 'Strong'],
        'X': 64,
        #'Poss Won/90',
        'Y': 39
        #'Pr passes/90'
    },
    'Top Wing-Backs': {
        'Position': [132, 133],
        #'WB (R)', 'WB (L)'
        'top10': [8, 12, 13, 43, 46, 14, 15, 41, 49, 54, 56, 64, 67, 86],
        #'Av Rat', 'Ast', 'Asts/90', 'xA/90', 'Drb/90', 'CCC', 'Ch C/90', 'K Ps/90', 'Cr C/90', 'OP-KP/90', 'OP-Crs C/90', 'Poss Won/90', 'Tck/90', 'Int/90'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Explosive'],
        'X': 44,
        #'Sprints/90',
        'Y': 49,
        #'Cr C/90'
    },
    'Top Full-Backs': {
        'Position': [130, 131],
        #'D (R)', 'D (L)'
        'top10': [8, 49, 54, 56, 64, 67, 71, 86, 80],
        #'Av Rat', 'Cr C/90', 'OP-KP/90', 'OP-Crs C/90', 'Poss Won/90', 'Tck/90', 'K Tck/90', 'Int/90', 'Blk/90'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Explosive'],
        'X': 47,
        #'Distance',
        'Y': 44
        #'Sprints/90'
    },
    'Top Central Defenders': {
        'Position': 129,
        #'D (C)',
        'top10': [8, 67, 71, 86, 82, 73, 78],
        #'Av Rat', 'Tck/90', 'K Tck/90', 'Int/90', 'Shts Blckd/90', 'Hdrs W/90', 'K Hdrs/90'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Commanding', 'Powerful', 'Solid',
                              'Strong'],
        'X': 47,
        #'Distance',
        'Y': 76
        #'Hdr %'
    },
    'Top Goalkeepers': {
        'Position': 128,
        #'GK',
        'top10': [8, 88, 89, 90, 94],
        #'Av Rat', 'Clean Sheets', 'Cln/90', 'Saves/90', 'Sv %'
        'Media Description': ['Wonderkid', 'World class', 'Elite', 'Legendary', 'Capable', 'Commanding', 'Fearless',
                              'Instinctive', 'Playmaking'],
        'X': 88,
        #'Clean Sheets',
        'Y': 90
        #'Saves/90'
    },
    'Top Youngsters': {
        'Age': 18,
        # 'Age', 'Int Apps'
        'top10': [122, 117, 9, 10, 12, 13, 14, 15, 54, 41, 46, 49, 37, 64, 86, 71, 78, 89, 90],
        # 'Int Apps', 'Apps', 'Gls', 'Gls/90', 'Ast', 'Asts/90', 'CCC', 'Ch C/90', 'OP-KP/90', 'K Ps/90', 'Drb/90',
        # 'Cr C/90', 'Pas %', 'Poss Won/90', 'Int/90', 'K Tck/90', 'K Hdrs/90', 'Cln/90', 'Saves/90'
        'Media Description': ['Wonderkid', 'Promising'],
        'X': 8,
        #'Apps',
        'Y': 117
        #'Av Rat'
    },
}
