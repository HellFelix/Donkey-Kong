import pygame
from game import game

game = game.Game()

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
