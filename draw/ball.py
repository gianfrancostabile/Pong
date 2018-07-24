
import pygame
from .frame import Frame


class Ball(Frame):

    def __init__(self, color):
        width, height = pygame.display.get_surface().get_size()
        x = int(width / 2)
        y = int(height / 2)

        super(Ball, self).__init__(x, y, 5, 5, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_tuple_format(), 5)
        pygame.display.flip()

    def move(self):
        pass