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
    def __init__(self,pos, bData, image, screen):
        super().__init__()
        self._image = pygame.transform.scale(pygame.image.load(image),beatSize)
        self._screen: pygame.Surface = screen
        self.type: BeatData = bData
        self.rect = pygame.rect.Rect(pos[0],pos[1],10,10)
        self.valid = True

    def show(self):
        self._screen.blit(self._image,self.rect)
        
    def collide(self):
        pass
    
    def update(self):
        self.rect.top += gameSpeed

def readBeatMap(file: path) -> list[BeatData]:
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