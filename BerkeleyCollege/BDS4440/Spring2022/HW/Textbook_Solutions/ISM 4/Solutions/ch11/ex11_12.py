# Exercise 11.12
def solve_towers(disks, source_peg, destination_peg, temp_peg):
    """recursively move disks between towers"""
    # base case -- only one disk to move
    if disks == 1:
        print(f'\n{source_peg} --> {destination_peg}', end='')         
        return

    # recursion step -- move (disk - 1) disks from source_peg
    # to temp_peg using destination_peg
    solve_towers(disks - 1, source_peg, temp_peg, destination_peg)

    # move last disk from source_peg to destination_peg
    print(f'\n{source_peg} --> {destination_peg}', end='')

    # move (disks - 1) disks from temp_peg to destination_peg
    solve_towers(disks - 1, temp_peg, destination_peg, source_peg)

    
start_peg = 1  # value 1 used to indicate start_peg in output
end_peg = 3  # value 3 used to indicate end_peg in output
temp_peg = 2  # value 2 used to indicate temp_peg in output
total_disks = 3  # number of disks

# initial nonrecursive call: move all disks
solve_towers(total_disks, start_peg, end_peg, temp_peg)

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
