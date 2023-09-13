import pygame
import os
from time import sleep

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

def showText(canvas: pygame.Surface, text: str, color: tuple, pos: tuple):
    font = game_font.render(text,False,color)
    canvas.blit(font,pos)
    
def startMenu(canvas: pygame.Surface):
    clock = pygame.time.Clock()
    countdown = False
    
    canvas.fill((51,51,51))
    showText(canvas,"Click to Start",(255,255,255),(width / 3, height / 2.5))
    pygame.display.update()
    while not countdown:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                countdown = True
            if event.type == pygame.QUIT:
                exit(0)

def countDown(canvas, count):
    for seconds in reversed(range(count)):
        canvas.fill(bgcolor)
        showText(canvas,str(seconds + 1),(255,255,255),(width / 2, height / 2.5))
        pygame.display.update()
        sleep(1)
        
def gameLoop(canvas: pygame.Surface):
    # Preload all objects to be used in the game loop
    beat_map = readBeatMap(track_path)
    lanes = loadLanes()
    landings = loadLandings()
    input_state = Input()
    
    # Show a countdown before the game starts
    canvas.fill((51,51,51))
    countDown(canvas,3)
    
    clock = pygame.time.Clock()
    dt = 0

    # Setup and play music
    pygame.mixer.init()
    pygame.mixer.music.load(
        os.path.join(music,"main.mp3")
    )
    pygame.mixer.music.set_volume(music_volume)
    pygame.mixer.music.play()
    
    
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
            # if e.type == beatEVENT:
            #     #call beat spawn function
            #     pass
            if e.type == pygame.KEYDOWN:
                handleInput(e,input_state)
            if e.type == pygame.KEYUP:
                resetInput(e,input_state)
        pygame.display.flip()


def endMenu(canvas):
    # Show final score and grade
    # 
    pass

def main():
    pygame.init()
    pygame.display.set_caption("Rhythm Game")
    canvas = pygame.display.set_mode((width, height))
    startMenu(canvas)
    gameLoop(canvas)
    endMenu(canvas)