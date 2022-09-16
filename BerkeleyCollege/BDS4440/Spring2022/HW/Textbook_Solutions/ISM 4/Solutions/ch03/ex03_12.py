# Exercise 3.12
"""Test for a palindrome"""
number = int(input('Enter a 5-digit number: '))
 
digit1 = number // 10000
digit2 = number % 10000 // 1000
digit4 = number % 10000 % 1000 % 100 // 10
digit5 = number % 10000 % 1000 % 100 % 10

if digit1 == digit5 and digit2 == digit4:
    print(f'{number} is a palindrome!!!')
else:
    print(f'{number} is not a palindrome.')

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
