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

def format_time(timeAmount):
    mil = math.floor(int(timeAmount * 1000 % 1000) / 100)
    second = int(round(timeAmount % 60, 1))


    return f"{second:02d}.{mil}"

def draw_top_bar(window, timePassed, pressed, font, misses):
    pygame.draw.rect(window, "grey", (0,0, window.get_width(), 50))
    timeText = font.render(f"Time: {format_time(timePassed)}", 1, "black")

    speed = round(pressed / timePassed, 1)
    speedText = font.render(f"Speed: {speed} t/s", 1, "black")
    pressedText = font.render(f"Hits: {pressed}", 1, "black")

    window.blit(timeText, (5,5))
    window.blit(speedText, (200,5))
    window.blit(pressedText, (450,5))




def main():
    # Sets things
    pygame.init()
    pygame.font.init()
    resolution = (800, 600)
    pygame.display.set_caption("Aim Trainer")
    clock = pygame.time.Clock()
    dt = 0
    frames = 12
    backColor = pygame.Color(0, 0, 0)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    running = True
    start = time.time()
    padding = 30

    font = pygame.font.SysFont("comicsans", 24)
    
    # Collision Variables
    targetPressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    # Makes sure there is target when started
    target = Target(random.randrange(0 + padding, screen.get_width() - padding), random.randrange(0 + padding + 50, screen.get_height() - padding))
    target.draw(screen)

    # Game
    while running:
        # Loop
        mousePos = pygame.mouse.get_pos()
        click = False
        timePassed = time.time() - start
        
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
            target = Target(random.randrange(0 + padding, screen.get_width() - padding), random.randrange(0 + padding + 50, screen.get_height() - padding))
            targetPressed += 1
            screen.fill(backColor)
            target.draw(screen)

        # Render/Display
        draw_top_bar(screen, timePassed, targetPressed, font, misses)
        pygame.display.flip()
        clock.tick(frames)
    pygame.quit()

if __name__ == "__main__":
    main()