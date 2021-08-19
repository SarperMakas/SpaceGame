"""Game"""
import pygame, os
from SpaceShip import SpaceShip
from Enemie import Enemie


class Game:
    """Game class of the game"""
    def __init__(self, W, H, screen, color):
        # define width, height and screen
        self.WIDTH = W
        self.HEIGHT = H
        self.screen = screen
        # SpaceShip class
        self.spaceShip = SpaceShip(W, H, screen, color)
        # Enemie class
        self.enemie = Enemie(W, H, screen, color)
        # health
        self.health = 100
        # hearth img
        self.hearth = pygame.image.load(os.path.join("IMG", "Hearth.png"))
        self.hearthRect = self.hearth.get_rect(topright=(self.WIDTH-100, 25))
        # health font and text
        self.font = pygame.font.Font("04B_19.ttf", 30)
        self.text = self.font.render(f"{self.health}", True, (245, 245, 245))
        self.textRect = self.text.get_rect(topleft=(self.hearthRect.right+10, 25))
        self.coinUp = False
        del W, H, screen

    def checkShipAndEnemie(self):
        """check ship and enemie collision"""
        for value in self.enemie.enemieList:
            rect = value[0]
            # check collide rect
            if self.spaceShip.rect.colliderect(rect):
                self.enemie.enemieList.remove(value)
                self.health -= 10
                # redefine text and textRect
                self.text = self.font.render(f"{self.health}", True, (245, 245, 245))
                self.textRect = self.text.get_rect(topleft=(self.hearthRect.right + 10, 25))

    def checkBulletAndEnemie(self):
        """check ship and enemie collision"""
        for index, value in enumerate(self.enemie.enemieList):
            rect = value[0]
            # check collide rect
            if self.spaceShip.bullet.shotRect.colliderect(rect):
                self.enemie.enemieList[index][1] -= 50
                if self.enemie.enemieList[index][1] <= 0:
                    self.enemie.enemieList.remove(value)
                    self.coinUp = True
                    self.enemie.makeRect()
                self.spaceShip.bullet.changeBulletPos(True)

    def checkEnemie(self):
        """check enemie"""
        for enemie in self.enemie.enemieList:
            if enemie[0].right <= 0:
                self.health -= 5
                self.enemie.enemieList.remove(enemie)
                # redefine text and textRect
                self.text = self.font.render(f"{self.health}", True, (245, 245, 245))
                self.textRect = self.text.get_rect(topleft=(self.hearthRect.right + 10, 25))

    def check(self):
        """checking collision and enemies"""
        self.checkShipAndEnemie()
        self.checkBulletAndEnemie()
        self.checkEnemie()

    def draw(self):
        """draw game"""
        # draw health text and hearth
        self.screen.blit(self.hearth, self.hearthRect)
        self.screen.blit(self.text, self.textRect)
        # draw space ship and enemie
        self.spaceShip.draw()
        self.enemie.draw()
