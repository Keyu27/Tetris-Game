W =  10
H = 20
TILE = 35
FPS = 60
FIELD_W = (W * TILE)
FIELD_H = (H * TILE)

fallen_blocks = []

# Dict of all tetris block positions of individual squares within them,
# coordinates used by pygame.Rect rfering to top right corner of the squares.
# Also contians RGB color value for that partitcular block
Tetris_Blocks = {
    'O_block': [[0, 0], [0, -1], [-1, -1], [-1, 0], (255, 255, 0)],  # Yellow
    'I_block': [[0, 0], [0, 1], [0, -1], [0, -2], (3, 223, 252)],    # Light blue
    'S_block': [[0, 0], [-1, 0], [0, -1], [1, -1], (0, 255, 0)],       # Green
    'Z_block': [[0, 0], [1, 0], [0, -1], [-1, -1], (255, 0, 0)],       # Red
    'L_block': [[0, 0], [-1, 0], [-1, -1], [-1, -2], (255, 165, 0)],    # Orange
    'J_block': [[0, 0], [-1, 0], [0, -1], [0, -2], (0, 0, 255)],        # Blue
    'T_block': [[0, 0], [-1, -1], [0, -1], [1, -1], (128, 0, 128)]     # Purple
}