from urllib import request
from urllib import error

url = 'https://www.google.com'
req = request.Request(url)
try:
    response = request.urlopen(req)
except error.HTTPError as e:
    print("The server couldn't fulfill the request.")
    print("Error code: ", e.code)
except error.URLError as e:
    print("We failed to reach a server.")
    print("Reason: ", e.reason)

