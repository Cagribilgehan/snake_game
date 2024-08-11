import pygame
import config

class SnakeEntity:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = pygame.K_RIGHT
        self.score = 0

    def change_direction(self, key):
        if key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
            self.direction = key

    def move(self):
        head = self.body[0][:]
        if self.direction == pygame.K_UP:
            head[1] -= 10
        elif self.direction == pygame.K_DOWN:
            head[1] += 10
        elif self.direction == pygame.K_LEFT:
            head[0] -= 10
        elif self.direction == pygame.K_RIGHT:
            head[0] += 10

        head[0] %= self.screen_width
        head[1] %= self.screen_height

        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.score += 1
        tail = self.body[-1][:]
        if self.direction == pygame.K_UP:
            tail[1] += 10
        elif self.direction == pygame.K_DOWN:
            tail[1] -= 10
        elif self.direction == pygame.K_LEFT:
            tail[0] += 10
        elif self.direction == pygame.K_RIGHT:
            tail[0] -= 10
        self.body.append(tail)

    def has_eaten(self, food_position):
        return self.body[0] == food_position

    def has_collided(self):
        return self.body[0] in self.body[1:]

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, config.COLOR_ORANGE, pygame.Rect(segment[0], segment[1], 10, 10))

