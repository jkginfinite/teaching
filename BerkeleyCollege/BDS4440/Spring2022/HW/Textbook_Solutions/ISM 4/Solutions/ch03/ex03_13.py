# Exercise 3.13
"""Calculate the factorial of a non-negative integer"""
number = int(input('Enter a non-negative integer: '))

if number < 0:
    print('Number must be non-negative')
else:
    factorial = 1
    
    for i in range(number, 1, -1):
        factorial *= i
    
    print(f'{number}! is {factorial}')

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
