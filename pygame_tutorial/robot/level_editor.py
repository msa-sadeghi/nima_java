import pygame
pygame.init()
screen_width = 1000
SIDE_MARGIN = 400
screen_height = 640
LOWER_MARGIN = 100
screen = pygame.display.set_mode((screen_width + SIDE_MARGIN, screen_height + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()
FPS = 60
running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")  # Fill the screen with black
    pygame.draw.rect(screen, "lightblue", (screen_width, 0, SIDE_MARGIN, screen_height + LOWER_MARGIN))  # Draw the black rectangle
    pygame.draw.rect(screen, "lightblue", (0, screen_height, screen_width, LOWER_MARGIN))  # Draw the black rectangle
    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Control the frame rate
pygame.quit()