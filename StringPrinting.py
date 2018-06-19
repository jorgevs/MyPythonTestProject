print("================================================================")
print('Hello world!')  # Python 2 syntax
# or
print('Hello world!')  # Python 3 syntax

print("================================================================")
hello = "hello world 123!"
print(hello)
variable = "Dereck"
print(variable)

print("================================================================")
x = 1
y = 2
print('x is equal to y: %s' % (x == y))
z = 1
print('x is equal to z: %s' % (x == z))

print("================================================================")
names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']
if names == words:
    print('Names list is equal to words')
else:
    print("Names list isn't equal to words")
new_names = ['Donald', 'Jake', 'Phil']
print('New names list is equal to names: %s' % (new_names == names))

print("================================================================")
cars = 30
trucks = 10
debt = 10.456
decimalValue = 10
print("there are", cars, "available.")
print("There are %d cars and %d trucks." % (cars, trucks))
x = "The number of trucks is: %d" % trucks
print(x)
print("The total debt is: %F" % debt)
print("The total debt is: %.2f" % debt)
print("The hexadecimal value is (lowercase): %x - (uppercase): %X" % (decimalValue, decimalValue))

print("================================================================")
# You should use %s and only use %r for getting debugging information about something.
# The %r will give you the "raw programmer's" version of variable, also known as the "representation."
formatter = "%r %r %r %r"
formatter2 = "%s %s %s %s"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

print(formatter2 % (1, 2, 3, 4))
print(formatter2 % ("one", "two", "three", "four"))
print(formatter2 % (True, False, False, True))
print(formatter2 % (formatter2, formatter2, formatter2, formatter2))
print(formatter2 % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

print("================================================================")
# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)

print("================================================================")
# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list.
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
print('-' * 10)

print("================================================================")
long_string = "This is a very loooooong string"
print(long_string[3])   # Prints the character in the 3rd position
print(long_string[0:8]) # Prints the characters from the 0 position to the 8th position
print(long_string[-5:])
print(long_string[:-5])
print(long_string[0:15] + "short string")

print("================================================================")
print("%c is my %s letter and my number %d number id %f.5f" % ('X', 'favorite', 1, .14))
print("%s %s %s" % ("xx", "sss", "xxx"))
print("\n" * 2)

print("================================================================")
hello = "hello world 123!"
print(hello[0].capitalize() + hello[1] + hello[2] + hello[3] + "!!!")
print(hello[0:4] + "!!!")

print("================================================================")
lowercase_string = "lower case string          "
print("Capitalize fist letter: " + lowercase_string.capitalize())
print("Find \'case\' position:", lowercase_string.find('case'))
print("lowercase_string is Alpha:", lowercase_string.isalpha())
print("lowercase_string is Alphanumeric:", lowercase_string.isalnum())
print("lowercase_string length:", len(lowercase_string))
print("lowercase_string replace:", lowercase_string.replace('lower', 'upper'))
print("lowercase_string strip:" + lowercase_string.strip() + " end")

quote_list = lowercase_string.strip().split(" ")
print("quote_list: %r" % quote_list)

print("================================================================")
hello2 = 'Hello world X!'
# Looping through a String
print("Looping through a String:")
for letter in hello2:
    print(letter)

print("================================================================")
# Placeholders in Strings
print("%s Vazquez" % "Jorge")
print("My name is %s and I'm %d years old" % ("Jorge", 37))

print("================================================================")
# Strings can be concatenated (glued together) with the + operator, and repeated with *
print("Jorge " * 3)

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

# Two or more string literals next to each other are automatically concatenated.
print('Py' 'thon')

# This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# Strings can be indexed (subscripted), with the first character having index 0.
# There is no separate character type; a character is simply a string of size one:
word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5

