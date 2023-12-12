import pygame
import copy
import random

# Initialize the pygame module
pygame.init()

# load and set the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Tetris")

W =  10
H = 20
TILE = 45
FPS = 60
FIELD_W = (W * TILE)
FIELD_H = (H * TILE)

screen = pygame.display.set_mode((FIELD_W, FIELD_H))
clock = pygame.time.Clock()

# Dict of all tetris block positions of individual squares within them,
# coordinates used by pygame.Rect rfering to top right corner of the squares.
# Also contians RGB color value for that partitcular block
Tetris_Blocks = {
    'O_block': [[0, 0], [0, -1], [-1, -1], [-1, 0], (3, 223, 252)],
    'I_block': [[0, 0], [0, 1], [0, -1], [0, -2], (3, 223, 252)],
    'S_block': [[0, 0], [-1, 0], [0, -1], [1, -1], (3, 223, 252)],
    'Z_block': [[0, 0], [1, 0], [0, -1], [-1, -1], (3, 223, 252)],
    'L_block': [[0, 0], [-1, 0], [-1, -1], [-1, -2], (3, 223, 252)],
    'J_block': [[0, 0], [-1, 0], [0, -1], [0, -2], (3, 223, 252)],
    'T_block': [[0, 0], [-1, -1], [0, -1], [1, -1], (3, 223, 252)]
}


# Making many rectangles on the screen that cover the window
grid = []
for x in range(W):
    for y in range(H):
        rect = pygame.Rect((x * TILE), (y * TILE), TILE, TILE)
        grid.append(rect)

# Tetris Block Class
class TetrisPiece:
    def __init__(self, block_name):
        self.block_name = block_name
        self.color = Tetris_Blocks[block_name][4]
        self.position = [W // 2, 0]
        self.orientation = Tetris_Blocks[block_name]
    
    def draw(self):
        screen.fill(pygame.Color('black'))

        for i_rect in grid:
            pygame.draw.rect(screen, (100, 100, 100), i_rect, 1)

        for i in range(4):
            x = self.orientation[i][0]
            y = self.orientation[i][1]
            # Position is a list that contains the x and y coordinates of that 
            # current instance of the class and when the block needs to be drawn 
            # again it draws it with the new coordinates and uses the coordinates 
            # from the dictionary.
            block_x = (self.position[0] + x) * TILE
            block_y = (self.position[1] + y) * TILE
            
            block = pygame.Rect(block_x, block_y, TILE, TILE)
            pygame.draw.rect(screen, self.color, block)

    # Methods
    def down(self):
        # Check if moving down would exceed the bottom boundary for any square
        for i in range(4):
            x = Tetris_Blocks[self.block_name][i][0]
            y = Tetris_Blocks[self.block_name][i][1]

            if self.position[1] + y + 1 >= H:
                return
        self.position[1] += 1

    def left(self):
        # Check if moving left would exceed the left boundary for any square
        for i in range(4):
            x = Tetris_Blocks[self.block_name][i][0]
            y = Tetris_Blocks[self.block_name][i][1]

            if self.position[0] + x - 1 < 0:
                return
        self.position[0] -= 1

    def right(self):
        # Check if moving right would exceed the right boundary for any square
        for i in range(4):
            x = Tetris_Blocks[self.block_name][i][0]
            y = Tetris_Blocks[self.block_name][i][1]

            if self.position[0] + x + 1 >= W:
                return
        self.position[0] += 1
    
    def rotate(self):
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
                # Rotation would go beyond the boundaries so revert the changes
                return

        # If the rotated piece is within bounds update the orientation
        self.orientation = original_orientation


while True:
    # Randomly picks a Tetris Block to spawn
    current_piece = TetrisPiece(random.choice(list(Tetris_Blocks.keys())))
    move_timer = pygame.time.get_ticks()

    while True:
        # Add the block to the 2D List that tracks all positions



        # Block is draged down until it reaches the bottom
        


        # Draw the grid using the 'grid' list 
        for i_rect in grid:
            pygame.draw.rect(screen, (40, 40, 40), i_rect, 1)

        # Stop the program when it's closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        # Get the state of all keys
        keys = pygame.key.get_pressed()

        # Continue to make the blocks fall
        move_speed = 320
        if pygame.time.get_ticks() - move_timer > move_speed:
            current_piece.down()
            move_timer = pygame.time.get_ticks()
        
        if keys[pygame.K_DOWN]:
            move_speed = 50
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_piece.down()
                move_timer = pygame.time.get_ticks()

        if keys[pygame.K_LEFT]:
            move_speed = 80
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_piece.left()
                move_timer = pygame.time.get_ticks()

        if keys[pygame.K_RIGHT]:
            move_speed = 80
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_piece.right()
                move_timer = pygame.time.get_ticks()
        
        if keys[pygame.K_UP]:
            move_speed = 90
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_piece.rotate()
                move_timer = pygame.time.get_ticks()
                
        
        # Draw after any change or no change.
        current_piece.draw()


        pygame.display.flip()
        clock.tick(FPS)