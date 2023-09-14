import pygame
import os

from dataclasses import dataclass, field
from enum import Enum, auto
from .config import *
from .beat import *
from .landing import *

class Track:
    def __init__(self,music, bMap, landings, canvas):
        self.music = music
        self.bMap: list[BeatData] = bMap
        self.landings: list[Landing] = landings
        self.curr_beats = []
        self.canvas = canvas
        self.start_time = pygame.time.get_ticks()
        self.valid = True
    
    def start(self):
        # Start playing music
        pygame.mixer.init()
        pygame.mixer.music.load(
            os.path.join(music,"main.mp3")
        )
        pygame.mixer.music.set_volume(music_volume)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(songOver)
    

    def show(self):
        """ Show all current beats """
        for beat in self.curr_beats:
            beat.show()


    def checkCreateBeat(self) -> Beat:
        """ See if a new beat should be created, if so create it"""
        
        curr_time = pygame.time.get_ticks() - self.start_time
        time_diff = curr_time - self.bMap[0].timing + 100 * gameSpeed
        
        if time_diff < -50 or time_diff > 50:
            return
        bData = self.bMap.pop(0)
        # print(curr_time)
        # print(bData.timing)
        # print(time_diff)
        
        beat_img = None
        beat_landing = None
        if bData.b_type == BeatType.First:
            beat_img = createBeatImage("arrow.png",beatSize,(0,0,255),180.0)
            beat_landing = self.landings[0]
        elif bData.b_type == BeatType.Second:
            beat_img = createBeatImage("arrow.png",beatSize,(0,255,0),270.0)
            beat_landing = self.landings[1]
        elif bData.b_type == BeatType.Third:
            beat_img = createBeatImage("arrow.png",beatSize,(255,255,0),90.0)
            beat_landing = self.landings[2]
        elif bData.b_type == BeatType.Fourth:
            beat_img = createBeatImage("arrow.png",beatSize,(255,0,0),0.0)
            beat_landing = self.landings[3]
        
        newBeat = Beat((beat_landing.rect.left,-beatSize[1]),bData,beat_img,self.canvas,beat_landing)
        self.curr_beats.append(newBeat)

    def checkInvalid(self):
        if len(self.bMap) == 0 and len(self.curr_beats) == 0:
            self.valid = False
            return True
        return False


    def update(self):
        if self.checkInvalid(): return
        
        """ Spawn in new beats offscreen and update their position"""
        if len(self.bMap) > 0:
            self.checkCreateBeat()
                    
    
        for beat in self.curr_beats:
            if not beat.valid:
                self.curr_beats.remove(beat)
                
        for beat in self.curr_beats:
            beat.update()
        


    def end(self):
        pygame.mixer.music.stop()
        self.valid = False
        

