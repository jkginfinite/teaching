# Exercise 6.11
# ex06_11.py
"""Simulating the dice game Craps."""
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

wins = {}
losses = {}

for i in range(1_000_000):
    # determine game status and point, based on first roll
    die_values = roll_dice()  # first roll
    sum_of_dice = sum(die_values)
    rolls = 1

    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        rolls += 1
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
    
    # display "wins" or "loses" message
    if rolls > 21:
        rolls = 21
        
    if game_status == 'WON':
        wins[rolls] = wins[rolls] + 1 if rolls in wins else 1
    else:
        losses[rolls] = losses[rolls] + 1 if rolls in losses else 1
                                       
# display number of wins and losses on all rolls
total_length = 0

for i in range(1, 22):
    print(f'{wins.get(i, 0):7d} games won and {losses.get(i, 0):7d} games lost on',
         f'roll #{i}' if i in range(1, 21) else 'after the 20th roll')

    # for calculating length of game
    # number of wins/losses on that roll multiplied
    # by the roll number, then add them to length
    total_length += wins.get(i, 0) * i + losses.get(i, 0) * i;

# calculate chances of winning
total_games = sum(wins.values()) + sum(losses.values())
total_wins = sum(wins.values())
                                       
print(f'\nThe chances of winning are {total_wins} / {total_games} = {total_wins / total_games:.2%}')
print(f'The average game length is {total_length / total_games:.2f} rolls')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
