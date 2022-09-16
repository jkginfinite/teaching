# Exercise 6.8
# ex06_08.py
number_to_word = {
    0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 
    5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE',
    10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 
    14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 
    18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 30: 'THIRTY', 
    40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY', 
    80: 'EIGHTY', 90: 'NINETY'
}

amount = input('Enter a dollar amount less than 1000.00: ')
dollars, cents = amount.split('.')
dollars = int(dollars)
cents = int(cents)
amount_in_words = []

if dollars == 0:
    amount_in_words.append(number_to_word[dollars])
elif dollars >= 100:
    amount_in_words.append(number_to_word[dollars // 100] + ' HUNDRED')

dollars %= 100 

if dollars in range(10, 20):
    amount_in_words.append(number_to_word[dollars])
elif dollars in range(20, 100):
    amount_in_words.append(number_to_word[dollars // 10 * 10])
    dollars %= 10 

if dollars in range(1, 10):
    amount_in_words.append(number_to_word[dollars])

print(f'{" ".join(amount_in_words)} AND {cents}/100')

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
