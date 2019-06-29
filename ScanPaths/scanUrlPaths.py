from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

myFile = open("paths.list", 'rt')
for line in myFile:
    requestUrl = "http://10.0.0.243" + line
    print("Checking >> " + requestUrl)

    req = Request(requestUrl)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        str_data = response.read()
        print(str_data)

myFile.close()
