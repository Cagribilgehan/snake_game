import pygame
import sys
from game import SnakeGame
from audio.music import play_background_music

def main():
    pygame.init()
    play_background_music()
    game = SnakeGame()
    game.start()

if __name__ == "__main__":
    main()

ls