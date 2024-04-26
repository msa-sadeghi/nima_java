from constants import *
from bullet import Bullet
import math
class Castle:
    def __init__(self):
        self.image_100 = pygame.transform.scale(castle_100_img, \
            (castle_100_img.get_width() * .3, castle_100_img.get_height() * .3))
        self.image_50 = pygame.transform.scale(castle_50_img, \
            (castle_50_img.get_width() * .3, castle_50_img.get_height() * .3))
        self.image_25 = pygame.transform.scale(castle_25_img, \
            (castle_25_img.get_width() * .3, castle_25_img.get_height() * .3))
        
        self.health = 1000
        self.max_health = 1000
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH - 400, SCREEN_HEIGHT-550))
        self.fired = False
        
    def draw(self, screen):
        if self.health <= 250:
            self.image = self.image_25
        elif self.health <= 500:
            self.image = self.image_50
        else:
            self.image = self.image_100
        screen.blit(self.image, self.rect)
        
    def fire(self, group):
        m_pos = pygame.mouse.get_pos()
        x_dis = m_pos[0] - self.rect.midleft[0]
        y_dis = -(m_pos[1] - self.rect.midleft[1])
        if pygame.mouse.get_pressed()[0] and not self.fired:
            self.fired = True
            Bullet(self.rect.midleft[0],
                   self.rect.midleft[1],
                   math.atan2(y_dis, x_dis),
                   group
                   )
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False
        