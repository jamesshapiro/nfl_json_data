import requests
import pandas as pd
import tempfile
import json

games_loc = {'regular_season': 'reg_games',
             'pre_season': 'pre_games',
             'post_season': 'post_games'}

def get_date(game_id):
    game_id = str(game_id)
    year = game_id[:4]
    month = game_id[4:6]
    day = game_id[6:8]
    return (day, month, year)

def jsonify_games(hyperlink, key, year):
    r = requests.get(hyperlink)
    f = tempfile.NamedTemporaryFile()
    with open(f.name, 'w') as infile:
        infile.write(r.text)
    df = pd.read_csv(f.name)
    f.close()
    all_games = []
    for index, row in df.iterrows():    
        day, month, year = get_date(row['game_id'])
        game = {
            'home_team': row['home_team'], 'away_team': row['away_team'],
            'game_id': row['game_id'], 'week': row['week'], 'season': row['season'],
            'state_of_game': row['state_of_game'], 'game_url': row['game_url'],
            'home_score': row['home_score'], 'away_score': row['away_score'],
            'date': f'{month}-{day}-{year}'
        }
        all_games.append(game)
    year = int(cyear)
    season = {'games': all_games, 'season': f'{cyear}-{cyear+1}', 'type': key}
    with open(f'games_data/{key}/{games_loc[key]}_{cyear}-{cyear+1}.json', 'w') as f:
        f.write(json.dumps(season))

for key in games_loc:
    for cyear in range(2009, 2020):
        link = f'https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/{key}/{games_loc[key]}_{cyear}.csv'
        print(link)
        jsonify_games(link, key, cyear)

