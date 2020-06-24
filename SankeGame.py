import math
import pygame
import random
import time

# Variables
sw = sh = 600
snkx = 300
snky = 300
bgColor = (148, 0, 211)
snakeColor = (0, 128, 128)
foodColor = (255, 0, 0)
fontColor = (255, 255, 255)
x_change = 0
y_change = 0
snake_list = []
len_of_snake = 1
foodx = random.randint(25, 590)
foody = random.randint(25, 590)

# Initialization
pygame.init()
wn = pygame.display.set_mode((sw, sh))
caption = pygame.display.set_caption("Snake by Aadil")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 50)

#Function
def snk(snake_list):
    for x in snake_list:
        pygame.draw.circle(wn, snakeColor, [x[0], x[1]], 10, 0)

#Main loop
run = True
while run:
    wn.fill(bgColor)
    food = pygame.draw.circle(wn, foodColor, (foodx, foody), 8, 0)
    score = font.render("Score: " + str(len_of_snake - 1), True, fontColor)
    wn.blit(score, (200, 20))
    # Border
    border1 = pygame.draw.rect(wn, fontColor, (15, 0, 2, 600), 0)
    border2 = pygame.draw.rect(wn, fontColor, (0, 15, 600, 2), 0)
    border3 = pygame.draw.rect(wn, fontColor, (585, 0, 2, 600), 0)
    border4 = pygame.draw.rect(wn, fontColor, (0, 585, 600, 2), 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_change = -10
                x_change = 0
            if event.key == pygame.K_s:
                y_change = 10
                x_change = 0
            if event.key == pygame.K_a:
                x_change = -10
                y_change = 0
            if event.key == pygame.K_d:
                x_change = 10
                y_change = 0
    if snkx >= 575:
        snkx = 26
    if snkx <= 25:
        snkx = 575
    if snky >= 575:
        snky = 26
    if snky <= 25:
        snky = 575
    for i in snake_list[:-1]:
        if i == snake_head:
            run = False
    snkx += x_change
    snky += y_change
    snake_head = []
    snake_head.append(snkx)
    snake_head.append(snky)
    snake_list.append(snake_head)
    if len(snake_list) > len_of_snake:
        del snake_list[0]
    snk(snake_list)
    if math.pow(math.pow(snky - foody, 2) + math.pow(snkx - foodx, 2), 0.5) <= 10:
        len_of_snake += 1
        foodx = random.randint(10, 590)
        foody = random.randint(10, 590)
    clock.tick(15)
    pygame.display.update()
wn.fill(bgColor)
endText = font.render("Game over!! SCORE: " + str(len_of_snake - 1), True, fontColor)
wn.blit(endText, (50, 200))
pygame.display.update()
time.sleep(4)
