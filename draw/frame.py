
import pygame
from pictures import picture


class Frame(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def get_tuple_format(self):
        tuple_format = (self.x, self.y, self.width, self.height)
        return tuple_format

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_tuple_format(), 0)
        pygame.display.flip()

    def clean(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.get_tuple_format(), 0)
        pygame.display.flip()

    def is_colliding(self, obj):
        collision = False

        top_obj, bottom_obj, left_obj, right_obj = 0, 0, 0, 0
        top_this, bottom_this, left_this, right_this = \
            self.y, self.y + self.height, self.x, self.x + self.width

        if isinstance(obj, Frame):
            top_obj, bottom_obj, left_obj, right_obj = \
                obj.y, obj.y + obj.height, obj.x, obj.x + obj.width

            if top_obj >= top_this >= bottom_obj or top_obj <= bottom_this <= bottom_obj:
                if left_obj <= left_this <= right_obj or left_obj <= right_this <= right_obj:
                    collision = True
                elif left_this <= left_obj <= right_this and left_this <= right_obj <= right_this:
                    collision = True

        elif isinstance(obj, tuple):
            top_obj, right_obj, bottom_obj, left_obj = \
                obj[0], obj[1], obj[2], obj[3]

            if top_obj >= top_this or right_this >= right_obj or bottom_this >= bottom_obj or left_obj >= left_this:
                collision = True


        return collision