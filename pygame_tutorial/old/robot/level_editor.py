import pygame
pygame.init()
import os
from button import Button
import pickle
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
        pygame.draw.line(screen, "brown", (i * TILE_SIZE -scroll, 0), (i *TILE_SIZE -scroll, screen_height))


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
                screen.blit(buttons_list[world_map[i][j]].image, (j * TILE_SIZE - scroll, i * TILE_SIZE))

scroll = 0
scroll_left, scroll_right = (False, False)

f = pygame.font.SysFont('arial', 22)
level = 1
level_text = f.render(f"level: {level}", True, "black")
level_rect = level_text.get_rect(center = ( 50, screen_height + 50))

arrow_image_up = pygame.image.load("./arrow.png")
arrow_image_up = pygame.transform.rotate(arrow_image_up, -90)
arrow_image_up = pygame.transform.scale_by(arrow_image_up, 0.2)

arrow_image_down = pygame.transform.rotate(arrow_image_up, 180)
arrow_up_btn = Button(arrow_image_up, 200, screen_height + 25,"btn")
arrow_down_btn = Button(arrow_image_down, 270, screen_height + 25,"btn")

save_btn_image = pygame.image.load("./save.png")
save_btn_image = pygame.transform.scale(save_btn_image, (50, 50))
load_btn_image = pygame.image.load("./load.png")
load_btn_image = pygame.transform.scale(load_btn_image, (50, 50))

save_btn = Button(save_btn_image, 370, screen_height + 25,"btn")
load_btn = Button(load_btn_image, 440, screen_height + 25,"btn")


def save_level(level_number):
    with open(f"level{level_number}", "wb") as f:
        pickle.dump(world_map,  f)

def load_level(level):
    global world_map
    with open(f"level{level}", "rb") as f:
        world_map = pickle.load(f)

running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
    
    if scroll_left and scroll > 0:
        scroll -= 5
    elif scroll_right:
        scroll += 5
    screen.fill("white")  # Fill the screen with black
    draw_lines()
    draw_world()
    pygame.draw.rect(screen, "lightblue", (screen_width, 0, SIDE_MARGIN, screen_height + LOWER_MARGIN))  # Draw the black rectangle
    pygame.draw.rect(screen, "lightblue", (0, screen_height, screen_width, LOWER_MARGIN))  # Draw the black rectangle
    level_text = f.render(f"level: {level}", True, "black")
    screen.blit(level_text, level_rect)
    if arrow_up_btn.update(screen):
        level += 1
    if arrow_down_btn.update(screen) and level > 1:
        level -= 1

    if save_btn.update(screen):
        save_level(level)
    if load_btn.update(screen):
        load_level(level)
    for i,btn in enumerate(buttons_list):
       if btn.update(screen) == True:
            selected_button_index = i
    
    mouse_pos = pygame.mouse.get_pos()
    if  mouse_pos[0] < screen_width and mouse_pos[1] < screen_height:
        r = mouse_pos[1] //  TILE_SIZE
        c = (mouse_pos[0] + scroll) //  TILE_SIZE
        if pygame.mouse.get_pressed()[0]:
            world_map[r][c] = selected_button_index
        elif pygame.mouse.get_pressed()[2]:
            world_map[r][c] = -1
    
    pygame.draw.rect(screen, "orangered", buttons_list[selected_button_index].rect, 3)
    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Control the frame rate
pygame.quit()