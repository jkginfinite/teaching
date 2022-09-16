# Exercise 5.11

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    counts = []
    
    for letter in string.lower():
        if letter in ALPHABET:
            if letter in letters:
                index = letters.index(letter)
                counts[index] += 1
            else:
                letters.append(letter)
                counts.append(1)
           
    tuples = list(zip(letters, counts))
    tuples.sort()
    return tuples

panagram = 'The Quick Brown Fox Jumps Over The Lazy Dog'
summary = summarize_letters(panagram)

# display counts
for char, count in summary:
    print(f'{char}: {count}')

# check if all letters of the alphabet were found in the string
all_letters = True

if len(summary) == len(ALPHABET):
    for item in summary:
        if item[0] not in ALPHABET:
            all_letters = False
            break  
else:
    all_letters = False

if all_letters:
    print(f'"{panagram}" contains all the letters in the alphabet')
else:
    print(f'"{panagram}" does not contain all the letters in the alphabet')
    

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
