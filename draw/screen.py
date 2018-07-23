
import pygame
import os
from .ball import Ball

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Screen(object):

    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))

    def create_screen(self):
        self.paint_corners()

        ball = Ball()
        ball.put(self.screen, (255, 255, 255))

        return self.screen


    def paint_corners(self):
        width, height = pygame.display.get_surface().get_size()
        pygame.draw.rect(self.screen, (128, 128, 128), (int(width*0), int(height*0), int(width*0.1), int(height*0.1)), 0)
        pygame.draw.rect(self.screen, (128, 128, 128), (int(width*0), int(height*0.9), int(width*0.1), int(height*1)), 0)
        pygame.draw.rect(self.screen, (128, 128, 128), (int(width*0.9), int(height*0), int(width*1), int(height*0.1)), 0)
        pygame.draw.rect(self.screen, (128, 128, 128), (int(width*0.9), int(height*0.9), int(width*1), int(height*1)), 0)
        pygame.display.flip()

    def add_players(self, player_list):
        for player in player_list:
            player.bar.draw(self.screen)