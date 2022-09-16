# Exercise 5.15

import random

letters = ['abcdef'[random.randrange(6)] for i in range(20)]

letters

# Sort the list in ascending order.
sorted(letters)
 
# Sort the list in descending order.
sorted(letters, reverse=True)

# Get the unique values sort them in ascending order.
non_duplicates = []

for c in letters:
    if c not in non_duplicates:
        non_duplicates.append(c)
        
sorted(non_duplicates)

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
