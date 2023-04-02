import pygame
import barrel

animation = [pygame.image.load("./assets/kong1.png"), pygame.image.load("./assets/kong2.png"),
             pygame.image.load("./assets/kong3.png"), pygame.image.load("./assets/kong4.png"),
             pygame.image.load("./assets/kong5.png")]

barrels = []

class Kong:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation = animation
        self.image = animation[0]
        self.loop = 0

    def move(self):
        self.loop += 1

        if self.loop == 0:
            self.image = self.animation[1]
        elif self.loop == 50:
            self.image = self.animation[2]
        elif self.loop == 100:
            self.image = self.animation[1]
        elif self.loop == 150:
            self.image = self.animation[3]
        elif self.loop == 200:
            self.image = self.animation[4]
            barrel.barrels.append(barrel.Barrel(252, 308, 0.15, 0, 0.002, (0, 255, 0)))
        elif self.loop == 250:
            self.loop = -1

king_kong = Kong(80, 224)
