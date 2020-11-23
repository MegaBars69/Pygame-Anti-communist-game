import pygame as pg
from pygame import mixer
import random,math

pg.init()
#functions
def player(x,y):
    screen.blit(player_img,(x,y))
def rock(x,y,i):
    screen.blit(rock_img[i],(x,y))
def fire_bullet(x,y):
    global bulletx_state
    bulletx_state = "Fire"
    screen.blit(bullet_img,(x+16,y+10))
def isCollision(rockx,rocky,bulletx,bullety):
    distance =  math.sqrt(math.pow(rockx - bulletx, 2) + (math.pow(rocky - bullety, 2)))
    if distance<27:
        return True
    else:
        return False
def game_over():
    running = False
def show_score(x,y):
    score_screen = font.render("Score: " + str(score),True,(144,55,155))
    screen.blit(score_screen,(x,y))

#variables
screen = pg.display.set_mode((800,1200))
clock = pg.time.Clock()

pg.display.set_caption("Space Invanders")
icon = pg.image.load("Space game/image.png")
pg.display.set_icon(icon)

player_img = pg.image.load("Space game/russia.png").convert_alpha()
playerx = 280
playery = 780
player_changex = 0
player_changey = 0

bg_surface = pg.image.load("Space game/background.png").convert()

win_surface = pg.image.load('Space game/elcin.jpg').convert()

rock_img=[]
rockx=[]
rocky=[]
rock_x_change=[]
rock_y_change=[]
rocks = random.randint(3,9)
num_of_rocks = rocks 
for i in range(num_of_rocks):
    rock_img.append(pg.image.load("Space game/communist.png").convert_alpha())
    rockx.append( random.randint(0,800))
    rocky.append( random.randint(50,150))
    rock_x_change.append(2.8)
    rock_y_change.append(25)

bullet_img = pg.image.load("Space game/bullet.png").convert_alpha()
bullet_img = pg.transform.scale2x(bullet_img)
bulletx = 0
bullety = 780
bullet_x_change = 0
bullet_y_change = 10
bulletx_state = "ready"

game_over_surface = pg.transform.scale2x(pg.image.load("C:/Users/sinic/OneDrive/Фотографии/Пленка/barsuk/pygame/Pictures/message.png").convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))
game_font = pg.font.Font("freesansbold.ttf",40)

score = 0
font = pg.font.Font('freesansbold.ttf',32)

textx = 10
texty = 10

mixer.music.load("Space game/Егор Летов - Всё идёт по плану..mp3") 
mixer.music.play(-1)

game_active = True
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False  

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                player_changex = 5
            if event.key == pg.K_LEFT:
                player_changex = -5
            if event.key == pg.K_SPACE:
                if bulletx_state == "ready":
                    shoot_sound = mixer.Sound('Space game/shoot.wav')
                    shoot_sound.play()
                    bulletx = playerx
                    fire_bullet(bulletx,bullety)
        if event.type == pg.KEYUP:
            if  event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player_changex = 0

    screen.blit(bg_surface,(0,0))
    #player
    playerx += player_changex
    if playerx<=0:
        playerx = 0
    elif playerx>=690:
        playerx=690
    player(playerx,playery)

    
    #rock
    for i in range(num_of_rocks):   
        rockx[i] += rock_x_change[i]
        if rockx[i]<=0:
            rock_x_change[i] = 2.8
            rocky[i] += rock_y_change[i]
        elif rockx[i] >= 690:
            rock_x_change[i]=-2.8
            rocky[i] += rock_y_change[i]
        
        #collision
        collision = isCollision(rockx[i],rocky[i],bulletx,bullety)
        if collision:
            score += 1
            print(score)
            rockx [i]= random.randint(0,800)
            rocky[i] = random.randint(50,100) 
        if score > 3:
            rockx[i] = rockx[i] + 1.5 
        elif score > 6:
            rockx[i] = rockx -1.5
        if rockx[i] <= 1050:
            game_active = False 

        rock(rockx[i],rocky[i],i)   
        #bullet
    if bullety<=0:
        bullety = 780
        bulletx_state = "ready"
    if bulletx_state == "Fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullet_y_change

        #if score == 13:
        #    screen.blit(win_surface,(0,0))
    show_score(50,50)

    clock.tick(120)
    pg.display.update()