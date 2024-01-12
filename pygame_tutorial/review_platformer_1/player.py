from constants import *


class Player:
    def __init__(self, image,rect,x,y, type):
        self.image = image
        self.rect = rect
        self.rect.x = x
        self.rect.y = y
        self.type = type
    def draw(self):
        if self.type == 2:
            player1_rect = pygame.Rect(self.rect.x + 50, self.rect.y + 10, self.image.get_width()  -80, self.image.get_height()  -22)
        elif self.type == 1:
            player1_rect = self.rect
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (0,0,0), player1_rect,5)
