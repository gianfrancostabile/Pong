
import pygame
import os
from draw.ball import Ball

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Screen(object):

    def __init__(self):
        self.width = 850
        self.height = 400
        self.screen = self.create_screen()

    def create_screen(self):
        screen = pygame.display.set_mode((self.width, self.height))
        ball = Ball()

        return screen


