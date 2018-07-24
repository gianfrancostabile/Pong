
import pygame
from pygame import *
from draw.screen import Screen
from exceptions.excessplayerexception import ExcessPlayerException
from player import Player
from draw.bar import Bar


def main():
    screen = Screen()
    window = screen.create_screen()

    width, height = pygame.display.get_surface().get_size()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)

    width_bar, height_bar = 70, 10

    x_bar = int(width * 0.1)
    y_bar = int(height * 0.94)
    pos_one = Bar(x_bar, y_bar, width_bar, height_bar, 1, red)

    x_bar = int(width * 0.1)
    y_bar = int(height * 0.04)
    pos_two = Bar(x_bar, y_bar, width_bar, height_bar, 2, blue)

    x_bar = int(width * 0.04)
    y_bar = int(height * 0.1)
    pos_three = Bar(x_bar, y_bar, width_bar, height_bar, 3, green)

    x_bar = int(width * 0.94)
    y_bar = int(height * 0.1)
    pos_four = Bar(x_bar, y_bar, width_bar, height_bar, 4, yellow)

    player_list = list()

    try:
        player_list.append(Player("Juan", pos_one))
        player_list.append(Player("Pedro", pos_two))
        player_list.append(Player("Luis", pos_three))
        player_list.append(Player("Jorge", pos_four))

    except ExcessPlayerException as epe:
        print(epe)
    else:
        screen.add_players(player_list)

    running = True
    while running:
        keydown_pressed = False
        key_pressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            elif event.type == KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                keydown_pressed = True

        if keydown_pressed:
            screen.move_player(key_pressed)
if __name__ == "__main__":
    pygame.init()
    main()