from sys import exit

# Getting input from the user =========================================================================
response = raw_input("Please enter your name: ")
print'Hello ' + response
if 'Jorge' in response or 'Luis' in response:
    print "Wonderful name! =)   You win!"
    exit(0)
# =====================================================================================================

response = raw_input("male of female?")
while response != "male":
    response = raw_input("male of female?")
print("Great answer!!!")

# =====================================================================================================

# Here is an example Python command line script that demonstrates how to obtain data from the user with
# the Python 2 or 3 interpreter.
from sys import version_info

py3 = version_info[0] > 2  # creates boolean value for test that Python major version > 2

