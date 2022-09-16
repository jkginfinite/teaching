# Exercise 6.7
# ex06_07.py
"""Character counts."""

text = ('this is sample text with several words ' 
        'this is more sample text with some different words')

characters = []
for word in text.lower().split():
    characters.extend(list(word))

character_counts = {}

# count occurrences of each unique word
for character in characters:
    if character in character_counts: 
        character_counts[character] += 1  # update existing key-value pair
    else:
        character_counts[character] = 1  # insert new key-value pair

print(f'{"CHARACTER":<12}COUNT')

for character, count in sorted(character_counts.items()):
    print(f'{character:<12}{count}')

# Note: We did not introduce string.ascii_lowercase or string.digits in the book,
# but they contain the alphabet and digits respectively, so you can have your 
# students use these or simply define their own strings
import string
unique_letters = set(character_counts.keys()) - set('string.digits')
alphabet = set(string.ascii_lowercase) 
print(f'\nletters not in original string\n{sorted(alphabet - unique_letters)}')

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
