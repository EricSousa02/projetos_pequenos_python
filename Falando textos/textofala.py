# pip install gtts
from gtts import gTTS

texto = "Num ninho de mafagafos há sete mafagafinhos. Quando a mafagafa gafa, gafam os sete mafagafinhos"
lingua = "pt"

tts = gTTS(texto, lang=lingua)
tts.save("audio.mp3")

import os

os.system('ffplay -autoexit -nodisp audio.mp3')