# Install appkit llb - pip3 install -U PyObjC

from gtts import gTTS
from playsound import playsound
import os


# Provide name for the file and text to speach

# Install appkit llb - pip3 install -U PyObjC



# Inputs from user

name = input('Nadaj nazwe tekstu? ')
tekst = input('Wpisz tekst, ktory program ma wypowiedziec: ')


# Modul gTTS, provide service Text to Speach
# save file in mp3 format



#Text to Speach conversion

texttospeach = gTTS(text=tekst, lang='pl')
texttospeach.save(name + '.mp3')


# Modul playsound play sound

# Save as a mp3


playsound(name+'.mp3')



# Adding to catalog mp3 ( Needs line for creating catalog)
os.rename('/Users/sebastianmarynicz/Python/New_classes/OpenAG_course/Pieguska/'+ name+'.mp3','/Users/sebastianmarynicz/Python/New_classes/OpenAG_course/Pieguska/mp3/'+ name + '.mp.3')


# if else statement Checks for folder "mp3", if exist it moves file there, if not it's creates folder and puts file in this folder

if os.path.isdir(
        './mp3') == True:
    os.rename('./' + name+'.mp3',
              './mp3/' + name + '.mp.3')
else:
    os.mkdir('./mp3/')
    os.rename('./' + name+'.mp3',
              './mp3/' + name + '.mp.3')
