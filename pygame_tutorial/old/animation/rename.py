import os

files = os.listdir("./images")
for f in files:
    os.rename(
        f"./images/{f}",
        f"./images/{f}".replace(" ", "").replace("(", "").replace(")", "")
    )
    
    
img = pygame.transform.scale(img, (,))