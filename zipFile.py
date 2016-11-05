import zipfile
import glob
import os

# open the zip file for writing, and write stuff to it
myFile = zipfile.ZipFile("test.zip", "w")

for name in glob.glob('*.txt'):
    myFile.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)

myFile.close()

# open the file again, to see what's in it

myFile = zipfile.ZipFile("test.zip", "r")
for info in myFile.infolist():
    print info.filename, info.date_time, info.file_size, info.compress_size
