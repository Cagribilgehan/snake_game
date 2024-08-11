import pygame

def create_fullscreen(width, height):
    """
    Create a fullscreen game window.

    Parameters:
    - width: The width of the screen.
    - height: The height of the screen.

    Returns:
    - The created fullscreen game window.
    """
    return pygame.display.set_mode((width, height), pygame.FULLSCREEN)

