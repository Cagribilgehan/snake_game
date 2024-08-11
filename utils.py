import pygame

def show(game_window, score, choice, color, font, size, screen_width, screen_height):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (screen_width / 10, 15)
    else:
        score_rect.midtop = (screen_width / 2, screen_height / 1.25)
    game_window.blit(score_surface, score_rect)

