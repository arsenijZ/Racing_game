import pygame
import random
import math
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Captions and Icon
pygame.display.set_caption("8 bit highway")
icon = pygame.image.load("car.ico")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerImg = pygame.transform.scale(playerImg, (160, 160))
playerX = 325
playerY = 420
playerYCoords = [20, 220, 420]
playerYIndex = 2

# Road coordinates
roadCoords = [35, 325, 610]
roadIndex = 1

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyImg = pygame.transform.scale(enemyImg, (160, 160))
enemyX = 0
enemyY = -160
roadIndexForEnemy = random.randint(0, 2)
enemySpeed = 0.5

# Enemy 2
enemyX2 = 0
enemyY2 = -160
roadIndexForEnemy2 = random.randint(0, 2)
enemySpeed2 = 0.5

# Background
backgroundImg = pygame.image.load("background.png")

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Score
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_value = 0

# Time
time = 0


def timeToScore(time_value):
    global score_value
    if time_value % 1000 == 0:
        score_value += 1


def show_score(x, y):
    score = score_font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_score_game_over(x, y, Time):
    score = score_font.render("Your score is " + str(Time), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255)) # 0 - 255
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def enemy2(x, y):
    screen.blit(enemyImg, (x, y))


def isCollision(eY, pY, eRoad, pRoad):
    distance = pY - eY
    if 160 > distance > 20 and eRoad == pRoad:
        return True
    else:
        return False


# Game loop
running = True
while running:

    # Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressing
        if event.type == pygame.KEYDOWN and playerYIndex != 3:
            if event.key == pygame.K_LEFT:
                if roadIndex != 0:
                    roadIndex = roadIndex - 1

            if event.key == pygame.K_RIGHT:
                if roadIndex != 2:
                    roadIndex = roadIndex + 1

            if event.key == pygame.K_UP:
                if playerYIndex != 0:
                    playerYIndex = playerYIndex - 1

            if event.key == pygame.K_DOWN:
                if playerYIndex != 2:
                    playerYIndex = playerYIndex + 1

    # Enemy 1 movement
    enemyY += enemySpeed
    if enemyY >= 620:
        enemyY = -160
        enemySpeed = 0.2 + random.random()  # 0.5 - 1.5
        roadIndexForEnemy = random.randint(0, 2)

    # Enemy 2 movement
    enemyY2 += enemySpeed2
    if enemyY2 >= 620:
        enemyY2 = -160
        enemySpeed2 = 0.2 + random.random()
        roadIndexForEnemy2 = random.randint(0, 2)

    collision = isCollision(enemyY, playerY, roadIndexForEnemy, roadIndex)
    collision2 = isCollision(enemyY2, playerY, roadIndexForEnemy2, roadIndex)

    # Game Over
    if collision or collision2 or playerYIndex == 3:
        game_over_text()
        enemySpeed = 0
        enemySpeed2 = 0
        enemyY = -160
        enemyY2 = -160
        playerYCoords.append(-160)
        playerYIndex = 3
        show_score_game_over(250, 350, time//1000)

    enemy(roadCoords[roadIndexForEnemy] - 10, enemyY)
    enemy2(roadCoords[roadIndexForEnemy2] - 10, enemyY2)
    player(roadCoords[roadIndex], playerYCoords[playerYIndex])

    if playerYIndex != 3:
        time += 1

    timeToScore(time)
    show_score(10, 10)

    pygame.display.update()
