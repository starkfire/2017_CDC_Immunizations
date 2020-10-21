import pandas as pd
import numpy as np
import scipy.stats as stats
import re

AREAS = [
    'New York City',
    'Los Angeles',
    'San Francisco Bay Area',
    'Chicago',
    'Dallas–Fort Worth',
    'Washington, D.C.',
    'Philadelphia',
    'Boston',
    'Minneapolis–Saint Paul',
    'Denver',
    'Miami–Fort Lauderdale',
    'Phoenix',
    'Detroit',
    'Toronto',
    'Houston',
    'Atlanta',
    'Cleveland',
    'Charlotte',
    'Indianapolis',
    'Milwaukee',
    'New Orleans',
    'Orlando',
    'Portland',
    'Salt Lake City',
    'San Antonio',
    'Sacramento',
    'Oklahoma City',
    'Memphis'
]

def nba_correlation():
    nba_df = pd.read_csv('nba.csv', usecols=['team', 'W', 'L', 'year'])
    # get only the 2018 data
    df_2018 = nba_df.loc[nba_df['year'].values == 2018]
    # fetch cities from the HTML file
    cities = pd.read_html('wikipedia_data.html')[1]
    cities = cities.iloc[:-1, [0,3,5,6,7,8]]
    # create variables
    population_by_region = []
    win_loss_by_region = []
    # temporary variables
    teams = []
    wins = []
    losses = []
    for area in AREAS:
        # population by region
        entry = cities.loc[cities['Metropolitan area'].values == str(area)]
        population_by_region.append(int(entry['Population (2016 est.)[8]'].values[0]))
        # get NBA team(s) for the city
        team = entry['NBA'].values[0]
        # clean the text before passing the value to teams[]
        team = team.split('[')[0]
        check_space = bool(re.search(r'\s', team))
        team = re.sub(r"([A-Z])", r" \1", team).split() if not check_space else [team]
        teams.append(team)
        # get wins and losses of each team in the area
        if len(team) > 1:
            temp_wins, temp_losses = [], []
            for t in range(len(team)):
                scores = df_2018[df_2018['team'].str.contains(team[t])]
                temp_wins.append(int(scores['W'].values[0]))
                temp_losses.append(int(scores['L'].values[0]))
            wins.append(temp_wins)
            losses.append(temp_losses)
            # Win/Loss
            wlr = sum(temp_wins) / (sum(temp_wins) + sum(temp_losses))
            win_loss_by_region.append(wlr)
        else:
            scores = df_2018[df_2018['team'].str.contains(team[0])]
            wins.append(int(scores['W'].values[0]))
            losses.append(int(scores['L'].values[0]))
            # Win/Loss
            wlr = int(scores['W'].values[0]) / (int(scores['W'].values[0]) + int(scores['L'].values[0]))
            win_loss_by_region.append(wlr)
    
    scoreboard = pd.DataFrame({
        'area': AREAS,
        'population': population_by_region,
        'WLR': win_loss_by_region,
        'W': wins,
        'L': losses
    })

    return stats.pearsonr(population_by_region, win_loss_by_region)

print(nba_correlation())