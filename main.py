import pygame
import random
from TetrisClass import TetrisPiece
from settings import W, H, TILE, FPS, FIELD_W, FIELD_H, Tetris_Blocks


# Initialize the pygame module
pygame.init()

# load and set the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Tetris")


screen = pygame.display.set_mode((650, FIELD_H))
clock = pygame.time.Clock()



# Making many rectangles on the screen that cover the window
grid = []
for x in range(W):
    for y in range(H):
        rect = pygame.Rect((x * TILE), (y * TILE), TILE, TILE)
        grid.append(rect)
        

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