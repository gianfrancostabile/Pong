
import pygame


class Frame(object):

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def get_tuple_format(self):
        return (self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_tuple_format(), 0)
        pygame.display.flip()

    def clean(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.get_tuple_format(), 0)
        pygame.display.flip()

    def is_colliding(self, obj):
        collision = False

        if isinstance(obj, Frame):
            top_this, bottom_this, left_this, right_this = \
                self.y, self.y + self.height, self.x, self.x + self.width
            top_obj, bottom_obj, left_obj, right_obj = \
                obj.y, obj.y + obj.height, obj.x, obj.x + obj.width

            if top_obj >= top_this >= bottom_obj or top_obj <= bottom_this <= bottom_obj:
                if left_obj <= left_this <= right_obj or left_obj <= right_this <= right_obj:
                    collision = True
                elif left_this <= left_obj <= right_this and left_this <= right_obj <= right_this:
                    collision = True

        return collision