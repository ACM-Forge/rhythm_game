import pygame
import re

from dataclasses import dataclass
from enum import Enum
from .config import *
from .landing import Landing
from .score import *

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
    def __init__(self,pos, bData, image, screen, landing):
        super().__init__()
        self._image: pygame.Surface = image
        self._screen: pygame.Surface = screen
        self.landing: Landing = landing
        self.type: BeatData = bData
        self.rect = pygame.rect.Rect(pos[0],pos[1],10,10)
        self.valid = True

    def show(self):
        #if(self.landing.input_time != 0):
        #    self._screen.blit(self._image,self._image.fill((255,255,255), special_flags=pygame.BLEND_RGBA_MULT))
        self._screen.blit(self._image,self.rect)
        
    def checkCollide(self):
        global score
        if self.landing.input_time == 0.0:
            return
        coll = self.rect.colliderect(self.landing.rect)
        if coll:
            diff = abs(self.landing.input_time - self.type.timing)
            print(diff)
            if diff <= 5 * input_threshold:
                points = 5 - (diff / input_threshold)
                score.updateScore(points)
                #print(score.score)
            self.valid = False
                

    
    def update(self):
        self.checkCollide()
        self.rect.top += gameSpeed
        if self.rect.top > height:
            self.valid = False


def readBeatMap(file: path) -> list[BeatData]:
    new_beat_map = []
    with open(file, "r") as f:
        for line in f:
            if line == "\n" or line[0] == "#":
                continue
            type_str, timing = re.split(r" {1,}",line.strip())

            if type_str in (list(map(str.lower,BeatType._member_names_))):
                beat_type = BeatType(type_str)
            else:
                beat_type = BeatType.First

            new_beat = BeatData(beat_type,float(timing))
            new_beat_map.append(new_beat)
    return new_beat_map