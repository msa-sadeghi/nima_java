from config import *
from character import Character
clock = pygame.time.Clock()


player = Character('player', 100, 300, 60, 10)
moving_left, moving_right, moving_up = (False, False, False)
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
            if event.key == pygame.K_UP:
                moving_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
                
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                moving_up = False
    if moving_left or moving_right:
        player.change_animation("Run")  
    else:
        player.change_animation("Idle")          
    if moving_up and player.in_air == False:
        player.in_air = True
        player.yspeed = -15
        
    if player.in_air:
        player.change_animation("Jump")
    screen.fill((0,0,0))  
    player.move(moving_left, moving_right)      
    player.draw(screen)
    pygame.display.update()
    clock.tick(FPS)