# import speech_recognition as sr
# import webbrowser
# r = sr.Recognizer()

# with sr.Microphone() as source: 

#     while True:
#         audio = r.listen(source)

#         result = r.recognize_google(audio)
#         print("You said " + result)
#         words = result.lower()
#         if words=="facebook":
#             webbrowser.open('https://www.facebook.com')
#         if words=="google":
#             webbrowser.open('https://www.google.co.uk')
#         if words=="stop":
#             break

#    

import speech_recognition as sr
def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)  