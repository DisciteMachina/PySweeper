import pygame
import random

class PySweeper:
    def __init__(self):
        pygame.init()
        
        # Screen settings
        self.window_size = 512
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption("PySweeper")
        
        # Define grid size
        self.rows = 16
        self.cols = 16
        
        self.cell_size = self.window_size // self.rows
        
        # Grid line color
        self.line_color = (255, 255, 255)
        
        # Initalize the grid
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Num of mines
        self.num_mines = 40
        
        # Add the mines
        self.generate_mines()
        
        # Run the game
        self.run_game()
        
    def generate_mines(self):
        mines = set()
        
        while len(mines) < self.num_mines:
            # pick a random col and row 
            # -1 because of python 0 indexing 
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            mines.add((row, col))
            
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in mines:
                    self.grid[row][col] = "M" # Mine
                else:
                    self.grid[row][col] = 0 # Empty
        
    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.line_color, rect, 1)  # Grid line
                if self.grid[row][col] == "M":
                    pygame.draw.circle(self.screen, (255, 0, 0), rect.center, 5)
                    
    def run_game(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            
            # Draw grid
            self.draw_grid()
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        col = pos[0] // self.cell_size
                        row = pos[1] // self.cell_size
                        print(f"Cell clicked: ({row}, {col})")
            pygame.display.flip()
        pygame.quit()
            
game = PySweeper()