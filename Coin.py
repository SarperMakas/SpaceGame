"""Coin of the game"""
import pygame, os, math


class Coin:
    """Coin class of the game"""
    def __init__(self, W, H, screen, coin):
        # defining width, height and screen
        self.WIDTH = W
        self.HEIGHT = H
        self.screen = screen
        # coin value
        self.value = int(coin)
        self.coinLog = [self.value, self.value]
        # imgTuple
        self.imgTuple = (pygame.transform.scale2x(pygame.image.load(os.path.join("IMG/Coins", "coin1.png"))),
                         pygame.transform.scale2x(pygame.image.load(os.path.join("IMG/Coins", "coin2.png"))),
                         pygame.transform.scale2x(pygame.image.load(os.path.join("IMG/Coins", "coin3.png"))),
                         pygame.transform.scale2x(pygame.image.load(os.path.join("IMG/Coins", "coin4.png"))))

        # wait and count value
        self.count = 0
        self.wait = 5
        # chosen img
        self.img = self.imgTuple[self.count // self.wait]
        self.coinRect = self.img.get_rect(center=(28, 28))
        # text and texts rect
        self.font = pygame.font.Font("04B_19.ttf", self.img.get_height())
        self.text = self.font.render(f"{self.value}", True, (245, 245, 245))
        self.textRect = self.text.get_rect(topleft=(self.coinRect.right + self.img.get_width() / 4, self.coinRect.x))
        del W, H, screen, coin

    def imgAnimation(self):
        """make the coin animation"""
        # increase count
        self.count += 1
        # check if the count is big for redefine img
        if self.count == self.wait*len(self.imgTuple):
            self.count = 0

        # redefine img and rect
        self.img = self.imgTuple[self.count // self.wait]
        self.coinRect = self.img.get_rect(center=(28, 28))

    def textAnimation(self, num):
        """Make the coin animation"""
        if self.coinLog[-1] != self.coinLog[-2]:
            if self.coinLog[-2] < self.coinLog[-1]:
                self.coinLog[-2] += 1
            else:
                self.coinLog[-2] -= 1
            self.value = self.coinLog[-2]
            self.text = self.font.render(f"{math.floor(self.value)}", True, (245, 245, 245))
            if num <= 3:
                self.textAnimation(num+1)
        # drawing text
        self.screen.blit(self.text, self.textRect)


    def draw(self):
        """draw coin and run animation function"""
        # start coin animation and coin text animation
        self.imgAnimation()
        self.textAnimation(1)
        # drawing coin to the screen
        self.screen.blit(self.img, self.coinRect)
