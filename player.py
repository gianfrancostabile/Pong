
import pygame

from exceptions.excessplayerexception import ExcessPlayerException
from draw.bar import Bar

PLAYER_COUNTER = 0

class Player(object):

    def __init__(self, name, position):
        global PLAYER_COUNTER

        if 4 > PLAYER_COUNTER >= 0:
            self.name = name
            self.bar = Bar(position)
            self.score = 0
            self.lives = 5

            PLAYER_COUNTER += 1
        else:
            raise ExcessPlayerException

    def move_bar(self, screen, key_pressed):
        if key_pressed == "LEFT":
            self.bar.move_left(screen)
        elif key_pressed == "RIGHT":
            self.bar.move_right(screen)