# Exercise 9.5
import csv

with open('grades.csv', 'r', newline='') as grades:
    print(f'{"First":<10}{"Last":<10}{"Test1":>5}  {"Test2":>5}  {"Test3":>5}  {"Average"}')
    reader = csv.reader(grades)
    test1_total = 0
    test2_total = 0
    test3_total = 0
          
    for record in reader:  
        first, last, test1, test2, test3 = record
        test1, test2, test3 = int(test1), int(test2), int(test3)
        test1_total += test1
        test2_total += test2
        test3_total += test3
        average = (test1 + test2 + test3) / 3
        print(f'{first:<10}{last:<10}{test1:>5}  {test2:>5}  {test3:>5}  {average:>7.2f}')

    print(f'{"Test Averages":<20}{test1_total/3:>5.2f}  {test2_total/3:>5.2f}  {test2_total/3:>5.2f}')

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
