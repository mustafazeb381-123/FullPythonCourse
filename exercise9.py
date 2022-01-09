# #akhbar padh k sunnao\
def speak(str):#if you use the  def speak func so u can give tab after this line
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    speak.Speak("but i love umar ass he has big ass that i wannaa to fuck his ass")
if __name__ == '__main__':
    speak("soory about your girlfriend shaaam")