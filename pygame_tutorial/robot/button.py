import pygame
class Button:
    def __init__(self, image, x,y, type):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.type = type
        self.is_clicked = False


    def update(self, screen):
        screen.blit(self.image, self.rect)
        clicked = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] and not self.is_clicked:
                clicked = True
                self.is_clicked = True
            if not pygame.mouse.get_pressed()[0]:
                self.is_clicked = False

        return clicked
