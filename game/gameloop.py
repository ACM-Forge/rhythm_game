import pygame
import os
from time import sleep

from .types import *
from .landing import *
from .beat import *
from .button import *
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
    
def get_font(size): 
    return pygame.font.Font("sprites/font.ttf", size)
    
def startMenu(canvas: pygame.Surface):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Start Menu")
    looping = True
    while looping:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()

        titleText = get_font(75).render("ACM Rhythm", True, "#FFFFFF")
        titleRect = titleText.get_rect(center=(width / 2, (height / 2) - 200))

        playButton = Button(image=pygame.image.load("sprites/Play_Rect.png"), pos=(width / 2, (height / 2)), 
                        text_input="Play Game", font=get_font(40), base_color="#D3D3D3", hovering_color="White")
        quitButton = Button(image=pygame.image.load("sprites/Play_Rect.png"), pos=(width / 2, (height / 2) + 100), 
                        text_input="Quit Game", font=get_font(40), base_color="#D3D3D3", hovering_color="White")

        canvas.blit(titleText, titleRect)

        for button in [playButton,quitButton]:
            button.changeColor(mouse)
            button.update(canvas)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mouse):
                    looping = False
                if quitButton.checkForInput(mouse):
                    exit(0)
            
        pygame.display.update()
        canvas.fill((bgcolor))

def countDown(canvas, count):
    for seconds in reversed(range(count)):
        countdownText = get_font(75).render(str(seconds + 1), True, "#FFFFFF")
        countdownRect = countdownText.get_rect(center=(width / 2, height / 2))
        canvas.fill(bgcolor)
        canvas.blit(countdownText, countdownRect)
        pygame.display.update()
        sleep(1)
        
def gameLoop(canvas: pygame.Surface):
    # Preload all objects to be used in the game loop
    beat_map = readBeatMap(track_path)
    music_path = os.path.join(music,"main.mp3")
    track = Track(music_path,beat_map,canvas)
    
    lanes = loadLanes()
    landings = loadLandings()
    input_state = Input()
    
    # Show a countdown before the game starts
    canvas.fill((51,51,51))
    countDown(canvas,3)
    pygame.display.set_caption("ACM Rhythm")
    
    clock = pygame.time.Clock()
    dt = 0

    #Setup and play music
    track.start()
    
    while track.valid:
        canvas.fill(bgcolor)
        pygame.display.set_caption("ACM Rythm Game")
        
        dt = clock.tick(60)

        
        
        showLanes(lanes,canvas)
        showLandings(landings,canvas, input_state)
        
        track.show()
        track.update()
        
        print(input_state)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit(0)
            if e.type == songOver:
                print("SONG OVER")
                track.valid = False
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