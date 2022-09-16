# Exercise 9.16
import pandas as pd

df = pd.read_csv('diamonds.csv', index_col=0)

df.head(7)

df.tail(7)

df.describe()

df.cut.describe()

df.color.describe()

df.clarity.describe()

df.cut.unique()

df.color.unique()

df.clarity.unique()

%matplotlib 

df.hist()



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
