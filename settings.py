W =  10
H = 20
TILE = 35
FPS = 60
FIELD_W = (W * TILE)
FIELD_H = (H * TILE)

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