import random
import pygame
import time

class Target():

    def __init__(self, pos=(0,0), size=30):
        self.pos = pos
        self.size = size

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color("cadetblue1"), self.pos, self.size)
        pygame.draw.circle(surface, pygame.Color("white"), self.pos, self.size * 0.8)
        pygame.draw.circle(surface, pygame.Color("cadetblue1"), self.pos, self.size * 0.6)
        pygame.draw.circle(surface, pygame.Color("white"), self.pos, self.size * 0.4)

    def collide (self, x, y):

def on_mouse_down(event):
  print("Mouse down at", event.pos)

def main():
    pygame.init()
    resolution = (800, 600)
    pygame.display.set_caption("Aim Trainer")
    clock = pygame.time.Clock()
    dt = 0
    frames = 12
    backColor = pygame.Color(0, 0, 0)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    running = True

    targetPressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    while running:
        # Loop
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
                on_mouse_down(event)
                screen.fill(backColor)
                target.draw(screen)
        # Logic
        target = Target((random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height())))
        # Render/Display
        
        pygame.display.flip()
        clock.tick(frames)
    pygame.quit()

if __name__ == "__main__":
    main()