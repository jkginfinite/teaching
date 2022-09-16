# Exercise 4.10
"""Guess the number."""
import random

def get_number():
    """Create a new number to guess."""
    return random.randrange(1, 1001)
   
def new_game():
    """Start a new game."""
    return get_number()
    print('Guess a number between 1 and 1000')

def check_guess(guess, answer):
    """Check user input"""
    correct = False
    
    if (guess < answer):
        print(f'{guess} is too low. Try again.')
    elif (guess > answer):
        print(f'{guess} is too high. Try again.')
    else:
        correct = True 
        print('Congratulations. You guessed the number!')
        print()

    return correct

# game logic
game_over = False    
            
while not game_over:
    answer = new_game()

    correct = False
    
    while not correct:
        correct = check_guess(int(input('Guess (1 - 1000): ')), answer)

    play_again = input('Play again (yes or no)? ')

    if play_again == 'no': 
       game_over = True

print('Thanks for playing!')

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
