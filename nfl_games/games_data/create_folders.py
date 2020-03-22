import os
import json
import sys

teams = {'ATL', 'TB', 'SEA', 'TEN', 'SF', 'IND', 'KC', 'CAR', 'NO', 'MIN', 'STL', 'OAK', 'DAL', 'CIN', 'CLE', 'NE', 'SD', 'HOU', 'WAS', 'CHI', 'PIT', 'NYG', 'JAC', 'ARI', 'MIA', 'BAL', 'DET', 'BUF', 'NYJ', 'DEN', 'GB', 'PHI'}

for d in ['regular_season', 'post_season', 'pre_season']:
    for cyear in range(2009,2020):
        argo = d
        if argo == 'regular_season':
            argo = 'reg_games'
        elif argo=='post_season':
            argo = 'post_games'
        else:
            argo = 'pre_games'
        with open(f'/home/james/code/nfl/nfl_games/games_data/{d}/{cyear}-{cyear+1}/{argo}_{cyear}-{cyear+1}.json') as f:
            data = json.loads(f.read())
        games = data['games']
        for team in teams:
            all_games = [game for game in games if game['home_team'] == 'WAS' or game['away_team'] == 'WAS']
            weeks = set([game['week'] for game in all_games])
            bye_week = [idx for idx in range(1,18) if idx not in weeks][0]
            result = {'team': team, 'games': all_games, 'bye_week': bye_week}
            dest =  f'/home/james/code/nfl/nfl_games/games_data/{d}/{cyear}-{cyear+1}/by_team/{team}_{argo}_{cyear}-{cyear+1}.json'
            with open(dest, 'w') as outfile:
                json.dump(result, outfile)
            print(dest)


