import urllib.request as url
import xml.etree.ElementTree as et

def addupnumbers(A):
    result = 0
    for number in A:
        result = result + number
    return result


web_data = url.urlopen("https://www.w3schools.com/xml/cd_catalog.xml")
str_data = web_data.read()
#print(str_data)

xml_data = et.fromstring(str_data)
cd_list = xml_data.findall("CD")
cd_prices = []

for x in cd_list:
    #print(x.find("TITLE").text)
    f = float(x.find("PRICE").text)
    cd_prices.append(f)

print("Sum of prices: %f", addupnumbers(cd_prices))
