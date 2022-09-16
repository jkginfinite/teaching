# Exercise 5.28
import numpy as np
import statistics as stats

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values, counts = np.unique(responses, return_counts=True)
values = list(values)
counts = list(counts)

print('Reponses and frequencies:')
for value, count in zip(values, counts):
    print(f'{value}: {count}')

print(f'Min response count: {values[counts.index(min(counts))]} occurred {min(counts)} time(s)')
print(f'Max response count: {values[counts.index(max(counts))]} occurred {max(counts)} time(s)')
print(f'Range of response counts: {min(counts)}-{max(counts)}')
print(f'Mean response count: {stats.mean(counts)}')
print(f'Median response count: {stats.mean(counts)}')
print(f'Mode response count: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard deviation: {stats.pstdev(counts)}')


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
