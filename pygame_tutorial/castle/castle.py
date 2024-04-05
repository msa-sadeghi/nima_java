from constants import *
from bullet import Bullet
import math
class Castle:
    def __init__(self):
        self.image = pygame.transform.scale(castle_100_img, \
            (castle_100_img.get_width() * .3, castle_100_img.get_height() * .3))
        
        self.health = 1000
        self.max_health = 1000
        self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH - 400, SCREEN_HEIGHT-550))
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def fire(self, group):
        m_pos = pygame.mouse.get_pos()
        x_dis = m_pos[0] - self.rect.midleft[0]
        y_dis = -(m_pos[1] - self.rect.midleft[1])
        if pygame.mouse.get_pressed()[0]:
            Bullet(self.rect.midleft[0],
                   self.rect.midleft[1],
                   math.atan2(y_dis, x_dis),
                   group
                   )
        