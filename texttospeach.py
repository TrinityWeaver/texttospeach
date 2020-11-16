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
        if os.path.exists('./mp3/' + name + '.mp3') == True:
            overWrite = input(
                'This file name exist, would you like to overwrite?\nY or N?: ')
            if overWrite == 'N':
                continue
        tekst = input(
            'Provide text for text to speach: ')
        Lang = 'en'
        texttospeach = gTTS(text=tekst, lang=Lang)
        texttospeach.save(name + '.mp3')
        playsound(name + '.mp3')
        saveFile = input('Would you like save it as a mp3?\n(Y or N): ')
        if saveFile == 'Y':
            if os.path.isdir('./mp3') == True:
                os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
            else:
                os.mkdir('./mp3/')
                os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
        else:
            os.remove('./' + name + '.mp3')
        execute = input(
            'If you want to quit\nType in "Stop" if continue "Start": ')
        if execute == 'Stop':
            print('You left program')
    else:
        name = input('Nadaj nazwe tekstu?: ')
        if os.path.exists('./mp3/' + name + '.mp3') == True:
            overWrite = input(
                'Taki plik juz istnieje, czy chcesz nadpisac?\nT or N?: ')
            if overWrite == 'N':
                continue
        tekst = input(
            'Wpisz tekst, ktory program ma wypowiedziec: ')
        Lang = 'pl'
        texttospeach = gTTS(text=tekst, lang=Lang)
        texttospeach.save(name + '.mp3')
        playsound(name + '.mp3')
        saveFile = input('Czy chcesz zapisac plik?\n(T or N): ')
        if saveFile == 'T':
            if os.path.isdir('./mp3') == True:
                os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
            else:
                os.mkdir('./mp3/')
                os.rename('./' + name+'.mp3', './mp3/' + name + '.mp3')
        else:
            os.remove('./' + name + '.mp3')
        execute = input(
            'Czy chcesz zakonczyc program?\nWpisz "Stop" by zakonczyc, jesli kontynuowac wpisz "Start": ')
        if execute == 'Stop':
            print('Opusciles Program')


# GUI
# Utilize time stamps
# Read out some poem - This might require to build web scrapper
# Deploy as an App
# Polish letter does not recognize when mp3 file is named with it
