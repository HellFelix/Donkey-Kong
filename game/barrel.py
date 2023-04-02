import pygame
import random
import level1

barrels = []

endpoint = pygame.Rect(60, 888, 64, 120)

animation = [pygame.image.load("./assets/Barrel1.png"), pygame.image.load("./assets/Barrel2.png"), 
             pygame.image.load("./assets/Barrel3.png"), pygame.image.load("./assets/Barrel4.png"),
             pygame.image.load("./assets/Barrel5.png")]

explosion = [pygame.image.load("./assets/explosion1.png"), pygame.image.load("./assets/explosion2.png"),
             pygame.image.load("./assets/explosion3.png"), pygame.image.load("./assets/explosion4.png")]

class Barrel:
    def __init__(self, x, y, dx, dy, gravity, colour, width = 48, height = 40):
        self.x = x
        self.y = y
        self.dx = dx
        self.stored_dx = dx
        self.dy = dy
        self.gravity = gravity
        self.colour = colour
        self.width = width
        self.height = height
        self.rolling = True
        self.touching_ground = False
        self.climbing = False
        self.animation = animation
        self.image = animation[0]
        self.animation_index = 0
        self.increment = 0

        self.hostile = True

        self.exploding = False
        self.exp_stage = 0
        self.visible = True


    def bottom(self):
        return pygame.Rect(self.x, self.y + self.height, self.width, 2)
    
    def center(self):
        return pygame.Rect(self.x + self.width / 2, self.y, 4, self.height)

    def check_collision_floor(self):
        for g in level1.ground:
            if self.rolling:
                if self.rolling_hitbox().colliderect(g) and self.y + self.height - 20 < g.y and not self.climbing:
                    self.touching_ground = True
                    self.dy = 0
                    while self.y + self.height > g.y:
                        self.y -= 1
                    return
                elif self.bottom().colliderect(g):
                    self.touching_ground = True
                    return
            
            self.touching_ground = False

    def check_collision_ladder(self):
        for l in level1.ladders:
            if self.rolling_hitbox().colliderect(l.rect()) and self.climbing and not self.center().colliderect(l.ladder_hook):
                for g in level1.ground:
                    if self.bottom().colliderect(g):
                        self.climbing = False
                        self.dx = self.stored_dx * -1
                        self.stored_dx *= -1
                        self.image = self.animation[0]
                        return

            if self.center().colliderect(l.ladder_hook):
                if random.randrange(5) == 1:
                    self.climbing = True
                    return

    def explode(self):
        self.exploding = True
        self.dx = 0
        self.dy = 0
        self.gravity = 0
        self.exp_stage = 1
        self.image = explosion[0]
        self.increment = 0
        self.hostile = False

    def delete(self):
        barrels.remove(self)
        del self

    def hitbox(self):
        if self.climbing:
            return pygame.Rect(self.x, self.y, 64, 40)
        else:
            return self.rolling_hitbox()

    def move(self, dt):
        self.check_collision_floor()
        if not self.touching_ground:
            self.dy += self.gravity * dt
        
        if self.x + self.dx * dt < 0 or self.x + self.width > level1.SIZE[0]:
            self.dx *= -1
            self.stored_dx = self.dx
        
        if self.climbing:
            self.dy = 0.1
            self.dx = 0


        self.x += self.dx * dt
        self.y += self.dy * dt


        self.increment += 1
        
        if self.increment == 70 and not self.exploding:
            if self.animation_index < 3:
                self.animation_index += 1
            else:
                self.animation_index = 0
            self.image = self.animation[self.animation_index]
            self.increment = 0
        if self.climbing:
            self.image = self.animation[4]

        if self.increment == 5 and self.exploding:
            self.exp_stage += 1
            if self.exp_stage == 5:
                self.delete()
            else:
                self.image = explosion[self.exp_stage-1]
                self.increment = 0

        

        self.check_collision_ladder()

        if self.rolling_hitbox().colliderect(endpoint) and self.hostile:
            self.explode()


    def rolling_hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
