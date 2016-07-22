print "================================================================"
for x in xrange(1, 4):
    print ('Hello, new Python user! '
           'This is time number %d') % x

print "================================================================"
elements = []
for x in range(1, 9):
    elements.append(x)   # It simply appends x to the end of the list

for x in elements:
    print x

print "================================================================"
for item in ['jorge', 'ivis', 'igue', 'eto']:
    print item

print "================================================================"
counter = 0
while counter < 10:
    print counter
    counter += 1

print "================================================================"
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for i in change:
    print "I got %r" % i

print "================================================================"

for number in [10, 20, 30, 40, 50, 60]:
    print(number)