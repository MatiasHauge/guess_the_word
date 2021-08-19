import pygame
import os

pygame.init()

# Colors for the game
WHITE = (255, 255, 255)

HEIGHT, WIDTH = 700, 500
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
WIN.fill(WHITE)
pygame.display.set_caption('Guess the word')

FPS = 60

def main_loop():

    clock = pygame.time.Clock()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(FPS)
        pygame.display.update()







if __name__ == '__main__':
    main_loop()