from gtts import gTTS
from playsound import playsound
import  os

# Install appkit llb - pip3 install -U PyObjC


# Inputs from user

name = input('Nadaj nazwe tekstu? ')
tekst = input('Wpisz tekst, ktory program ma wypowiedziec: ')

#Text to Speach conversion

texttospeach = gTTS(text=tekst, lang='pl')

# Save as a mp3

texttospeach.save(name + '.mp3')
playsound(name+'.mp3')

# Adding to catalog mp3 ( Needs line for creating catalog)
os.rename('/Users/sebastianmarynicz/Python/New_classes/OpenAG_course/Pieguska/'+ name+'.mp3','/Users/sebastianmarynicz/Python/New_classes/OpenAG_course/Pieguska/mp3/'+ name + '.mp.3')


