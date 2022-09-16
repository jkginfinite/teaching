# Exercise 5.5

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# The first half of the string using starting and ending indices.
alphabet[0:len(alphabet) // 2]

# The first half of the string using only the ending index.
alphabet[:len(alphabet) // 2]

alphabet[len(alphabet) // 2:len(alphabet)]
# The second half of the string using starting and ending indices.

alphabet[len(alphabet) // 2:len(alphabet)]
# The second half of the string using only the starting index.

alphabet[len(alphabet) // 2:]

# Every second letter in the string starting with 'a'.
alphabet[::2]

# The entire string in reverse. 
alphabet[::-1]

# Every third letter of the string in reverse starting with 'z'.
alphabet[::-3]

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
