import pygame

width = 400
height = 500
image = pygame.image.load("./bear.png")
rect = image.get_rect(center = (100, 200))
screen = pygame.display.set_mode(
    (width, height)
)

FPS  = 60
clock = pygame.time.Clock()
moving_left, moving_right= (False, False)
running = True
while running == True:
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
    if moving_left:
        rect.x -= 5       
    if moving_right:
        rect.x += 5      
    screen.fill("lightgreen") 
    screen.blit(image, rect)
    pygame.display.update()
    clock.tick(FPS)
            