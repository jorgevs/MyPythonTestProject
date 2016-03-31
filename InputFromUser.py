# Getting input from the user =======================================================
person = raw_input('Enter your name: ')
print('Hello', person)
# =====================================================================================================

response = raw_input("male of female?")
while response != "male":
    response = raw_input("male of female?")
print(
"Great answer!!!")  # =====================================================================================================
# Here is an example Python command line script that demonstrates how to obtain data from the user with
# the Python 2 or 3 interpreter.
from sys import version_info

py3 = version_info[0] > 2  # creates boolean value for test that Python major version > 2

if py3:
    response = input("Please enter your name: ")
else:
    response = raw_input("Please enter your name: ")
