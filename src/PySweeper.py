import pygame

class PySweeper:
    
    def __init__(self):
        pygame.init()
        
        # Screen settings
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("PySweeper")
        
        # Running state
        self.running = True
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def update(self):
        pass
    
    def draw(self):
        
        # Dark gray background
        self.screen.fill((30,30,30))
        pygame.display.flip() # Update Display
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        
        pygame.quit()
        
if __name__ == "__main__":
    game = PySweeper()
    game.run()