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

class Body():
    def __init__(self,img,x1,y1):
        self.image = pygame.transform.scale(pygame.image.load(img),(SIZE,SIZE))
        self.rect = self.image.get_rect() 
        self.rect.x = x1
        self.rect.y = y1
        self.dx = 1
        self.dy = 1
        self.direction_x = -1  #-1 means left  , and 1 means right
        self.direction_y = 0  # -1 means up and 1 means down
    def draw(self,win):
        win.blit(self.image,self.rect)
    def update(self,win):
        if self.direction_x < 0:  # left
            self.rect.x = self.rect.x - self.dx
        if self.direction_x > 0:
            self.rect.x = self.rect.x + self.dx
        if self.direction_y < 0:  # UP
            self.rect.y = self.rect.y - self.dy
        if self.direction_y > 0:    #Down
            self.rect.y = self.rect.y + self.dy

class Food():
    def __init__(self,x1,y1):
        self.image = pygame.transform.scale(pygame.image.load('frog.png'),(SIZE,SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x1 
        self.rect.y = y1
    def draw(self,win):
        win.blit(self.image,self.rect)
    def update(self,win):
        self.draw(win)    
run = True

head = Body('head_left.png',500,200)
body_list = []
for i in range(10):
    body = Body('body3.jpg',head.rect.x+SIZE*(i+1),head.rect.y)
    body_list.append(body)

food = Food(300,200)

def redrawwindow():
    win.fill((0,0,0))
    head.update(win)
    head.draw(win)
    for i in range(len(body_list)):
        body_list[i].update(win)
        body_list[i].draw(win)
    food.draw(win)
    pygame.display.update()
while run:
    redrawwindow()
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