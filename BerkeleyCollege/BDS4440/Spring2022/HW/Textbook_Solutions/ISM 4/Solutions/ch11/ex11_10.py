# Exercise 11.10

def test_palindrome(text, left, right):
    # remove punctuation on left of current substring
    while not text[left].isalnum():
        left += 1

    # remove punctuation on right of current substring
    while not text[right].isalnum():
        right -= 1

    # if there are no characters left in array to analyze
    if left >= right:
        return True
    elif text[left].lower() != text[right].lower():  # if left/right characters are not equal
        return False
    else:
        return test_palindrome(text, left + 1, right - 1)
    
s = 'radar'
test_palindrome(s, left=0, right=len(s) - 1)

s = 'hello'
test_palindrome(s, left=0, right=len(s) - 1)

s = 'able was i ere i saw elba'
test_palindrome(s, left=0, right=len(s) - 1)

s = 'a man a plan a canal panama'
test_palindrome(s, left=0, right=len(s) - 1)

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
