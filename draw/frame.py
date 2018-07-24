
import pygame


class Frame(object):

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def get_tuple_format(self):
        return "({x}, {y}, {width}, {height})".format(x=self.x, y=self.y, width=self.width, height=self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_tuple_format(), 0)
        pygame.display.flip()

    def clean(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.get_tuple_format(), 0)
        pygame.display.flip()

    def is_colliding(self, obj):
        bool = False
        if isinstance(obj, Frame):
            pass

        return bool