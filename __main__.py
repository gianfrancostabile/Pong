
import pygame
from draw.screen import Screen

def main():
    screen = Screen()
    pg_screen = screen.create_screen()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()