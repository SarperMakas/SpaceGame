"""Enemie"""
import pygame, os, random


class Enemie:
    """Enemie class of the game"""
    def __init__(self, W, H, screen, color):
        # define width, height, screen
        self.WIDTH = W
        self.HEIGHT = H
        self.screen = screen
        del W, H, screen

        # color and path
        self.path = ("blue", "brown", "gray", "green", "orange", "red", "yellow")
        self.dictColor = {"blue": 0, "brown": 1, "gray": 2, "green": 3, "orange": 4, "red": 5, "yellow": 6}
        self.color = color

        # making img Tuple
        self.imgTuple = []
        for path in self.path:
            self.imgTuple.append(pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("IMG/Enemie", f"{path}.png")), True, False), (32, 75)))
        self.imgTuple = tuple(self.imgTuple)
        # vel
        self.vel = 0

        # enemie img
        self.img = self.imgTuple[self.dictColor[self.color]]
        # enemie list
        # is will contains rects, [rect, health]
        self.enemieList = []
        self.makeRect()

    def makeRect(self):
        """Making rect"""
        y = []
        value = random.randint(0, self.HEIGHT)
        while value - 50 in y or value + 50 in y:
            value = random.randint(0, self.HEIGHT)
        else:
            y.append(value)
            rect = self.img.get_rect(midleft=(self.WIDTH, value))
            self.enemieList.append([rect, 100, 3])

    def moveEnemie(self):
        """moving enemies"""

        enemieList = []
        for value in self.enemieList:
            value[2] += 0.125
            rect = value[0]
            health = value[1]
            enemieList.append([self.img.get_rect(midleft=(rect.x-value[2], rect.centery)), health, 3])
        self.enemieList = enemieList


    def changeColor(self, color):
        """change color of the enemie"""
        # change color and img
        self.color = color
        self.img = self.imgTuple[self.dictColor[self.color]]

    def draw(self):
        """drawing enemie"""
        # use for loop
        self.moveEnemie()
        for value in self.enemieList:
            self.screen.blit(self.img, value[0])
