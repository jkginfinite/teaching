# Exercise 9.9
"""Telephone-Number Word Generator."""
# Note: phone number must be input in the form #######.
# Only the digits 2 through 9 are recognized.
letters = ['   ', '   ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'TUV', 'WXY']

phone = int(input('Enter a 7-digit phone number'))

# get the digits
digits = []

for i in range(7):
    digits.insert(0, phone % 10)
    phone //= 10
print(digits)

with open('phone.txt', 'w') as phone:
    # output all possible combinations
    for loop1 in range(3):
        for loop2 in range(3):
            for loop3 in range(3):
                for loop4 in range(3):
                    for loop5 in range(3):
                        for loop6 in range(3):
                            for loop7 in range(3):
                                print(letters[digits[0]][loop1], end='', file=phone)
                                print(letters[digits[1]][loop2], end='', file=phone)
                                print(letters[digits[2]][loop3], end='', file=phone)
                                print(letters[digits[3]][loop4], end='', file=phone)
                                print(letters[digits[4]][loop5], end='', file=phone)
                                print(letters[digits[5]][loop6], end='', file=phone)
                                print(letters[digits[6]][loop7], end=' ', file=phone)



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
