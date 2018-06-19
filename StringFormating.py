import math

name = 'Monty'
print('Hello, %s' % name)  # string interpolation
print('Hello, {}'.format(name))  # string formatting

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
#=========================================================================================
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
#=========================================================================================
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
#=========================================================================================
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
#=========================================================================================
