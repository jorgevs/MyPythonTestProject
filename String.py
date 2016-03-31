# Strings ===========================================================================
hello = "hello world 123!"

long_string = "This is a very loooooong string"
print(long_string[0:8])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[0:15] + "short string")

print("%c is my %s letter and my number %d number id %f.5f" % ('X', 'favorite', 1, .14))

print("%s %s %s" % ("xx", "sss", "xxx"))
print("\n" * 2)
print(hello[0].capitalize() + hello[1] + hello[2] + hello[3] + "!!!")
print(hello[0:4] + "!!!")

lowercase_string = "lower case string          "
print("Capitalize fist letter: " + lowercase_string.capitalize())
print("Find \'case\' position:", lowercase_string.find('case'))
print("lowercase_string is Alpha:", lowercase_string.isalpha())
print("lowercase_string is Alphanumeric:", lowercase_string.isalnum())
print("lowercase_string length:", len(lowercase_string))
print("lowercase_string replace:", lowercase_string.replace('lower', 'upper'))
print("lowercase_string strip:" + lowercase_string.strip() + " end")
quote_list = lowercase_string.strip().split(" ")
print(quote_list)

# Looping through a String
print("Looping through a String:")
for letter in hello:
    print(letter)
