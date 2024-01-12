import pygame
from random import choice
pygame.init()
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the clown")
FPS = 60
PLAYER_STARTING_LIVES = 5
CLOWNS_STARTING_VELOCITY = 5
CLOWN_ACCELERATION = 1
score = 0
player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWNS_STARTING_VELOCITY
clown_dx = choice([-1, 1])
clown_dy = choice([-1, 1])
my_color = (216, 38, 22)
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

font = pygame.font.Font("AttackGraffiti.ttf", 32)

title_text = font.render("Catch the clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render(f"Score: {score}", True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

click_sound = pygame.mixer.Sound("click_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("ctc_background_music.wav")

background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)


clown_image = pygame.image.load("clown.png")
clow_rect = clown_image.get_rect()
clow_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

pygame.mixer.music.play(-1, 0.0)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            if clow_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION

                previous_dx = clown_dx
                previous_dy = clown_dy

                while (previous_dx == clown_dx and previous_dy == clown_dy):

                    clown_dx = choice([-1, 1])
                    clown_dy = choice([-1, 1])

            else:
                miss_sound.play()
                player_lives -= 1

    # این دو خط مسئول حرکت دادن دلقک هستند
    clow_rect.x += clown_dx * clown_velocity
    clow_rect.y += clown_dy * clown_velocity

    # این کدها مسئول چک کردن برخورد به لبه ها و برگشت دلقک از لبه ها هستند
    if clow_rect.left <= 0 or clow_rect.right >= WINDOW_WIDTH:
        clown_dx = -1 * clown_dx

    if clow_rect.top <= 0 or clow_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1 * clown_dy

    score_text = font.render(f"Score: {score}", True, YELLOW)
    lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)

    # TODO   اضافه کردن game over

    display_surface.blit(background_image, background_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(clown_image, clow_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
