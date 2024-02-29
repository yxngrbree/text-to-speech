from gtts import gTTS
import pygame

text_input = input("Put ur message here Lnerd: ")
tts = gTTS(text=text_input, lang='en')
tts.save("output.mp3")

pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

