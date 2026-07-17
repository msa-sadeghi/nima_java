# https://www.iconarchive.com/
# https://www.fontspace.com/
import pygame
# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH,
                                           WINDOW_HEIGHT))
pygame.display.set_caption("First Game")

# Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

display_surface.fill(BLUE)
# Draw various shapes on our display
pygame.draw.line(display_surface,
                 RED, (0, 0),
                 (100, 100), 5)
pygame.draw.line(display_surface,
                 GREEN, (100, 100),
                 (200, 300), 5)
pygame.draw.circle(display_surface, WHITE,
                   (WINDOW_WIDTH//2,
                    WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW,
                   (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 6)
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))
# The main game loop
running = True
while running:
    # Loop through a list of event objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    # Update the display
    pygame.display.update()
pygame.quit()
