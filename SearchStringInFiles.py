import glob
import os

sValue = 'requests'
print("\nSearching for files with string: " + sValue)

# os.chdir("/home/jorgevs/PycharmProjects/MyPythonTestProject")
# for files in glob.glob("*.txt"):
#     f = open(files, 'r')
#     file_content = f.read()
#     if sValue in file_content:
#         print("xx" + f.name)
#     f.close()


os.chdir("C:\\workspaces\\workspace_PyCharm\\MyPythonTestProject")
for files in glob.glob("*.py"):
    with open(files, 'r') as inF:
        for line in inF:
            # print(line)
            if sValue in line:
                print(">> " + inF.name)
                break
    inF.close()
