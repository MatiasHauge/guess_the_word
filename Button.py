import pygame
pygame.font.init()

BLACK_COL = (0, 0, 0)

class Button:

    def __init__(self, text, font, pos, bg="BLACK", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont('Arial', font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback

    def show_btns(self, text, bg="BLACK"):
        self.text = self.font.render(text, True, pygame.Color("Black"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self

