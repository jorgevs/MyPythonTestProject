import urllib.request as url

# urllib.request
web_data = url.urlopen("http://www.tecnohobby.net")
print(web_data.read())
# Stores the extracted data from the web into a "urllib.text.html" file
data = url.urlretrieve("http://www.tecnohobby.net", "urllib.text.html")

# SMTPlib


# abs
print(abs(-32))

# bool
print(bool(1))
print(bool(0))
print(bool(10))
print(bool(None))

# dir
print(dir(1))
print(dir("Hello"))

# help
sent = "hello"
help(sent.upper)
help(sent.splitlines)


# eval and exec
sent = 'print("Hi")'
eval(sent)
exec(sent)

# functions for parsing
a = 1
print(str(a))
print(float(a))
print(int(a))

