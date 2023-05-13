import pygame
from random import choice, randint
from pygame.locals import *
from sys import exit

SCORE = 0
SOLID = 1
FRAGILE = 2
DEADLY = 3
BELT_LEFT = 4
BELT_RIGHT = 5
BODY = 6
GAME_ROW = 40
GAME_COL = 28
OBS_WIDTH = GAME_COL // 4
SIDE = 13
SCREEN_WIDTH = SIDE*GAME_COL
SCREEN_HEIGHT = SIDE*GAME_ROW
COLOR = {SOLID: 0x0000ff, FRAGILE: 0xee5500, DEADLY: 0xee2222, SCORE: 0xeecccc,BELT_LEFT: 0xeeff44, BELT_RIGHT: 0xff99ff, BODY: 0x00ff00}
CHOICE = [SOLID, SOLID, SOLID, FRAGILE, FRAGILE, BELT_LEFT, BELT_RIGHT, DEADLY]

FOUR_NEIGH = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}
EIGHT_NEIGH = list(FOUR_NEIGH.values()) + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
DIRECTION = {pygame.K_UP: "up", pygame.K_LEFT: "left", pygame.K_RIGHT: "right", pygame.K_DOWN: "down"}

class Game(object):
    def __init__(self, title, size, fps=30):
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size, 0, 32)
        pygame.display.set_caption(title)
        self.keys = {}
        self.keys_up = {}
        self.clicks = {}
        self.timer = pygame.time.Clock()
        self.fps = fps
        self.score = 0
        self.end = False
        self.fullscreen = False
        self.last_time = pygame.time.get_ticks()
        self.is_pause = False
        self.is_draw = True
        self.score_font = pygame.font.SysFont("Calibri", 130, True)

    def bind_key(self, key, action):
        if isinstance(key, list):
            for k in key:
                self.keys[k] = action
        elif isinstance(key, int):
            self.keys[key] = action

    def bind_key_up(self, key, action):
        if isinstance(key, list):
            for k in key:
                self.keys_up[k] = action
        elif isinstance(key, int):
            self.keys_up[key] = action