import random
from pygame.sprite import Sprite
import pygame
from constants import *
from enemy_bullet import EnemyBullet


class Enemy(Sprite):
    def __init__(self,x,y,bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/alien.png")
        self.image = pygame.transform.scale(self.image, (64,64))
        # first way
        self.enemy_hit_sound = pygame.mixer.Sound("assets/alien_hit.wav")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.bullet_group = bullet_group
        self.direction = 1
        self.speed = 2
        
    def update(self):
        self.rect.x += self.direction * self.speed
        if random.randint(1,1000) > 999 and len(self.bullet_group) < 3:################
            self.fire()

    def fire(self):################
        EnemyBullet(self.rect.centerx, self.rect.top, self.bullet_group)
