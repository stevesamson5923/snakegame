import pygame
pygame.init()

WIDTH = 700
HEIGTH = 480

win = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption('My Third Game -Snake')
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS',30)

SIZE = 20
score = 0




while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_r:
                pass
pygame.quit()          