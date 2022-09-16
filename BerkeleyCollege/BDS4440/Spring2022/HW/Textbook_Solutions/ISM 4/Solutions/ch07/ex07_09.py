# Exercise 7.9

import numpy as np

numbers = np.arange(1, 16).reshape(3, 5)

numbers

# Part a
numbers[2]

# **INSTRUCTOR NOTE: Part b should say "Select column 4"
# Part b
numbers[:, 4]

# Part c
numbers[:, 0:2]

# Part d
numbers[:, 2:5]

# Part e
numbers[1, 4]

# Part f
numbers[1:3, [0, 2, 4]]

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
