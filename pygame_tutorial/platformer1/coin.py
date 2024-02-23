from pygame.sprite import Sprite
import pygame
class Coin(Sprite):
    def __init__(self,image, x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.direction = 1
        self.counter = 0
        
    def update(self):
        self.counter += 1
        self.rect.y +=  self.direction
        if self.counter > 32:
            self.counter *= -1
            self.direction *= -1
            