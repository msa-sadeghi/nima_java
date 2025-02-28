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
    def draw(self, screen):
        screen.blit(self.image, self.rect)




