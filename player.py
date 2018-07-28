
import pygame
import time
from exceptions.excessplayerexception import ExcessPlayerException
from draw.bar import Bar

PLAYER_COUNTER = 0


class Player(object):

    def __init__(self, name, bar):
        global PLAYER_COUNTER

        if 4 > PLAYER_COUNTER >= 0:
            self.name = name
            self.bar = bar
            self.score = 0
            self.lives = 5

            PLAYER_COUNTER += 1
        else:
            raise ExcessPlayerException

    def move_bar(self, screen, key_pressed, corners_between):
        if key_pressed == "LEFT":
            corner_left = corners_between[0]
            self.bar.move_left(screen, corner_left)
        elif key_pressed == "RIGHT":
            corner_right = corners_between[1]
            self.bar.move_right(screen, corner_right)
