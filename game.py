""" Gameplay logic
"""

import copy
import pygame

from actors import Wall
from params import SCREEN_HEIGTH
from utils import (
    rgb,
    get_block_size,
    load_level,
    play_sound,
    draw_grid,
)
from levels import LEVELS, LEVEL_TIMER
from scene import SceneBase, TransitionScene, WinScene

class GameScene(SceneBase):
    """ Gameplay """

    def __init__(self, screen, level):
        SceneBase.__init__(self, screen)
        self.level = level
        self.labyrinth = LEVELS[level]
        self.max_time = LEVEL_TIMER[level]
        self.start_ticks = pygame.time.get_ticks()  # starter tick
        self.seconds = 0
        self.seconds_win = None
        self.seconds_left = int(self.max_time - self.seconds)
        self.beep_at_seconds_left = 5
        self.walls, self.end_rect, self.blocks = load_level(self.labyrinth)
        self.blocks.sort(key=lambda x: x.number_id)
        # old_blocks will store the previous position of blocks before moving
        # so we can know which parts of the screen render we want to refresh
        self.old_blocks = copy.deepcopy(self.blocks)
        self.selected_block = 0  # Which is block number 1
        self.block_size = get_block_size(self.labyrinth)
        self.rendered_once = False

        ### Asset preloading
        self.number_font = pygame.font.Font("resources/fonts/Retro.ttf", 35)
        self.timer_font = pygame.font.Font("resources/fonts/Retro.ttf", 40)

        self.end_image = pygame.image.load("resources/images/end_block2.png").convert()
        self.end_image = pygame.transform.scale(self.end_image, (self.block_size))

        self.wall_image = pygame.image.load("resources/images/wall_neon.png").convert()
        self.wall_image = pygame.transform.scale(self.wall_image, (self.block_size))

        # UserBlock selected
        self.block_standing = pygame.image.load(
            "resources/images/block_selected_static.png"
        ).convert()
        self.block_standing = pygame.transform.scale(
            self.block_standing, (self.block_size)
        )

        self.block_moving = pygame.image.load(
            "resources/images/block_selected_direction.png"
        ).convert()

        self.block_up = pygame.transform.scale(self.block_moving, (self.block_size))

        self.block_left = pygame.transform.rotate(self.block_moving, 90)
        self.block_left = pygame.transform.scale(self.block_left, (self.block_size))

        self.block_down = pygame.transform.rotate(self.block_moving, 180)
        self.block_down = pygame.transform.scale(self.block_down, (self.block_size))

        self.block_right = pygame.transform.rotate(self.block_moving, 270)
        self.block_right = pygame.transform.scale(self.block_right, (self.block_size))

        # UserBlock unselected
        self.block_unselected_standing = pygame.image.load(
            "resources/images/block_unselected_static.png"
        ).convert()
        self.block_unselected_standing = pygame.transform.scale(
            self.block_unselected_standing, (self.block_size)
        )

        self.block_unselected_moving = pygame.image.load(
            "resources/images/block_unselected_direction.png"
        ).convert()

        self.block_unselected_up = pygame.transform.scale(
            self.block_unselected_moving, (self.block_size)
        )

        self.block_unselected_left = pygame.transform.rotate(
            self.block_unselected_moving, 90
        )
        self.block_unselected_left = pygame.transform.scale(
            self.block_unselected_left, (self.block_size)
        )

        self.block_unselected_down = pygame.transform.rotate(
            self.block_unselected_moving, 180
        )
        self.block_unselected_down = pygame.transform.scale(
            self.block_unselected_down, (self.block_size)
        )

        self.block_unselected_right = pygame.transform.rotate(
            self.block_unselected_moving, 270
        )
        self.block_unselected_right = pygame.transform.scale(
            self.block_unselected_right, (self.block_size)
        )
        ###

    def process_input(self, events, pressed_keys):

        if pressed_keys[pygame.K_r]:
            self.switch_to_scene(TransitionScene(self.screen, self.level))

        if pressed_keys[pygame.K_1]:
            self.selected_block = 0
        elif pressed_keys[pygame.K_2] and len(self.blocks) > 1:
            self.selected_block = 1
        elif pressed_keys[pygame.K_3] and len(self.blocks) > 2:
            self.selected_block = 2

        if pressed_keys[pygame.K_LEFT]:
            self.blocks[self.selected_block].new_direction = "left"
        elif pressed_keys[pygame.K_RIGHT]:
            self.blocks[self.selected_block].new_direction = "right"
        elif pressed_keys[pygame.K_UP]:
            self.blocks[self.selected_block].new_direction = "up"
        elif pressed_keys[pygame.K_DOWN]:
            self.blocks[self.selected_block].new_direction = "down"

    def update(self):
        # make a copy of the list and its objects before moving
        self.old_blocks = copy.deepcopy(self.blocks)


        for block in self.blocks:
            block.move(self.blocks, self.walls)
            if block.rect.colliderect(self.end_rect):
                # Wait a bit before switching to new level
                # just to make the collision with the end blockless rude
                if self.seconds_win is None:
                    self.seconds_win = pygame.time.get_ticks()  # starter tick
                else:
                    if (pygame.time.get_ticks() - self.seconds_win) / 1000 > 0.2:
                        if len(LEVELS) > self.level + 1:
                            self.switch_to_scene(
                                TransitionScene(self.screen, self.level + 1)
                            )
                        else:
                            self.switch_to_scene(WinScene(self.screen))
                            # raise SystemExit("You have passed all levels!")

        # calculate how many seconds have passed since the scene started
        self.seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        if self.seconds > self.max_time:
            # if time runs out, reset to the same level
            self.switch_to_scene(TransitionScene(self.screen, self.level))

        self.seconds_left = int(self.max_time - self.seconds)
        if self.seconds_left == self.beep_at_seconds_left:
            play_sound("resources/sounds/beep.wav")
            self.beep_at_seconds_left -= 1

    def render_once(self):
        self.screen.fill(rgb("black"))
        for wall in self.walls:
            self.screen.blit(self.wall_image, wall.rect)
        self.screen.blit(self.end_image, self.end_rect)
        draw_grid(self.screen, len(self.labyrinth[0]), len(self.labyrinth), "darkgray")

        pygame.display.update()

    def render(self):
        if not self.rendered_once:
            self.render_once()
            self.rendered_once = True

        rects_to_draw = []

        for block in self.old_blocks:
            rects_to_draw.append(
                pygame.draw.rect(self.screen, rgb("black"), block.rect)
            )

        draw_grid(self.screen, len(self.labyrinth[0]), len(self.labyrinth), "darkgray")

        for i, block in enumerate(self.blocks):
            if i == self.selected_block:
                if block.new_direction == "left":
                    selected_rect = self.screen.blit(self.block_left, block.rect)
                elif block.new_direction == "right":
                    selected_rect = self.screen.blit(self.block_right, block.rect)
                elif block.new_direction == "down":
                    selected_rect = self.screen.blit(self.block_down, block.rect)
                elif block.new_direction == "up":
                    selected_rect = self.screen.blit(self.block_up, block.rect)
                else:
                    selected_rect = self.screen.blit(self.block_standing, block.rect)
            else:
                if block.new_direction == "left":
                    selected_rect = self.screen.blit(
                        self.block_unselected_left, block.rect
                    )
                elif block.new_direction == "right":
                    selected_rect = self.screen.blit(
                        self.block_unselected_right, block.rect
                    )
                elif block.new_direction == "down":
                    selected_rect = self.screen.blit(
                        self.block_unselected_down, block.rect
                    )
                elif block.new_direction == "up":
                    selected_rect = self.screen.blit(
                        self.block_unselected_up, block.rect
                    )
                else:
                    selected_rect = self.screen.blit(
                        self.block_unselected_standing, block.rect
                    )

            rects_to_draw.append(selected_rect)

            number = self.number_font.render(str(block.number_id), 0, rgb("lightgreen"))
            # This rect should be inside the Userblock rect
            # so there is no need to put it in the rects to draw
            self.screen.blit(
                number,
                (
                    block.rect.x + (self.block_size[0] / 2 - number.get_width() / 2),
                    block.rect.y + (self.block_size[1] / 2 - number.get_height() / 2),
                ),
            )

        bottom_left_wall = Wall(
            (0, SCREEN_HEIGTH - self.block_size[1]),
            self.block_size[0],
            self.block_size[1],
        )
        rects_to_draw.append(self.screen.blit(self.wall_image, bottom_left_wall.rect))

        timer = self.timer_font.render(str(self.seconds_left), 0, rgb("yellow"))
        rects_to_draw.append(
            self.screen.blit(
                timer,
                (
                    self.block_size[0] / 2 - (timer.get_width() / 2),
                    SCREEN_HEIGTH - self.block_size[1] + timer.get_height() / 2,
                ),
            )
        )

        pygame.display.update(rects_to_draw)
