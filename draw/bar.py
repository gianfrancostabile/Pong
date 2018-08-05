
from .frame import Frame


class Bar(Frame):

    def __init__(self, x, y, width, height, position, color):
        self.position = position
        super(Bar, self).__init__(x, y, width, height, color)

    def move_left(self, screen, obj):
        self.clean(screen)
        i = 0
        while i < 4:
            collision = obj.is_colliding(self)
            if collision[0]:
                break
            self.x -= 1
            i += 1
        self.draw(screen)

    def move_right(self, screen, obj):
        self.clean(screen)
        i = 0
        while i < 4:
            collision = obj.is_colliding(self)
            if collision[0]:
                break
            self.x += 1
            i += 1
        self.draw(screen)
