import pygame
from dataclasses import dataclass, field
from enum import Enum, auto
import config

class BeatTypes(Enum):
    Left = auto 
    Right = auto
    Up = auto
    Down = auto



class Beat(pygame.sprite.Sprite):
    def __init__(self,pos, type, image, screen):
        super().__init__()
        self.type = type
        self._image = image
        self.rect = self.image.get_rect(center=pos)
        self._screen = screen

    def show(self):
        self._screen.blit(self.image.self.rect)
    
    def update(self):
        self.rect.top -= config.gameSpeed



@dataclass
class BeatMap:
    map: list[Beat]

def readBeatMap(f) -> BeatMap:
    new_beat_map = []

    return new_beat_map

class Track:
    def __init__(self,music):
        self.music = music
        self.track = []
    
    def start():
        pass

    def show():
        pass

    def update():
        pass

    def end():
        pass

