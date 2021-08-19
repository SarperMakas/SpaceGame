"""Shop of the game"""
import pygame, os


class Shop:
    """Shop class"""
    def __init__(self, W, H, screen):
        # define width, height and screen of the width
        self.WIDTH = W
        self.HEIGHT = H
        self.screen = screen

        # list of bought imgs
        file = open("file.txt", "r")
        file.readline()
        boughtDict = {"True\n": True, "True": True, "False\n": False, "False": False}
        self.bought = [boughtDict[file.readline()], boughtDict[file.readline()],
                       boughtDict[file.readline()], boughtDict[file.readline()],
                       boughtDict[file.readline()], boughtDict[file.readline()],
                       boughtDict[file.readline()]]

        # imgs
        self.buyIMG = pygame.image.load(os.path.join("IMG/Shop", "buyIMG.png"))
        self.choseIMG = pygame.image.load(os.path.join("IMG/Shop", "chose.png"))

        # dict for translate True and False
        self.translate = {True: self.choseIMG, False: self.buyIMG}

        # sale imgs
        self.saleList = []
        for bought in self.bought:
            self.saleList.append(self.translate[bought].copy())

        # making rect list
        self.rectTupleBuy = []
        for length in range(len(self.bought)):
            gap = 142.8571428571429
            self.rectTupleBuy.append(self.buyIMG.get_rect(center=((length + 0.5) * gap, self.HEIGHT - self.HEIGHT / 6)))
        self.rectTupleBuy = tuple(self.rectTupleBuy)

        # loading spaceship
        self.path = ("blue", "brown", "gray", "green", "orange", "red", "yellow")
        self.imgTuple = []
        for path in self.path:
            self.imgTuple.append(pygame.transform.rotate(pygame.image.load(os.path.join("IMG/Spaceship", f"{path}.png")), 90))
        self.imgTuple = tuple(self.imgTuple)

        # making spaceships rect
        self.rectTuple = []
        for (length, rect) in zip(range(len(self.bought)), self.rectTupleBuy):
            gap = 142.8571428571429
            self.rectTuple.append(self.buyIMG.get_rect(center=(rect.centerx + self.imgTuple[0].get_width() / 8, self.HEIGHT - self.HEIGHT / 3)))
        self.rectTuple = tuple(self.rectTuple)
        del W, H, screen

    def checkAlpha(self):
        """changing alpha value of the buy and change"""
        x, y = pygame.mouse.get_pos()
        for index, rect in enumerate(self.rectTupleBuy):
            if rect.left <= x <= rect.right and rect.top <= y <= rect.bottom:
                self.saleList[index].set_alpha(150)
                break
            else:
                self.saleList[index].set_alpha(255)


    def checkClick(self):
        """check if we click to the buy or chose"""
        x, y = pygame.mouse.get_pos()
        for index, rect in enumerate(self.rectTupleBuy):
            if rect.left <= x <= rect.right and rect.top <= y <= rect.bottom:
                return self.path[index], index
        return False

    def draw(self):
        """drawing spaceships and sale things"""
        # draw buy and chose
        for index, rect in enumerate(self.rectTupleBuy):
            img = self.saleList[index]
            # change alpha
            self.screen.blit(img, rect)
        # draw space ships
        for index, rect in enumerate(self.rectTuple):
            self.screen.blit(self.imgTuple[index], rect)


