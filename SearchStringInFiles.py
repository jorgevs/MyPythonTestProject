import glob
import os

sValue = 'written'
print("\nSearching for files with string: " + sValue)

# os.chdir("/home/jorgevs/PycharmProjects/MyPythonTestProject")
# for files in glob.glob("*.txt"):
#     f = open(files, 'r')
#     file_content = f.read()
#     if sValue in file_content:
#         print("xx" + f.name)
#     f.close()


os.chdir("/home/jorgevs/PycharmProjects/MyPythonTestProject")
for files in glob.glob("*.txt"):
    with open(files, 'r') as inF:
        for line in inF:
            # print(line)
            if sValue in line:
                print(">> " + inF.name)
    inF.close()
