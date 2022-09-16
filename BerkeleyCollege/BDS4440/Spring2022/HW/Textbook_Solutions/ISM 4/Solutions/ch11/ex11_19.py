# Exercise 11.19
def quick_sort(data, left, right):
    """recursive method to sort array using quicksort"""
    pivot = partition(data, left, right)

    if left < pivot - 1:  # if more than one element on left
        quick_sort(data, left, pivot - 1)  # sort left side

    if pivot + 1 < right:  # if more than one element on right
        quick_sort(data, pivot + 1, right)  # sort right side

def partition(data, left, right):
    """partition the given range and return final index of pivot"""
    pivot = left  # index of pivot element

    # loop until two edges meet
    while True: 
        # search for data to right of pivot greater than pivot
        while data[right] >= data[pivot]: 
            if right == pivot:
                return pivot  # partitioning completed
            
            right -= 1  # move left one element

        # move right element into correct location
        data[pivot], data[right] = data[right], data[pivot]

        pivot = right  # update pivot location
        right -= 1  # move right edge left

        while data[left] <= data[pivot]:
            if left == pivot:
                return pivot  # partitioning completed
            
            left += 1  # move right one element

        # move left element into correct location
        data[pivot], data[left] = data[left], data[pivot]

        pivot = left  # update pivot location 
        left += 1  # move left edge right

import numpy as np
data = np.random.randint(100, size=20)
print(f'Unsorted array: {data}')
quick_sort(data, 0, len(data) - 1)  # sort array
print(f'Unsorted array: {data}')   

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
