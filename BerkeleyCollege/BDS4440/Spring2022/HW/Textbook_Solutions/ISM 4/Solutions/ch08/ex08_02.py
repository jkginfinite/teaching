# Exercise 8.2
import random

article = ['the', 'a', 'one', 'some', 'any']
noun = ['boy', 'girl', 'dog', 'town', 'car']
verb = ['drove', 'jumped', 'ran', 'walked', 'skipped']
preposition = ['to', 'from', 'over', 'under', 'on']

for i in range(20):
    words = [
        article[random.randrange(len(article))].capitalize(),
        noun[random.randrange(len(noun))],
        verb[random.randrange(len(verb))],
        preposition[random.randrange(len(preposition))],
        article[random.randrange(len(article))],
        noun[random.randrange(len(noun))]
    ]

    print(' '.join(words) + '.')


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
