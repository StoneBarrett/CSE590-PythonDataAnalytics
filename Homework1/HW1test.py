# Test script for HW1.py
from random import randint
from matplotlib.pyplot import draw
import HW1

successprct = randint(1,100)
yardrange = (5, 25)
yards_to_TD = 80
num_drives = randint(1,10)
prctT1 = randint(1,100)
prctT2 = randint(1,100)
yrangeT1 = (5,25)
yrangeT2 = (5,25)


team1wins = 0
team2wins = 0
draws = 0

for i in range(1000):
    finalscore = HW1.simulategame(num_drives, prctT1, yrangeT1, prctT2, yrangeT2)
    print("Final score", finalscore)
    if finalscore[0] > finalscore[1]:
        team1wins += 1
    elif finalscore[0] < finalscore[1]:
        team2wins += 1
    else:
        draws += 1

print("t1 wins: ", team1wins)
print("t2 wins: ", team2wins)
print("draws: ", draws)