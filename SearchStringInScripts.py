import glob
import os
from sys import argv

script = argv[0]

scriptDirectory = os.path.split(script)[0]
scriptName = os.path.split(script)[1]

print "The script location is: " + scriptDirectory


stringToSearch = '[:]'
print("\nSearching for files with string: " + stringToSearch)

os.chdir(scriptDirectory)
for fileName in glob.glob("*.py"):
    file = open(fileName, 'r')
    file_content = file.read()
    if stringToSearch in file_content:
        print(">> " + file.name)
    file.close()

# os.chdir(scriptDirectory)
# for file in glob.glob("*.py"):
#     with open(file, 'r') as inF:
#         for line in inF:
#             # print(line)
#             if stringToSearch in line:
#                 print(">> " + inF.name)
#     inF.close()
