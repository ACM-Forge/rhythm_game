import pygame
import os

from .types import *
from .track import *
from .config import *

def showLandings(screen: pygame.Surface, inputs: Input):
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
    if inputs.first != 0:
        screen.blit(leftArrowImage,leftArrowRect)
    if inputs.second != 0:
        screen.blit(downArrowImage,downArrowRect)
    if inputs.third != 0:
        screen.blit(upArrowImage,upArrowRect)
    if inputs.fourth != 0:
        screen.blit(rightArrowImage,rightArrowRect)


def handleInput(event: pygame.event.Event, input_state: Input, clock: pygame.time.Clock):
    if event.key == InputButtons["First"]:
        input_state.first = float(clock.tick())
    if event.key == InputButtons["Second"]:
        input_state.second = float(clock.tick())
    if event.key == InputButtons["Third"]:
        input_state.third = float(clock.tick())
    if event.key == InputButtons["Fourth"]:
        input_state.fourth = float(clock.tick())


def resetInput(event: pygame.event.Event,input_state: Input):
    if event.key == InputButtons["First"]:
        input_state.first = 0
    if event.key == InputButtons["Second"]:
        input_state.second = 0
    if event.key == InputButtons["Third"]:
        input_state.third = 0
    if event.key == InputButtons["Fourth"]:
        input_state.fourth = 0


def main():
    pygame.init()
    canvas = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    input_state = Input()
    dt = 0

    # pygame.mixer.init()
    # print(os.path.join(music,"main.mp3"))
    # pygame.mixer.music.load(
    #     os.path.join(music,"main.mp3")
    # )
    # pygame.mixer.music.play()

    currScene = Scenes.StartMenu
    
    track = Track()
    
    gameOver = False
    while not gameOver:
        canvas.fill(bgcolor)
        dt = clock.tick(60)
        r = pygame.rect.Rect(0,0,100,100)
        r.center = (width/2,height/2)
    
        showLandings(canvas, input_state)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gameOver = True
            if e.type == pygame.KEYDOWN:
                handleInput(e,input_state,clock)
            if e.type == pygame.KEYUP:
                resetInput(e,input_state)
                pass
        pygame.display.flip()


