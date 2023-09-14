import pygame
import math
pygame.init()


width, height = 1000, 1000
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


while True:
    # Set the tickrate of the game
    clock.tick(60)
    # Fill the screen with a background color
    screen.fill((51,51,51))
    
    # Draw several shapes onto the screen
    pygame.draw.ellipse(screen,(50,150,255), (width / 5, height / 4,width / 5,height / 5))
    pygame.draw.ellipse(screen,(50,150,255), ((3 * width) / 5,height / 4,width / 5, height / 5))
    pygame.draw.arc(screen,(50,150,255),(width / 4, height / 3,width / 2, height / 2),math.pi,0, int((width + height) / 20))
    
    # Handle all events which could occur during the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    # Clear the screen for the next draw cycle
    pygame.display.flip()
