# Exercise 2.11
number = int(input('Enter a five-digit integer:'))

digit1 = number // 10000
number = number % 10000

digit2 = number // 1000
number = number % 1000

digit3 = number // 100
number = number % 100

digit4 = number // 10

digit5 = number % 10

print(digit1, ' ', digit2, ' ', digit3, ' ', digit4, ' ', digit5)

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
