# Exercise 11.18
"""Use recuirsive binary search to locate an item in an array."""
import numpy as np

def recursive_binary_search(data, key, low, high):
    """Perform binary search of data looking for key."""
    
    if low > high:  # test base case; no element left to check
        return -1
    
    middle = (low + high + 1) // 2  # middle element index
    
    # print remaining elements of array
    print(remaining_elements(data, low, high))
        
    print('   ' * middle, end='')  # output spaces for alignment
    print(' * ')  # indicate current middle
    
    location = -1  # return value -1 if not found
    
    # if the element is found at the middle                    
    if key == data[middle]:                                   
        location = middle  # location is the current middle     
    elif key < data[middle]:  # middle element is too high
        # eliminate the higher half    
        location = recursive_binary_search(data, key, low, middle - 1)      
    else:  # middle element is too low                         
        low = middle + 1  
        # eliminate the lower half   
        location = recursive_binary_search(data, key, middle + 1, high)

    return location  # return location of search key
                            
def remaining_elements(data, low, high):
    """Display remaining elements of the binary search."""
    return '   ' * low + ' '.join(str(s) for s in data[low:high + 1])

def main():
    # create and display array of random values
    data = np.random.randint(10, 91, 15)
    data.sort()
    print(data, '\n')

    key = int(input('Enter an integer value (-1 to quit): ')) 

    # repeatedly input an integer; -1 terminates the program
    while key != -1:
        location = recursive_binary_search(data, key, 0, len(data) - 1) 

        if location == -1:  # not found
            print(f'{key} was not found\n') 
        else:
            print(f'{key} found in position {location}\n')

        key = int(input('Enter an integer value (-1 to quit): '))

# call main if this file is executed as a script
if __name__ == '__main__':
    main()
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
