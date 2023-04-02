import pygame
SIZE = (896, 1040)
background = pygame.image.load("./game/assets/background.png")

ground = []

# describe how the ground should act
class Ground:
    def __init__(self, width, x, y, colour,  height = 32):
        self.width = width
        self.x = x
        self.y = y
        self.height = height
        self.colour = colour
        self.visible = False
    
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

ground_colour = (0, 255, 0)

# Make the floor

# first level
ground.append(Ground(447, 0, 1007, ground_colour))
for i in range(0, 7):
    ground.append(Ground(64, 447 + i * 64, 1003 - i * 4, ground_colour))


# second level
for i in range(0, 13):
    ground.append(Ground(64, 768 - i * 64, 895 - i * 4, ground_colour))

# third level
for i in range(0, 13):
    ground.append(Ground(64, 64 + i * 64, 764 - i * 4, ground_colour))

# fourth level
for i in range(0, 13):
    ground.append(Ground(64, 768 - i * 64, 632 - i * 4, ground_colour))

# fifth level
for i in range(0, 13):
    ground.append(Ground(64, 64 + i * 64, 500 - i * 4, ground_colour))

# sixth level
for i in range(0, 4):
    ground.append(Ground(64, 768 - i * 64, 368 - i * 4, ground_colour))
ground.append(Ground(576, 0, 352, ground_colour))

# top level
ground.append(Ground(192, 353, 240, ground_colour))


ladders = []


# define how the ladder should act
class Ladder:
    def __init__(self, height, x, y, colour, climbable, width = 32):
        self.height = height
        self.x = x
        self.y = y
        self.colour = colour
        self.width = width
        self.climbable = climbable
        self.visible = False
        self.ladder_hook = pygame.Rect(x + width / 2, y-20, 1, 20)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
ladder_colour = (0, 0, 255)

# First level
ladders.append(Ladder(144, 320, 864, ladder_colour, False))
ladders.append(Ladder(100, 736, 890, ladder_colour, True))

# second level
ladders.append(Ladder(140, 384, 740, ladder_colour, True))
ladders.append(Ladder(100, 128, 760, ladder_colour, True))

#third level
ladders.append(Ladder(160, 256, 596, ladder_colour, False))
ladders.append(Ladder(140, 448, 610, ladder_colour, True))
ladders.append(Ladder(100, 736, 630, ladder_colour, True))

# fourth level
ladders.append(Ladder(100, 128, 494, ladder_colour, True))
ladders.append(Ladder(120, 288, 486, ladder_colour, True))
ladders.append(Ladder(174, 672, 456, ladder_colour, False))

# fifth level
ladders.append(Ladder(100, 736, 360, ladder_colour, True))

# sixth level
ladders.append(Ladder(120, 512, 236, ladder_colour, True))
ladders.append(Ladder(214, 320, 140, ladder_colour, True))
ladders.append(Ladder(214, 256, 140, ladder_colour, True))
