from gtts import gTTS
from playsound import playsound


name = input('Nadaj nazwe tekstu? ')
tekst = input('Wpisz tekst, ktory program ma wypowiedziec: ')
#pelnyTekst = name + ' ' + tekst


texttospeach = gTTS(text=tekst, lang='pl')


texttospeach.save(name + '.mp3')
playsound(name+'.mp3')
