# Exercise 10.14
import dataclasses

from decimal import Decimal


Account = dataclasses.make_dataclass('Account',
              ['account', 'name', ('balance', Decimal)])

account1 = Account('100', 'Blue', Decimal('123.45'))

account2 = Account('200', 'Green', Decimal('765.43'))

account3 = Account('100', 'Blue', Decimal('123.45'))

account1

account2

account3

account1 == account2

account1 == account3

account1 != account2


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
