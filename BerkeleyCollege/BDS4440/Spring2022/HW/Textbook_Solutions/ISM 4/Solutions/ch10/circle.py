# circle.py
"""Circle class definition."""

class Circle:
    """Circle class for maintaining a point and radius."""
    
    def __init__(self, point, radius):
        """Initialize a Point object."""
        self._point = point
        self.radius = radius
        
    @property
    def point(self):
        return self._point
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius  # could validate
        
    def __repr__(self):
        return f'Circle(point={self.point}, radius={self.radius})'
    
    def move(self, new_location):
        self.point.move(new_location)


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
