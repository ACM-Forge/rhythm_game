import pygame
import os

from dataclasses import dataclass, field
from enum import Enum, auto
from .config import *


class BeatType(Enum):
    Left = auto 
    Right = auto
    Up = auto
    Down = auto

class Landing(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super().__init__()
        
        self.size = size
        self.image = pygame.transform.scale(
        pygame.image.load(os.path.join(sprites,"arrow.png")),
        self.size)
        
        colorImage = pygame.Surface(self.size).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        


class Beat(pygame.sprite.Sprite):
    def __init__(self,pos, type, image, screen, time):
        super().__init__()
        self._image = image
        self._screen: pygame.Surface = screen
        self.type: BeatType = type
        self.rect: pygame.Rect = self.image.get_rect(center=pos)
        self.time = time

    def show(self):
        self._screen.blit(self.image,self.rect)
    
    def update(self):
        self.rect.top -= gameSpeed

@dataclass
class BeatMap:
    map: list[Beat]

def readBeatMap(f: path) -> BeatMap:
    new_beat_map = []
    return new_beat_map


class Track:
    def __init__(self,music, bMap):
        self.music = music
        self.track = bMap
    
    def start(self):
        pass

    def show():
        """ Show all current beats """
        pass

    def update():
        """ Spawn in new beats offscreen and update their position"""
        pass

    def end():
        pass

