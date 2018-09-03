#Python Snake
#Made By David Latorre

import pygame
import sys
import random
import time

class Snake():
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50]], [90,50],[80,50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirTo(self,dir):
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction

