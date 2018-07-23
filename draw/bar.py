
import pygame


class Bar_Position(object):

    def __init__(self, position, form, color):
        self.position = position
        self.form = form
        self.color = color


class Bar(object):

    def __init__(self, position):
        self.position = position

    def draw(self, screen):
        pygame.draw.rect(screen, self.position.color, self.position.form, 0)
        pygame.display.update()

    def clean(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.position.form, 0)
        pygame.display.update()

    def move_left(self, screen):
        self.clean(screen)

        border_left = self.position.form[0] - 1
        border_top = self.position.form[1]
        body_width = self.position.form[2]
        body_height = self.position.form[3]

        self.position.form = (border_left, border_top, body_width, body_height)
        self.draw(screen)

    def move_right(self, screen):
        self.clean(screen)

        border_left = self.position.form[0] + 1
        border_top = self.position.form[1]
        body_width = self.position.form[2]
        body_height = self.position.form[3]

        self.position.form = (border_left, border_top, body_width, body_height)
        self.draw(screen)
