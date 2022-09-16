# Exercise 5.7

non_duplicates
def unique(values):
    non_duplicates = []
    
    for value in values:
        if value not in non_duplicates:
            non_duplicates.append(value)
    
    non_duplicates.sort()
    return non_duplicates

unique(numbers)
numbers = [11, 11, 2, 2, 7, 7, 5, 5, 3, 3]

colors = ['red', 'red', 'orange', 'orange', 'yellow', 'yellow', 'green', 'green']
unique(colors)

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
