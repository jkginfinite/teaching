# Exercise 9.4
import csv

with open('grades.csv', 'r', newline='') as grades:
    print(f'{"First":<10}{"Last":<10}{"Test1":>5}  {"Test2":>5}  {"Test3":>5}')
    reader = csv.reader(grades)
    for record in reader:  
        first, last, test1, test2, test3 = record
        print(f'{first:<10}{last:<10}{test1:>5}  {test2:>5}  {test3:>5}')


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
