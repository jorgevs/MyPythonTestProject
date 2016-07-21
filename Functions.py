# Functions =========================================================================


def addNumbers(a, b):
    sumNum = a + b
    return sumNum


def add_one(x):
    return x + 1


def sayHello():
    print ("hello world!")


def foo(a=1, b=2):
    sumNum = a + b
    return sumNum


def bar(*args):  # Receives parameters as a list
    print args


print foo()
print foo(3, 3)
print foo(b=3)
print bar(1, 2, 3, 4)
sayHello()
print(add_one(10))
print "addNumbers(10,20):", addNumbers(10, 20)
