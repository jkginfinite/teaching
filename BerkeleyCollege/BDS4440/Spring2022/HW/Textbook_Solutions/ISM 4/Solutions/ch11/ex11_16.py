# Exercise 11.16
# Instructor Note: We reduced the size of the array 
# from 100,000 to 10,000 as 100,000 elements caused 
# our system to freeze.

import numpy as np

import selectionsort, insertionsort, mergesort

data1 = np.random.randint(10_000, size=10_000)

data2 = data1.copy()

data3 = data1.copy()

%timeit -n 1 -r 1 selectionsort.selection_sort(data1)

%timeit -n 1 -r 1 insertionsort.insertion_sort(data2)

%timeit -n 1 -r 1 mergesort.merge_sort(data3)

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
