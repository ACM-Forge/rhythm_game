import pygame
import os

from dataclasses import dataclass, field
from enum import Enum, auto
from .config import *

class Landing(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super().__init__()
        self.size = size
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join(sprites,"arrow.png")),
            self.size,
        )
        colorImage = pygame.Surface(self.size).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

def loadLandings() -> []:
    rightArrow = Landing((255,0,0), iconSize)
    leftArrow = Landing((0,0,255) , iconSize)
    downArrow = Landing((0,255,0) , iconSize)
    upArrow = Landing((255,255,0) , iconSize)

    leftArrow.image = pygame.transform.rotate(leftArrow.image, 180)
    downArrow.image = pygame.transform.rotate(downArrow.image,90)
    upArrow.image = pygame.transform.rotate(upArrow.image,270)
    center = (width / 2,9 * height / 10)

    spacing = 1.5
    leftArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    downArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    upArrowRect =   pygame.rect.Rect(center[0],center[1],iconSize[0],iconSize[1])
    rightArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    leftArrowRect.center =  (center[0] - 150 * spacing,center[1])
    downArrowRect.center =  (center[0] - 50 * spacing,center[1])
    upArrowRect.center =    (center[0] + 50 * spacing,center[1])
    rightArrowRect.center = (center[0] + 150 * spacing,center[1])

    return [
        [leftArrow,leftArrowRect],
        [downArrow,downArrowRect],
        [upArrow,upArrowRect],
        [rightArrow,rightArrowRect],
    ]
    
def showLandings(landings: list,screen: pygame.Surface, inputs: input):
    global width, height, sprites
    
    # if inputs.first != 0:
    #     # Show the icon filled in
    # elif inputs.second != 0:
    #     # Show the icon filled in
    # elif inputs.third != 0:
    #     # Show the icon filled in
    # elif inputs.fourth != 0:
    #     # Show the icon filled in
    
    for landing in landings:
        screen.blit(landing[0].image,landing[1])