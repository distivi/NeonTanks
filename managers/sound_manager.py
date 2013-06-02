#!/usr/bin/env python

import cocos
import pyglet
import pygame

class SoundManager:
    def __init__(self,soundType):
        self.soudType = soundType
        pygame.mixer.init()
        if soundType == 0:
            pygame.mixer.music.load("resources/sounds/GUNSHOT.WAV")
        else:
            pass

    def play(self):
        pygame.mixer.music.play()
