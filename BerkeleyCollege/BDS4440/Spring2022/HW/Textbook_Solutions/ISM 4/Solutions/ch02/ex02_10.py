# Exercise 2.10
number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

print('Sum:', number1 + number2 + number3)
print('Average:', (number1 + number2 + number3) / 3)
print('Product:', number1 * number2 * number3)

smallest = number1

if number2 < smallest: 
    smallest = number2
    
if number3 < smallest: 
    smallest = number3

print('Smallest:', smallest)

largest = number1

if number2 > largest: 
    largest = number2
    
if number3 > largest: 
    largest = number3

print('Largest:', largest)

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
