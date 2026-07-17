from constants import *
class Button:
    def __init__(self, image, x,y):
        self.image= image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self):
        SCREEN.blit(self.image, self.rect)