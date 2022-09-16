# salariedemployee.py
"""SalariedEmployee class."""
from decimal import Decimal

class SalariedEmployee:
    """An employee who gets paid a fixed weekly salary."""

    def __init__(self, first_name, last_name, ssn, salary):
        """Initialize SalariedEmployee's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.salary = salary  # validate via property

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        """Set salary or raise ValueError if invalid."""
        if salary < Decimal('0.00'):
            raise ValueError('Salary must be >= to 0')
        
        self._salary = salary
        
    def earnings(self):
        """Calculate earnings."""   
        return self.salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('SalariedEmployee: ' + 
            f'{self.first_name} {self.last_name}\n' +
            f'social security number: {self.ssn}\n' +
            f'salary: {self.salary:.2f}')


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
