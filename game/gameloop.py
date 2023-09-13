import pygame
import os

from .types import *
from .track import *
from .config import *

def loadLandings() -> []:
    rightArrow = Landing((255,0,0), iconSize)
    leftArrow = Landing((0,0,255) , iconSize)
    downArrow = Landing((0,255,0) , iconSize)
    upArrow = Landing((255,255,0) , iconSize)

    leftArrow.image = pygame.transform.rotate(leftArrow.image, 180)
    downArrow.image = pygame.transform.rotate(downArrow.image,90)
    upArrow.image = pygame.transform.rotate(upArrow.image,270)
    center = (width / 2,9 * height / 10)

    spacing = 1.5
    leftArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    downArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    upArrowRect =   pygame.rect.Rect(center[0],center[1],iconSize[0],iconSize[1])
    rightArrowRect = pygame.rect.Rect(0,0,iconSize[0],iconSize[1])
    leftArrowRect.center =  (center[0] - 150 * spacing,center[1])
    downArrowRect.center =  (center[0] - 50 * spacing,center[1])
    upArrowRect.center =    (center[0] + 50 * spacing,center[1])
    rightArrowRect.center = (center[0] + 150 * spacing,center[1])

    return [
        [leftArrow,leftArrowRect],
        [downArrow,downArrowRect],
        [upArrow,upArrowRect],
        [rightArrow,rightArrowRect],
    ]


def showLandings(landings: list,screen: pygame.Surface, inputs: Input):
    global width, height, sprites
    
    # if inputs.first != 0:
    #     # Show the icon filled in
    # elif inputs.second != 0:
    #     # Show the icon filled in
    # elif inputs.third != 0:
    #     # Show the icon filled in
    # elif inputs.fourth != 0:
    #     # Show the icon filled in
    
    for landing in landings:
        screen.blit(landing[0].image,landing[1])
        

def handleInput(event: pygame.event.Event, input_state: Input, clock: pygame.time.Clock):
    if event.key == InputButtons["First"]:
        input_state.first = float(clock.tick())
    if event.key == InputButtons["Second"]:
        input_state.second = float(clock.tick())
    if event.key == InputButtons["Third"]:
        input_state.third = float(clock.tick())
    if event.key == InputButtons["Fourth"]:
        input_state.fourth = float(clock.tick())


def resetInput(event: pygame.event.Event,input_state: Input):
    if event.key == InputButtons["First"]:
        input_state.first = 0
    if event.key == InputButtons["Second"]:
        input_state.second = 0
    if event.key == InputButtons["Third"]:
        input_state.third = 0
    if event.key == InputButtons["Fourth"]:
        input_state.fourth = 0


def loadLanes():
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
    beat_map = readBeatMap(track_path)
    [print(beat) for beat in beat_map]
    
    lanes = loadLanes()
    landings = loadLandings()
    #track = Track()
    
    gameOver = False
    while not gameOver:
        canvas.fill(bgcolor)
        
        dt = clock.tick(60)
            
        showLanes(lanes,canvas)
        showLandings(landings,canvas, input_state)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gameOver = True
            if e.type == pygame.KEYDOWN:
                handleInput(e,input_state,clock)
            if e.type == pygame.KEYUP:
                resetInput(e,input_state)
        pygame.display.flip()


