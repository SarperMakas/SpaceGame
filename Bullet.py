"""Bullet"""
import pygame, os
from pygame.math import Vector2 as vec


class Bullet:
    """Bullet class of the game"""
    def __init__(self, W, H, screen, color, pos):
        # define width, height and screen
        self.WIDTH = W
        self.HEIGHT = H
        self.screen = screen

        # color tuple
        self.path = ("blue", "brown", "gray", "green", "orange", "red", "yellow")
        self.color = color
        self.dictColor = {"blue": 0, "brown": 1, "gray": 2, "green": 3, "orange": 4, "red": 5, "yellow": 6}

        # define shot imgs
        self.shotTuple = []
        for path in self.path:
            self.shotTuple.append(pygame.transform.scale2x(pygame.image.load(os.path.join("IMG/Shots", f"{path}.png"))))
        self.shotTuple = tuple(self.shotTuple)

        # vel and acc
        self.SHIP_ACC = 0.7
        self.pos = vec(60, self.HEIGHT/2)

        self.shotVel = vec(0, 0)
        self.shotAcc = vec(0, 0)
        self.SHOT_ACC = 2
        self.shotPos = vec()
        self.shotPos.x = self.pos.x
        self.shotPos.y = self.pos.y

        # starting shot

        # chosen img and rect
        self.shotIMG = self.shotTuple[self.dictColor[color]]
        self.shotRect = self.shotIMG.get_rect(center=self.shotPos)

        self.startShot = False
        del W, H, screen, color

    def bulletMove(self):
        """moving bullet"""
        if self.startShot is True:
            self.shotVel.x = -self.SHOT_ACC
            # update acc
            self.shotAcc.x += self.shotVel.x * -0.8
            # equations of motion
            self.shotVel += self.shotAcc
            self.shotPos += self.shotVel + 1 * self.shotAcc

        else:
            self.shotPos.y = self.pos.y

    def changeBulletPos(self, value=False):
        """changing bullet pos"""
        if self.shotPos.x - self.shotIMG.get_width()/2 >= self.WIDTH or value is True:
            self.shotVel.x = 0
            self.shotAcc.x = 0
            self.startShot = False
            self.shotPos.x = self.pos.x
            self.shotPos.y = self.pos.y

    def changeColor(self, color):
        """changing color and img"""
        self.color = color
        self.shotIMG = self.shotTuple[self.dictColor[color]]


    def shot(self):
        """Shot"""
        # check shot
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.startShot is False:
            self.startShot = True

        # bullet move and changing pos of the bullet
        self.bulletMove()
        self.changeBulletPos()

        self.shotRect.center = self.shotPos

    def draw(self, pos):
        """drawing bullet"""
        self.pos = pos
        self.shot()
        if self.startShot is True and pos.x < self.shotPos.x:
            self.screen.blit(self.shotIMG, self.shotRect)
