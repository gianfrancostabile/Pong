
import pygame
from draw.draw_entity import DrawEntity

class Ball(DrawEntity):

    def __init__(self, screen):
        self.put(screen)

    def put(self, screen):
        width = int(screen.width / 2) - 2
        height = int(screen.height / 2) - 2
        white = (255, 255, 255)
        rectangle = (width, height, 5, 5)
        self.draw(screen, white, rectangle)

    def draw(self, screen, color, rectangle):
        pygame.draw.rect(screen, color, rectangle, 5)