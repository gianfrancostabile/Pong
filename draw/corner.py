
import pygame

class Corner(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, (128, 128, 128), (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)
        pygame.display.flip()

    def verify_collision(self, obj):
        pass