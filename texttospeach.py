# Install appkit llb - pip3 install -U PyObjC

from gtts import gTTS
from playsound import playsound
import os

# Provide name for the file and text to speach

name = input('Nadaj nazwe tekstu? ')
tekst = input('Wpisz tekst, ktory program ma wypowiedziec: ')

# Modul gTTS, provide service Text to Speach
# save file in mp3 format


texttospeach = gTTS(text=tekst, lang='pl')
texttospeach.save(name + '.mp3')

# Modul playsound play sound

playsound(name+'.mp3')

# if else statement Checks for folder "mp3", if exist it moves file there, if not it's creates folder and puts file in this folder

if os.path.isdir(
        './mp3') == True:
    os.rename('./' + name+'.mp3',
              './mp3/' + name + '.mp.3')
else:
    os.mkdir('./mp3/')
    os.rename('./' + name+'.mp3',
              './mp3/' + name + '.mp.3')
