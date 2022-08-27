#modules
import pygame
from random import randint
# musica de fundo
# definição de musica de fundo
default = 'settings/music/default.mp3'

#default volume
sound = 0.50

def songs(sound=sound, music=default):
    pygame.mixer.music.set_volume(sound)
    music_background = pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

#função de evolução da cobra
def snake_evolution( p, display ):
    for x in p:
        pygame.draw.rect(display, (0, 255, 0), (x[0], x[1], 20, 20))

def clear(props):
    del props



