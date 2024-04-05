import pygame
class MousePointer:
    def __init__(self):
        img = pygame.image.load("assets/crosshair.png")
        self.image = pygame.transform.scale(img,
        (img.get_width() * 0.06, img.get_height() * 0.06)
        )
        pygame.mouse.set_visible(False)
        
    def draw(self,screen):
        screen.blit(self.image, pygame.mouse.get_pos())