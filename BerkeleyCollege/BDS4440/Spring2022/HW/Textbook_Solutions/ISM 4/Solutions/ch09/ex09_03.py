# Exercise 9.3
import csv

with open('grades.csv', mode='w', newline='') as grades:
    writer = csv.writer(grades)
    
    print("""Enter a student's first name, last name and 
    three grades, separated by spaces. Enter -1 to end input """)
    line = input('?')
    
    while line != '-1':
        line = line.split()
        writer.writerow([line[0], line[1], int(line[2]), 
                         int(line[3]), int(line[4])])
        line = input('?')


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
