
import pygame
from draw.screen import Screen
from exceptions.excessplayerexception import ExcessPlayerException
from player import Player
from draw.bar import Bar_Position

def main():
    screen = Screen()
    window = screen.create_screen()

    width, height = pygame.display.get_surface().get_size()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)

    widthTL = int(width * 0.1)
    heightTL = int(height * 0.94)
    form = (widthTL, heightTL, 70, 10)
    POS_ONE = Bar_Position(1, form, red)

    widthTL = int(width * 0.1)
    heightTL = int(height * 0.04)
    form = (widthTL, heightTL, 70, 10)
    POS_TWO = Bar_Position(1, form, blue)

    widthTL = int(width * 0.04)
    heightTL = int(height * 0.1)
    form = (widthTL, heightTL, 10, 70)
    POS_THREE = Bar_Position(1, form, green)

    widthTL = int(width * 0.94)
    heightTL = int(height * 0.1)
    form = (widthTL, heightTL, 10, 70)
    POS_FOUR = Bar_Position(1, form, yellow)

    player_list = list()

    try:
        player_list.append(Player("Juan", POS_ONE))
        player_list.append(Player("Pedro", POS_TWO))
        player_list.append(Player("Luis", POS_THREE))
        player_list.append(Player("Jorge", POS_FOUR))

    except ExcessPlayerException as epe:
        print(epe)
    else:
        screen.add_players(player_list)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            key_pressed = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                player_list[0].move_bar(window, key_pressed)

if __name__ == "__main__":
    pygame.init()
    main()