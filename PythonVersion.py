# coding=utf-8
import sys

data = "oergpoaerǵoergaergerg"

if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    import base64
    print base64.b64encode(data).decode()
else:
    # Python 2 code in this block
    print data.encode("base64")
