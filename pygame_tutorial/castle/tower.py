from pygame.sprite import Sprite
from constants import tower_100_img, tower_50_img, tower_25_img
import pygame
class Tower(Sprite):
    def __init__(self, x,y, health, group):
        super().__init__()
        t_img_100 = pygame.transform.scale(tower_100_img, (80,100))
        t_img_50 = pygame.transform.scale(tower_50_img, (80,100))
        t_img_25 = pygame.transform.scale(tower_25_img, (80,100))
        self.images = [
            t_img_100,
            t_img_50,
            t_img_25
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center= (x,y))
        
        self.health = health
        group.add(self)
        
    def update(self):
        pass