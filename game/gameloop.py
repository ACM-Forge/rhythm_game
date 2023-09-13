import pygame
import os

from .types import *
from .landing import *
from .beat import *
from .track import *
from .config import *

def handleInput(event: pygame.event.Event, input_state: Input):
    seconds = (pygame.time.get_ticks() / 1000.0)
    if event.key == InputButtons["First"]:
        input_state.first = float(seconds)
    if event.key == InputButtons["Second"]:
        input_state.second = float(seconds)
    if event.key == InputButtons["Third"]:
        input_state.third = float(seconds)
    if event.key == InputButtons["Fourth"]:
        input_state.fourth = float(seconds)


def resetInput(event: pygame.event.Event,input_state: Input):
    if event.key == InputButtons["First"]:
        input_state.first = 0
    if event.key == InputButtons["Second"]:
        input_state.second = 0
    if event.key == InputButtons["Third"]:
        input_state.third = 0
    if event.key == InputButtons["Fourth"]:
        input_state.fourth = 0


def loadLanes() -> []:
    """Create all lanes for beats to travel along to be displayed on each frame"""
    lane_1 = pygame.rect.Rect(width / 6.5,0,100,height)
    lane_2 = pygame.rect.Rect(width / 2.9,0,100,height)
    lane_3 = pygame.rect.Rect(width / 1.9,0,100,height)
    lane_4 = pygame.rect.Rect(width / 1.4,0,100,height)
    
    return [lane_1,lane_2,lane_3,lane_4]


def showLanes(lanes:[pygame.Rect], screen):
    """Draw each lane to the screen at their respective position"""
    for lane in lanes:
        pygame.draw.rect(screen,(81,81,81),lane)


def main():
    pygame.init()
    canvas = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    input_state = Input()
    dt = 0

    # pygame.mixer.init()
    # print(os.path.join(music,"main.mp3"))
    # pygame.mixer.music.load(
    #     os.path.join(music,"main.mp3")
    # )
    # pygame.mixer.music.play()

    currScene = Scenes.StartMenu
    
    # Create all objects to be used in the game loop
    
    beatEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(beatEVENT, 500)
    
    beat_map = readBeatMap(track_path)
    [print(beat) for beat in beat_map]
    
    lanes = loadLanes()
    landings = loadLandings()
    #track = Track()
    
    gameOver = False
    while not gameOver:
        canvas.fill(bgcolor)
        pygame.display.set_caption("ACM Rythm Game")
        
        dt = clock.tick(60)
            
        showLanes(lanes,canvas)
        showLandings(landings,canvas, input_state)
        print(input_state)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gameOver = True
            if e.type == beatEVENT:
                #call beat spawn function
                pass
            if e.type == pygame.KEYDOWN:
                handleInput(e,input_state)
            if e.type == pygame.KEYUP:
                resetInput(e,input_state)
        pygame.display.flip()


