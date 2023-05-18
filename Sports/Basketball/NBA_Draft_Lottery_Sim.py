# I want to build my own way to simulate the draft lottery!

# import necessary packages
import random
import itertools
import time

# these are the numbers on the ping pong ball
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#print(numbers)

# conduct drawing. We draw all 4 numbers simeltaneously for ease, but then reveal them one at a time
draw = random.sample(numbers,4)

# generate all possible combinations
combinations = list(itertools.combinations(numbers, 4))

# manually input team odds.
teams_odds = {'Detroit': .14, 'Houston':.14, 'San Antonio': .14, 'Charlotte': .125, 'Portland':.105, 'Orlando':.09, 'Indiana':.068, 'Washington':.067, 'Utah':.0450, 'Dallas':.03, 'Chicago':.018, 'OKC':.017,'Toronto':.01,'NO':.005}

# initialize dict for combos assigned to each team.
teams_combos = dict.fromkeys(teams_odds.keys())

# Loops to assign combos
ind_init = 0
for ind,val in enumerate(teams_odds):
    #print(ind,val)
    if ind_init==int(0):
        teams_combos[val] = combinations[ind_init:int((len(combinations)-1)*teams_odds[val])]
        ind_init+=int((len(combinations)-1)*teams_odds[val])
        #print(ind_init, ind, val)
    else:
        #print(ind_init)
        second_int = int(ind_init+((len(combinations)-1)*teams_odds[val]))
        teams_combos[val] = combinations[ind_init:second_int]
        ind_init+=int((len(combinations)-1)*teams_odds[val])
        #print(ind_init, second_int, ind,val)

# Begin (or begin to report) Draw!
teams_percentage = dict.fromkeys(teams_odds.keys())
teams_counts = dict.fromkeys(teams_odds.keys())
for ind_k,val_k in enumerate(draw):
    check = draw[:(ind_k+1)]
    print(check)
    for teams in teams_combos:
        #print(teams)
        a=0
    
        for ind,val in enumerate(teams_combos[teams]):
            #print(ind,val)
            if all(x in val for x in check):
                a+=1
            teams_counts[teams] = a
    #print(teams_counts)
    b = 0
    b = sum(teams_counts.values())
    for teams in teams_combos:
        teams_percentage[teams] = teams_counts[teams]/b
    sorted_dict = dict(sorted(teams_percentage.items(), key=lambda item: item[1], reverse=True))

    print(sorted_dict)
    time.sleep(10)
