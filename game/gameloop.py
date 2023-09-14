import pygame
import os
from time import sleep

from .types import *
from .landing import *
from .beat import *
from .button import *
from .track import *
from .config import *
from .score import *

def handleInput(event: pygame.event.Event, input_state: Input):
    currTime = pygame.time.get_ticks()
    if event.key == InputButtons["First"]:
        input_state.first = float(currTime)
    if event.key == InputButtons["Second"]:
        input_state.second = float(currTime)
    if event.key == InputButtons["Third"]:
        input_state.third = float(currTime)
    if event.key == InputButtons["Fourth"]:
        input_state.fourth = float(currTime)


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
    center = width / 2
    lane_1 = pygame.rect.Rect(center - 275,0,100,height)
    lane_2 = pygame.rect.Rect(center - 125,0,100,height)
    lane_3 = pygame.rect.Rect(center + 25,0,100,height)
    lane_4 = pygame.rect.Rect(center + 175,0,100,height)
    
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
    canvas.fill((51,51,51))
    for seconds in reversed(range(count)):
        countdownText = get_font(75).render(str(seconds + 1), True, "#FFFFFF")
        countdownRect = countdownText.get_rect(center=(width / 2, height / 2))
        canvas.fill(bgcolor)
        canvas.blit(countdownText, countdownRect)
        pygame.display.update()
        sleep(1)

  
def gameLoop(canvas: pygame.Surface):
    global score
    # Preload all objects to be used in the game loop
    beat_map = readBeatMap(track_path)
    music_path = os.path.join(music,"main.mp3")
    
    score.setMax(len(beat_map) * 5)
    
    lanes = loadLanes()
    landings = loadLandings()
    input_state = Input()
    
    
    # Show a countdown before the game starts
    countDown(canvas,0)
    
    track = Track(music_path,beat_map, landings,canvas)
    pygame.display.set_caption("ACM Rhythm")
    clock = pygame.time.Clock()
    
    dt = 0

    #Setup and play music
    track.start()
    
    while track.valid:
        canvas.fill(bgcolor)
        pygame.display.set_caption("ACM Rythm Game")
        
        print(score.score)
        dt = clock.tick(60)

        #print(beat_map)
        
        showLanes(lanes,canvas)
        showLandings(landings,canvas, input_state)
        
        track.show()
        track.update()
        
        #print(track.bMap)
        
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
    global score
    clock = pygame.time.Clock()
    pygame.display.set_caption("End Menu")
    looping = True
    while looping:
        clock.tick(60)
        canvas.fill(bgcolor)
        mouse = pygame.mouse.get_pos()

        titleText = get_font(60).render("Game Over!", True, "#FFFFFF")
        titleRect = titleText.get_rect(center=(width / 2, (height / 2) - 250))
        
        gradeText = get_font(60).render(score.determineGrade(), True, "#FFA500")
        gradeRect = gradeText.get_rect(center=(width / 2, (height / 2) - 150))
        
        scoreText = get_font(30).render("Final Score: " + str(score.score) + " / " + str(score.maxScore), True, "#FFFFFF")
        scoreRect = scoreText.get_rect(center=(width / 2, (height / 2) - 50))

        #playAgainButton = Button(image=pygame.image.load("sprites/Play_Rect.png"), pos=(width / 2, (height / 2) + 100), 
        #                text_input="Play Again?", font=get_font(30), base_color="#D3D3D3", hovering_color="White")
        quitButton = Button(image=pygame.image.load("sprites/Play_Rect.png"), pos=(width / 2, (height / 2) + 200), 
                        text_input="Quit Game", font=get_font(30), base_color="#D3D3D3", hovering_color="White")

        canvas.blit(titleText, titleRect)
        canvas.blit(gradeText, gradeRect)
        canvas.blit(scoreText, scoreRect)

        for button in [quitButton]:
            button.changeColor(mouse)
            button.update(canvas)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playAgainButton.checkForInput(mouse):
                    looping = False
                if quitButton.checkForInput(mouse):
                    exit(0)
            
        pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption("Rhythm Game")
    canvas = pygame.display.set_mode((width, height))
    startMenu(canvas)
    gameLoop(canvas)
    endMenu(canvas)