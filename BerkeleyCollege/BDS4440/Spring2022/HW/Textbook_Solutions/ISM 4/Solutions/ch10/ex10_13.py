# Exercise 10.13

def maximum(value1, value2, value3):
    """Return the maximum of three values.
    
    >>> maximum(1, 2, 3)
    3
    >>> maximum(2, 1, 3)
    3
    >>> maximum(3, 1, 2)
    3
    >>> maximum(1.1, 2.2, 3.3)
    3.3
    >>> maximum(2.2, 1.1, 3.3)
    3.3
    >>> maximum(3.3, 1.1, 2.2)
    3.3
    >>> maximum('a', 'b', 'c')
    'c'
    >>> maximum('b', 'a', 'c')
    'c'
    >>> maximum('c', 'a', 'b')
    'c'
    """
    max_value = value1
    
    if value2 > max_value:
        max_value = value2
        
    if value3 > max_value:
        max_value = value3
        
    return max_value

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    
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
