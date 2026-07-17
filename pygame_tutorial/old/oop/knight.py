import pygame.image
from pygame.sprite import Sprite
class Knight(Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load("knight.png")
        self.image = pygame.transform.scale(image, (65,64))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > WIN:
            self.rect.y -= self.velocity