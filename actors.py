"""
Class and logic related to the blocks that the user can move
"""
import pygame

from params import BLOCK_VELOCITY


class Wall:
    """ Wall block rect """

    def __init__(self, pos, width, heigth):
        self.rect = pygame.Rect(pos[0], pos[1], width, heigth)


class UserBlock:
    """ User block class """

    def __init__(self, pos, width, heigth, number_id):
        self.rect = pygame.Rect(pos[0], pos[1], width, heigth)
        self.number_id = number_id  # Must be unique
        self.moving = False
        self.direction = "standing"
        self.new_direction = "standing"

    def move(self, userblocks, walls):
        """ Updates the position of the block """
        if not self.moving and self.new_direction != "standing":
            self.moving = True
            self.direction = self.new_direction

        if self.direction == "left":
            move_x = -BLOCK_VELOCITY
            move_y = 0
        elif self.direction == "right":
            move_x = BLOCK_VELOCITY
            move_y = 0
        elif self.direction == "up":
            move_x = 0
            move_y = -BLOCK_VELOCITY
        elif self.direction == "down":
            move_x = 0
            move_y = BLOCK_VELOCITY
        else:
            move_x = 0
            move_y = 0

        if self.moving:
            self.rect.x += move_x
            self.rect.y += move_y

            ### Collisions
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.moving = False
                    if move_x > 0:
                        # Moving right, Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    elif move_x < 0:
                        # Moving left, Hit the right side of the wall
                        self.rect.left = wall.rect.right
                    elif move_y > 0:
                        # Moving down, Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                    elif move_y < 0:
                        # Moving up, Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom

            for block in userblocks:
                if block is self:
                    # don't check if it collides with itself
                    continue

                if self.rect.colliderect(block.rect):
                    self.moving = False
                    if move_x > 0:
                        # Moving right; Hit the left side of the wall
                        self.rect.right = block.rect.left
                    elif move_x < 0:
                        # Moving left; Hit the right side of the wall
                        self.rect.left = block.rect.right
                    elif move_y > 0:
                        # Moving down; Hit the top side of the wall
                        self.rect.bottom = block.rect.top
                    elif move_y < 0:
                        # Moving up; Hit the bottom side of the wall
                        self.rect.top = block.rect.bottom
            ### end Collisions
