from os import path
import pygame

# Settings for graphics
width = 800
height = 600
gameSpeed = 1
beatSize = (100,100)
bgcolor = (51,51,51)
iconSize = (100,100)

# Settings for music
music_volume = 0.05

# Setup font configuration
pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans",60)

# Settings for file paths
game_path = path.split(path.split(path.abspath(__file__))[0])[0]
sprites = path.join(game_path,"sprites")
music = path.join(game_path,"music")
track_path = path.join(game_path,"track.txt")

# Settings for the correct inputs 
InputButtons = {
    "First": pygame.K_LEFT,
    "Second": pygame.K_UP,
    "Third" : pygame.K_DOWN,
    "Fourth" : pygame.K_RIGHT,
}

