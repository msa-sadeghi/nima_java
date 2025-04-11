from pygame.sprite import Sprite
import pygame
import os

class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.actions = os.listdir("png")
        self.all_images = {}
        for action in self.actions:
            images = os.listdir(f"png/{action}")
            temp = []
            for image in images:
                img = pygame.image.load(f"png/{action}/{image}")
                img = pygame.transform.scale_by(img, 0.3)
                temp.append(img)

            self.all_images[action] = temp
        self.action = "Idle"
        self.frame_index = 0
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_update_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.animation()
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx += -5
        elif keys[pygame.K_RIGHT]:
            dx += 5
        self.rect.x += dx
        self.rect.y += dy

    def animation(self):
        self.image = self.all_images[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.last_update_time >= 100:
            self.frame_index += 1
            self.last_update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
      