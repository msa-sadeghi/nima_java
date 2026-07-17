import pygame

pygame.init()
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
clock = pygame.time.Clock()

castle_25_img = pygame.image.load("assets/castle/castle_25.png")
castle_50_img = pygame.image.load("assets/castle/castle_50.png")
castle_100_img = pygame.image.load("assets/castle/castle_100.png")

tower_25_img = pygame.image.load("assets/tower/tower_25.png")
tower_50_img = pygame.image.load("assets/tower/tower_50.png")
tower_100_img = pygame.image.load("assets/tower/tower_100.png")

armour_img = pygame.image.load("assets/armour.png")
bg_img = pygame.image.load("assets/bg.png")
bullet_img = pygame.image.load("assets/bullet.png")
crosshair_img = pygame.image.load("assets/crosshair.png")
repair_img = pygame.image.load("assets/repair.png")

shoot_sound = pygame.mixer.Sound("assets/jump.wav")

all_enemies_images = []
all_enemies_types = ("knight", "goblin", "purple_goblin", "red_goblin")
all_enemies_healths = (1, 2, 3, 4)
all_animations_types = ("walk", "attack", "death")
for enemy in all_enemies_types:
    enemy_animation = []
    for anime in all_animations_types:
        animation_images = []
        for i in range(20):
            img = pygame.image.load(f"assets/enemies/{enemy}/{anime}/{i}.png")
            w = img.get_width()
            h = img.get_height()
            img = pygame.transform.scale(img, (w * 0.3, h * 0.3))
            animation_images.append(img)
        enemy_animation.append(animation_images)
    all_enemies_images.append(enemy_animation)
