# Lists ==============================================================================
print ("================================================================================")

dynamic_languages = ['Python', 'Ruby', 'Groovy']
dynamic_languages.append('Lisp')
print ("dynamic_languages is: %r" % dynamic_languages)

print ("================================================================================")

myList = ['Jorge', 'Silvia', 'Magda', 'Eto', 'Michael']
myList.insert(2, 'Didier')
myList[5] = 'Igue'
print ("myList is: %r" % myList)
print ("myList sorted: %r" % sorted(myList))

print ('myList[0]: %s' % myList[0])
print ('myList[4]: %s' % myList[4])
print ('myList[1:4]: %s' % myList[1:4])
print ("max: %s" % max(myList))
print ("min: %s" % min(myList))
print ("Is Jorge in myList?: %s" % ("Jorge" in myList))
print ("Index of Silvia in myList: %d" % myList.index("Silvia"))

print ("================================================================================")
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print ("Iterating through animals:")
for name in animals:
    print (">> " + name)

print ("================================================================================")

otraLista = [1, 2, 4, 5, 9]
otraLista.append(6)
otraLista.append(7)
otraLista.remove(7)
otraLista.insert(2, 3)
otraLista.reverse()
print ("otraLista is: %r" % otraLista)
print("len: ", len(otraLista))
print("max: ", max(otraLista))
print("min: ", min(otraLista))

print ("================================================================================")

for number in [10, 20, 30, 40, 50, 60]:
    print(number)

for d in range(0, 10):
    print(d)

print ("================================================================================")

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for a in range(0, 3):
    for b in range(0, 3):
        print(num_list[a], [b])

print ("================================================================================")

listaDeListas = [myList, otraLista]
print ("listaDeListas es: %r" % listaDeListas)

print ("================================================================================")
# A Python way of copying a list. You use the list slice syntax [:] to
# effectively make a slice from the very first element to the very last one.
newList = myList[:]
print (newList)
