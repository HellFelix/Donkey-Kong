import pygame
import level1
import barrel
import player
import kong
import target

pygame.init()

SIZE = level1.SIZE
GRAVITY = 0.001 
 


# Add the player

# Add the target

# CREATING CANVAS


# TITLE OF CANVAS
pygame.display.set_caption("Donkey Kong")
exit = False

class Game:
    def __init__(self, 
                 ladders = level1.ladders, 
                 ground = level1.ground, 
                 barrels = barrel.barrels,
                 player = player.Player(200, 920, (0, 255, 0), GRAVITY), 
                 target = target.target, 
                 canvas = pygame.display.set_mode(SIZE),
                 background = level1.background,
                 barrel_stack = pygame.image.load("./assets/barrel_stack.png"),
                 oil_barrel = pygame.image.load("./assets/oil_barrel.png"),
                 king_kong = kong.king_kong):
        self.ladders = ladders
        self.ground = ground
        self.barrels = barrels
        self.player = player
        self.target = target
        self.canvas = canvas
        self.background = background
        self.barrel_stack = barrel_stack
        self.oil_barrel = oil_barrel
        self.king_kong = king_kong

        self.run = True
        self.clock = pygame.time.Clock()

        self.controls_left = False
        self.controls_right = False
        self.controls_up = False
        self.controls_down = False
        self.controls_attack = False

    def display_player(self):
    
        if self.player.dead:
            self.canvas.blit(self.player.image, dest=(self.player.x - 27, self.player.y + 12))

        elif self.player.animation == [0, 0]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 9, self.player.y - 4))
        elif self.player.animation == [0, 1]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 15, self.player.y))
        elif self.player.animation == [0, 2]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 15, self.player.y - 4))
        elif self.player.animation == [0, 3]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 6, self.player.y - 40))
        elif self.player.animation == [0, 4]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 15, self.player.y - 4))
        elif self.player.animation == [0, 5]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 11, self.player.y - 40))
        elif self.player.animation == [0, 6]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 17, self.player.y - 4))

        elif self.player.animation == [1, 0]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 9, self.player.y - 4))
        elif self.player.animation == [1, 1]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 15, self.player.y))
        elif self.player.animation == [1, 2]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 15, self.player.y - 4))
        elif self.player.animation == [1, 3]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 11, self.player.y - 40))
        elif self.player.animation == [1, 4]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 75, self.player.y - 4))
        elif self.player.animation == [1, 5]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 11, self.player.y - 40))
        elif self.player.animation == [1, 6]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 77, self.player.y - 4))

        elif self.player.animation == [2, 0] or self.player.animation == [2, 1]:
            self.canvas.blit(self.player.image, dest=(self.player.x - 11, self.player.y - 4))


    def place_items(self):
        self.canvas.blit(self.background, dest=(0, 0))
        self.canvas.blit(self.barrel_stack, dest=(0, 224))
        self.canvas.blit(self.oil_barrel, dest=(barrel.endpoint.x, barrel.endpoint.y))
        self.canvas.blit(self.target.image, dest=(self.target.x, self.target.y))
        for g in self.ground:
            if g.visible:
                pygame.draw.rect(self.canvas, g.colour, g.rect())

        for l in self.ladders:
            if l.visible:
                pygame.draw.rect(self.canvas, l.colour, l.rect())

        self.canvas.blit(self.king_kong.image, dest=(self.king_kong.x, self.king_kong.y))

        for b in self.barrels:
            if not b.climbing:
                self.canvas.blit(b.image, dest=(b.x, b.y))
            else:
                self.canvas.blit(b.image, dest=(b.x - 8, b.y))

        if self.player.visible:
            pygame.draw.rect(self.canvas, self.player.colour, self.player.rect())
            pygame.draw.rect(self.canvas, (0,0, 255), self.player.feet())
        self.display_player()

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        if self.controls_left:           
            self.player.move_left()
        else:
            self.player.stop_moving_left()

        if self.controls_right:
            self.player.move_right()
        else:
            self.player.stop_moving_right()

        if self.controls_up:
            self.player.up()
        else:
            self.player.stop_climbing_up()

        if self.controls_down:
            self.player.climb_down()
        else:
            self.player.stop_climbing_down()

        if self.controls_attack:
            self.player.attack()

        dt = self.clock.tick()
        self.target.animate()
        self.player.move(dt)
        self.king_kong.move()
        for b in self.barrels:
            b.move(dt)

        self.place_items()



    
game = Game()

while game.run:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        game.controls_left = True
    else:
        game.controls_left = False

    if keys[pygame.K_RIGHT]:
        game.controls_right = True
    else:
        game.controls_right = False
    
    if keys[pygame.K_UP]:
        game.controls_up = True
    else:
        game.controls_up = False

    
    if keys[pygame.K_DOWN]:
        game.controls_down = True
    else:
        game.controls_down = False

    
    if keys[pygame.K_SPACE]:
        game.controls_attack = True
    else:
        game.controls_attack = False

    game.loop()

    pygame.display.update()
