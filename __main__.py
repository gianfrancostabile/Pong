
import pygame
import time
from draw.screen import Screen
from draw.bar import Bar
from draw.corner import Corner
from player import Player
from exceptions.excessplayerexception import ExcessPlayerException


def create_screen():
    height = width = 500
    players = list()
    corners = list()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    width_bar, height_bar = 70, 10

    corners.append(Corner(0, 0, int(width * 0.1), int(height * 0.1), (128, 128, 128)))
    corners.append(Corner(int(width * 0.9), 0, int(width * 0.1), int(height * 0.1), (128, 128, 128)))
    corners.append(Corner(0, int(height * 0.9), int(width * 0.1), int(height * 0.1), (128, 128, 128)))
    corners.append(Corner(int(width * 0.9), int(height * 0.9), int(width * 0.1), int(height * 0.1), (128, 128, 128)))

    player_one = Bar(int(width * 0.5) - (width_bar / 2), int(height * 0.9), width_bar, height_bar, 1, red)
    player_two = Bar(int(width * 0.5) - (width_bar / 2), int(height * 0.1) - height_bar, width_bar, height_bar, 2, blue)
    player_three = Bar(int(width * 0.1) - height_bar, int(height * 0.5) - (width_bar / 2), height_bar, width_bar, 3, green)
    player_four = Bar(int(width * 0.9), int(height * 0.5) - (width_bar / 2), height_bar, width_bar, 4, yellow)

    try:
        players.append(Player("Player 1", player_one))
        players.append(Player("Player 2", player_two))
        players.append(Player("Player 3", player_three))
        players.append(Player("Player 4", player_four))
    except ExcessPlayerException as epe:
        print(epe)

    screen = Screen(width, height)
    screen.add_corners(corners)
    screen.add_players(players)
    return screen


def main(screen):
    screen.draw_screen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        key_pressed = pygame.key.get_pressed()
        if key_pressed:
            screen.move_player(key_pressed)

        screen.move_ball()
        out = screen.check_ball_out()

        """if out:
            running = False
            pygame.quit()
            quit()
"""
        time.sleep(0.01)


if __name__ == "__main__":
    pygame.init()
    screen = create_screen()
    main(screen)
