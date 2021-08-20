import pygame
import sys, os

pygame.init()
pygame.font.init()

# Colors for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

res = (720, 720)
WIN = pygame.display.set_mode(res)
FPS = 60

# Get the entire windows height and width
height = WIN.get_height()
width = WIN.get_width()

pygame.display.set_caption('Guess the word')

# Button object
class Buttons:

    def __init__(self, text, font, pos, bg="BLACK", feedback=""):
        self.x = pos
        self.y = pos
        self.font = pygame.font.SysFont('Arial', font, bold=True, italic=False)
        if feedback == "":
            self.feedback = text 
        else:
            self.feedback = feedback

    def change_text(self, text, bg):
        self.text = self.font.render(text, True, BLACK)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    # When we have constructed our buttons, then i can give the coordinates down here.
    def show(self):
        WIN.blit()

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")

def main_loop():

    clock = pygame.time.Clock()
    #mouse = pygame.mouse.get_pos()
    while True:

        WIN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


        clock.tick(FPS)
        pygame.display.update()

word_one = Buttons(
    "Hello there",
    (100, 100),
    30,
    bg="navy",
    feedback="Button got clicked"
)

main_loop()