from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.all_images = {}
        idle_images = []
        run_images = []
        images_names = os.listdir("./images")
        for im in images_names:
            if im.find("Idle")!=-1:
                img = pygame.image.load(f"./images/{im}")
                img = pygame.transform.scale_by(img, 0.5)
                idle_images.append(img)
            elif im.find("Run")!=-1:
                img = pygame.image.load(f"./images/{im}")
                img = pygame.transform.scale_by(img, 0.5)
                run_images.append(img)
        self.all_images["Idle"] = idle_images
        self.all_images["run"] = run_images

        self.frame_index = 0
        self.image = self.all_images['Idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_image_time = pygame.time.get_ticks()
        self.action = "Idle"
    def draw(self, screen):
        img = self.all_images[self.action][self.frame_index]
        screen.blit(img, self.rect)
        self.animation()


    def animation(self):
        if pygame.time.get_ticks() - self.last_image_time >= 100:
            self.last_image_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5

        self.rect.x += dx
        self.rect.y += dy





