# point.py
"""Point class definition."""

class Point:
    """Point class for maintaining an x-y location."""
    
    def __init__(self, x, y):
        """Initialize a Point object."""
        self.x = x
        self.y = y
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y
        
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
    
    def move(self, p):
        self.x = p.x
        self.y = p.y

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
