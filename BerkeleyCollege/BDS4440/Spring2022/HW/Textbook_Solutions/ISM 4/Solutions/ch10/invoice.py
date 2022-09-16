# invoice.py
"""Invoice class definition."""
from decimal import Decimal

class Invoice:
    """Invoice class."""
    
    def __init__(self, part_number, part_description, quantity, price):
        """Initialize an Invoice object."""
        self.part_number = part_number
        self.part_description = part_description
        self.quantity = quantity
        self.price = price
        
    @property
    def part_number(self):
        return self._part_number
    
    @part_number.setter
    def part_number(self, part_number):
        self._part_number = part_number
    
    @property
    def part_description(self):
        return self._part_description
    
    @part_description.setter
    def part_description(self, part_description):
        self._part_description = part_description
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise ValueError('Quantity must be >= to 0.')
        
        self._quantity = quantity
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price < Decimal('0.00'):
            raise ValueError('Proce must be >= to 0.00.')
        
        self._price = price
    
    def calculate_invoice(self):
        return self.quantity * self.price
    
    def __repr__(self):
        return (f'Invoice(part_number={self.part_number}, ' +
               f'part_description={self.part_description}, ' +
               f'quantity={self.quantity}, price={self.price})')
        


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
