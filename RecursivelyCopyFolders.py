import shutil

#This script reads
# 1- Read a list of directory names from directoryNames.txt
# 2- For each item(x) in that list, move from src (C:/dir1/) to dest (C:/dir1/dir2/)

src = "C:/dir1/"
dest = "C:/dir1/dir2/"

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


# Using a for loop to read all lines in a file
myFile = open("directoryNames.txt", 'rt')
for line in myFile:
    print(">> " + line)
    # Remove the \n character (newline) from the string right side
    if line.find("\n") != -1:
        line = line.rstrip("\n")
    copyDirectory(src + line, dest + line)
myFile.close()

