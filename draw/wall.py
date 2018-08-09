
import pygame
from .frame import Frame


class Wall(Frame):

    def __init__(self, x, y, width, height, color):
        super(Wall, self).__init__(x, y, width, height, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        pygame.display.flip()
