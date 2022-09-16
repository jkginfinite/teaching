# Exercise 5.8
"""Sieve of Eratosthenes."""
primes = [True for i in range(1000)]

# starting at index 2, cycle through the list and set all 
# multiples of the current index to False 
# as the value of any greater number that is a multiple
for i in range(2, len(primes)):
    if primes[i]:
        for j in range(i + i, len(primes), i):
            primes[j] = False
            
# cycle through the array one last time to print all primes
primes_found = 0  

for i in range(2, len(primes)):
    if primes[i]:
        print(f'{i:4d} ', end='')
        primes_found += 1
        
        if primes_found % 10 == 0:
            print()

print(f'\nFound {primes_found} primes')

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
