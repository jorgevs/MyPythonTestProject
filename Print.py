print 'Hello world!'  # Python 2 syntax
# or
print('Hello world!')  # Python 3 syntax

hello = "hello world 123!"
print(hello)
variable = "Dereck"
print(variable)

x = 1
y = 2
print 'x is equal to y: %s' % (x == y)
z = 1
print 'x is equal to z: %s' % (x == z)
names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']
if names == words:
    print 'Names list is equal to words'
else:
    print "Names list isn't equal to words"
new_names = ['Donald', 'Jake', 'Phil']
print 'New names list is equal to names: %s' % (new_names == names)

cars = 30
trucks = 10
debt = 10.456
decimalValue=10
print "there are", cars, "available."
print "There are %d cars and %d trucks." % (cars, trucks)
x = "The number of trucks is: %d" % trucks
print x
print "The total debt is: %F" % debt
print "The total debt is: %.2f" % debt
print "The hexadecimal value is (lowercase): %x - (uppercase): %X" % (decimalValue, decimalValue)

# You should use %s and only use %r for getting debugging information about something.
# The %r will give you the "raw programmer's" version of variable, also known as the "representation."
formatter = "%r %r %r %r"
formatter2 = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print formatter2 % (1, 2, 3, 4)
print formatter2 % ("one", "two", "three", "four")
print formatter2 % (True, False, False, True)
print formatter2 % (formatter2, formatter2, formatter2, formatter2)
print formatter2 % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print "A list: %s" % mylist