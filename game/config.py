import os


width = 800
height = 600
gameSpeed = 1
beatSize = (100,100)
bgcolor = (0,0,0)

game_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
sprites = os.path.join(game_path,"sprites")
music = os.path.join(game_path,"music")
