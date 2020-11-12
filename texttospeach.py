from gtts import gTTS
from playsound import playsound


name = input('Jak masz na imie? ')
lname = input('Jak masz na nazwisko: ')
pelnyTekst = name + ' ' + lname
print(pelnyTekst)


texttospeach = gTTS(text=pelnyTekst, lang='pl')

pelnyTekst = name

texttospeach.save(name + '.mp3')
playsound(name+'.mp3')
