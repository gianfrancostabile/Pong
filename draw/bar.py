
import pygame
from .frame import Frame


class Bar(Frame):

    def __init__(self, x, y, width, height, position, color):
        self.position = position
        super(Bar, self).__init__(x, y, width, height, color)

    def move_left(self, screen, object):
        if not self.is_colliding(object):
            self.clean(screen)
            self.x -= 2
            self.draw(screen)

    def move_right(self, screen, object):
        if not self.is_colliding(object):
            self.clean(screen)
            self.x += 2
            self.draw(screen)
