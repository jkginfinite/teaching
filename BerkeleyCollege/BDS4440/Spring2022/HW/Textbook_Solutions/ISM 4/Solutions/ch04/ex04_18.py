# Exercise 4.18
"""Print four triangles of asterisks, side-by-side"""
for row in range(1, 11):
    # first triangle
    for column in range(1, row + 1):
        print('*', end='')
    for spaces in range(1, 10 - row):
        print(' ', end='')
    print('\t', end='')

    # second triangle
    for column in range(10, row - 1, -1):
        print('*', end='')
    for spaces in range(1, row):
        print(' ', end='')
    print('\t', end='')

    # third triangle
    for space in range(1, row):
        print(' ', end='')
    for column in range(10, row - 1, -1):
        print('*', end='')
    print('\t', end='')

    # fourth triangle
    for space in range(10, row, -1):
        print(' ', end='')
    for column in range(1, row + 1):
        print('*', end='')
    print()
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
