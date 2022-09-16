# Exercise 5.13
"""Word or Phrase to Phone-Number Generator."""
# Requires a string containing only letters in ABCDEFGHIJKLMNOPRSTUVWXY

letters = ['   ', '   ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'TUV', 'WXY']

word = input('Enter a 7-character word with no punctuation and no Qs and Zs: ')

# get the digits
phone = ''

for letter in word:
    for index, string in enumerate(letters):
        if letter in string:
            phone += str(index)

print(phone)



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
