# Exercise 8.3

def pig_latin(sentence):
    tokens = sentence.lower().split()
        
    for index, word in enumerate(tokens):
        if len(word) > 1:
            if word[0] in 'aeiou':
                tokens[index] = word + 'ay'
            else:
                tokens[index] = word[1:] + word[0] + 'ay'
                
    return ' '.join(tokens)

sentence = input('Enter a sentence: ')

print(pig_latin(sentence))


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
