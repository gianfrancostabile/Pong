
import pygame
from draw.screen import Screen
import time


def main():
    screen = Screen()
    window = screen.create_screen()

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
    main()
