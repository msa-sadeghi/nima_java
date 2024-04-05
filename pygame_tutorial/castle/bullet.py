from pygame.sprite import Sprite
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        group.add(self)
        
        
    def update(self):
        self.rect.x += math.cos(self.direction) * 10
        self.rect.y += -math.sin(self.direction) * 10
        
        