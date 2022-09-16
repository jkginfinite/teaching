# Exercise 3.19
"""Calculate Pythagorean triples."""
print(f'{"Side 1":<8}{"Side 2":<8}Hypotenuse')
for side1 in range(1, 21):
    for side2 in range(1, 21):
        for hypotenuse in range(1, 21):
            # use Pythagorean Theorem to print right triangles
            if side1 * side1 + side2 * side2 == hypotenuse * hypotenuse:
                print(f'{side1:<8}{side2:<8}{hypotenuse}')     

 

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
