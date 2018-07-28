
import pygame
from .frame import Frame


class Ball(Frame):

    def __init__(self, color):
        width, height = pygame.display.get_surface().get_size()
        x = int(width / 2)
        y = int(height / 2)

        super(Ball, self).__init__(x, y, 10, 10, color)
        self.speedX = 2
        self.speedY = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_tuple_format(), 0)
        pygame.display.flip()

    def clean(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.get_tuple_format(), 0)
        pygame.display.flip()

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

