# Exercise 9.1

with open('grades.txt', mode='w') as grades:
    grade = int(input('Enter grade, -1 to end: '))  # get one grade
    
    while grade != -1:
        print(grade, file=grades)  # or grades.write(str(grade) + '\n')
        grade = int(input('Enter grade, -1 to end: '))  # get one grade


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
