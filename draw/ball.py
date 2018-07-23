
import pygame

class Ball(object):

    def put(self, screen, color, form=None):
        if not form:
            width, height = pygame.display.get_surface().get_size()
            width = int(width / 2)
            height = int(height / 2)
            form = (width - 2, height - 2, 5, 5)
        self.draw(screen, color, form)

    def draw(self, screen, color, form):
        pygame.draw.rect(screen, color, form, 5)
        pygame.display.flip()

    def move(self):
        pass