# Exercise 3.28
"""Calculate the mean, median and mode of the values 
9, 11, 22, 34, 17, 22, 34, 22 and 40."""
import statistics as stats

values = [9, 11, 22, 34, 17, 22, 34, 22, 40]

print(f'Mean: {stats.mean(values):.2f}')
print(f'Median: {stats.median(values):.2f}')
print(f'Mode: {stats.mode(values):.2f}')

    
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
