# Install appkit llb - pip3 install -U PyObjC

from gtts import gTTS
from playsound import playsound
import os


# Language choice

language = int(input(
    'Choose your language:\nFor English choose 1 \nFor Polish choose 2 \nChoose now: '))
execute = 'Start'


# While loop covers:
# Provide name for the file and text to speach
# Modul gTTS, provide service Text to Speach
# Text to Speach conversion
# Save file to mp3 format
# Modul playsound play sound
# if else statement Checks for folder "mp3", if exist it moves file there, if not it's creates folder and puts file in this folder


while execute != 'Stop':
    if language == 1:
        name = input('Give a name for text: ')
        tekst = input(
            'Provide text for text to speach: ')
        Lang = 'en'
        texttospeach = gTTS(text=tekst, lang=Lang)
        texttospeach.save(name + '.mp3')
        playsound(name + '.mp3')
    else:
        name = input('Nadaj nazwe tekstu?: ')
        tekst = input(
            'Wpisz tekst, ktory program ma wypowiedziec: ')
        Lang = 'pl'
        texttospeach = gTTS(text=tekst, lang=Lang)
        texttospeach.save(name + '.mp3')
        playsound(name + '.mp3')
    saveFile = input(
        'Would you like save it as a mp3?\nCzy chcesz zapisac plik?\n(Yes or No): ')
    if saveFile == 'Yes':
        if os.path.isdir('./mp3') == True:
            os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
        else:
            os.mkdir('./mp3/')
            os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
    else:
        os.remove('./' + name + '.mp3')
    execute = input(
        'If you want to quit type in "Stop" if continue "Start": \nCzy chcesz zakonczyc program? Wpisz "Stop" by wyjsc, lub "Start" by kontynuowac: ')
print('You left program')


# If file exists ask for overwrite
# Done - Ask user if he wants to save result
# Done - Choose Language with '/n'. Implemented choice of english and Polish already.
# GUI
# Utilize time stamps
# Read out some poem
# Deploy as an App
# Done- While loop is done -Loop through a program
# Polish letter does not recognize when mp3 file is named with it
