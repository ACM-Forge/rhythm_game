import pygame
import os

from enum import Enum, auto
from .config import *


def createBeatImage(img_path,size,color,rotation):
    image = pygame.transform.rotate(pygame.transform.scale(
        pygame.image.load(os.path.join(sprites,img_path)),
        size,
    ), rotation)
    colorImage = pygame.Surface(size).convert_alpha()
    colorImage.fill(color)
    image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
    return image


class Landing(pygame.sprite.Sprite):
    def __init__(self, img_path,color, rect, rotation):
        super().__init__()
        self.rect = rect
        self.image = createBeatImage(img_path,(rect.width,rect.height),color,rotation)


def loadLandings() -> list[Landing]:
    center = (width / 2,9 * height / 10)
    
    leftArrowRect  = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    downArrowRect  = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    upArrowRect    = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    rightArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    
    leftArrowRect.center  = (center[0] - 225,center[1])
    downArrowRect.center  = (center[0] - 75 ,center[1])
    upArrowRect.center    = (center[0] + 75 ,center[1])
    rightArrowRect.center = (center[0] + 225,center[1])
    
    rightArrow = Landing("arrow.png",(255,0,0),rightArrowRect, 0.0)
    downArrow  = Landing("arrow.png",(0,255,0), downArrowRect, 270.0)
    leftArrow  = Landing("arrow.png",(0,0,255), leftArrowRect, 180.0)
    upArrow    = Landing("arrow.png",(255,255,0), upArrowRect, 90.0)

    return [leftArrow,downArrow,upArrow,rightArrow]
    
def showLandings(landings: list[Landing],screen: pygame.Surface, inputs: input):
    
    # if inputs.first != 0:
    #     # Show the icon filled in
    # elif inputs.second != 0:
    #     # Show the icon filled in
    # elif inputs.third != 0:
    #     # Show the icon filled in
    # elif inputs.fourth != 0:
    #     # Show the icon filled in
    
    for landing in landings:
        screen.blit(landing.image,landing.rect)