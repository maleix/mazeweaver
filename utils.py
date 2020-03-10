"""
Useful stuff to be used by other files
"""
import os
import pygame
from actors import UserBlock, Wall
from params import SCREEN_WIDTH, SCREEN_HEIGTH, MUSIC_VOLUME, SOUND_VOLUME


def rgb(name):
    """ Given a color name, returns its RGB value """
    switcher = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "gray": (80, 80, 80),
        "darkgray": (50, 50, 50),
        "red": (255, 0, 0),
        "darkred": (170, 0, 0),
        "green": (0, 255, 0),
        "blue": (51, 204, 255),
        "lightgreen": (37, 255, 17),
        "yellow": (255, 255, 0),
    }
    return switcher.get(name, "Non registered colour")


def draw_grid(screen, horizontal_lines, vertical_lines, color):
    """ Draws lines to make a grid """
    horizontal_block = int(SCREEN_WIDTH / horizontal_lines)
    vertical_block = int(SCREEN_HEIGTH / vertical_lines)

    for i in range(0, SCREEN_WIDTH, horizontal_block):
        pygame.draw.line(screen, rgb(color), (i, 0), (i, SCREEN_HEIGTH))
    for i in range(0, SCREEN_HEIGTH, vertical_block):
        pygame.draw.line(screen, rgb(color), (0, i), (SCREEN_WIDTH, i))


def get_block_size(level):
    """ Returns the size of a screen block """
    width = int(SCREEN_WIDTH / len(level[0]))
    heigth = int(SCREEN_HEIGTH / len(level))
    return width, heigth


def load_level(level):
    """ Given a concrete level, it loads its sprites and returns them """
    walls = []
    userblocks = []
    x_pos = y_pos = 0

    block_width, block_heigth = get_block_size(level)

    for row in level:
        for col in row:
            if col == "W":
                walls.append(Wall((x_pos, y_pos), block_width, block_heigth))
            elif col == "E":
                end_rect = pygame.Rect(x_pos, y_pos, block_width, block_heigth)
            elif col.isdigit():
                userblocks.append(
                    UserBlock((x_pos, y_pos), block_width, block_heigth, col)
                )
            x_pos += block_width
        y_pos += block_heigth
        x_pos = 0

    return walls, end_rect, userblocks


_SOUND_LIBRARY = {}


def play_sound(path):
    """ Plays a sound once """
    # global _SOUND_LIBRARY
    sound = _SOUND_LIBRARY.get(path)
    if sound is None:
        canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _SOUND_LIBRARY[path] = sound
    sound.set_volume(SOUND_VOLUME)
    sound.play()


def play_song(path):
    """ Plays a song indefinately until another song is played """
    canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
    pygame.mixer.music.load(canonicalized_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)


def queue_song(path):
    """ Queues a song to be played after the current one finishes """
    canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
    pygame.mixer.music.queue(canonicalized_path)
