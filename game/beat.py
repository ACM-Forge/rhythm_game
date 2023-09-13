import pygame
import os

from dataclasses import dataclass, field
from enum import Enum, auto
from .config import *

class BeatType(Enum):
    First = "first" 
    Second = "second"
    Third = "third"
    Fourth = "fourth"

@dataclass
class BeatData:
    b_type: BeatType
    timing: float

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

def readBeatMap(file: path) -> [BeatData]:
    new_beat_map = []
    with open(file, "r") as f:
        for line in f:
            type_str, timing = line.strip().split(" ")
            
            if type_str in (list(map(str.lower,BeatType._member_names_))):
                beat_type = BeatType(type_str)
            else:
                beat_type = BeatType.First
            
            new_beat = BeatData(beat_type,float(timing))
            new_beat_map.append(new_beat)
    return new_beat_map