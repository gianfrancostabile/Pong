
import pygame


def load_picture(url):
    picture = None
    try:
        picture = pygame.image.load(url)
        picture = picture.convert()
    except pygame.error:
        pass

    return picture


def charge_pictures():
    ball = load_picture("pictures/ball.png")
    pictures = {
        "ball": ball
    }
    return pictures


PICTURES = charge_pictures()


def get_picture(content):
    global PICTURE
    return PICTURES.get(content)