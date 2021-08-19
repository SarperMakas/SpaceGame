"""Space Ships"""
import pygame, os
from Bullet import Bullet
from pygame.math import Vector2 as vec


class SpaceShip:
    """SpaceShip class of the game"""
    def __init__(self, W, H, screen, color):
        # define width, height and screen
        self.WIDTH = W
        self.HEIGHT = H
        self.screen = screen

        # color tuple
        self.path = ("blue", "brown", "gray", "green", "orange", "red", "yellow")
        self.color = color
        self.dictColor = {"blue": 0, "brown": 1, "gray": 2, "green": 3, "orange": 4, "red": 5, "yellow": 6}
        # define img Tuple
        self.imgTuple = []
        for path in self.path:
            self.imgTuple.append(pygame.image.load(os.path.join("IMG/Spaceship", f"{path}.png")))
        self.imgTuple = tuple(self.imgTuple)
        # vel and acc
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.SHIP_ACC = 0.7
        self.pos = vec(60, self.HEIGHT/2)
        # chosen imgs
        self.img = self.imgTuple[self.dictColor[color]]
        # imgs rect
        self.rect = self.img.get_rect(center=self.pos)
        # bullet
        self.bullet = Bullet(self.WIDTH, self.HEIGHT, self.screen, "blue", self.pos)
        del W, H, screen, color

    def keys(self):
        """check keys for moving"""
        keys = pygame.key.get_pressed()
        # check going up
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.acc.y = -self.SHIP_ACC
        # check going down
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.acc.y = self.SHIP_ACC

    def checkSides(self):
        """Check sides"""
        if self.rect.top <= 0:
            # do not go so up
            self.rect.top = 0
            self.pos.y = self.rect.centery

        if self.rect.bottom >= self.HEIGHT:
            # do not go so down
            self.rect.bottom = self.HEIGHT
            self.pos.y = self.rect.centery

    def move(self):
        """check moves"""
        self.acc = vec(0, 0)
        # check for move
        self.keys()

        # update acc
        self.acc.y += self.vel.y * -0.1
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 1 * self.acc

        # change rects pos
        self.rect.center = self.pos
        # check sides
        self.checkSides()

    def changeColor(self, color):
        """change color of the space ship"""
        # redefine color, img, bullet
        self.color = color
        self.img = self.imgTuple[self.dictColor[self.color]]
        # change color of the bullet
        self.bullet.changeColor(color)

    def draw(self):
        """draw space ship"""
        # check move
        self.move()
        self.bullet.draw(self.pos)
        self.screen.blit(self.img, self.rect)
