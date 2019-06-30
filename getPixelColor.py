import win32.win32api as api

while True:
    x, y = api.GetCursorPos()
    print("Mouse position: x: %d y: %d" % (x, y))

