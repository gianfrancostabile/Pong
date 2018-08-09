
import pygame
import time
from draw.screen import Screen
from draw.bar import Bar
from draw.wall import Wall
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

    corner_tl = Wall(0, 0, int(width * 0.1), int(height * 0.1), (128, 128, 128))
    corner_tr = Wall(int(width * 0.9), 0, int(width * 0.1), int(height * 0.1), (128, 128, 128))
    corner_bl = Wall(0, int(height * 0.9), int(width * 0.1), int(height * 0.1), (128, 128, 128))
    corner_br = Wall(int(width * 0.9), int(height * 0.9), int(width * 0.1), int(height * 0.1), (128, 128, 128))
    corners.append(corner_tl)
    corners.append(corner_tr)
    corners.append(corner_bl)
    corners.append(corner_br)

    wall_top = Wall(int(width * 0.1), 0, int(width * 0.9), int(height * 0.1), (128, 128, 128))
    wall_right = Wall(int(width * 0.9), int(height * 0.1), int(width * 0.1), int(height * 0.9), (128, 128, 128))
    wall_bottom = Wall(int(width * 0.1), int(height * 0.9), int(width * 0.9), int(height * 0.1), (128, 128, 128))
    wall_left = Wall(0, int(height * 0.1), int(width * 0.1), int(height * 0.9), (128, 128, 128))

    bar_player_one = Bar(int(width * 0.5) - (width_bar / 2), int(height * 0.9), width_bar, height_bar, 1, red)
    bar_player_two = Bar(int(width * 0.5) - (width_bar / 2), int(height * 0.1) - height_bar, width_bar, height_bar, 2, blue)
    bar_player_three = Bar(int(width * 0.1) - height_bar, int(height * 0.5) - (width_bar / 2), height_bar, width_bar, 3, green)
    bar_player_four = Bar(int(width * 0.9), int(height * 0.5) - (width_bar / 2), height_bar, width_bar, 4, yellow)

    try:
        players.append(Player("Player 1", bar_player_one, wall_bottom))
        players.append(Player("Player 2", bar_player_two, wall_top))
        players.append(Player("Player 3", bar_player_three, wall_left))
        players.append(Player("Player 4", bar_player_four, wall_right))
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

        if out:
            screen.reset_screen()

        time.sleep(0.01)


if __name__ == "__main__":
    pygame.init()
    screen = create_screen()
    main(screen)
