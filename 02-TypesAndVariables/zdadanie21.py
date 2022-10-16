####

# True/False dice roll #

# ? #
print('Rolling a dice...')

# dirce roll#
from random import randint
dice=randint(1,6)

# asking for number #
number=int(input('Choose a number from 1 to 6.\n'))

# true/false #

if number==dice:
    print('True')
if number!=dice:
    print('False')


