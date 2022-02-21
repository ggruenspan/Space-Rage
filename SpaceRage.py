# SpaceRage.py
# June 12, 2018
# Gerred and Ibrahim


import pygame
from pygame.locals import *
import time
import os
from os import path
import random
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

WIDTH = 1000
HEIGHT = 600
icon = pygame.image.load("data/game logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Rage')
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 100)
CYAN = (0, 255, 255)
FONTGREEN = (0,218, 17)
BUTTONS = (28, 40, 55)

#Main Menu Music
#################################################################################################
menuGame = pygame.mixer.music.load ("data/blassic.ogg") #blassic.ogg
pygame.mixer.music.play(-1)
#################################################################################################


#Load images
#################################################################################################
title = pygame.image.load("data/Title.png")# load image

menuBackground = pygame.image.load("data/Main Menu Screen.png")# load image

gameBackground = pygame.image.load("data/Game Screen.png")# load image

instructionsBackground = pygame.image.load("data/InstructionsScreen.png")# load image

userShip = pygame.image.load("data/User Ship.png")# load image

laser = pygame.image.load("data/Green Laser Up.png")# load image

redLaser = pygame.image.load("data/Red Laser Up.png")# load image

motherShip = pygame.image.load("data/motherShip.png")# load image

Enemy = pygame.image.load("data/Enemy Ship 5.png")# load image

gameOver = pygame.image.load("data/Game Over Text.png")# load image

explosion = pygame.image.load("data/enemyexplosion.png")# load image
#################################################################################################


#Def
#################################################################################################
def scoreGUI():
    pygame.draw.rect(gameWindow, BUTTONS , (WIDTH - 350, HEIGHT - 488 , 250, 30), 0)

    graphics = font1.render("Menu", 0, WHITE)
    gameWindow.blit(graphics, (745, 113) )

    pygame.draw.rect(gameWindow, BUTTONS, (WIDTH - 350, HEIGHT - 418 , 250, 30), 0)

    graphics = font1.render("Quit", 0, WHITE)
    gameWindow.blit(graphics, (745, 183) )
    
def gameGUI():
    pygame.draw.rect(gameWindow, BUTTONS, (0, 0, 1000, 20), 0)
    pygame.draw.rect(gameWindow, BUTTONS, (960, 0, 36, 20), 0)
    graphics = font2.render("Menu", 0, WHITE)
    gameWindow.blit(graphics, (960, 0) )

    pygame.draw.rect(gameWindow, BUTTONS, (920, 0, 28, 20), 0)
    graphics = font2.render("Quit", 0, WHITE)
    gameWindow.blit(graphics, (920, 0) )
    
    pygame.draw.rect(gameWindow, BUTTONS, (99, 0, 60, 20), 0) 
    graphics = font2.render("Score: " +str(score), 0, WHITE)
    gameWindow.blit(graphics, (100, 0) )
    
    pygame.draw.rect(gameWindow, BUTTONS, (10, 0, 75, 20), 0)
    graphics = font2.render("Timer: ", 0, WHITE)
    gameWindow.blit(graphics, (10, 0))

    timer = str(int(time.time() - startTime))
    graphics = font2.render(timer, 0, WHITE)
    gameWindow.blit(graphics, (60, 0) )
    
    pygame.draw.rect(gameWindow, BUTTONS, (300, 0, 115, 20), 0)
    graphics = font2.render("User Health: " +str(userHealth), 0, WHITE)
    gameWindow.blit(graphics, (300, 0))
    
    pygame.draw.rect(gameWindow, BUTTONS, (600, 0, 130, 20), 0)
    graphics = font2.render("Mother Health: " + str(motherHealth), 0, WHITE)
    gameWindow.blit(graphics, (600, 0))

def menuGUI():
    gameWindow.fill(WHITE)
        
    gameWindow.blit (menuBackground, (0,0))
    
    gameWindow.blit (title, (580,50))
    
    pygame.draw.rect(gameWindow, BUTTONS , (WIDTH - 350, HEIGHT - 488 , 250, 30), 0)

    graphics = font1.render("Start", 0, WHITE)
    gameWindow.blit(graphics, (745, 113) )

    pygame.draw.rect(gameWindow, BUTTONS, (WIDTH - 350, HEIGHT - 453 , 120, 30), 0)

    graphics = font2.render("Instructions", 0, WHITE)
    gameWindow.blit(graphics, (670, 153) )

    pygame.draw.rect(gameWindow, BUTTONS, (WIDTH - 220, HEIGHT - 453 , 120, 30), 0)

    graphics = font2.render("Credits", 0, WHITE)
    gameWindow.blit(graphics, (815, 153) )

    pygame.draw.rect(gameWindow, BUTTONS, (WIDTH - 350, HEIGHT - 418 , 250, 30), 0)

    graphics = font1.render("Quit", 0, WHITE)
    gameWindow.blit(graphics, (745, 183) )
#################################################################################################



#Var
#################################################################################################
gameProgram = True
menuButton = True
instructionsButton = False
startButton = False
creditsButton = False
quitButton = False
xlaserNewRight = False
xlaserNewLeft = False
scoreboard = False
shoot = False
enemyX = []
enemyY = []
enemyFire = []
enemyFireT = []
enemyBulletX = []
enemyBulletY = []
LaserX = []
LaserY = []
userHealth = 100
motherHealth = 150
xEnemy = 0
yEnemy = 0
score = 0
xuserShip = WIDTH/2 - 30
yuserShip = HEIGHT/2 + 100
xMother = WIDTH/2 - 125
yMother = HEIGHT/2 + 200
font1 = pygame.font.SysFont("Arial", 25)
font2 = pygame.font.SysFont("Arial", 15)
clock = pygame.time.Clock()
FPS = 60
#################################################################################################


#start of game ---------------------------------------------------------------------- start of game
while gameProgram == True:
##    (mouseX, mouseY) = pygame.mouse.get_pos()
##    pygame.event.get()
##    pygame.time.delay(200)
##    print mouseX
##    print mouseY

    clock.tick(FPS)
    #start of Menu ------------------------------------------------------------------ start of menu
    if menuButton == True:
        menuGUI()
        pygame.display.update()
        (mouseX, mouseY) = pygame.mouse.get_pos()
        pygame.event.get()
        #instructions Button
        if mouseX >= 650 and mouseY >= 147 and mouseX <= 770 and mouseY <= 177:
            if pygame.mouse.get_pressed()[0]:
                menuButton = False
                instructionsButton = True
            #end if
        #end if
                
        #credits Button
        if mouseX >= 780 and mouseY >= 147 and mouseX <= 900 and mouseY <= 177:
            pygame.mixer.music.unpause()
            if pygame.mouse.get_pressed()[0]:
                menuButton = False
                creditsButton = True
            #end if
        #end if
                
        #start Button
        if mouseX >= 650 and mouseY >= 112 and mouseX <= 900 and mouseY <= 142:
            if pygame.mouse.get_pressed()[0]:
                menuButton = False
                spawnTime = time.time()
                startTime = time.time()
                shootTime = time.time()
                startButton = True
            #end if
        #end if
                
        #quit Button
        if mouseX >= 650 and mouseY >= 182 and mouseX <= 900 and mouseY <= 212:
            if pygame.mouse.get_pressed()[0]:  
                gameProgram = False  # ends outer loop  (program loop)
            #end if
        #end if
    #end of Menu -------------------------------------------------------------------- end of menu
                
    #start or instructions ---------------------------------------------------------- start or instructions  
    if instructionsButton == True:       
        gameWindow.blit (instructionsBackground, (0,0))
        pygame.draw.rect(gameWindow, BUTTONS , (WIDTH - 250, 0 , 250, 30), 0)
        graphics = font1.render("Menu", 0, WHITE)
        gameWindow.blit(graphics, (845, 0) )
        pygame.display.update()
        
        (mouseX, mouseY) = pygame.mouse.get_pos()
        pygame.event.get()
        # BACK button to MENU 
        if mouseX >= 750 and mouseY >= 0 and mouseX <= 1000 and mouseY <= 30:
            if pygame.mouse.get_pressed()[0]:
                instructionsButton = False
                menuButton = True
                pygame.time.delay(100)
            #end if     
        #end if
    #end if 
    #end or instructions ------------------------------------------------------------ end or instructions

    #start of credits --------------------------------------------------------------- start of credits
    if creditsButton == True:
        gameWindow.blit (menuBackground, (0,0))
        pygame.draw.rect(gameWindow, BUTTONS , (WIDTH - 250, 0 , 250, 30), 0)
        graphics = font1.render("Menu", 0, WHITE)
        gameWindow.blit(graphics, (845, 0) )
        pygame.display.update()

        (mouseX, mouseY) = pygame.mouse.get_pos()
        pygame.event.get()
        # BACK button to MENU 
        if mouseX >= 750 and mouseY >= 0 and mouseX <= 1000 and mouseY <= 30:
            if pygame.mouse.get_pressed()[0]:
                creditsButton = False
                menuButton = True
                pygame.time.delay(100)
            #end if     
        #end if
    #end if
    #end of credits ----------------------------------------------------------------- end of credits

    #start of Enemys ---------------------------------------------------------------- start of Enemys
    if startButton == True:
        if time.time() - spawnTime >= 1.5:
            spawnTime = time.time()
            enemyX.append(random.randrange(0,WIDTH-57))
            enemyY.append(-120)
            enemyFire.append(random.randrange(2,5))
            enemyFireT.append(time.time())
        #end if
            
        gameWindow.blit (gameBackground , (0,0))# place image
        for i in range(len(enemyX)): 
            gameWindow.blit (Enemy, (enemyX[i], enemyY[i]))# place image
        #end range
        
        for i in range(len(enemyY)):
            enemyY[i] = enemyY[i] + 2
        #end range
            
        if len(enemyY) >= 1:
            if enemyY[0] >= HEIGHT:
                motherHealth = motherHealth - 10
                enemyY.pop(0)
                enemyX.pop(0)
            #end if
        #end if
                
        for i in range(len(enemyX)):
            if time.time() - enemyFireT[i] >= enemyFire[i]:
                enemyFireT[i] = time.time()
                enemyBulletX.append(enemyX[i] + 25)
                enemyBulletY.append(enemyY[i] + 20)
            #end if
        #end range
                
        for i in range(len(enemyBulletY)):
            enemyBulletY[i] = enemyBulletY[i] + 10
            gameWindow.blit(redLaser, (enemyBulletX[i], enemyBulletY[i]))# place image
        #end range
            
        for i in range(len(enemyBulletY)-1,-1,- 1):
            tempenemyLaser = pygame.Rect(enemyBulletX[i], enemyBulletY[i], 13, 51)
            tempPlayer = pygame.Rect(xuserShip , yuserShip, 57, 101)
            if tempenemyLaser.colliderect(tempPlayer) == True:
                enemyBulletX.pop(i)
                enemyBulletY.pop(i)
                userHealth = userHealth - 10
            #end if
        #end range
                
        gameGUI()
        gameWindow.blit (userShip, (xuserShip, yuserShip))# place image
        gameWindow.blit (motherShip, (xMother, yMother))# place image
        pygame.display.update()
    #end if
    #end of Enemys ------------------------------------------------------------------ end of Enemys
        
    #start of Player ---------------------------------------------------------------- start of Player
    if startButton == True:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            xuserShip = xuserShip + 10
            yuserShip = yuserShip
        # end if

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            xuserShip = xuserShip - 10
            yuserShip = yuserShip
        #end if
            
        if keys[pygame.K_SPACE]:
            if time.time() - shootTime >= 1:
                shootTime = time.time()  
                LaserX.append(xuserShip + 23)
                LaserY.append(yuserShip)
            #end if
            
        for i in range(len(LaserX)):
            LaserY[i] = LaserY[i] - 30
            
        for i in range(len(LaserX)):
            gameWindow.blit (laser, (LaserX[i], LaserY[i]))# place image
            pygame.display.update()
        
        for q in range(len(enemyX)-1,-1,-1):
            for i in range(len(LaserY)-1,-1,-1):
                tempLaser = pygame.Rect(LaserX[i], LaserY[i], 13, 51)
                tempEnemy = pygame.Rect(enemyX[q] , enemyY[q], 57, 101)
                if tempLaser.colliderect(tempEnemy) == True:
                    enemyX.pop(q)
                    enemyY.pop(q)
                    LaserX.pop(i)
                    LaserY.pop(i)
                    score = score + 100
                #end if    
                
        if xuserShip > WIDTH-57:
            xuserShip = xuserShip - 10
        #end if
            
        if xuserShip < 0:
            xuserShip = xuserShip + 10 
        #end if
            
##        for i in range(len(LaserY)):    
##            if LaserY[i] <= 0:
##            #end if
        
        if userHealth <= 0 or motherHealth <= 0:
            startButton = False
            scoreboard = True
        #end if
            
        gameGUI()
        gameWindow.blit (motherShip, (xMother, yMother))# place image
        gameWindow.blit (userShip, (xuserShip, yuserShip))# place image    
        pygame.display.update()

        end = time.time() - startTime
        endTime = format(end,'.0f')
        (mouseX, mouseY) = pygame.mouse.get_pos()
        pygame.event.get()
        # BACK button to MENU 
        if mouseX >= 960 and mouseY >= 0 and mouseX <= 996 and mouseY <= 20:
            if pygame.mouse.get_pressed()[0]:
                startButton = False
                menuButton = True
                enemyX = []
                enemyY = []
                enemyFire = []
                enemyFireT = []
                enemyBulletX = []
                enemyBulletY = []
                LaserX = []
                LaserY = []
                userHealth = 100
                motherHealth = 150
                xEnemy = 0
                yEnemy = 0
                score = 0
                xuserShip = WIDTH/2 - 30
                yuserShip = HEIGHT/2 + 100
                xMother = WIDTH/2 - 125
                yMother = HEIGHT/2 + 200
                pygame.time.delay(100)
            #end if     
        #end if
                
        if mouseX >= 920 and mouseY >= 0 and mouseX <= 950 and mouseY <= 20:
           if pygame.mouse.get_pressed()[0]:  
                gameProgram = False  # ends outer loop  (program loop)
            #end if
        #end if
    #end if
    #start of Player ---------------------------------------------------------------- start of Player
                
    #start of Scoreboard ------------------------------------------------------------ start of Scoreboard
    if scoreboard == True:
        gameWindow.blit (menuBackground , (0,0))# place image
        gameWindow.blit (gameOver, (200, 150))# place image
        scoreGUI()
##        print format(score,'.0f')
##        print format(endtime,'.0f')
        (mouseX, mouseY) = pygame.mouse.get_pos()
        pygame.event.get()
        graphics = font1.render("Score = " +str(score), 0, WHITE)
        gameWindow.blit(graphics, (650, 450) )
        graphics = font1.render("Time = " +str(endTime ), 0, WHITE)
        gameWindow.blit(graphics, (650, 500) )
        if mouseX >= 650 and mouseY >= 112 and mouseX <= 900 and mouseY <= 142:
            if pygame.mouse.get_pressed()[0]:
                scoreboard = False
                menuButton = True
                enemyX = []
                enemyY = []
                enemyFire = []
                enemyFireT = []
                enemyBulletX = []
                enemyBulletY = []
                LaserX = []
                LaserY = []
                userHealth = 100
                motherHealth = 150
                xEnemy = 0
                yEnemy = 0
                score = 0
                xuserShip = WIDTH/2 - 30
                yuserShip = HEIGHT/2 + 100
                xMother = WIDTH/2 - 125
                yMother = HEIGHT/2 + 200
                pygame.time.delay(100)
            #end if
        #end if

        if mouseX >= 650 and mouseY >= 182 and mouseX <= 900 and mouseY <= 212:
            if pygame.mouse.get_pressed()[0]:  
                gameProgram = False  # ends outer loop  (program loop)
            #end if
        #end if
                
##        pygame.time.delay(500)
        pygame.display.update()
    #end of Scoreboard -------------------------------------------------------------- end of Scoreboard

#end of game ------------------------------------------------------------------------ end of game   

# if gameProgram is False .... game is over and done!
# display gameOVer screen

pygame.display.update()

pygame.time.delay(1000)
pygame.quit()
