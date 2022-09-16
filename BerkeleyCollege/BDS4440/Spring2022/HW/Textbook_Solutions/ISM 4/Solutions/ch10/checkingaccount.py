# checkingaccount.py
"""Account class definition."""
from account import Account
from decimal import Decimal

class CheckingAccount(Account):
    """CheckingAccount class."""
    
    def __init__(self, name, balance, transaction_fee):
        """Initialize an CheckingAccount object."""
        
        # if transaction_fee is less than 0.00, raise an exception
        if transaction_fee < Decimal('0.00'):
            raise ValueError('Transaction fee must be >= to 0.00.')
         
        super().__init__(name, balance)
        self._transaction_fee = transaction_fee
        
    @property
    def transaction_fee(self):
        return self._transaction_fee
        
    def deposit(self, amount):
        """Deposit money to the account."""

        self._balance += amount - self.transaction_fee

    def withdraw(self, amount):
        """Withdraw money from the account."""

        # if amount is greater than balance, raise an exception
        if (amount + self.transaction_fee) > self._balance:
            raise ValueError('amount + transaction fee must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self._balance -= amount + self.transaction_fee
        


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
