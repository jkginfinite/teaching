# Exercise 5.24

import random

import random

FACES = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def initialize_deck():
    deck = [(FACES[i % 13], SUITS[i // 13]) for i in range(52)]
    random.shuffle(deck)
    return deck

deck = initialize_deck()

for i, (face, suit) in enumerate(deck):
    card = face + ' of ' + suit
    print(f'{card:19}', end='')
    
    if (i + 1) % 4 == 0:
        print()


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
