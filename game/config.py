from os import path
from enum import Enum
import pygame

width = 800
height = 600
gameSpeed = 1
beatSize = (100,100)
bgcolor = (0,0,0)

game_path = path.split(path.split(path.abspath(__file__))[0])[0]
sprites = path.join(game_path,"sprites")
music = path.join(game_path,"music")

InputButtons = {
    "First": pygame.K_LEFT,
    "Second": pygame.K_UP,
    "Third" : pygame.K_DOWN,
    "Fourth" : pygame.K_RIGHT,
}

