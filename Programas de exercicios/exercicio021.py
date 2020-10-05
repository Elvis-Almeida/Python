#criar um leitor de audio
from pygame import mixer
mixer.init()
mixer.music.load('audio.mp3')
input('Press for play')
mixer.music.play()
input('press for stop')

