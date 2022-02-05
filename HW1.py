# Stone Barrett
# CSE 590 Python Data Analytics
# Homework 1

# Importing libraries
from random import randint

#################################################################
#################### PROBLEM 1 ##################################
#################################################################
# Optional: include sacks and penalties for extra credit (done)

# Down method
def down(successprct, yardrange):
    
    # Setting up variables
    randnum = randint(1,100)
    sackchance = randint(1,100)
    penaltychance = randint(1,100)
    yardsreturned = randint(min(yardrange), max(yardrange))

    # Running down
    # Case: play fails
    if randnum > successprct:
        return 0
    # Case: sack and no offensive penalty
    elif sackchance > successprct and penaltychance < successprct:
        return yardsreturned - 5
    # Case: offensive penalty and no sack
    elif penaltychance > successprct and sackchance < successprct:
        return yardsreturned - 10
    # Case: sack and offensive penalty
    elif sackchance > successprct and penaltychance > successprct:
        return yardsreturned - 15
    # Case: no sack and no offensive penalty
    else:
        return yardsreturned

#################################################################
#################### PROBLEM 2 ##################################
#################################################################
# Optional: include notions of first downs for extra credit (done)

# Drive method
def drive(yards_to_TD, successprct, yardrange):
    
    # Setting up variables
    pointsscored = 0
    oposition = 0
    extrapointchance = randint(1,100)
    yardsgained = 0
    currentdownyards = 0

    # Running 4 downs
    for i in range(4):
        currentdownyards = down(successprct, yardrange)
        yards_to_TD -= currentdownyards
        # Extra penalty handling
        if yards_to_TD > 100:
            yards_to_TD = 100
        yardsgained += currentdownyards
        # Case: first down
        if yardsgained >= 10:
            i = 0
        if yards_to_TD <= 0:
            # Case: score and extra point
            if extrapointchance >= 90:
                pointsscored = 7
                oposition = 80
                break
            # Case: score and no extra point
            else:
                pointsscored = 6
                oposition = 80
                break
        # Case: havent scored by end of 4th down
        if i == 3:
            pointsscored = 0
            oposition = 100 - yards_to_TD

    # Returning
    returntuple = (pointsscored, oposition)
    return returntuple
   
#################################################################
#################### PROBLEM 3 ##################################
#################################################################
# Optional: use visualisation libraries to make a better representation of the simulation for extra credit (not done)

# Depiction method
def drive_depicted(yards_to_TD, successprct, yardrange):
    
    # Setting up variables
    pointsscored = 0
    oposition = 0
    extrapointchance = randint(1,100)
    yardsgained = 0
    currentdownyards = 0
    depiction = list("O----------------------------------------------------------------------------------------------------X")
    
    # Running 4 downs
    for i in range(4):
        currentdownyards = down(successprct, yardrange)
        yards_to_TD -= currentdownyards
        yardsgained += currentdownyards
        # Extra penalty handling
        if yards_to_TD > 100:
            yards_to_TD = 100
        # Case: first down
        if yardsgained >= 10:
            i = 0
            # Edge case handling
            if yards_to_TD < 0:
                yards_to_TD = 0
            depiction[100 - yards_to_TD] = ">"
            print(*depiction)
            print("1st Down, {} yards to go".format(yards_to_TD))
        if yards_to_TD <= 0:
            # Case: score and extra point
            if extrapointchance >= 90:
                pointsscored = 7
                oposition = 80
                depiction[101] = "T"
                print(*depiction)
                print("TD + Extra Point Scored!")
                break
            # Case: score and no extra point
            else:
                pointsscored = 6
                oposition = 80
                depiction[101] = "T"
                print(*depiction)
                print("TD Scored!")
                break
        # Case: havent scored by end of 4th down
        if i == 3:
            pointsscored = 0
            oposition = 100 - yards_to_TD
            # Edge case handling
            if yards_to_TD < 0:
                yards_to_TD = 0
            depiction[100 - yards_to_TD] = "Q"
            print(*depiction)
            print("Turnover, {} yards to go".format(yards_to_TD))
            break
        # Case: havent scored but more downs remaining
        # Edge case handling
        if yards_to_TD < 0:
            yards_to_TD = 0
        depiction[100 - yards_to_TD] = ">"
        print(*depiction)
        print("{} Down, {} yards to go".format(i+1, yards_to_TD))

    # Returning
    returntuple = (pointsscored, oposition)
    return returntuple

#################################################################
#################### PROBLEM 4 ##################################
#################################################################

# Game method
def simulategame(num_drives, prctT1, yrangeT1, prctT2, yrangeT2):

    # Setting up variables
    scoreT1 = 0
    scoreT2 = 0
    yards_to_TD = 80

    # Running game
    for i in range(num_drives):

        # Drive T1
        t1tuple = drive_depicted(yards_to_TD, prctT1, yrangeT1)
        scoreT1 += t1tuple[0]
        yards_to_TD = t1tuple[1]

        # Drive T2
        t2tuple = drive_depicted(yards_to_TD, prctT2, yrangeT2)
        scoreT2 += t2tuple[0]
        yards_to_TD = t2tuple[1]

    # Ending game
    finalscore = (scoreT1, scoreT2)
    return finalscore
