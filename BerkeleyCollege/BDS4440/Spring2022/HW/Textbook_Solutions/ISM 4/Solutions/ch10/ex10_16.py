# Exercise 10.16

from savingsaccount import SavingsAccount

from checkingaccount import CheckingAccount

from decimal import Decimal

savings_account = SavingsAccount('Amanda Blue', Decimal('500.00'), Decimal('0.03'))

savings_account.calculate_interest()

savings_account.deposit(savings_account.calculate_interest())

savings_account.balance

checking_account = CheckingAccount('Bob Greem', Decimal('300.00'), Decimal('0.50'))

checking_account.deposit(Decimal('100.00'))

checking_account.balance

checking_account.withdraw(Decimal('100.00'))

checking_account.balance

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
