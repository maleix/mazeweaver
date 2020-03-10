 ## TODO

#import argparse
#import os
#import sys
#import pygame
#from params import SCREEN_WIDTH, SCREEN_HEIGTH, FPS
#from scene import TitleScene, InstructionsScene, TransitionScene

#def levelmaker():
#    """ Main logic
#    """
#    os.environ["SDL_VIDEO_CENTERED"] = "1"
#    pygame.init()
#    screen = pygame.display.set_mode((SCREEN_WIDTH+150, SCREEN_HEIGTH))
#    pygame.display.set_caption("Level maker")
#    clock = pygame.time.Clock()
#
#    while True:
#        pressed_keys = pygame.key.get_pressed()
#
#        # Event filtering
#        filtered_events = []
#        for event in pygame.event.get():
#            quit_attempt = False
#            if event.type == pygame.QUIT:
#                quit_attempt = True
#            elif event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_ESCAPE:
#                    quit_attempt = True
#                elif event.type == pygame.K_F4 and pressed_keys[pygame.K_LALT]:
#                    quit_attempt = True
#        if quit_attempt:
#            pygame.quit()
#            sys.exit()
#        else:
#            filtered_events.append(event)
#
#        process_input(filtered_events, pressed_keys)
#        update()
#        render()
#        pygame.display.flip()
#        clock.tick(FPS)
#
#def process_input(events, pressed_keys):
#    pass
#
#def update():
#    pass
#
#def render():
#    pass
#
#levelmaker()
