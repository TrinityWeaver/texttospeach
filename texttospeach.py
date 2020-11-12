from gtts import gTTS
from playsound import playsound
import  os


# Install appkit llb - pip3 install -U PyObjC

name = input('Nadaj nazwe tekstu? ')
tekst = input('Wpisz tekst, ktory program ma wypowiedziec: ')
#pelnyTekst = name + ' ' + tekst


texttospeach = gTTS(text=tekst, lang='pl')


texttospeach.save(name + '.mp3')
playsound(name+'.mp3')
os.rename('/Users/sebastianmarynicz/Python/New_classes/OpenAG_course/Pieguska/'+ name+'.mp3','/Users/sebastianmarynicz/Python/New_classes/OpenAG_course/Pieguska/mp3/'+ name + '.mp.3')


