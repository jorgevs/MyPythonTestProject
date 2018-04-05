from sys import argv

try:
    script, first, second, third = argv
except ValueError:
    script = "scriptName"
    first = "variableA"
    second = "variableB"
    third =  "variableC"

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third