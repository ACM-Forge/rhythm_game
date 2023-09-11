from dataclasses import dataclass
from enum import Enum, auto


class Scenes(Enum):
    StartMenu = auto
    SettingsMenu = auto
    Game = auto
    
    
@dataclass
class Input:
    """ State used to represent how long its been since last input in each button """
    first: float = 0.0 # Zero value represents no input
    second: float = 0.0 # Non-zero represents time in which last input occured
    third: float = 0.0
    fourth: float = 0.0



    