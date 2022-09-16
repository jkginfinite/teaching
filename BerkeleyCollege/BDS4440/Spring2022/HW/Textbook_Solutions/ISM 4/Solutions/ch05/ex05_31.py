# Exercise 5.31

"""Graphing frequencies of coin flips with Seaborn."""
import matplotlib.pyplot as plt
import numpy as np
import random 
import seaborn as sns
import sys

# use list comprehension to create a list of coin flips
face = ['head', 'tail']
flips = [face[random.randrange(2)] for i in range(int(sys.argv[1]))]  

# NumPy unique function returns unique faces and frequency of each face
values, frequencies = np.unique(flips, return_counts=True)

title = f'Flipping a coin {len(flips):,} Times'
sns.set_style('whitegrid')  # white backround with gray grid lines
axes = sns.barplot(values, frequencies, palette='bright')  # create bars
axes.set_title(title)  # set graph title
axes.set(xlabel='Face', ylabel='Frequency')  # label the axes

# scale y-axis by 10% to make room for text above bars
axes.set_ylim(top=max(frequencies) * 1.10)

# display frequency & percentage above each patch (bar)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(flips):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')

plt.show()  # display graph 
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
