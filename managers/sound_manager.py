#!/usr/bin/env python

import cocos
import pyglet
import pygame

class SoundManager:
    def __init__(self,soundType,volume=0.5): # volume should be 0.0 -> 1.0
        #self.soudType = soundType
        pygame.mixer.init()
        self.setVolume(volume)
        #if soundType == 0: #shoot
        #    pygame.mixer.music.load("GUNSHOT.WAV")
        #else:
        #    pass

    def playShoot(self):
        pygame.mixer.music.load("resources/sounds/GUNSHOT.WAV")
        pygame.mixer.music.play()

    def playMoving(self):
        pygame.mixer.music.load("resources/sounds/TANK_MOVE.WAV")
        pygame.mixer.music.play()

    def playTankDestroy(self):
        pygame.mixer.music.load("resources/sounds/TANK_DESTROYED.WAV")
        pygame.mixer.music.play()

    def setVolume(self,volume): # value should be between 0.0 and 1.0
        pygame.mixer.music.set_volume(volume)
