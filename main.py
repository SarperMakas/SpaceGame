"""Space Game's Main Documnt"""
import pygame, os
from shop import Shop
from Coin import Coin
from Game import Game
pygame.init()


class Main:
    """Main class for main"""
    def __init__(self):
        # width, height and screen
        self.WIDTH = 1000
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # running var for game
        self.running = True
        # background for game
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("IMG/Menu", "bg.png")), (self.WIDTH, self.HEIGHT))
        # modes
        self.mode = "Menu"
        # texts and rect of text
        self.font = pygame.font.Font("04B_19.ttf", 65)
        self.text = self.font.render("SPACE GAME", True, (245, 245, 245))
        self.textRect = self.text.get_rect(center=(self.WIDTH/2, self.HEIGHT/4))
        # start text
        self.startFont = pygame.font.Font("04B_19.ttf", 35)
        self.startText = self.startFont.render("PRESS ANY KEY FOR START", True, (245, 245, 245))
        self.startTextRect = self.startText.get_rect(center=(self.WIDTH/2, self.HEIGHT-45))
        # switch buttons
        self.switchButtonList = (pygame.image.load(os.path.join("IMG/Menu", "menu.png")), pygame.image.load(os.path.join("IMG/Menu", "Shop.png")))
        self.switchButtonRect = self.switchButtonList[0].get_rect(center=(self.WIDTH / 2, self.HEIGHT / 4 + self.switchButtonList[0].get_height() * 2))
        self.switchButtonIMG = self.switchButtonList[0]
        # Shop class
        self.shop = Shop(self.WIDTH, self.HEIGHT, self.screen)
        # color
        self.color = "blue"
        # coin
        file = open("file.txt", "r")
        self.coin = Coin(self.WIDTH, self.HEIGHT, self.screen, file.readline())
        # space ship class
        self.game = Game(self.WIDTH, self.HEIGHT, self.screen, self.color)
        # clock of the game and user event
        self.clock = pygame.time.Clock()
        self.userEvent = pygame.USEREVENT
        pygame.time.set_timer(self.userEvent, 50000)

    def checkChange(self):
        """Checking we change the mode"""
        x, y = pygame.mouse.get_pos()
        # check if we click to the switch button
        if self.switchButtonRect.left <= x <= self.switchButtonRect.right and self.switchButtonRect.top <= y <= self.switchButtonRect.bottom:
            # switch the switch button img
            if self.mode == "Menu":
                # change mode and rect
                self.mode = "Shop"
                self.switchButtonIMG = self.switchButtonList[1]
            elif self.mode == "Shop":
                # change mode and rect
                self.mode = "Menu"
                self.switchButtonIMG = self.switchButtonList[0]

    def checkShop(self, value):
        """checking shop"""
        # check if the mode is Shop
        if self.mode == "Shop":
            # check alpha
            self.shop.checkAlpha()
            # for mouse clicks
            if self.shop.checkClick() is not False and value == pygame.MOUSEBUTTONDOWN:
                # check if we can buy a new character
                if self.shop.bought[self.shop.checkClick()[1]] is False and self.coin.value >= 350:
                    # buying a new character decreasing coin adding to the coinLog and change saleList
                    self.shop.bought[self.shop.checkClick()[1]] = True
                    self.coin.value -= 350
                    self.coin.coinLog.append(self.coin.value)
                    self.shop.saleList[self.shop.checkClick()[1]] = self.shop.choseIMG.copy()
                # check for chose
                elif self.shop.bought[self.shop.checkClick()[1]] is True:
                    # change color of the spaceShip, enemie and main class
                    self.color = self.shop.checkClick()[0]
                    self.game.spaceShip.changeColor(self.color)
                    self.game.enemie.changeColor(self.color)

    def checks(self, value):
        """Checking stuffs"""
        self.checkShop(value)
        self.game.check()
        if self.game.health <= 0:
            self.mode = "Main"
            self.shop = Shop(self.WIDTH, self.HEIGHT, self.screen)
            self.color = "blue"
            self.coin = Coin(self.WIDTH, self.HEIGHT, self.screen, 400)
            self.game = Game(self.WIDTH, self.HEIGHT, self.screen, self.color)
        if self.game.coinUp is True:
            self.coin.value += 10
            self.coin.coinLog.append(self.coin.value)
            self.game.coinUp = False

    def save(self):
        """saving app"""
        file = open("file.txt", "w")
        file.write(f"{self.coin.value}")
        for bought in self.shop.bought:
            file.write(f"\n{bought}")

    def event(self):
        """event function"""
        # use for loop for event
        for event in pygame.event.get():
            # quiting from the game
            if event.type == pygame.QUIT:
                self.save()
                self.running = False
            # check click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.checkChange()
                self.checks(pygame.MOUSEBUTTONDOWN)
            elif event.type == pygame.KEYDOWN and self.mode != "Game":
                self.mode = "Game"
                pygame.time.set_timer(self.userEvent, 3000)
            elif event.type == self.userEvent:
                self.game.enemie.makeRect()

    def draw(self):
        """drawing the window"""
        # check drawing
        if self.mode != "Game":
            # fill the bg
            self.screen.fill((25, 25, 25))
            # draw switch button and texts
            self.screen.blit(self.switchButtonIMG, self.switchButtonRect)
            self.screen.blit(self.text, self.textRect)

            self.screen.blit(self.startText, self.startTextRect)
        # game draw
        elif self.mode == "Game":
            # drawing background
            self.screen.blit(self.bg, (0, 0))
            self.game.draw()
        # shop draw
        if self.mode == "Shop":
            # drawing shop
            self.shop.draw()
        # draw the coin
        self.coin.draw()
        pygame.display.flip()


    def main(self):
        """main function for game"""
        while self.running:
            self.clock.tick(35)
            self.event()
            self.checks(None)
            self.draw()


if __name__ == '__main__':
    Main().main()
