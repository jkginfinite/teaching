# Exercise 11.2
# Answer: The recursion step does not make n approach the base case. Change sum(n) to sum(n - 1).

# def sum(n):
#    if n == 0:
#        return 0
#    else:
#        return n + sum(n)

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)  # error corrected
    
sum(10)

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
