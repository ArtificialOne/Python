import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "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"
lang = 'en'
openai.api_key = api_key
guy = ""

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source: #May need to modify to determine microphone
            audio = r.listen(source) #Listen to what is playing in
            said = ""

            try:
                said = r.recognize_google(audio) #Pass in audio to google text to speech
                print(said) #Ensures text is processed
                global guy
                guy = said

                if "Unique" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")
                    playsound.playsound("welcome1.mp3")

            except Exception:
                print("Exception")

        return said

    if "stop" in guy:
        break

get_audio()