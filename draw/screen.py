
import pygame
import os
from .corner import Corner
from .ball import Ball
from .bar import Bar
from player import Player
from exceptions.excessplayerexception import ExcessPlayerException

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Screen(object):

    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.players = list()
        self.corners = list()
        self.ball = None

    def create_screen(self):
        self.add_corners()
        self.add_players()
        self.add_ball()
        return self.screen

    def add_corners(self):
        self.corners.append(Corner(0, 0, int(self.width*0.1), int(self.height*0.1), (128, 128, 128)))
        self.corners.append(Corner(int(self.width*0.9), 0, int(self.width*0.1), int(self.height*0.1), (128, 128, 128)))
        self.corners.append(Corner(0, int(self.height*0.9), int(self.width*0.1), int(self.height*0.1), (128, 128, 128)))
        self.corners.append(Corner(int(self.width*0.9), int(self.height*0.9), int(self.width*0.1), int(self.height*0.1), (128, 128, 128)))
        self.draw_corners()

    def add_players(self):
        red = (255, 0, 0)
        blue = (0, 0, 255)
        green = (0, 255, 0)
        yellow = (255, 255, 0)
        width_bar, height_bar = 70, 10

        pos_one = Bar(int(self.width * 0.5) - (width_bar/2), int(self.height * 0.9), width_bar, height_bar, 1, red)
        pos_two = Bar(int(self.width * 0.5) - (width_bar/2), int(self.height * 0.1) - height_bar, width_bar, height_bar, 2, blue)
        pos_three = Bar(int(self.width * 0.1) - height_bar, int(self.height * 0.5) - (width_bar/2), height_bar, width_bar, 3, green)
        pos_four = Bar(int(self.width * 0.9), int(self.height * 0.5) - (width_bar/2), height_bar, width_bar, 4, yellow)

        try:
            self.players.append(Player("Player 1", pos_one))
            self.players.append(Player("Player 2", pos_two))
            self.players.append(Player("Player 3", pos_three))
            self.players.append(Player("Player 4", pos_four))
        except ExcessPlayerException as epe:
            print(epe)
        self.draw_players()

    def add_ball(self):
        self.ball = Ball((255, 255, 255))
        self.ball.draw(self.screen)

    def draw_corners(self):
        for corner in self.corners:
            corner.draw(self.screen)

    def draw_players(self):
        for player in self.players:
            player.bar.draw(self.screen)

    def move_ball(self):
        frames_collision = self.players + self.corners
        self.ball.move(self.screen, frames_collision)

    def move_player(self, key_pressed):
        player = None
        corners_between = []
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_RIGHT]:
            player = self.get_player_in_position(1)
            corners_between = self.get_corners_side("Bottom")
            if key_pressed[pygame.K_LEFT]:
                key_pressed = "LEFT"
            else:
                key_pressed = "RIGHT"

        if player and len(corners_between) != 0:
            player.move_bar(self.screen, key_pressed, corners_between)

    def get_player_in_position(self, position):
        for player in self.players:
            if player.bar.position == position:
                return player
        return None

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

    def check_ball_out(self):
        out = False
        if 0 > (self.ball.x + self.ball.width):
            out = True
        elif self.ball.x > self.width:
            out = True
        elif 0 > (self.ball.y + self.ball.height):
            out = True
        elif self.ball.y > self.height:
            out = True
        return out
