# Exercise 5.9

def is_palindrome(string):
    stack = []
    for character in string:
        stack.append(character)
    
    for character in string:
        popped_value = stack.pop()
        if character.lower() != popped_value.lower():
            return False
    
    return True

is_palindrome('abcd')

is_palindrome('radar')

is_palindrome('able was i ere I Saw 

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
