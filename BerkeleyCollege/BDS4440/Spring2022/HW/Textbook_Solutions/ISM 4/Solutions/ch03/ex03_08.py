# Exercise 3.8
total = 0
product = 1
smallest = 100000000000000000000000000000000000000000000000
largest = -100000000000000000000000000000000000000000000000

for i in range(4):
    number = int(input('Enter an integer: '))
    total += number
    product *= number
    
    if number < smallest:
        smallest = number

    if number > largest:
        largest = number

print('Sum:', total)
print('Average:', (total) / 3)
print('Product:', product)
print('Smallest:', smallest)
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
