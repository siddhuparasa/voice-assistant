import speech_recognition as s
import webbrowser

# Create a Recognizer instance
r = s.Recognizer()
r.energy_threshold = 5000


print(" ")
print(" ")
print("WELCOME TO SIDDHU'S VOICE ASSISTANT")
print("DO YOU WANT TO SEARCH")
print("yes: Y")
print("no: N")

# Get user input
n = input()

if n == 'Y':
    # Using the Microphone
    with s.Microphone(device_index=1) as source:
        print("Speak now!!....listening....")
        audio = r.listen(source)
        try:
            # Recognize speech using Google Web Speech API
            text = r.recognize_google(audio)
            print("You searched for: {}".format(text))
            url = 'https://www.google.co.in/search?q='
            search_url = url + text
            webbrowser.open(search_url)
        
       
        except s.UnknownValueError:
            print("Could not understand the audio")
else:
    print("THANK YOU!!!")
