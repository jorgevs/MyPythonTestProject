import re

url1 = "https://d2q77462htbdyg.cloudfront.net/visualisation-5535931/index.html"
url2 = "https://d2q77462htbdyg.cloudfront.net/visualisation-5535931/"
url3 = "https://d2q77462htbdyg.cloudfront.net/visualisation-5535931"

urls = [url1, url2, url3]

for url in urls:
    pattern1 = re.compile(".html" + "$")
    pattern2 = re.compile("/" + "$")

    if pattern1.search(url) is None:
        if pattern2.search(url) is not None:
            url = url + 'index.html'
        else:
            url = url + '/index.html'

    print(url)
