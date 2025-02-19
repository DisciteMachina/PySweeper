import pygame
import random

class PySweeper:
    
    
    def __init__(self, width=800, height=640, grid_width=10, grid_height=10, num_mines=15):
        pygame.init()
        
        # Screen settings
        self.WIDTH, self.HEIGHT = width, height
        self.grid_width, self.grid_height = grid_width, grid_height
        self.num_mines = num_mines
        self.cell_size = self.WIDTH // self.grid_width 
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("PySweeper")
        
        # Initialize grid and mine positions
        self.grid = [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.mines = set()
        self.generate_mines()
        
        # Running state
        self.running = True
        
    def generate_mines(self):
        placed = 0
        while placed < self.num_mines:
            row = random.randint(0, self.grid_height - 1)
            col = random.randint(0, self.grid_width - 1)
            if (row, col) not in self.mines:
                self.mines.add((row, col))
                placed +=1
    
    def draw_grid(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                
                # Position and size of each cell
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                
                # Cell color
                pygame.draw.rect(self.screen, (200, 200, 200), rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
                
                # If cell is a mine
                if (row, col) in self.mines:
                    pygame.draw.circle(self.screen, (255, 0, 0), rect.center, self.cell_size // 4)
                                
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // self.cell_size
                col = x // self.cell_size
                self.handle_click(row, col)
                
    def handle_click(self, row, col):
        if (row, col) in self.mines:
            self.running = False
        else:
            pass
                
    def update(self):
        pass
    
    def draw(self):
        # White background
        self.screen.fill((255, 255, 255))
        self.draw_grid()
        pygame.display.flip() 

        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        
        pygame.quit()
        
if __name__ == "__main__":
    game = PySweeper()
    game.run()