# Exercise 5.25

import numpy as np
import random

FACES = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def initialize_deck():
    """Create and shuffle deck."""
    deck = [(FACES[i % 13], SUITS[i // 13]) for i in range(52)]
    random.shuffle(deck)
    return deck

def get_faces(hand):
    """Return just the faces in hand."""
    return [face for face, suit in hand]

def get_suits(hand):
    """Return just the suits in hand."""
    return [suit for face, suit in hand]

def sort_hand(hand):
    """Order hand by index of each face in FACES."""
    return sorted(hand, key=lambda card: FACES.index(card[0]))

# These functions assume the hand is in increasing order
# by the faces' index values in FACES
def is_straight_flush(hand):
    """Returns a Boolean indicating whether hand contains a straight and a flush,
    thus forming a straight flush."""
    return is_straight(hand) and is_flush(hand)

def is_four_of_a_kind(hand):
    """Returns a Boolean indicating whether hand contains four of a kind."""
    faces, counts = np.unique(get_faces(hand), return_counts=True)
    four_of_a_kind = len([count for count in counts if count == 4])
    return four_of_a_kind == 1

def is_full_house(hand):
    """Returns a Boolean indicating whether hand contains a full_house."""
    faces, counts = np.unique(get_faces(hand), return_counts=True)
    three_of_a_kind = len([count for count in counts if count == 3])
    two_of_a_kind = len([count for count in counts if count == 2])
    return three_of_a_kind == 1 and two_of_a_kind == 1

def is_flush(hand):
    """Returns a Boolean indicating whether hand contains a flush."""
    faces, counts = np.unique(get_suits(hand), return_counts=True)
    flush = len([count for count in counts if count in (2, 3)])
    return len(counts) == 1

def is_straight(hand):
    """Returns a Boolean indicating whether hand contains a straight."""
    # check for any 5 consecutive faces
    faces = get_faces(hand)
    for i in range(8):
        if faces == FACES[i:i+5]:
            return True
    
    # check for Ace-high straight
    if faces[0] == 'Ace' and faces[1:] == FACES[9:]:
        return True
    
    return False

def is_three_of_a_kind(hand):
    """Returns a Boolean indicating whether hand contains three of a kind."""
    faces, counts = np.unique(get_faces(hand), return_counts=True)
    three_of_a_kind = len([count for count in counts if count == 3])
    return three_of_a_kind == 1

def is_two_pair(hand):
    """Returns a Boolean indicating whether hand contains two pair."""
    faces, counts = np.unique(get_faces(hand), return_counts=True)
    pairs = len([count for count in counts if count == 2])
    return pairs == 2

def is_pair(hand):
    """Returns a Boolean indicating whether hand contains a pair."""
    faces, counts = np.unique(get_faces(hand), return_counts=True)
    pairs = len([count for count in counts if count == 2])
    return pairs == 1

def evaluate_hand(hand):
    if is_straight_flush(hand):
        return 'straight flush', 9
    elif is_four_of_a_kind(hand):
        return 'four of a kind', 8
    elif is_full_house(hand):
        return 'full house'
    elif is_flush(hand):
        return 'flush'
    elif is_straight(hand):
        return 'straight'
    elif is_three_of_a_kind(hand):
        return 'three of a kind'
    elif is_two_pair(hand):
        return 'two pair'
    elif is_pair(hand):
        return 'pair'
    else:
        return 'high card'
    
for i in range(1000):
    deck = initialize_deck()
    for i in range(0, 46, 5):
        hand = sort_hand(deck[i:i + 5])
        result = evaluate_hand(hand)
        print(result)
        for face, suit in hand:
            print(f'{face} of {suit}', end='  ')
        print('\n')

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
