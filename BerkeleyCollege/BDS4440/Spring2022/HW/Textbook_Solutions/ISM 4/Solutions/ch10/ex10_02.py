# Exercise 10.2

# Importing Classes Account and Decimal
from account import Account

from decimal import Decimal

# Create an Account Object with a Constructor Expression
account1 = Account('John Green', Decimal('50.00'))

# Getting an Account’s Name and Balance
account1.name

account1.balance

# Depositing Money into an Account
account1.deposit(Decimal('25.53'))

account1.balance

# Account Methods Perform Validation
account1.deposit(Decimal('-123.45'))


# Attempting to modify the name and balance
account1.name = 'Bob Blue'

account1.balance = Decimal('12345.67')

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
