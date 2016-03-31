# Lists ==============================================================================
dynamic_languages = ['Python', 'Ruby', 'Groovy']
dynamic_languages.append('Lisp')

myList = ['Jorge', 'Silvia', 'Magda', 'Eto', 'Michael']
myList.insert(2, 'Didier')
myList[5] = 'Igue'
print(myList)
print("sort: ", myList.sort())
print('%s' % (myList[0]))
print('%s' % (myList[4]))
print('%s' % (myList[1:4]))
print("max: ", max(myList))
print("min: ", min(myList))

otraLista = [1, 2, 4, 5]
otraLista.append(6)
otraLista.append(7)
otraLista.remove(7)
otraLista.insert(2, 3)
otraLista.reverse()
print(otraLista)
print("len: ", len(otraLista))
print("max: ", max(otraLista))
print("min: ", min(otraLista))

print("Iterating through myList:")
for name in myList:
    print(">> " + name)

for number in [10, 20, 30, 40, 50, 60]:
    print(number)

for d in range(0, 10):
    print(d)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for a in range(0, 3):
    for b in range(0, 3):
        print(num_list[a], [b])

print("Is Jorge in myList?: ", ("Jorge" in myList))
print("Index of Silvia in myList: ", myList.index("Silvia"))
print("Index of Silvia in myList: %s" % myList.index("Silvia"))

listaDeListas = [myList, otraLista]
print(listaDeListas)
