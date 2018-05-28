import glob
import os

sValue = 'smtp'
print("\nSearching for files with string: " + sValue)

# os.chdir("/home/jorgevs/PycharmProjects/MyPythonTestProject")
# for files in glob.glob("*.txt"):
#     f = open(files, 'r')
#     file_content = f.read()
#     if sValue in file_content:
#         print("xx" + f.name)
#     f.close()


os.chdir("/data/workspaces/workspace_Pycharm/MyPythonTestProject")
for files in glob.glob("*.py"):
    with open(files, 'r') as inF:
        for line in inF:
            # print(line)
            if sValue in line:
                print(">> " + inF.name)
                break
    inF.close()
