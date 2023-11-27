import random
import pygame

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
        # Render/Display
        screen.fill(backColor)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()