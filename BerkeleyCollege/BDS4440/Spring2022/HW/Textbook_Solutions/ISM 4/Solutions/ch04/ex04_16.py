# Exercise 4.16
"""Generate single-digit multiplication problems."""
import random
  
def create_question(difficulty_level):
    """Creates a new question and returns the question text and answer."""
    # get two random numbers between 0 and 9
    number1 = random.randrange(10 ** difficulty_level)
    number2 = random.randrange(10 ** difficulty_level)

    return (f'How much is {number1} * {number2}?', number1 * number2)

def check_answer(guess, answer):
    """Check if user answered correctly and return a Boolean."""
    if guess != answer:
        print(get_response(correct=False))
        return False
    else:
        print(get_response(correct=True))
        return True

def get_response(correct):
    if correct:
        response = random.randrange(4)
        
        if response == 0:
           return 'Very good!'
        elif response == 1:
           return 'Excellent!'
        elif response == 2:
           return 'Nice work!'
        elif response == 3:
           return 'Keep up the good work!'
    else:
        response = random.randrange(4)

        if response == 0:
           return 'No. Please try again.'
        elif response == 1:
           return 'Wrong. Try once more.'
        elif response == 2:
           return "Don't give up!"
        elif response == 3:
           return 'No. Keep trying.'

# run the computer assisted instruction program
difficulty_level = int(input('Enter difficulty level (1 or 2): '))
question, answer = create_question(difficulty_level)
print(question)

guess = int(input('Enter your answer (-1 to exit): '))

while guess != -1:
    correct = check_answer(guess, answer)

    if correct:
        question, answer = create_question(difficulty_level)
        print(question)
        
    guess = int(input('Enter your answer (-1 to exit): '))

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
