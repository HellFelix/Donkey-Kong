import pygame

class Target:
    def __init__(self, x, y):
        self.animation = [pygame.image.load("./game/assets/target1.png"), pygame.image.load("./game/assets/target2.png"),
                          pygame.image.load("./game/assets/target3.png")]
        self.image = self.animation[0]
        self.x = x
        self.y = y
        self.increment = 0

    def hitbox(self):
        return pygame.Rect(self.x, self.y, 156, 92)

    def animate(self):
        self.increment += 1

        if self.increment < 180:
            self.image = self.animation[0]
        elif self.increment < 360:
            self.image = self.animation[1]
        elif self.increment < 720:
            self.image = self.animation[2]
        else:
            self.increment = 0

target = Target(390, 146)


