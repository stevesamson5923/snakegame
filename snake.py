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
turning_x = []
turning_y = []
def redrawwindow():
    win.fill((0,0,0))
    head.update(win)
    head.draw(win)
    
    for i in range(len(body_list)):
        body_list[i].update(win)
        body_list[i].draw(win)
        for j in range(len(turning_x)):
            if body_list[i].rect.x == turning_x[j] and body_list[i].rect.y == turning_y[j]:
                if i==0:
                    body_list[i].direction_x = head.direction_x
                    body_list[i].direction_y = head.direction_y
                else:
                    body_list[i].direction_x = body_list[i-1].direction_x
                    body_list[i].direction_y = body_list[i-1].direction_y
                    if i==len(body_list)-1:                       
                        turning_x.pop(0)
                        turning_y.pop(0)
                        break

    food.draw(win)
    pygame.display.update()
while run:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                head.image = pygame.transform.scale(pygame.image.load('head_up.png'),(SIZE,SIZE))
                head.direction_x = 0
                head.direction_y = -1
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
            if event.key == pygame.K_DOWN:
                head.image = pygame.transform.scale(pygame.image.load('head_down.png'),(SIZE,SIZE))
                head.direction_x = 0
                head.direction_y = 1
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
            if event.key == pygame.K_LEFT:
                head.image = pygame.transform.scale(pygame.image.load('head_left.png'),(SIZE,SIZE))
                head.direction_x = -1
                head.direction_y = 0
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
            if event.key == pygame.K_RIGHT:
                head.image = pygame.transform.scale(pygame.image.load('head_right.png'),(SIZE,SIZE))
                head.direction_x = 1
                head.direction_y = 0
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
            if event.key == pygame.K_r:
                pass
    redrawwindow()
pygame.quit()          