print ("================================================================")
for x in range(1, 4):
    print ('Hello, new Python user! '
           'This is time number %d' % x)

for i in range(0, 10):
    print(i)

print ("================================================================")
elements = []
for x in range(1, 9):
    elements.append(x)   # It simply appends x to the end of the list
for x in elements:
    print (x)

print ("================================================================")
elements = []
for x in range(0, 100, 20):
    elements.append(x)   # It simply appends x to the end of the list
for x in elements:
    print (x)

print ("================================================================")
for item in ['jorge', 'ivis', 'igue', 'eto']:
    print (item)

print ("================================================================")
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for i in change:
    print ("I got %r" % i)

print ("================================================================")
num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for x in range(0, 3):
    for y in range(0, 3):
        print (num_list[x][y])

print ("================================================================")
for number in [10, 20, 30, 40, 50, 60]:
    print(number)

print ("================================================================")
counter = 0
while counter < 10:
    print (counter)
    counter += 1

print ("================================================================")
i = 0
while i < 20:
    if(i % 2 == 0):
        print (i)
    if(i == 9):
        break
    if (i == 5):
        pass     # Does nothing
        print("Counter == 5")
    else:
        i += 1
        continue
    i += 1

