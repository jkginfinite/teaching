# Exercise 8.15

import re

string = 'this string contains words and 1234567890'

digits = re.findall(r'\d', string)
print('The number of digits is', len(digits))

non_digits = re.findall(r'\D', string)
print('The number of non-digit characters is', len(non_digits))

whitespace = re.findall(r'\s', string)
print('The number of whitespace characters is', len(whitespace))

words = re.findall(r'\w+', string)
print('The number of words is', len(words))


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
