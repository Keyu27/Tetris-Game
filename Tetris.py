import pygame
import copy
from settings import *

# Tetris Block Class
class TetrisPiece:
    def __init__(self, block_name):
        self.block_name = block_name
        self.color = Tetris_Blocks[block_name][4]
        self.position = [W // 2, 0]
        self.orientation = Tetris_Blocks[block_name]
        self.old_position = None

    

    def undraw(self, surface):
        if self.old_position:
            for i in range(4):
                x = self.old_position[0] + self.orientation[i][0]
                y = self.old_position[1] + self.orientation[i][1]
                prev_block_x = (x * TILE) + 1
                prev_block_y = (y * TILE) + 1

                prev_block = pygame.Rect(prev_block_x, prev_block_y, TILE - 2, TILE - 2)
                pygame.draw.rect(surface, (0, 0, 0), prev_block)


    def draw(self, surface):
        #self.undraw(surface)   #undraw the old positions
        for i in range(4):
            x = self.orientation[i][0]
            y = self.orientation[i][1]
            block_x = ((self.position[0] + x) * TILE) + 1
            block_y = ((self.position[1] + y) * TILE) + 1

            block = pygame.Rect(block_x, block_y, TILE-2, TILE-2)
            pygame.draw.rect(surface, self.color, block)

    def down(self, surface):
        self.old_position = self.position.copy()  # Store the old position

        # Check if moving down would exceed the bottom boundary for any square
        for i in range(4):
            x = self.orientation[i][0]
            y = self.orientation[i][1]

            if self.position[1] + y + 1 >= H:
                return False

        self.position[1] += 1
        self.undraw(surface)  # undraw the old positions
        return True


    def left(self, surface):
        self.old_position = self.position.copy()  # Store the old position
        # Check if moving left would exceed the left boundary for any square
        for i in range(4):
            x = self.orientation[i][0]
            y = self.orientation[i][1]

            if self.position[0] + x - 1 < 0:
                return
        self.undraw(surface) #undraw the old positions
        self.position[0] -= 1

    def right(self, surface):
        self.old_position = self.position.copy()  # Store the old position
        # Check if moving right would exceed the right boundary for any square
        for i in range(4):
            x = self.orientation[i][0]
            y = self.orientation[i][1]

            if self.position[0] + x + 1 >= W:
                return
        self.undraw(surface) #undraw the old positions
        self.position[0] += 1
    
    def rotate(self, surface):
        # If 'O_block' then do nothing
        if self.block_name == 'O_block':
            return

        original_orientation = copy.deepcopy(self.orientation)

        # Apply a 90-degree clockwise rotation to the piece's orientation
        for i in range(4):
            x = original_orientation[i][0]
            y = original_orientation[i][1]
            original_orientation[i][0] = -y
            original_orientation[i][1] = x

        # Check if the rotated piece would be within the bounds
        for i in range(4):
            x = original_orientation[i][0]
            y = original_orientation[i][1]

            if (
                self.position[0] + x < 0
                or self.position[0] + x >= W
                or self.position[1] + y >= H
            ):

                return

        self.old_position = self.position.copy()  # Store the old position
        self.undraw(surface) #undraw the old positions

        # If the rotated piece is within bounds, update the orientation
        self.orientation = original_orientation
