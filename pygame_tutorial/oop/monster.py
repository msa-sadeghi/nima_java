import pygame
from pygame.sprite import Sprite
from random import randint


class Monster(Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load("monster.png")
        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = randint(1, 10)


    def update(self):
        self.rect.y += self.velocity
