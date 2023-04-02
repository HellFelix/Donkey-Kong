import pygame
import level1
import barrel
import target

ground = level1.ground
ladders = level1.ladders

barrels = barrel.barrels

target1 = target.target

animation_right = [pygame.image.load("./assets/player/right/normal.png"), pygame.image.load("./assets/player/right/walking1.png"),
                   pygame.image.load("./assets/player/right/walking2.png"), pygame.image.load("./assets/player/right/normal_hammer_up.png"),
                   pygame.image.load("./assets/player/right/normal_hammer_down.png"), pygame.image.load("./assets/player/right/walking_hammer_up.png"),
                   pygame.image.load("./assets/player/right/walking_hammer_down.png")]

animation_left = [pygame.image.load("./assets/player/left/normal.png"), pygame.image.load("./assets/player/left/walking1.png"),
                   pygame.image.load("./assets/player/left/walking2.png"), pygame.image.load("./assets/player/left/normal_hammer_up.png"),
                   pygame.image.load("./assets/player/left/normal_hammer_down.png"), pygame.image.load("./assets/player/left/walking_hammer_up.png"),
                   pygame.image.load("./assets/player/left/walking_hammer_down.png")]

animation_climbing = [pygame.image.load("./assets/player/climbing/right.png"), pygame.image.load("./assets/player/climbing/left.png")]

dead = pygame.image.load("./assets/player/dead.png")

animations = [animation_right, animation_left, animation_climbing, dead]

# define how the player should act
class Player:
    def __init__(self, x, y, colour, gravity, width = 30, height = 60):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.colour = colour
        self.gravity = gravity
        self.dx = 0
        self.dy = 0
        self.moving_left = False
        self.looking_left = False
        self.moving_right = False
        self.looking_right = True
        self.climbing_up = False
        self.climbing_down = False
        self.touching_ground = False
        self.touching_ladder = False
        self.visible = False

        self.jumping = False

        self.hammer_eq = True
        self.hammer = False

        self.dead = False
        self.image = animations[0][0]
        self.animation = [0, 0]
        self.increment = 0

        self.target = target1
        self.win = False

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def feet(self):
        return pygame.Rect(self.x, self.y + self.height, self.width, 2)

    def check_collision_floor(self):
        for g in ground:
            if self.rect().colliderect(g) and self.y + 50 < g.y:
                self.touching_ground = True
                self.dy = 0
                while self.y + self.height > g.y:
                    self.y -= 1
                self.jumping = False
                return
            elif self.feet().colliderect(g) and not self.rect().colliderect(g):
                self.touching_ground = True 
                return
        self.touching_ground = False

    def check_collision_ladder(self):
        for l in ladders:
            if self.rect().colliderect(l) and l.climbable:
                self.touching_ladder = True
                return
        self.touching_ladder = False

    def move_left(self):
        self.moving_left = True
        self.moving_right = False
        self.looking_left = True
        self.looking_right = False

    def stop_moving_left(self):
        self.moving_left = False
    
    def move_right(self):
        self.moving_right = True
        self.moving_left = False
        self.looking_right = True
        self.looking_left = False

    def stop_moving_right(self):
        self.moving_right = False

    def jump(self):
        self.jumping = True
        self.dy = -0.4

    def up(self):
        if self.touching_ladder:
            self.climb_up()
        elif self.touching_ground:
            self.jump()

    def climb_up(self):
        if self.touching_ladder:
            self.climbing_up = True
            self.climbing_down = False

    def stop_climbing_up(self):
        self.climbing_up = False

    def climb_down(self):
        if self.touching_ladder:
            self.climbing_down = True
            self.climbing_up = False

    def stop_climbing_down(self):
        self.climbing_down = False


    def attack(self):
        if self.hammer_eq and not self.climbing_up and not self.climbing_down:
            self.increment = 0
            self.hammer = True

    def hammer_hitbox(self):
        if self.looking_right:
            return pygame.Rect(self.x + 45, self.y - 4, 60, 60)
        else:
            return pygame.Rect(self.x - 75, self.y - 4, 60, 60)

    def check_attack(self):
        if self.hammer and self.increment > 20:
            for b in barrels:
                if self.hammer_hitbox().colliderect(b.hitbox()):
                    b.explode()


    def die(self):
        self.dead = True

    def check_dead(self):
        for b in barrels:
            if self.rect().colliderect(b.hitbox()) and b.hostile:
                self.die()
                b.explode()
                return

    def check_win(self):
        if self.rect().colliderect(self.target.hitbox()):
            self.win = True


    def animate(self):
        if self.dead:
            self.image = animations[3]
            return

        elif self.climbing_down or self.climbing_up:
            if self.increment < 30:
                self.animation = [2, 0]
            elif self.increment < 60:
                self.animation = [2, 1]
            else:
                self.increment = 0


        elif self.moving_right:
            if self.increment < 30:
                self.animation = [0, 1]
            elif self.increment < 60:
                self.animation = [0, 2]
            else:
                self.increment = 0
            if self.hammer:
                if self.increment < 20:
                    self.animation = [0, 5] 
                elif self.increment < 40:
                    self.animation = [0, 6]
                else:
                    self.hammer = False


        elif self.looking_right:
            self.animation = [0, 0]
            if self.hammer:
                if self.increment < 20:
                    self.animation = [0, 3]
                elif self.increment < 40:
                    self.animation = [0, 4]
                else:
                    self.hammer = False

        #         
        elif self.moving_left:
            if self.increment < 30:
                self.animation = [1, 1]
            elif self.increment < 60:
                self.animation = [1, 2]
            else:
                self.increment = 0
            if self.hammer:
                if self.increment < 20:
                    self.animation = [1, 5]
                elif self.increment < 40:
                    self.animation = [1, 6]
                else:
                    self.hammer = False


        elif self.looking_left:
            self.animation = [1, 0]
            if self.hammer:
                if self.increment < 20:
                    self.animation = [1, 3]
                elif self.increment < 40:
                    self.animation = [1, 4]
                else:
                    self.hammer = False

        self.increment += 1

        self.image = animations[self.animation[0]][self.animation[1]]



    def move(self, dt):
        if self.dead or self.win:
            return


        self.check_collision_floor()
        self.check_collision_ladder()
        if (not self.touching_ground and not self.touching_ladder) or self.jumping:
            # Account for gravity
            self.dy += self.gravity * dt
        elif self.climbing_up:
            self.dy = -0.1
        elif self.climbing_down:
            self.dy = 0.1
        else:
            self.dy = 0

        # Account for horisontal movement
        if self.moving_left:
            self.dx = -0.2
        elif self.moving_right:
            self.dx = 0.2
        else:
            self.dx = 0

        if self.x + self.dx * dt > 0 and self.x + self.dx * dt + self.width < level1.SIZE[0]:
            self.x += self.dx * dt

        self.y += self.dy * dt

        if not self.touching_ladder:
            self.stop_climbing_up()
            self.stop_climbing_down()

        self.check_dead()
        self.check_attack()
        self.check_win()
        self.animate()

