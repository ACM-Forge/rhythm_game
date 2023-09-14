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
        self.landings = landings
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

    def checkCreateBeat(self, bData: BeatData) -> Beat:
        """ See if a new beat should be created"""
        #beat_img = None
        if bData.b_type == BeatType.First:
            #beat_img = Landing(())
            pass
        elif bData.b_type == BeatType.Second:
            pass
        elif bData.b_type == BeatType.Third:
            pass
        elif bData.b_type == BeatType.Third:
            pass
        #newBeat = Beat()
        
        
        #self.curr_beats.append(newBeat)


    def update(self):
        """ Spawn in new beats offscreen and update their position"""
        
        self.checkCreateBeat(self.bMap[0])
            
        # b = Beat((width/2,-beatSize[1]),BeatData(BeatType.Second,2000),path.join(sprites,"arrow.png"),self.canvas)
        # self.curr_beats.append(self.createBeat(front))
            
    
        for beat in self.curr_beats:
            if not beat.valid:
                self.curr_beats.remove(beat)
                
        for beat in self.curr_beats:
            beat.update()
        


    def end(self):
        pygame.mixer.music.stop()
        self.valid = False
        

