from sys import argv
from os.path import split

script = argv[0]
scriptDirectory = split(script)[0]


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)   # Each time you do f.seek(0) you're moving to the start of the file


def print_a_line(f):
    print f.readline()



current_file = open(scriptDirectory + "/myTxtFile.txt")

print "First let's print the whole file:\n"
print_all(current_file)
print "Now let's rewind, kind of like a tape."
rewind(current_file)
print "Let's print the first line:"
print_a_line(current_file)