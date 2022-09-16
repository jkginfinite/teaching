# Exercise 3.17
"""Print four triangles of asterisks, one below the other"""

# first triangle
for row in range(1, 11):
    for column in range(1, row + 1):
        print('*', end='')
    print()
print()

# second triangle
for row in range(10, 0, -1):
    for column in range(1, row + 1):
        print('*', end='')
    print()
print()

# third triangle
for row in range(10, 0, -1):
    for space in range(10, row, -1):
        print(' ', end='')
    for column in range(1, row + 1):
        print('*', end='')
    print()
print()

# fourth triangle
for row in range(10, 0, -1):
    for space in range(1, row):
        print(' ', end='')
    for column in range(10, row - 1, -1):
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
