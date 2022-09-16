# Exercise 4.14
"""Generate single-digit multiplication problems."""
import random
  
def create_question():
    """Creates a new question and returns the question text and answer."""
    # get two random numbers between 0 and 9
    digit1 = random.randrange(10)
    digit2 = random.randrange(10)

    return (f'How much is {digit1} * {digit2}?', digit1 * digit2)

def check_answer(guess, answer):
    """Check if user answered correctly and return a Boolean."""
    if guess != answer:
        print('No. Please try again.')
        return False
    else:
        print('Very Good!')
        return True       
  
# run the computer assisted instruction program
question, answer = create_question()
print(question)

guess = int(input('Enter your answer (-1 to exit): '))

while guess != -1:
    correct = check_answer(guess, answer)

    if correct:
        question, answer = create_question()
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
