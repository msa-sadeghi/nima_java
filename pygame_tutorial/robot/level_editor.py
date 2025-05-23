import pygame
pygame.init()
import os
from button import Button
screen_width = 1000
SIDE_MARGIN = 400
screen_height = 640
LOWER_MARGIN = 100
screen = pygame.display.set_mode((screen_width + SIDE_MARGIN, screen_height + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()
TILE_SIZE = 50
ROWS = 20
COLS = 150
def draw_lines():
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "brown", (0, i * TILE_SIZE), (screen_width, i *TILE_SIZE))
    for i in range(COLS + 1):
        pygame.draw.line(screen, "brown", (i * TILE_SIZE, 0), (i *TILE_SIZE, screen_height))


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

r = 0
c = 0
buttons_list = []
for i in range(len(objects_images)):
    buttons_list.append(Button(objects_images[i], screen_width + 40 + c * 70, 70 + r * 70, 'object'))
    c += 1
    if c == 5:
        r += 1
        c = 0
for i in range(len(tiles_images)):
    buttons_list.append(Button(tiles_images[i], screen_width + 40 + c * 70, 70 + r * 70, 'object'))
    c += 1
    if c == 5:
        r += 1
        c = 0

selected_button_index = 0
FPS = 60

world_map = []
for i in range(ROWS):
    row = [-1] * COLS
    world_map.append(row)

def draw_world():
    for i in range(ROWS):
        for j in range(COLS):
            if world_map[i][j] != -1:
                screen.blit(buttons_list[world_map[i][j]].image, (j * TILE_SIZE, i * TILE_SIZE))



running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")  # Fill the screen with black
    draw_lines()
    pygame.draw.rect(screen, "lightblue", (screen_width, 0, SIDE_MARGIN, screen_height + LOWER_MARGIN))  # Draw the black rectangle
    pygame.draw.rect(screen, "lightblue", (0, screen_height, screen_width, LOWER_MARGIN))  # Draw the black rectangle
    draw_world()
    for i,btn in enumerate(buttons_list):
       if btn.update(screen) == True:
            selected_button_index = i
    
    mouse_pos = pygame.mouse.get_pos()
    if  mouse_pos[0] < screen_width and mouse_pos[1] < screen_height:
        r = mouse_pos[1] //  TILE_SIZE
        c = mouse_pos[0] //  TILE_SIZE
        if pygame.mouse.get_pressed()[0]:
            world_map[r][c] = selected_button_index
    
    pygame.draw.rect(screen, "orangered", buttons_list[selected_button_index].rect, 3)
    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Control the frame rate
pygame.quit()