# Exercise 5.4

values = [[0, 0, 0],
          [0, 0, 0]]

count = 1

for row in range(len(values)):
    for col in range(len(values[row])):
        values[row][col] = count
        count += 1
        
print('   ', end='')

for col in range(len(values[0])):
    print(f'{[col]} ', end='')
    
print()

for i, row in enumerate(values):
    print(f'{[i]}', end='')
    
    for value in row:
        print(f'{value:3d} ', end='')
        
    print()

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
