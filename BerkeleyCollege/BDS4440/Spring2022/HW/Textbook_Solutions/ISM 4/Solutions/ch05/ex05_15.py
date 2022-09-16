# Exercise 5.15

invoices = [(83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]

from operator import itemgetter

# sort the tuples by part description
for part, desc, quant, price in sorted(invoices, key=itemgetter(1)):
    print(f'{part:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
# sort the tuples by price
for part, desc, quant, price in sorted(invoices, key=itemgetter(3)):
    print(f'{part:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
# Map each invoice tuple to a tuple containing the part description
# and quantity, sort the results by quantity, then display the results.
quantities = [(desc, quant) for part, desc, quant, price in invoices]

for desc, quant in sorted(quantities, key=itemgetter(1)):
    print(f'{desc:<16}{quant:>3}')
    
# Map each invoice tuple to a tuple containing the part description and
# the value of the invoice, sort the results by the invoice value
prices = [(desc, quant * price) for part, desc, quant, price in invoices]

for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
# Modify Part (d) to filter the results to invoice values in the range $200 to $500.
prices = [(desc, quant * price) for part, desc, quant, price in invoices\
          if 200 <= quant * price <= 500]

for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
# Calculate the total of all the invoices. 
total = sum([(quant * price) for part, desc, quant, price in invoices])

print(f'Total for all invoices is: {total:.2f}')

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
