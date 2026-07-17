from constants import pygame,SCREEN_WIDTH, SCREEN_HEIGHT
class World:
    def __init__(self, bg_image):
        self.bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        
    def draw(self, screen):
        screen.blit(self.bg_image, (0,0))
        
        
        
    