# Exercise 10.18

import pandas as pd

la = pd.read_csv('ave_hi_la_jan_1895-2018.csv')

la.head()

la.tail()

la.columns = ['Date', 'Temperature', 'Anomaly']

la.head(3)

la.Date.dtype

la.Date = la.Date.floordiv(100)

la.head(3)

pd.set_option('precision', 2)

la.Temperature.describe()

from scipy import stats

linear_regression = stats.linregress(x=la.Date,
                                     y=la.Temperature)
linear_regression.slope

linear_regression.intercept

linear_regression.slope * 2019 + linear_regression.intercept

linear_regression.slope * 1850 + linear_regression.intercept

import seaborn as sns

sns.set_style('whitegrid')

axes = sns.regplot(x=la.Date, y=la.Temperature)

axes.set_ylim(10, 70)

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
