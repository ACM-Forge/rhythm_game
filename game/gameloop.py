import pygame
import os

from .config import *
from .scenes import Scenes as sc

def showLandings(screen: pygame.Surface):
    global width, height, sprites
    iconSize = (100,100)
    rightArrowImage = pygame.transform.scale(
        pygame.image.load(os.path.join(sprites,"arrow.png")),
        iconSize)
    leftArrowImage = pygame.transform.rotate(rightArrowImage,180)
    downArrowImage = pygame.transform.rotate(rightArrowImage,90)
    upArrowImage = pygame.transform.rotate(rightArrowImage,270)

    center = (width / 2,9 * height / 10)
    spacing = 1.5
    leftArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    leftArrowRect.center =          (center[0] - 150 * spacing,center[1])
    downArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    downArrowRect.center =          (center[0] - 50 * spacing,center[1])
    upArrowRect =   pygame.rect.Rect(center[0],center[1],iconSize[0],iconSize[1])
    upArrowRect.center =            (center[0] + 50 * spacing,center[1])
    rightArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    rightArrowRect.center =         (center[0] + 150 * spacing,center[1])

    screen.blit(leftArrowImage,leftArrowRect)
    screen.blit(downArrowImage,downArrowRect)
    screen.blit(upArrowImage,upArrowRect)
    screen.blit(rightArrowImage,rightArrowRect)


def main():
    
    pygame.init()
    canvas = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    pygame.mixer.init()

    pygame.mixer.music.load(
        os.path.join(music,"main.mp3")
    )

    pygame.mixer.music.play()

    currScene: sc = sc.StartMenu


    gameOver = False
    while not gameOver:
        canvas.fill(bgcolor)
        dt = clock.tick(60)
        r = pygame.rect.Rect(0,0,100,100)
        r.center = (width/2,height/2)
        
        pygame.draw.rect(canvas,(255,255,255),r)

        showLandings(canvas)


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gameOver = True
        pygame.display.flip()


