# Imports
import pygame
import random
import math
import sys
import os

if getattr(sys, 'frozen', False):
    current_path = sys._MEIPASS
else:
    current_path = os.path.dirname(__file__)


# Initialize game engine
pygame.init()


# Window
WIDTH = 1300
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
screen = pygame.display.set_mode(SIZE)
screen_stage1 = pygame.Surface(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)
PURPLE = (100, 5, 100)

# Images
ship_img = pygame.image.load(current_path + '/Images/Ship1.png')
ship_img2 = pygame.image.load(current_path + '/Images/Ship2.png')
ship_img3 = pygame.image.load(current_path + '/Images/Ship3.png')
ship_img4 = pygame.image.load(current_path + '/Images/Ship4.png')
ship_img5 = pygame.image.load(current_path + '/Images/Ship5.png')
ship_img6 = pygame.image.load(current_path + '/Images/Ship6.png')
ship_img7 = pygame.image.load(current_path + '/Images/Ship7.png')
laser_img = pygame.image.load(current_path + '/Images/laser1.png')
laser_img2 = pygame.image.load(current_path + '/Images/laser2.png')
laser_img3 = pygame.image.load(current_path + '/Images/laser3.png')
mob_img = pygame.image.load(current_path + '/Images/alien1.png')
mob_img2 = pygame.image.load(current_path + '/Images/alien2.png')
mob_img3 = pygame.image.load(current_path + '/Images/alien3.png')
mob_img4 = pygame.image.load(current_path + '/Images/alien4.png')
turret_img = pygame.image.load(current_path + '/Images/turret.png')
bomb_img = pygame.image.load(current_path + '/Images/Bomb1.png')
bomb_img2 = pygame.image.load(current_path + '/Images/Bomb2.png')
power_bomb = pygame.image.load(current_path + '/Images/power_bomb.png')
gattling = pygame.image.load(current_path + '/Images/gattling.png')
explo_img = pygame.image.load(current_path + '/Images/explo.png')
wrench_img = pygame.image.load(current_path + '/Images/wrench.png')
heart_img = pygame.image.load(current_path + '/Images/heart.png')
level_img = pygame.image.load(current_path + '/Images/power_up.png')
box = pygame.image.load(current_path + '/Images/box.png')
start_screen = pygame.image.load(current_path + '/Images/start_screen.png')
intro1 = pygame.image.load(current_path + '/Images/intro1.png')
intro2 = pygame.image.load(current_path + '/Images/intro2.png')
end_screen = pygame.image.load(current_path + '/Images/End.png')
boss_img = pygame.image.load(current_path + '/Images/boss.png')

# Sounds
laser_sound = pygame.mixer.Sound(current_path + '/Sounds/laser2.ogg')
MUSIC = pygame.mixer.music.load(current_path + '/Sounds/Brinstar.ogg')
HEY = pygame.mixer.Sound(current_path + '/Sounds/hey.ogg')
SCREAM = pygame.mixer.Sound(current_path + '/Sounds/scream.ogg')
BOOM = pygame.mixer.Sound(current_path + '/Sounds/boom.ogg')

# Fonts
FONT_TY = pygame.font.Font(current_path + '/Fonts/Mario64.ttf', 12)
FONT_SM = pygame.font.Font(current_path + '/Fonts/Mario64.ttf', 24)
FONT_MD = pygame.font.Font(current_path + '/Fonts/Mario64.ttf', 32)
FONT_LG = pygame.font.Font(current_path + '/Fonts/Mario64.ttf', 64)
FONT_XL = pygame.font.Font(current_path + '/Fonts/Mario64.ttf', 96)

# Stages
start = 0
stage1 = 1
stage2 = 2
stage3 = 3
stage4 = 4
end = 6
intro_1 = 7
intro_2 = 8
final = 9
status = start

# Boolean checks
s_show = False
t_show = False
e_show = False
v_show = False
h_show = False
a_show = False
x_show = False

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.shield = 5
        self.hp = 5
        self.level = 1
        self.alt_item = 0
        self.bomb_count = 0
        self.gun_count = 0
        self.active = False
        self.seconds = 60

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def shoot(self):
        if self.level == 1:
            laser = Laser(laser_img, 5)
            laser.rect.centerx = self.rect.centerx
            laser.rect.centery = self.rect.top
            lasers.add(laser)
        elif self.level == 2:
            laser1 = Laser(laser_img, 8)
            laser1.rect.centerx = (self.rect.centerx)
            laser1.rect.centery = self.rect.top
            lasers.add(laser1)
        elif self.level == 3:
            laser1 = Laser(laser_img, 5)
            laser2 = Laser(laser_img, 5)
            laser1.rect.centerx = (self.rect.centerx - 15)
            laser1.rect.centery = self.rect.top
            laser2.rect.centerx = (self.rect.centerx + 15)
            laser2.rect.centery = self.rect.top
            lasers.add(laser1, laser2)
        elif self.level == 4:
            laser1 = Laser(laser_img2, 5)
            laser2 = Laser(laser_img2, 5)
            laser1.rect.centerx = (self.rect.centerx - 15)
            laser1.rect.centery = self.rect.top
            laser2.rect.centerx = (self.rect.centerx + 15)
            laser2.rect.centery = self.rect.top
            lasers.add(laser1, laser2)
        elif self.level == 5:
            laser1 = Laser(laser_img2, 8)
            laser2 = Laser(laser_img2, 8)
            laser1.rect.centerx = (self.rect.centerx - 15)
            laser1.rect.centery = self.rect.top
            laser2.rect.centerx = (self.rect.centerx + 15)
            laser2.rect.centery = self.rect.top
            lasers.add(laser1, laser2)
        elif self.level == 6:
            laser1 = Laser(laser_img2, 8)
            laser2 = Laser(laser_img2, 8)
            laser3 = Laser(laser_img, 8)
            laser4 = Laser(laser_img, 8)
            laser1.rect.centerx = (self.rect.centerx - 15)
            laser1.rect.centery = self.rect.top
            laser2.rect.centerx = (self.rect.centerx + 15)
            laser2.rect.centery = self.rect.top
            laser3.rect.centerx = (self.rect.centerx - 5)
            laser3.rect.centery = self.rect.top
            laser4.rect.centerx = (self.rect.centerx + 5)
            laser4.rect.centery = self.rect.top
            lasers.add(laser1, laser2, laser3, laser4)
        elif self.level == 7:
            laser1 = Laser(laser_img3, 10)
            laser2 = Laser(laser_img3, 10)
            laser3 = Laser(laser_img3, 10)
            laser4 = Laser(laser_img3, 10)
            laser5 = Laser(laser_img, 10)
            laser6 = Laser(laser_img, 10)
            laser1.rect.centerx = (self.rect.centerx - 15)
            laser1.rect.centery = self.rect.top
            laser2.rect.centerx = (self.rect.centerx + 15)
            laser2.rect.centery = self.rect.top
            laser3.rect.centerx = (self.rect.centerx - 5)
            laser3.rect.centery = self.rect.top
            laser4.rect.centerx = (self.rect.centerx + 5)
            laser4.rect.centery = self.rect.top
            laser5.rect.centerx = (self.rect.centerx + 25)
            laser5.rect.centery = self.rect.top
            laser6.rect.centerx = (self.rect.centerx - 25)
            laser6.rect.centery = self.rect.top
            lasers.add(laser1, laser2, laser3, laser4, laser5, laser6)

    def alt_fire(self):
        if self.alt_item == 0:
            pass
        elif self.alt_item == 1 and self.bomb_count > 0:
            self.bomb_count -= 1
            bomb_launch = Bomb_Launch(power_bomb)
            bomb_launch.rect.centerx = self.rect.centerx
            bomb_launch.rect.centery = self.rect.top
            bomb_launches.add(bomb_launch)
            if self.gun_count == 0:
                if self.bomb_count == 0:
                    self.alt_item = 0
            else:
                self.alt_item = 2
        elif self.alt_item == 2 and self.gun_count > 0:
            self.active = True
            self.gun_count -= 1
            if self.bomb_count == 0:
                if self.gun_count == 0:
                    self.alt_item = 0
            else:
                self.alt_item = 1

    def update(self, status, pbombs, bombs, bullets, mobs, wrenches, hearts, p_ups, image2, image3, image4, image5, image6, image7):
        if self.level == 2:
            self.image = image2
        elif self.level == 3:
            self.image = image3
        elif self.level == 4:
            self.image = image4
        elif self.level == 5:
            self.image = image5
        elif self.level == 6:
            self.image = image6
        elif self.level == 7:
            self.image = image7
        
        hit_list = pygame.sprite.spritecollide(self, bombs, True)

        for hit in hit_list:
            self.shield -= 1

        if status == 3 or status == 4 or status == final:
            hit_list = pygame.sprite.spritecollide(self, bullets, True)

            for hit in hit_list:
                self.shield -= 1

        hit_list = pygame.sprite.spritecollide(self, mobs, True)

        for hit in hit_list:
            self.shield = 0

        hit_list = pygame.sprite.spritecollide(self, pbombs, True)

        for hit in hit_list:
            self.alt_item = 1
            self.bomb_count += 1

        hit_list = pygame.sprite.spritecollide(self, pguns, True)

        for hit in hit_list:
            self.alt_item = 2
            self.gun_count += 1

        hit_list_wrench = pygame.sprite.spritecollide(self, wrenches, True)

        for hit in hit_list_wrench:
            self.shield += 3
            if self.shield > self.hp:
                self.shield = self.hp

        hit_list_hp = pygame.sprite.spritecollide(self, hearts, True)

        for hit in hit_list_hp:
            self.hp += 1
            self.shield += 1

        hit_list_power = pygame.sprite.spritecollide(self, p_ups, True)

        for hit in hit_list_power:
            if self.level != 7:
                self.level += 1
                if (self.level%2) == 0:
                    self.speed += 1

        if self.shield == 0:
            self.kill()
            SCREAM.play()

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.right > 1300:
            self.rect.right = 1300

        if self.active:
            ship.shoot()
            self.seconds -= 1
            if self.seconds == 0:
                self.active = False
                self.seconds = 60
            
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image, speed):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()
    
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image, image2, image3, image4, status):
        super().__init__()
        if v_show:
           rand_n = random.randrange(1, 5)
           if status == 3:
               if rand_n == 2 or rand_n == 3 or rand_n == 4:
                   self.shield = 2
               elif rand_n == 1:
                   self.shield = 1
        else:
            rand_n = random.randrange(1, 3)
            if status == 3:
                if rand_n == 2:
                     self.shield = 2
                elif rand_n == 1:
                    self.shield = 1
        if status != 3:
            self.shield = 1
        if self.shield == 1:
            self.image = image
            self.image2 = image2
            self.big_bomb = False
        elif self.shield == 2:
            self.image = image3
            self.image2 = image4
            self.big_bomb = True
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.second = 0
        self.power_rate = 150


    def drop_bomb(self):
        if self.big_bomb:
            bomb = Bomb(bomb_img2)
            bomb.rect.centerx = self.rect.centerx
            bomb.rect.centery = self.rect.bottom
            bombs.add(bomb)
        else:
            bomb = Bomb(bomb_img)
            bomb.rect.centerx = self.rect.centerx
            bomb.rect.centery = self.rect.bottom
            bombs.add(bomb)
    
    def update(self, lasers, bomb_launches, explos, status):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)


        for hit in hit_list:
            self.shield -= 1
            player.score += 10

        hit_list = pygame.sprite.spritecollide(self, bomb_launches, True)

        for hit in hit_list:
            explosion = Explo(explo_img)
            explosion.rect.centerx = self.rect.centerx
            explosion.rect.centery = self.rect.bottom
            explos.add(explosion)
            self.shield -= 10

        hit_list = pygame.sprite.spritecollide(self, explos, False)

        for hit in hit_list:
            self.shield -= 10
            

        if status == 0:
            self.kill()

        if self.shield <= 0:
            BOOM.play()
            rand = random.randrange(0, self.power_rate)
            if rand == 0 or rand == 4 or rand == 5:
                wrench = Wrench(wrench_img)
                wrench.rect.centerx = self.rect.centerx
                wrench.rect.centery = self.rect.top
                wrenches.add(wrench)
            elif rand == 1 or rand == 7:
                heart = Hp(heart_img)
                heart.rect.centerx = self.rect.centerx
                heart.rect.centery = self.rect.top
                hearts.add(heart)
            elif rand == 2:
                p_up = Power(level_img)
                p_up.rect.centerx = self.rect.centerx
                p_up.rect.centery = self.rect.top
                p_ups.add(p_up)
            elif rand == 3:
                pbomb = Pbomb(power_bomb)
                pbomb.rect.centerx = self.rect.centerx
                pbomb.rect.centery = self.rect.top
                pbombs.add(pbomb)
            elif rand == 6:
                pgun = Pgun(gattling)
                pgun.rect.centerx = self.rect.centerx
                pgun.rect.centery = self.rect.top
                pguns.add(pgun)
            self.kill()
            
        self.second += 1
        
        if (self.second % 30 == 0):
            self.image, self.image2 = self.image2, self.image


class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 710:
            self.kill()
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.moving_right = True
        self.speed = 1
        self.bomb_rate = 25

    def move(self):
        reverse = False
        
        for m in mobs:
            if self.moving_right:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True
            else:
                m.rect.x -= self.speed
                if m.rect.left <=0:
                    reverse = True

        if reverse == True:
            self.moving_right = not self.moving_right
            for m in mobs:
                m.rect.y += 15
            

    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()

class Turret(pygame.sprite.Sprite):

    def __init__(self, x, y, image, num):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.second = 0
        self.shield = 10
        self.num = num

    def drop_bomb(self):
        if self.num == 1:
            bullet = Bullet(bomb_img, 1)
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.centery = self.rect.bottom
            bullets.add(bullet)
        elif self.num == 2:
            bullet2 = Bullet(bomb_img, 2)
            bullet2.rect.centerx = self.rect.centerx
            bullet2.rect.centery = self.rect.bottom
            bullets.add(bullet2)

    def update(self, lasers, bomb_launches, explos, status):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)

        for hit in hit_list:
            self.shield -= 1

        hit_list = pygame.sprite.spritecollide(self, bomb_launches, True)

        for hit in hit_list:
            explosion = Explo(explo_img)
            explosion.rect.centerx = self.rect.centerx
            explosion.rect.centery = self.rect.bottom
            explos.add(explosion)
            self.shield -= 10

        hit_list = pygame.sprite.spritecollide(self, explos, False)

        for hit in hit_list:
            self.shield -= 10

        self.second += 1

        if (self.second%60) == 0:
            self.drop_bomb()

        if status == 0:
            self.kill()

        if self.shield <= 0:
            BOOM.play()
            rand = random.randrange(0, 10)
            if rand == 0 or rand == 4 or rand == 5:
                wrench = Wrench(wrench_img)
                wrench.rect.centerx = self.rect.centerx
                wrench.rect.centery = self.rect.top
                wrenches.add(wrench)
            elif rand == 1:
                heart = Hp(heart_img)
                heart.rect.centerx = self.rect.centerx
                heart.rect.centery = self.rect.top
                hearts.add(heart)
            elif rand == 2:
                p_up = Power(level_img)
                p_up.rect.centerx = self.rect.centerx
                p_up.rect.centery = self.rect.top
                p_ups.add(p_up)
            elif rand == 3:
                pbomb = Pbomb(power_bomb)
                pbomb.rect.centerx = self.rect.centerx
                pbomb.rect.centery = self.rect.top
                pbombs.add(pbomb)
            self.kill()
            player.score += 50

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, image, num):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 5

        if num == 1:
            self.real_x = turret.rect.centerx
            self.real_y = turret.rect.centery
        elif num == 2:
            self.real_x = turret2.rect.centerx
            self.real_y = turret2.rect.centery
        if num == 3:
            self.real_x = 700
            self.real_y = 250
        elif num == 4:
            self.real_x = 750
            self.real_y = 250

        hypo = pygame.math.Vector2([(ship.rect.centerx - self.real_x), (ship.rect.centery - self.real_y)])

        self.corrdinents = hypo.normalize()

    def update(self):
        self.real_x += (self.corrdinents[0] * self.speed)
        self.real_y += (self.corrdinents[1] * self.speed)

        round(self.real_x)
        round(self.real_y)

        self.rect.x = round(self.real_x)
        self.rect.y = round(self.real_y)

        if self.rect.top > 710:
            self.kill()

class Wrench(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 700:
            self.kill()

class Hp(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 700:
            self.kill()

class Power(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 700:
            self.kill()

class Pbomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 700:
            self.kill()

class Pgun(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 700:
            self.kill()

class Bomb_Launch(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()

class Explo(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.time = 10

    def update(self):
        self.time -= 1

        if self.time < 0:
            self.kill()
        
class Boss(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = 5
        self.shoot_time = 60
        self.active = False
        self.shield = 500

    def shoot(self):
        bullet = Bullet(bomb_img2, 3)
        bullet.rect.centerx = 675
        bullet.rect.centery = 200
        bullet2 = Bullet(bomb_img2, 4)
        bullet2.rect.centerx = 750
        bullet2.rect.centery = 200
        bullets.add(bullet, bullet2)

    def update(self, turrets, mobs):
        self.time -= 1
        if self.time == 0:
            rand = random.randrange(0, 4)
            if rand == 3:
                if len(turrets) == 0:
                    setup_turret1()
                    print("3a")
                else:
                    self.active = True
                    print("3b")
            elif rand == 2:
                self.active = True
                print("2")
            elif rand == 1:
                setup_quick()
                fleet.speed += 10
                print("1")
            self.time = 180
        if self.active:
            self.shoot_time -= 1
            self.shoot()
            if self.shoot_time == 0:
                self.active = False
                self.shoot_time = 60
        hit_list = pygame.sprite.spritecollide(self, lasers, True)


        for hit in hit_list:
            self.shield -= 1
            player.score += 10

        hit_list = pygame.sprite.spritecollide(self, bomb_launches, True)

        for hit in hit_list:
            explosion = Explo(explo_img)
            explosion.rect.centerx = self.rect.centerx
            explosion.rect.centery = self.rect.bottom
            explos.add(explosion)
            self.shield -= 10

        hit_list = pygame.sprite.spritecollide(self, explos, False)

        for hit in hit_list:
            self.shield -= 1

        if self.shield <= 0:
            self.kill()

# Helper Functions

def ship_setup():
    global ship, player
    
    ship = Ship(650, 600, ship_img)

    player = pygame.sprite.GroupSingle()
    player.add(ship)

    player.score = 0

def setup():
    global mobs, bomb_launches, pguns, explos, fleet, pbombs, p_ups, wrenches, hearts, lasers, bombs
    
    mob1 = Mob(100, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob2 = Mob(150, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob3 = Mob(200, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob4 = Mob(250, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob5 = Mob(300, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob6 = Mob(350, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob7 = Mob(400, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob8 = Mob(450, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob9 = Mob(500, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob10 = Mob(550, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob11 = Mob(600, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob12 = Mob(650, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob13 = Mob(700, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob14 = Mob(750, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob15 = Mob(800, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob16 = Mob(850, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob17 = Mob(900, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob18 = Mob(950, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob19 = Mob(1000, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob20 = Mob(1050, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob21 = Mob(1100, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob22 = Mob(100, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob23 = Mob(150, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob24 = Mob(200, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob25 = Mob(250, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob26 = Mob(300, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob27 = Mob(350, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob28 = Mob(400, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob29 = Mob(450, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob30 = Mob(500, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob31 = Mob(550, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob32 = Mob(600, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob33 = Mob(650, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob34 = Mob(700, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob35 = Mob(750, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob36 = Mob(800, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob37 = Mob(850, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob38 = Mob(900, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob39 = Mob(950, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob40 = Mob(1000, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob41 = Mob(1050, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob42 = Mob(1100, 100, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob43 = Mob(100, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob44 = Mob(150, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob45 = Mob(200, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob46 = Mob(250, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob47 = Mob(300, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob48 = Mob(350, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob49 = Mob(400, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob50 = Mob(450, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob51 = Mob(500, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob52 = Mob(550, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob53 = Mob(600, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob54 = Mob(650, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob55 = Mob(700, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob56 = Mob(750, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob57 = Mob(800, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob58 = Mob(850, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob59 = Mob(900, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob60 = Mob(950, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob61 = Mob(1000, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob62 = Mob(1050, 150, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob63 = Mob(1100, 150, mob_img, mob_img2, mob_img3, mob_img4, status)


    # Make sprites
    lasers = pygame.sprite.Group()

    wrenches = pygame.sprite.Group()

    hearts = pygame.sprite.Group()

    p_ups = pygame.sprite.Group()

    pbombs = pygame.sprite.Group()

    pguns = pygame.sprite.Group()

    bomb_launches = pygame.sprite.Group()

    explos = pygame.sprite.Group()

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10,
             mob11, mob12, mob13, mob14, mob15, mob16, mob17, mob18, mob19, mob20,
             mob21, mob22, mob23, mob24, mob25, mob26, mob27, mob28, mob29, mob30,
             mob31, mob32, mob33, mob34, mob35, mob36, mob37, mob38, mob39, mob40,
             mob41, mob42, mob43, mob44, mob45, mob46, mob47, mob48, mob49, mob50,
             mob51, mob52, mob53, mob54, mob55, mob56, mob57, mob58, mob59, mob60,
             mob61, mob62, mob63)

    bombs = pygame.sprite.Group()

    fleet = Fleet(mobs)

def setup_quick():
    global mobs, fleet
    
    mob5 = Mob(300, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob6 = Mob(350, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob7 = Mob(400, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob8 = Mob(450, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob9 = Mob(500, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob10 = Mob(550, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob11 = Mob(600, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob12 = Mob(650, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob13 = Mob(700, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob14 = Mob(750, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob15 = Mob(800, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob16 = Mob(850, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob17 = Mob(900, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob18 = Mob(950, 50, mob_img, mob_img2, mob_img3, mob_img4, status)
    mob19 = Mob(1000, 50, mob_img, mob_img2, mob_img3, mob_img4, status)

    mobs = pygame.sprite.Group()
    mobs.add(mob5, mob6, mob7, mob8, mob9, mob10, mob11, mob12, mob13,
             mob14, mob15, mob16, mob17, mob18, mob19)

    fleet = Fleet(mobs)

def setup_turret1():
    global turret, turret2, turrets, bullets
    
    turret = Turret(1200, 200, turret_img, 1)
    turret2 = Turret(100, 200, turret_img, 2)

    turrets = pygame.sprite.Group()

    bullets = pygame.sprite.Group()

    turrets.add(turret, turret2)

def setup_boss():
    global bosses, boss, laser, wrenches, hearts, p_ups, pbombs, bomb_launches, explos, bombs

    boss = Boss(450, 50, boss_img)

    bosses = pygame.sprite.Group()
    bosses.add(boss)

    lasers = pygame.sprite.Group()

    wrenches = pygame.sprite.Group()

    hearts = pygame.sprite.Group()

    p_ups = pygame.sprite.Group()

    pbombs = pygame.sprite.Group()

    pguns = pygame.sprite.Group()

    bomb_launches = pygame.sprite.Group()

    explos = pygame.sprite.Group()

    bombs = pygame.sprite.Group()

def show_stats(player, ship):
    score_text = FONT_MD.render(("Score - " + str(player.score)), 1, WHITE)
    screen.blit(score_text, [32, 32])

    hp_total = ship.hp * 20
    hp_remain = (20 * ship.shield)
    
    health_text = FONT_MD.render(('Health - ' + str(hp_remain) + ' / ' + str(hp_total)), 1, WHITE)
    screen.blit(health_text, [1032, 32])

def show_alt(player, ship):
    screen.blit(box, [630, 0])
    if ship.alt_item == 1:
        screen.blit(power_bomb, [635, 5])
        count_text = FONT_TY.render((str(ship.bomb_count)), 1, WHITE)
        screen.blit(count_text, [660, 25])
    elif ship.alt_item == 2:
        screen.blit(gattling, [635, 5])
        count_text = FONT_TY.render((str(ship.gun_count)), 1, WHITE)
        screen.blit(count_text, [660, 25])

    
# Make game objects
setup()
ship_setup()

# Load Stage Backgrounds
stage1_backg = pygame.image.load(current_path + '/Images/stage1.png')
screen_stage1.blit(stage1_backg, [0,0])

# Game loop
pygame.mixer.music.play(-1)
done = False
HEY.play()
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if status != start or status != intro1 or status != intro2:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
                    laser_sound.play()
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    ship.alt_fire()
            if status == intro_2:
                if event.key == pygame.K_SPACE:
                    setup()
                    ship_setup()
                    if v_show:
                        fleet.speed += 2
                        fleet.bomb_rate -= 5
                    status = stage1
            if status == intro_1:
                if event.key == pygame.K_SPACE:
                    status = intro_2
            if status == end:
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    status = start
            if status == start:
                if event.key == pygame.K_SPACE:
                    status = intro_1
                elif event.key == pygame.K_s:
                    s_show = True
                elif event.key == pygame.K_t and s_show:
                    t_show = True
                elif event.key == pygame.K_e and t_show:
                    e_show = True
                elif event.key == pygame.K_v and e_show:
                    v_show = True
                    if v_show:
                        MUSIC = pygame.mixer.music.load(current_path + '/Sounds/Minecraft.ogg')
                        pygame.mixer.music.play(-1)


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        ship.move_left()
    elif pressed[pygame.K_RIGHT]:
        ship.move_right()
    '''if pressed[pygame.K_SPACE]:
        ship.shoot()'''
    
    # Game logic (Check for collisions, update points, etc.)

    if status == stage1:
        if ship.shield == 0:
            status = start
        elif len(mobs) == 0:
            status = stage2
            setup()
            if v_show:
                fleet.bomb_rate -= 10
                fleet.speed += 2
            else:
                fleet.bomb_rate -= 5
                fleet.speed += 1
            
    if status == stage2:
        if ship.shield == 0:
            status = start
        elif len(mobs) == 0:
            setup_turret1()
            setup()
            if v_show:
                fleet.bomb_rate -= 12
                fleet.speed += 3
            else:
                fleet.bomb_rate -= 7
                fleet.speed += 2
            status = stage3

    if status == stage3:
        if ship.shield == 0:
            status = start
        elif len(mobs) == 0:
            setup_turret1()
            setup()
            if v_show:
                fleet.bomb_rate -= 15
                fleet.speed += 3
            else:
                fleet.bomb_rate -= 10
                fleet.speed += 2
            status = stage4

    if status == stage4:
        if ship.shield == 0:
            status = start
        elif len(mobs) == 0 and len(turrets) == 0:
            setup_boss()
            if v_show:
                boss.shield = 1000
            status = final

    if status == final:
        if ship.shield == 0:
            status = start
        elif len(bosses) == 0:
            status = end
            

    
    if status != stage3:
        bomb_launches.update()
        player.update(status, pbombs, bombs, mobs, mobs, wrenches, hearts, p_ups, ship_img2, ship_img3, ship_img4, ship_img5, ship_img6, ship_img7)
    lasers.update()
    explos.update()
    wrenches.update()
    hearts.update()
    p_ups.update()
    pbombs.update()
    pguns.update()
    mobs.update(lasers, bomb_launches, explos, status)
    if status == final:
        bosses.update(turrets, mobs)
    if status == stage3 or status == stage4 or status == final:
        player.update(status, pbombs, bombs, bullets, mobs, wrenches, hearts, p_ups, ship_img2, ship_img3, ship_img4, ship_img5, ship_img6, ship_img7)
        turrets.update(lasers, bomb_launches, explos, status)
        bullets.update()
        bomb_launches.update()
    bombs.update()
    fleet.update()

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(PURPLE)
    if status != start and status != intro_2 and status != intro_1:
        screen.blit(screen_stage1, [0,0])
        explos.draw(screen)
        lasers.draw(screen)
        p_ups.draw(screen)
        wrenches.draw(screen)
        hearts.draw(screen)
        player.draw(screen)
        bombs.draw(screen)
        show_alt(player, ship)
        pguns.draw(screen)
        mobs.draw(screen)
        pbombs.draw(screen)
        bomb_launches.draw(screen)
        if status == final:
            bosses.draw(screen)
            if v_show:
                boss_text = FONT_MD.render(("Health - " + str(boss.shield) + " / 500"), 1, BLACK)
                screen.blit(boss_text, [500, 350])
            else:
                boss_text = FONT_MD.render(("Health - " + str(boss.shield) + " / 500"), 1, BLACK)
                screen.blit(boss_text, [500, 350])
        if status == stage3 or status == stage4 or status == final:
            turrets.draw(screen)
            bullets.draw(screen)
        if status == end:
            screen.blit(end_screen, [0,0])
        show_stats(player, ship)
        
    elif status == start:
        screen.blit(start_screen,[0,0])
        if s_show:
          s_text = FONT_XL.render("S", 1, WHITE)
          screen.blit(s_text, [50, 200])
        if t_show:
          t_text = FONT_XL.render("T", 1, WHITE)
          screen.blit(t_text, [50, 300])
        if e_show:
          e1_text = FONT_XL.render("E", 1, WHITE)
          screen.blit(e1_text, [50, 400])

          e2_text = FONT_XL.render("E", 1, WHITE)
          screen.blit(e2_text, [50, 600])
        if v_show:
          v_text = FONT_XL.render("V", 1, WHITE)
          screen.blit(v_text, [50, 500])

    elif status == intro_1:
        screen.blit(intro1,[0,0])
    elif status == intro_2:
        screen.blit(intro2,[0,0])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()


