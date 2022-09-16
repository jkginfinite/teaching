# Exercise 3.11
"""Calculating miles per gallon."""
total_miles = 0
total_gallons = 0

gallons = float(input('Enter the gallons used (-1 to end): '))

while gallons != -1:
    miles = float(input('Enter the miles driven: '))

    total_miles += miles
    total_gallons += gallons

    if gallons != 0:
        miles_per_gallon = miles / gallons
        print(f'The miles/gallon for this tank was {miles_per_gallon}')           

    gallons = float(input('Enter the gallons used (-1 to end): '))

if total_gallons != 0:
    total_miles_per_gallon = total_miles / total_gallons
    print(f'Total MPG so far: {total_miles_per_gallon}')

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
