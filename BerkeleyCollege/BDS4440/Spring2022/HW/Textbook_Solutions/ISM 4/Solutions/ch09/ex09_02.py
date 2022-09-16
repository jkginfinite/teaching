# Exercise 9.2

with open('grades.txt', mode='r') as grades:
    total = 0
    count = 0
    
    for grade in grades:
        total += int(grade)
        count += 1
        
    print(f'Number of grades read: {count}')
    print(f'Total of all grades: {total}')
    print(f'Average grade: {total / count:.2f}')


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
