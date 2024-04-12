from pygame.sprite import Sprite
import pygame
import math


class Bullet(Sprite):
    def __init__(self, x, y, direction, group):
        super().__init__()
        image = pygame.image.load("assets/bullet.png")
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image, (w * 0.2, h * 0.2))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction
        group.add(self)

    def update(self):
        self.rect.x += math.cos(self.direction) * 10
        self.rect.y += -math.sin(self.direction) * 10
