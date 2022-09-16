# Exercise 6.9
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

print('Canada' in tlds)

print('France' in tlds)

for key, value in tlds.items():
    print(f'{key:20}{value}')

tlds['Sweden'] = 'sw'
print(tlds)

tlds['Sweden'] = 'se'
print(tlds)

reverse_mapping = {value: key for key, value in tlds.items()}
print(reverse_mapping)

{key: value.upper() for key, value in reverse_mapping.items()}

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
