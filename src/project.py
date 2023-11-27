import random
import pygame

class Target():

    def __init__(self, pos=(0,0), size=15):
        self.pos = pos
        self.size = size

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color("cadetblue1"), self.pos, self.size)
        pygame.draw.circle(surface, pygame.Color("white"), self.pos, self.size * 0.8)
        pygame.draw.circle(surface, pygame.Color("cadetblue1"), self.pos, self.size * 0.6)
        pygame.draw.circle(surface, pygame.Color("white"), self.pos, self.size * 0.4)

def on_mouse_down(event):
  print("Mouse down at", event.pos)

def main():
    pygame.init()
    resolution = (800, 600)
    frames = 12
    backColor = pygame.Color(0, 0, 0)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    running = True
    
    while running:
        # Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                on_mouse_down(event)
        # Logic
        target = Target((random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height())))
        # Render/Display
        screen.fill(backColor)
        target.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()