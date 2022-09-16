# Exercise 3.27
"""Based on the current annual population growth rate and 
current world population, calcualte the world population 
after each of the next 100 years."""

print('Welcome to the world population calculator')
current_population = int(input('Enter the current world population: '))

growth_rate = float(input(
    'Enter the current growth rate: (e.g, 1.14% would be .0114): '))

print(f'Year{"Estimated Population":>22}{"Change":>13}')

for year in range(1, 101):
    future_population = current_population * (1 + growth_rate)
    print(f'{year:4d}{int(future_population):22d}', end='')
    print(f'{int(future_population - current_population):13d}')
    current_population = int(future_population)

    
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
