import random
import pygame
import config

class FoodItem:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, (self.screen_width // 10) - 1) * 10
        y = random.randint(0, (self.screen_height // 10) - 1) * 10
        return [x, y]

    def respawn(self):
        self.position = self.generate_position()

    def draw(self, surface):
        pygame.draw.rect(surface, config.COLOR_WHITE, pygame.Rect(self.position[0], self.position[1], 10, 10))

