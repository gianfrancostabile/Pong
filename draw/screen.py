
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

        ball = Ball(color=(255, 255, 255))
        ball.draw(self.screen)

        return self.screen

    def add_corners(self):
        self.corners.append(Corner(0, 0, int(self.width*0.1), int(self.height*0.1), (128, 128, 128)))
        self.corners.append(Corner(int(self.width*0.9), 0, int(self.width), int(self.height*0.1), (128, 128, 128)))
        self.corners.append(Corner(0, int(self.height*0.9), int(self.width*0.1), int(self.height), (128, 128, 128)))
        self.corners.append(Corner(int(self.width*0.9), int(self.height*0.9), int(self.width), int(self.height), (128, 128, 128)))
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
        corners_between = []
        if key_pressed[K_LEFT] or key_pressed[K_RIGHT]:
            player = self.get_player_in_position(1)
            corners_between = self.get_corners_side("Bottom")
            if key_pressed[K_LEFT]:
                key_pressed = "LEFT"
            else:
                key_pressed = "RIGHT"

        if player and len(corners_between) != 0:
            player.move_bar(self.screen, key_pressed, corners_between)

    def get_player_in_position(self, position):
        player_return = None
        for player in self.players:
            if player.bar.position.position == position:
                player_return = player
                break

        return player_return

    def get_corners_side(self, side):
        corners_between = []
        for corner in self.corners:
            if side == "Top":
                if corner.y == 0:
                    corners_between.append(corner)
            elif side == "Bottom":
                if corner.y != 0:
                    corners_between.append(corner)
            elif side == "Left":
                if corner.x == 0:
                    corners_between.append(corner)
            elif side == "Right":
                if corner.x != 0:
                    corners_between.append(corner)

        return corners_between