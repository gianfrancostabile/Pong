
import pygame
import random
from .frame import Frame
from player import Player


class Ball(Frame):

    def __init__(self, color):
        width, height = pygame.display.get_surface().get_size()
        x = int(width / 2)
        y = int(height / 2)

        super(Ball, self).__init__(x, y, 10, 10, color)
        speed_pool = [-2, -3, -4, 2, 3, 4]
        self.speedX = random.choice(speed_pool)
        speed_pool.remove(self.speedX)
        speed_pool.remove((-1)*self.speedX)
        self.speedY = random.choice(speed_pool)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_tuple_format(), 0)
        pygame.display.flip()

    def clean(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.get_tuple_format(), 0)
        pygame.display.flip()

    def move(self, screen, frames):
        self.clean(screen)

        speed_start, speed_end = 2, 4
        moves_x, moves_y = self.speedX, self.speedY
        counter_x, counter_y = 0, 0
        collision = [False, "Out"]
        random_speed = random.randint(speed_start, speed_end)
        flag = 0

        if moves_x < 0:
            moves_x = (-1) * moves_x
        if moves_y < 0:
            moves_y = (-1) * moves_y

        while counter_x < moves_x or counter_y < moves_y and not collision[0]:
            for frame in frames:
                if isinstance(frame, Player):
                    frame = frame.bar

                collision = frame.is_colliding(self)
                if collision[0]:
                    if collision[1] == "Top":
                        self.speedY = random_speed
                    elif collision[1] == "Right":
                        self.speedX = (-1) * random_speed
                    elif collision[1] == "Bottom":
                        self.speedY = (-1) * random_speed
                    elif collision[1] == "Left":
                        self.speedX = random_speed
                    break

            if flag == 0:
                if counter_x < moves_x:
                    if self.speedX < 0:
                        self.x -= 1
                    else:
                        self.x += 1
                    counter_x += 1
                flag = 1
            elif flag == 1:
                if counter_y < moves_y:
                    if self.speedY < 0:
                        self.y -= 1
                    else:
                        self.y += 1
                    counter_y += 1
                flag = 0
        self.draw(screen)
