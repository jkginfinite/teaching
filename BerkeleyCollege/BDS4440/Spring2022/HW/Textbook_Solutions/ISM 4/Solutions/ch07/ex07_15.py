# Exercise 7.15

import numpy as np

array1 = np.array([[0, 1], [2, 3]])

array1

array2 = np.array([[4, 5], [6, 7]])

array2

array3 = np.concatenate((array1, array2))

array3

array4 = np.concatenate((array1, array2), axis=1)

array4

array5 = np.concatenate((array4, array4))

array5

array6 = np.concatenate((array3, array3), axis=1)

array6


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
