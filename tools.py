#modules
import pygame
from random import randint

def start_songs(music):
    music_background = pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

def songs_volume(sound):
    pygame.mixer.music.set_volume(sound)

#função de evolução da cobra
def snake_evolution( p, display ):
    for x in p:
        pygame.draw.rect(display, (0, 255, 0), (x[0], x[1], 20, 20))

def clear(props):
    del props




