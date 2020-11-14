# Install appkit llb - pip3 install -U PyObjC

from gtts import gTTS
from playsound import playsound
import os


# Language choice

language = int(input(
    'Choose your language:\nFor English choose 1 \nFor Polish choose number 2 \nChoose now: '))
name = 'Start'


# While loop covers:
# Provide name for the file and text to speach
# Modul gTTS, provide service Text to Speach
# Text to Speach conversion
# Save file to mp3 format
# Modul playsound play sound
# if else statement Checks for folder "mp3", if exist it moves file there, if not it's creates folder and puts file in this folder


while name != 'Stop':
    if language == 1:
        name = input('Give a name for text (Type in a name "Stop" to close): ')
        tekst = input(
            'Provide text for text to speach: ')
        Lang = 'en'
        texttospeach = gTTS(text=tekst, lang=Lang)
        texttospeach.save(name + '.mp3')
        playsound(name + '.mp3')
        if os.path.isdir('./mp3') == True:
            os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
        else:
            os.mkdir('./mp3/')
            os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
    else:
        name = input('Nadaj nazwe tekstu? (Stop by zatrzymac program): ')
        tekst = input(
            'Wpisz tekst, ktory program ma wypowiedziec: ')
        Lang = 'pl'
        texttospeach = gTTS(text=tekst, lang=Lang)
        texttospeach.save(name + '.mp3')
        playsound(name + '.mp3')
        if os.path.isdir('./mp3') == True:
            os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
        else:
            os.mkdir('./mp3/')
            os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
print('You left program')


# If file exists ask for overwrite
# Ask user if he wants to save result
# Choose Language with '/n'. Implemented choice of english and Polish already.
# GUI
# Utilize time stamps
# Read out some poem
# Deploy as an App
# Loop through a program
# Polish letter does not recognize when mp3 file is named with it
