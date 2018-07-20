import pygame
from draw.board import Board

def main():
    screen = pygame.display.set_mode((850, 400))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()