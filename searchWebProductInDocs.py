import glob
import os

strData = '3a4f7b2a'
strSyndDocs = '3a4f7b29'

dataList = []
syndDocsList = []
bothList = []

#os.chdir("/data/endeca/teamsite_xmls/RES")
os.chdir("C://tempJVS//teamsite_xmls//RES")

for files in glob.glob("*.xml"):
    f = open(files, 'r')
    file_content = f.read()
    if strData in file_content:
        if strSyndDocs in file_content:
            bothList.append(f.name)
        else:
            dataList.append(f.name)
    elif strSyndDocs in file_content:
        syndDocsList.append(f.name)
    f.close()

print "IN BOTH =============================="
for item in bothList:
    print ">> " + item
print "ONLY DATA ============================"
for item in dataList:
    print ">> " + item
print "ONLY SYNDDOCS========================="
for item in syndDocsList:
    print ">> " + item


