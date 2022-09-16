# Exercise 9.8
import pickle as p

gradebook_dict = {'students' : []}

with open('grades.p', mode='wb') as grades:    
    print("""Enter a student's first name, last name and 
    three grades, separated by spaces. Enter -1 to end input """)
    line = input('?')
    
    while line != '-1':
        line = line.split()
        student_dict = {'first_name': line[0], 'last_name': line[1], 
            'exam1': int(line[2]), 'exam2': int(line[3]), 
            'exam3': int(line[4])}
        gradebook_dict['students'].append(student_dict)
        line = input('?')
        
    p.dump(gradebook_dict, grades)
    
with open('grades.p', 'rb') as grades:
    gradebook_dict = p.load(grades)

print(f'{"First":<10}{"Last":<10}{"Test1":>5}  {"Test2":>5}  {"Test3":>5}  {"Average"}')
test1_total = 0
test2_total = 0
test3_total = 0

for student in gradebook_dict['students']:  
    #test1, test2, test3 = int(test1), int(test2), int(test3)
    test1_total += student['exam1']
    test2_total += student['exam2']
    test3_total += student['exam3']
    average = (student['exam1'] + student['exam2'] + student['exam3']) / 3
    print(f"{student['first_name']:<10}{student['last_name']:<10}" +
          f"{student['exam1']:>5}  {student['exam2']:>5}  " +
          f"{student['exam3']:>5}  {average:>7.2f}")

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
