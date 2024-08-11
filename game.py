import pygame
import sys
import config
from snake import SnakeEntity
from food import FoodItem
from utils import game_over
from utils import score
from display.screen import create_fullscreen

class SnakeGame:
    def __init__(self):
        pygame.display.set_caption('Snake Game Reimagined')

        self.width = 1920  # Full HD width
        self.height = 1080  # Full HD height
        self.window = create_fullscreen(self.width, self.height)

        self.clock = pygame.time.Clock()
        self.snake = SnakeEntity(self.width, self.height)
        self.food = FoodItem(self.width, self.height)

        # Ses dosyalarını sırayla çalmak için liste
        self.eat_sounds = [
            pygame.mixer.Sound('audio/snake_music_collision1.wav'),
            pygame.mixer.Sound('audio/snake_music_collision2.wav'),
            pygame.mixer.Sound('audio/snake_music_collision3.wav')
        ]
        self.current_sound_index = 0  # İlk ses dosyasından başla

    def start(self):
        while True:
            self.handle_events()
            self.update_game()
            self.render_game()
            self.clock.tick(config.FRAME_RATE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)
                if event.key == pygame.K_ESCAPE:  # Kullanıcı ESC tuşuna basarsa oyunu kapat
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_x:  # Kullanıcı X tuşuna basarsa kapatmayı iptal et
                    print("X tuşuna basıldı, kapatma iptal edildi.")

    def update_game(self):
        self.snake.move()

        if self.snake.has_eaten(self.food.position):
            self.snake.grow()
            self.food.respawn()
            
            # Şu anki ses dosyasını çal
            self.eat_sounds[self.current_sound_index].play()
            
            # Bir sonraki ses dosyasına geç, eğer sona geldiyse başa dön
            self.current_sound_index = (self.current_sound_index + 1) % len(self.eat_sounds)

        if self.snake.has_collided():
            game_over.show(self.window, self.snake.score, self.width, self.height)

    def render_game(self):
        self.window.fill(config.COLOR_BLACK)
        self.food.draw(self.window)
        self.snake.draw(self.window)
        score.show(self.window, self.snake.score, 1, config.COLOR_WHITE, 'consolas', 20, self.width, self.height)
        pygame.display.update()

