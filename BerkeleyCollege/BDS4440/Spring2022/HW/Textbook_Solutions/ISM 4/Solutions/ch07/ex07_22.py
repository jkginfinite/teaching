# Exercise 7.22

import pandas as pd

pd.Series([7, 11, 13, 17])

pd.Series(100.0, range(5))

import numpy as np

random_numbers = pd.Series(np.random.randint(0, 101, 20))

random_numbers

random_numbers.describe()

temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], 
                         index=['Julie', 'Charlie', 'Sam', 'Andrea'])

temperatures

temps = {
    'Julie': 98.6, 
    'Charlie': 98.9, 
    'Sam': 100.2, 
    'Andrea': 97.9
}

pd.Series(temps)

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
