# the Python 2 or 3 interpreter.
from sys import version_info
print version_info

py3 = version_info[0] > 2  # creates boolean value for test that Python major version > 2
print "Is this Python3? %s" % py3

print "Python version: %d.%d.%d" % (version_info[0], version_info[1], version_info[2])


