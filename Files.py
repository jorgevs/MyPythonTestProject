import os

#===========================================================================
# Writting a line in a file
myFile = open("myTxtFile.txt", 'wt')
myFile.write("This is the content of my test file\n")
myFile.close()

#===========================================================================
f = open("myTxtFile.txt", 'r')
print f

#===========================================================================
# Writting a line in a file
myFile = open("test.txt", 'wb')   #use 'ab+' to read & append to file (It also opens or creates the file)
print("mode: " + myFile.mode)
print("fileName: " + myFile.name)
myFile.write(bytes("I have written to myFile\n"))
myFile.close()

#===========================================================================
# Appending a line in a file
myFile = open("myTxtFile.txt", 'at')
myFile.write("I have written to myFile")
myFile.close()

#===========================================================================
# Reading a file
myFile = open("test.txt", 'r+')
text_in_file = myFile.read()
print("Content of test.txt:" + text_in_file)
myFile.close()

#===========================================================================
# Deleting a file
os.remove("test.txt")

#===========================================================================
# Using a for loop to read all lines in a file
myFile = open("myTxtFile.txt", 'rt')
for line in myFile:
    print(">> " + line)
myFile.close()

myFile = open("myTxtFile.txt", 'rt')
content = myFile.read()
print("FILE: " + content)
myFile.close()
#===========================================================================
