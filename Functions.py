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


# *args tells Python to take all the arguments to the function and then put them in args as a list.
def bar(*args):
    print(args)
    print("The second value is: %d" % args[1])
    return args[0]


# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter.
def bar2(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))
    if options.get("number") == "first":
        return first


print("addNumbers(10,20):", addNumbers(10, 20))
print(add_one(10))
sayHello()

print(foo())
print(foo(3, 3))
print(foo(3+3, 1-1))
value=6
print(foo(value, 3))
print(foo(b=3))

print(bar(1, 2, 3, 4))
print(bar(1*1, 2+3, 3, 4+4))

result = bar2(1, 2, 3, action="sum", number="first")
print("Result is: %d" % result)

# ===========================================================================================================
print("===========================================================================================================")
# ===========================================================================================================

import Functions2

sentence = "All good things come to those who wait."
words = Functions2.break_words(sentence)
print(words)
sorted_words = Functions2.sort_words(words)
print(sorted_words)
Functions2.print_first_word(words)
Functions2.print_last_word(words)
print(words)
Functions2.print_first_word(sorted_words)
Functions2.print_last_word(sorted_words)
print(sorted_words)
sorted_words = Functions2.sort_sentence(sentence)
print(sorted_words)
Functions2.print_first_and_last(sentence)
Functions2.print_first_and_last_sorted(sentence)
