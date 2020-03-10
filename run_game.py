"""
Starting point
"""

import argparse
import os
import sys
import pygame
from params import SCREEN_WIDTH, SCREEN_HEIGTH, FPS
from scene import TitleScene, InstructionsScene, TransitionScene


def run_game(start_level):
    """ Main logic
    """
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("Get to the red square!")
    clock = pygame.time.Clock()

    if start_level is None:
        starting_scene = TitleScene(screen)
    else:
        starting_scene = TransitionScene(screen, int(start_level)-1)
    active_scene = starting_scene

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not isinstance(
                        active_scene, (InstructionsScene, TransitionScene)
                    ):
                        quit_attempt = True

                elif event.key == pygame.K_F4 and pressed_keys[pygame.K_LALT]:
                    quit_attempt = True

            if quit_attempt:
                pygame.quit()
                sys.exit()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render()

        active_scene = active_scene.next

        # pygame.display.flip()
        clock.tick(FPS)

parser = argparse.ArgumentParser()
parser.add_argument('--level', action='store', dest='start_level',
                    help='Level number to start the game')

results = parser.parse_args()

run_game(results.start_level)
