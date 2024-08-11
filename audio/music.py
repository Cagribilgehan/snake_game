import pygame

def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('snake_music.wav')
    pygame.mixer.music.play(-1)

