import pygame
class Button:
    def __init__(self,image, x,y, scale):
        image_width = image.get_width()
        image_height = image.get_height()
        
        self.image = pygame.transform.scale(image, (image_width * scale, image_height * scale))
        self.rect = self.image.get_rect(topleft=(x,y))
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def click(self):
        clickd_of_not = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                clickd_of_not = True
                
        return clickd_of_not
                