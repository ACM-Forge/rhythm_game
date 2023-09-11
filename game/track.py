import pygame
from os import path

from dataclasses import dataclass, field
from enum import Enum, auto
from .config import *


class BeatType(Enum):
    Left = auto 
    Right = auto
    Up = auto
    Down = auto


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

