import os
from gtts import gTTS
Text = "Be active! Take on responsibility! Work for the things you believe in. If you do not, you are surrendering your fate to others."
print("processing please wait….")
learn = gTTS(text = Text, lang = "en-us")
learn.save ("voice.mp3")
os.system("start voice.mp3")
