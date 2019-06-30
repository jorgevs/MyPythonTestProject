import win32com.client

# Github Repo
# https://github.com/mhammond/pywin32

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Magda, feed your husband!")
