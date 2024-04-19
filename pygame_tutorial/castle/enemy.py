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
        group.add(self)
    def update(self):

        self.move()
        self.animation()

    def move(self):
        self.rect.x += self.speed
    def animation(self):
        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_image_chng > 100:
            self.last_image_chng = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
