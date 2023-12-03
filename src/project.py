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

def draw_top_bar(window, timer, timePassed, pressed, font):
    pygame.draw.rect(window, "grey", (0,0, window.get_width(), 50))
    timeText = font.render(f"Time: {format_time(timer)}", 1, "black")

    speed = round(pressed / timePassed, 1)
    speedText = font.render(f"Speed: {speed} t/s", 1, "black")
    pressedText = font.render(f"Hits: {pressed}", 1, "black")

    window.blit(timeText, (middle(timeText),5))
    window.blit(speedText, (100,5))
    window.blit(pressedText, (600,5))

def end(window, timePassed, pressed, clicks, font):
    window.fill(pygame.Color(0, 0, 0))

    timeText = font.render(f"Time: {format_time(timePassed)}", 1, "white")

    speed = round(pressed / timePassed, 1)
    speedText = font.render(f"Speed: {speed} t/s", 1, "white")
    pressedText = font.render(f"Hits: {pressed}", 1, "white")
    accuracy = round(pressed / clicks * 100, 1)
    accuracyText = font.render(f"Accuracy: {accuracy}%", 1, "white")

    window.blit(timeText, (middle(timeText),100))
    window.blit(speedText, (middle(speedText),200))
    window.blit(pressedText, (middle(pressedText),300))
    window.blit(accuracyText, (middle(accuracyText),400))

    filename = "score.txt"
    try:
        file = open(filename, "r")
        print("File opened for reading")
        print(file.readlines())
    except FileNotFoundError:
        file = open(filename, "w")
        print(f"File not found. Creating a new {filename} instead")
    finally:
        file.close
        print("File closed.")

    with open(filename, "a") as file:
        file.writelines(str(pressed) + "\n")

    with open(filename, "r") as file:
        leaderboard = file.read().splitlines()
    list = []
    for number in leaderboard:
        list.append(int(number))
    list.sort(reverse=True)

    while len(list) > 3:
        list.pop()

    with open(filename, "w") as file:
        file.writelines([str(x) + '\n' for x in list])

    leaderboardText = font.render(f"Leaderboard:", 1, "white")

    if len(list) < 2:
        firstText = font.render(f"First: {list[0]}", 1, "white")
        window.blit(firstText, (50, 150))
    elif len(list) < 3:
        firstText = font.render(f"First: {list[0]}", 1, "white")
        window.blit(firstText, (50, 150))
        secondText = font.render(f"Second: {list[1]}", 1, "white")
        window.blit(secondText, (50, 200))
    else:
        firstText = font.render(f"First: {list[0]}", 1, "white")
        window.blit(firstText, (50, 150))
        secondText = font.render(f"Second: {list[1]}", 1, "white")
        window.blit(secondText, (50, 200))
        thirdText = font.render(f"Third: {list[2]}", 1, "white")
        window.blit(thirdText, (50, 250))

    window.blit(leaderboardText, (50, 100))
    

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def middle( surface):
    return 800 / 2 - surface.get_width() / 2

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
    startTime = 30

    font = pygame.font.SysFont("comicsans", 24)
    
    # Collision Variables
    targetPressed = 0
    clicks = 0
    misses = 0
    
    # Makes sure there is target when started
    target = Target(random.randrange(0 + padding, screen.get_width() - padding), random.randrange(0 + padding + 50, screen.get_height() - padding))
    target.draw(screen)

    # Game
    while running:
        # Loop
        mousePos = pygame.mouse.get_pos()
        click = False
        timePassed = time.time() - start
        timeLeft = startTime - timePassed 
        
        
        for event in pygame.event.get():

            # When the game is closed
            if event.type == pygame.QUIT:
                running = False
            
            # When the mouse is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
        # Logic
        if int(round(timePassed % 60, 1)) >= startTime:
            end(screen, timePassed, targetPressed, clicks, font)
        # Collision Detection
        if click and target.collide(mousePos[0], mousePos[1]):
            target = Target(random.randrange(0 + padding, screen.get_width() - padding), random.randrange(0 + padding + 50, screen.get_height() - padding))
            targetPressed += 1
            screen.fill(backColor)
            target.draw(screen)

        # Render/Display
        draw_top_bar(screen, timeLeft, timePassed, targetPressed, font)
        pygame.display.flip()
        clock.tick(frames)
    pygame.quit()

if __name__ == "__main__":
    main()