# We put a , (comma) at the end of each print line.
# This is so print doesn't end the line with a newline character and go to the next line.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)



# How do I get a number from someone so I can do math?
print "Give me a number?",
x = int(raw_input())
print x + 10

# You can also put in a prompt to show to a person so he knows what to type.
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)