# Exercise 5.

def display_table(twoD_list, column_width):
    # Note: you can use a variable for the field width by enclosing it in braces
    
    # indent headers by width of max row index 
    indent = len(str(len(twoD_list)))
    print(f'{"":{indent}}', end='')

    for col in range(len(twoD_list[0])):
        print(f'{col:>{column_width}}', end='')

    print()

    for i, row in enumerate(twoD_list):
        print(f'{i:>{indent}}', end='')

        for value in row:
            print(f'{value:>{column_width}}', end='')

        print()
          
values = [list(range(90, 100)), 
          list(range(100, 110)), 
          list(range(110, 120)), 
          list(range(120, 130)), 
          list(range(130, 140)), 
          list(range(140, 150)), 
          list(range(150, 160)), 
          list(range(160, 170)), 
          list(range(170, 180)), 
          list(range(180, 190)), 
          list(range(190, 200))]

display_table(values, 5)

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
