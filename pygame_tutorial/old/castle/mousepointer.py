import pygame


class MousePointer:
    def __init__(self):
        img = pygame.image.load("assets/crosshair.png")
        self.image = pygame.transform.scale(img,
                                            (img.get_width() * 0.06, img.get_height() * 0.06)
                                            )
        pygame.mouse.set_visible(False)

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if pos[1] > 70:
            pygame.mouse.set_visible(False)
            screen.blit(self.image, pos)
        else:
            pygame.mouse.set_visible(True)
