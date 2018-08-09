
import pygame
import os
from .ball import Ball

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Screen(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.players = list()
        self.corners = list()
        self.ball = None

    def draw_screen(self):
        self.draw_corners()
        self.draw_players()
        self.add_ball()
        return self.screen

    def add_corners(self, corners):
        self.corners = corners

    def add_players(self, players):
        self.players = players

    def add_ball(self):
        self.ball = Ball((255, 255, 255))
        self.ball.draw(self.screen)

    def draw_corners(self):
        for corner in self.corners:
            corner.draw(self.screen)

    def draw_players(self):
        for player in self.players:
            if player.is_dead:
                player.wall.draw(self.screen)
            else:
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
            self.get_player_in_position(3).remove_life()
            out = True
        elif self.ball.x > self.width:
            self.get_player_in_position(4).remove_life()
            out = True
        elif 0 > (self.ball.y + self.ball.height):
            self.get_player_in_position(2).remove_life()
            out = True
        elif self.ball.y > self.height:
            self.get_player_in_position(1).remove_life()
            out = True
        return out

    def center_players(self):
        self.get_player_in_position(1).bar.x = int(self.width * 0.5) - (self.get_player_in_position(1).bar.width / 2)
        self.get_player_in_position(1).bar.y = int(self.height * 0.9)
        self.get_player_in_position(2).bar.x = int(self.width * 0.5) - (self.get_player_in_position(2).bar.width / 2)
        self.get_player_in_position(2).bar.y = int(self.height * 0.1) - self.get_player_in_position(2).bar.height
        self.get_player_in_position(3).bar.x = int(self.width * 0.1) - self.get_player_in_position(2).bar.height
        self.get_player_in_position(3).bar.y = int(self.height * 0.5) - (self.get_player_in_position(2).bar.width / 2)
        self.get_player_in_position(4).bar.x = int(self.width * 0.9)
        self.get_player_in_position(4).bar.y = int(self.height * 0.5) - (self.get_player_in_position(2).bar.width / 2)

    def clean_screen(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def reset_screen(self):
        self.clean_screen()
        self.center_players()
        self.draw_screen()