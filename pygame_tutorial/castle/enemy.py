import pygame.time
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self, x, y, all_images, health,speed, group):
        Sprite.__init__(self)
        self.all_images = all_images
        self.image_number = 0
        self.action = 0
        self.image = self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = health
        self.speed = speed
        self.last_image_chng = pygame.time.get_ticks()
        self.last_injury_time = pygame.time.get_ticks()
        group.add(self)
    def update(self, castle):

        self.move(castle)
        self.next_costume()

    def move(self, castle):
        if self.rect.right >= castle.rect.left:
            self.change_action(1)
            
        if self.action == 0:
            self.rect.x += self.speed
        if self.action == 1:
            if pygame.time.get_ticks() - self.last_injury_time > 2500:
                self.last_injury_time = pygame.time.get_ticks()
                castle.health -= 10
    
            
    
    def change_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
    
    def next_costume(self):
        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_image_chng > 100:
            self.last_image_chng = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
