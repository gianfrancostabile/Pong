
import pygame
import os
from .corner import Corner
from pygame import *
from .ball import Ball

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Screen(object):

    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.players = list()
        self.corners = list()

    def create_screen(self):
        self.add_corners()

        ball = Ball()
        ball.put(self.screen, (255, 255, 255))

        return self.screen

    def add_corners(self):
        self.corners.append(Corner(0, 0, int(self.width*0.1), int(self.height*0.1)))
        self.corners.append(Corner(0, int(self.height*0.9), int(self.width*0.1), int(self.height)))
        self.corners.append(Corner(int(self.width*0.9), 0, int(self.width), int(self.height*0.1)))
        self.corners.append(Corner(int(self.width*0.9), int(self.height*0.9), int(self.width), int(self.height)))
        self.draw_corners()

    def draw_corners(self):
        for corner in self.corners:
            corner.draw(self.screen)

    def add_players(self, player_list):
        self.players = player_list
        self.draw_players()

    def draw_players(self):
        for player in self.players:
            player.bar.draw(self.screen)

    def move_player(self, key_pressed):
        player = None
        if key_pressed[K_LEFT] or key_pressed[K_RIGHT]:
            player = self.get_player_in_position(1)
            if key_pressed[K_LEFT]:
                key_pressed = "LEFT"
            else:
                key_pressed = "RIGHT"

        if player:
            player.move_bar(self.screen, key_pressed)

    def get_player_in_position(self, position):
        for player in self.players:
            if player.bar.position.position == position:
                return player

        return None

