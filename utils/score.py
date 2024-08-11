import pygame

def show(surface, score, position, color, font_name, font_size, width, height):
    font = pygame.font.SysFont(font_name, font_size)
    text_surface = font.render(f'Score: {score}', True, color)
    text_rect = text_surface.get_rect()

    if position == 1:
        text_rect.midtop = (width / 10, 15)
    else:
        text_rect.midtop = (width / 2, height / 1.25)

    surface.blit(text_surface, text_rect)

