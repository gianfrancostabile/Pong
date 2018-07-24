
import pygame
from .frame import Frame


class Corner(Frame):

    def __init__(self, x, y, width, height, color):
        super(Corner, self).__init__(x, y, width, height, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)
        pygame.display.flip()
