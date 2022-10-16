####

# sum of 3 dice rolls #

print('Rolling 3 dices...')

# rng dice rolls #
from random import randint
d1=randint(1,6)
d2=randint(1,6)
d3=randint(1,6)

# result #
print(f'You rolled: {d1},{d2},{d3}')
print('Sum of your rolls is:',d1+d2+d3)




 