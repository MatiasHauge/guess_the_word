import pygame
from Button import *
import sys, os

pygame.init()
pygame.font.init()

# Colors for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Necasary stuff
res = (720, 720)
WIN = pygame.display.set_mode(res)
pygame.display.set_caption("Guess the word")

# Fonts and texts
arial_24 = pygame.font.SysFont('Arial', 24)
start_btn_text = arial_24.render('Start', True, BLACK)

# Frames for second
FPS = 60

# Random images and its ref
x_pad = 50
y_pad = 50
image_width = 150
image_height = 350

image_one_container = pygame.Rect(x_pad, y_pad, image_width, image_height)
image_one_load = pygame.image.load(os.path.join('images', 'image_one.jpg'))
image_one = pygame.transform.scale(image_one_load, (image_width, image_height))

# Draw main relavant stuff.
def draw_main_win():
    WIN.fill(WHITE)
    WIN.blit(start_btn_text, (20, 20))

    image_one = pygame.Rect(image_one_container.x, image_one_container.y, image_width, image_height)
    draw_random_images(image_one)

    pygame.display.update()

def draw_random_images(image_one):
    # Going to make a custom object for images like buttons.
    # Image one
    pygame.draw.rect(WIN, WHITE, image_one_container)
    WIN.blit(image_one, (image_one.x, image_one.y))

def clicked_btns():
    # Find another solution.
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_pos)

def main_loop():

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        draw_main_win()
        clock.tick(FPS)
        clicked_btns()

        pygame.display.update()

main_loop()