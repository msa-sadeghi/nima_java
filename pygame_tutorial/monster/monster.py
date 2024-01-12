from random import choice, randint
import pygame
from pygame.sprite import Sprite
from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Monster(Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.type = monster_type

        self.dx = choice([-1, 1])
        self.dy = choice([-1, 1])

        self.velocity = randint(1, 5)

    def update(self):
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity
        if self.rect.bottom >= WINDOW_HEIGHT-100 or self.rect.top <= 100:
            self.dy *= -1
        if self.rect.right >= WINDOW_WIDTH or self.rect.left <= 0:
            self.dx *= -1
