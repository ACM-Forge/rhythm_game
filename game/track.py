import pygame
import os

from dataclasses import dataclass, field
from enum import Enum, auto
from .config import *

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

