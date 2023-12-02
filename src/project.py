import random
import pygame
import time
import math

class Target():

    # Defines Target
    def __init__(self, x, y, size=30):
        self.x = x
        self.y = y
        self.size = size

    # Creates what the target looks like
    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color("cadetblue1"), (self.x, self.y), self.size)
        pygame.draw.circle(surface, pygame.Color("white"), (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(surface, pygame.Color("cadetblue1"), (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(surface, pygame.Color("white"), (self.x, self.y), self.size * 0.4)

    # Collision Math
    def collide (self, x, y):
        dis = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        return dis <= self.size


def main():
    # Sets things
    pygame.init()
    resolution = (800, 600)
    pygame.display.set_caption("Aim Trainer")
    clock = pygame.time.Clock()
    dt = 0
    frames = 12
    backColor = pygame.Color(0, 0, 0)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    running = True
    
    # Collision Variables
    targetPressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    # Makes sure there is target when started
    target = Target(random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height()))
    target.draw(screen)

    # Game
    while running:
        # Loop
        mousePos = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():

            # When the game is closed
            if event.type == pygame.QUIT:
                running = False
            
            # When the mouse is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
        # Logic

        # Collision Detection
        if click and target.collide(mousePos[0], mousePos[1]):
            target = Target(random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height()))
            targetPressed += 1
            screen.fill(backColor)
            target.draw(screen)

        # Render/Display
        pygame.display.flip()
        clock.tick(frames)
    pygame.quit()

if __name__ == "__main__":
    main()