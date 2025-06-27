import pygame
from player import Player
import os
from world import World
pygame.init()
import pickle
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
TILE_SIZE = 50
objects_images = []
for img in os.listdir("./game_world/Objects"):
    image = pygame.image.load(f"./game_world/Objects/{img}")
    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
    objects_images.append(image)

tiles_images = []
for img in os.listdir("./game_world/Tiles"):
    image = pygame.image.load(f"./game_world/Tiles/{img}")
    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
    tiles_images.append(image)
    
objects_images.extend(tiles_images)

world_map = []
def load_level(level):
    global world_map
    with open(f"level{level}", "rb") as f:
        world_map = pickle.load(f)

load_level(1)
bomb_group = pygame.sprite.Group()
game_world = World(world_map, objects_images, bomb_group)


my_player = Player(100, 300)
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if my_player.in_air and my_player.shoot:
        my_player.change_animation("JumpShoot")
    elif my_player.shoot and not my_player.idle:
        my_player.change_animation("RunShoot")
    elif my_player.shoot:
        my_player.change_animation('Shoot')
    elif my_player.in_air:
        my_player.change_animation('Jump')
    elif my_player.slide:
        my_player.change_animation('Slide')
    elif my_player.idle:
        my_player.change_animation('Idle')
    else:
        my_player.change_animation('Run')
    my_player.draw(screen) 
    my_player.move()
    bomb_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)