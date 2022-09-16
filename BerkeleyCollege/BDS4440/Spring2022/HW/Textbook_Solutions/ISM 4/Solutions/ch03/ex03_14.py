# Exercise 3.14
"""Calculate pi from infinite series."""
pi = 0
numerator = 4.0 
denominator = 1.0
accuracy = 100000  # maximum number of terms in series

print(f'Accuracy: {accuracy}\n')
print(f'{"Term":<8}pi')

for term in range(1, accuracy + 1):
    if term % 2 != 0:
        pi += numerator / denominator
    else:
        pi -= numerator / denominator

    print(f'{term:<8}{pi:.16f}')
    denominator += 2.0

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
