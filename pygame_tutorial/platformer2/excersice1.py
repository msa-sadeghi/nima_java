import pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
circle_rect = pygame.Rect(100,300, 50, 50)
def move(moving_left, moving_right):
    if moving_left:
        circle_rect.x -= 5
    if moving_right:
        circle_rect.x += 5
oving_left, moving_right = (False, False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
                
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
                
            if event.key == pygame.K_RIGHT:
                moving_right = False        
    screen.fill((0,0,0)) 
    move(moving_left, moving_right) 
    pygame.draw.ellipse(screen, "red", circle_rect)
    pygame.display.update()
    clock.tick(60)