# Exercise 11.3
# Answer: Function mystery recursively totals the elements 
# of an array (will work for lists too).

def mystery(a_array, size):
    if size == 1:
        return a_array[0]
    else:
        return a_array[size - 1] + mystery(a_array, size - 1)
    
import numpy as np

numbers = np.arange(1, 11)

mystery(numbers, len(numbers))   

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
