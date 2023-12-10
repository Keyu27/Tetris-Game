import pygame

# initialize the pygame module
pygame.init()

# load and set the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Tetris")

W =  10
H = 20
TILE = 45
FPS = 60
GAME_RES = (W * TILE), (H * TILE)

screen = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

# making many rectangles on the screen that cover the window
grid = []
for x in range(W):
    for y in range(H):
        rect = pygame.Rect((x * TILE), (y * TILE), TILE, TILE)
        grid.append(rect)


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

class TetrisPiece: 
    def __init__(self, block_name):
        self.block_name = block_name
        self.color = Tetris_Blocks[block_name][4]
        self.position = [W // 2, 0]
    
    def draw(self):
        screen.fill(pygame.Color('black'))

        for i_rect in grid:
            pygame.draw.rect(screen, (40, 40, 40), i_rect, 1)

        for i in range(4):
            x, y = Tetris_Blocks[self.block_name][i][:2]
            rect = pygame.Rect(((self.position[0] + x) * TILE), ((self.position[1] + y) * TILE), TILE, TILE)
            pygame.draw.rect(screen, self.color, rect)

    #move methods
    def down(self):
        self.position[1] += 1
    
    def Left(self):
        self.position[0] -= 1

    def Right(self):
        self.position[0] += 1




current_piece = TetrisPiece('I_block')
move_timer = pygame.time.get_ticks()


while True:
    screen.fill(pygame.Color('black'))

    #draw the grid using the 'grid' list
    for i_rect in grid:
        pygame.draw.rect(screen, (40, 40, 40), i_rect, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    # Get the state of all keys
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_DOWN]:
        move_speed = 50
        if pygame.time.get_ticks() - move_timer > move_speed:
            current_piece.down()
            move_timer = pygame.time.get_ticks()


    if keys[pygame.K_LEFT]:
        move_speed = 80
        if pygame.time.get_ticks() - move_timer > move_speed:
            current_piece.Left()
            move_timer = pygame.time.get_ticks()

    if keys[pygame.K_RIGHT]:
        move_speed = 80
        if pygame.time.get_ticks() - move_timer > move_speed:
            current_piece.Right()
            move_timer = pygame.time.get_ticks()
    
    
    current_piece.draw()
    

    pygame.display.flip()
    clock.tick(FPS)