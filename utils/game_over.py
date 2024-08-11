import pygame
import sys
import time
import config

def show(surface, score, width, height):
    font = pygame.font.SysFont('times new roman', 90)
    text_surface = font.render('YOU DIED', True, config.COLOR_RED)
    text_rect = text_surface.get_rect(center=(width / 2, height / 4))

    surface.fill(config.COLOR_BLACK)
    surface.blit(text_surface, text_rect)

    from utils import score as score_utils
    score_utils.show(surface, score, 0, config.COLOR_RED, 'times', 20, width, height)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

