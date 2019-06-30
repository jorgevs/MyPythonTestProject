import win32.win32api as api

# Documentation:
# http://timgolden.me.uk/pywin32-docs/win32api.html
# http://timgolden.me.uk/pywin32-docs/contents.html

# Github Repo
# https://github.com/mhammond/pywin32

while True:
    x, y = api.GetCursorPos()
    print("Mouse position: x: %d y: %d" % (x, y))

