import pygame

def get_sprite(name):
    """ Given a color name, returns its RGB value """
    switcher = {
        "wall": "resources/images/wall_neon.png",
        "userblock_selected": pygame.image.load("resources"),
        "gray": (80, 80, 80),
        "red": (255, 0, 0),
        "darkred": (170, 0, 0),
        "green": (0, 255, 0),
        "blue": (51, 204, 255),
        "lightgreen": (37, 255, 17),
        "yellow": (255, 255, 0),
    }
    return switcher.get(name, "Non registered colour")
