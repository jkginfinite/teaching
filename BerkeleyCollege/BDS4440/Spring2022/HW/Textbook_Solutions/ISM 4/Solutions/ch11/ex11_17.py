# Exercise 11.17
import math

def bucket_sort(data):
    """Sort an array's values into ascending order using bucket sort."""

    # Determine largest number of digits in numbers to sort
    totalDigits = int(math.log10(max(data)) + 1)

    # bucket array where numbers will be placed
    pail = [[0] * len(data) for i in range(10)]

    # go through all digit places and sort each number
    # according to digit place value
    for pass_number in range(1, totalDigits + 1): 
        distribute_elements(data, pail, pass_number)  # distribution pass
        collect_elements(data, pail)  # gathering pass

        if pass_number != totalDigits: 
            empty_bucket(pail)  # set size of buckets to 0
    
def distribute_elements(data, pail, digit):
    """Distribute elements into buckets based on specified digit"""
    # determine the divisor used to get specific digit
    divisor = 10 ** digit

    for element in data:
        # bucket_number example for hundreds digit:
        # (1234 % 1000) // 100 --> 2
        bucket_number = (element % divisor) // (divisor // 10)

        # retrieve value in pail[bucket_number][0] to
        # determine which element of the row to store c[i]
        pail[bucket_number][0] += 1
        element_number = pail[bucket_number][0]
        pail[bucket_number][element_number] = element

def collect_elements(data, pails):
    """Eeturn elements to original array"""
    subscript = 0  # initialize location in data

    for i in range(10):  # loop over buckets
        for j in range(1, pails[i][0] + 1):  # loop over elements in each bucket
            data[subscript] = pails[i][j]  # add element to array
            subscript += 1

def empty_bucket(pails):
    """Set size of all buckets to zero"""
    for i in range(10): 
        pails[i][0] = 0 # set size of bucket to 0
        
        
import numpy as np    
data = np.random.randint(100, size=20)
print(f'Unsorted array: {data}')
bucket_sort(data)  # sort array
print(f'Sorted array: {data}')

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
