
import pygame


class Frame(object):

    def __init__(self, x, y, width, height, color):
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
        collision = [False, ""]
        top_this, bottom_this, left_this, right_this = \
            self.y, self.y + self.height, self.x, self.x + self.width

        if isinstance(obj, Frame):
            top_obj, bottom_obj, left_obj, right_obj = \
                obj.y, obj.y + obj.height, obj.x, obj.x + obj.width

            if (top_this <= top_obj <= bottom_this or top_this <= bottom_obj <= bottom_this
                    or (top_obj <= top_this <= bottom_obj and top_obj <= bottom_this <= bottom_obj)) and \
                (left_this <= left_obj <= right_this or left_this <= right_obj <= right_this
                    or (left_obj <= left_this <= right_obj and left_obj <= right_this <= right_obj)):
                if left_obj == right_this:
                    collision = [True, "Left"]
                elif right_obj == left_this:
                    collision = [True, "Right"]
                elif top_obj == bottom_this:
                    collision = [True, "Top"]
                elif bottom_obj == top_this:
                    collision = [True, "Bottom"]
        return collision
