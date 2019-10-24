import win32com.client

# Documentation:
# http://timgolden.me.uk/pywin32-docs/contents.html

# Github Repo
# https://github.com/mhammond/pywin32

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Firefox!  Firefox!  Firefox!")
#speaker.Speak("Gautam  Gautam  Gautam")
