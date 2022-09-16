# savingsaccount.py
"""SavingsAccount class definition."""
from account import Account
from decimal import Decimal

class SavingsAccount(Account):
    """SavingsAccount class."""
    
    def __init__(self, name, balance, interest_rate):
        """Initialize an SavingsAccount object."""
        
        # if interest_rate is out of range, raise an exception
        if interest_rate < Decimal('0.00') or interest_rate > Decimal('1.00'):
            raise ValueError('Interest rate must be in the range 0.0-1.0.')
            
        super().__init__(name, balance)
        self._interest_rate = interest_rate
        
    @property
    def interest_rate(self):
        return self._interest_rate
        
    def calculate_interest(self):
        return round(self.interest_rate * self.balance, 2)


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
