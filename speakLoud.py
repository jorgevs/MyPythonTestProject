import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Magda, feed your husband!")
