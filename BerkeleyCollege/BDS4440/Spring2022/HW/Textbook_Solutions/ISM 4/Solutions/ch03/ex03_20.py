# Exercise 3.20
"""Print the decimal equivalent of a binary number."""
bit = 1  # bit positional value
decimal = 0  # decimal value

binary = int(input('Enter a binary number: '))

# convert to decimal equivalent
while binary != 0:
    decimal += binary % 10 * bit
    binary //= 10
    bit *= 2

print(f'Decimal is: {decimal}')
 

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
