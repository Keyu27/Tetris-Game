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
TILE = 35
FPS = 60
FIELD_W = (W * TILE)
FIELD_H = (H * TILE)

screen = pygame.display.set_mode((650, FIELD_H))
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

        

# Create surfaces for background and foreground
background_surface = pygame.Surface((FIELD_W, FIELD_H))
background_surface.fill((0, 0, 0))  # Fill background with black
for i_rect in grid:
    pygame.draw.rect(background_surface, (40, 40, 40), i_rect, 1)

foreground_surface = pygame.Surface((FIELD_W, FIELD_H), pygame.SRCALPHA)

fallen_blocks = []


while True:
    # Randomly picks a Tetris Block to spawn
    current_block = TetrisPiece(random.choice(list(Tetris_Blocks.keys())))
    move_timer = pygame.time.get_ticks()

    while True:
        # Stop the program when it's closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        # Get the state of all keys
        keys = pygame.key.get_pressed()

        # Continue to make the blocks fall
        move_speed = 320
        if pygame.time.get_ticks() - move_timer > move_speed:
            # This moves the block down and once it sees that 
            # it can't, it breaks the inner while loop to generate anouther block
            if current_block.down(foreground_surface) == False:
                #Appends current_block to fallen_blocks list
                fallen_blocks.append(current_block)
                break
            move_timer = pygame.time.get_ticks()
        
        if keys[pygame.K_DOWN]:
            move_speed = 50
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_block.down(foreground_surface)
                move_timer = pygame.time.get_ticks()

        if keys[pygame.K_LEFT]:
            move_speed = 80
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_block.left(foreground_surface)
                move_timer = pygame.time.get_ticks()

        if keys[pygame.K_RIGHT]:
            move_speed = 80
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_block.right(foreground_surface)
                move_timer = pygame.time.get_ticks()
        
        if keys[pygame.K_UP]:
            move_speed = 90
            if pygame.time.get_ticks() - move_timer > move_speed:
                current_block.rotate(foreground_surface)
                move_timer = pygame.time.get_ticks()
                
        

        # Draw the background
        screen.blit(background_surface, (0, 0))

        # Draw the current falling piece
        current_block.draw(foreground_surface)

        # Draw the fallen pieces
        for piece in fallen_blocks:
            piece.draw(foreground_surface)

        # Draw the foreground on top of the background
        screen.blit(foreground_surface, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)