from constants import *
from player import Player
from enemy import Enemy
from door import Door
class World:
    def __init__(self, data, player_group, enemy_group, door_group):
        self.tiles_map = []
        self.image = BG_PIC
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.enemy_group = enemy_group
        self.door_group = door_group

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    img = DIRT_IMAGE
                    rect = img.get_rect(topleft=(j * TILE_SIZE, i * TILE_SIZE))
                    self.tiles_map.append((img,rect))
                if data[i][j] == 2:
                    img = GRASS_IMAGE
                    rect = img.get_rect(topleft=(j * TILE_SIZE, i * TILE_SIZE))
                    self.tiles_map.append((img, rect))
                if data[i][j] == 3:
                    img = WATER_IMAGE
                    rect = img.get_rect(topleft=(j * TILE_SIZE, i * TILE_SIZE))
                    self.tiles_map.append((img, rect))
                if data[i][j] == 4:
                    my_player = Player(j * TILE_SIZE, i * TILE_SIZE)
                    player_group.add(my_player)
                if data[i][j] == 5:
                    enemy = Enemy(ENEMY_IMAGE, j * TILE_SIZE, i * TILE_SIZE)
                    self.enemy_group.add(enemy)
                if data[i][j] == 6:
                    door = Door(j * TILE_SIZE, i * TILE_SIZE)
                    self.door_group.add(door)

        

    def draw(self):
        SCREEN.blit(self.image, self.rect)
        for tile in self.tiles_map:
            SCREEN.blit(tile[0],tile[1])