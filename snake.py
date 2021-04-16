import pygame
import random
pygame.init()

WIDTH = 700
HEIGHT = 480

win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption(' MY FIRST GAME' )
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

SIZE = 20
score = 0
class Body():
    def __init__(self,img,x,y,id):
        self.image = pygame.transform.scale(pygame.image.load(img),(SIZE,SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 1
        self.dy = 1
        self.direction_x = -1
        self.direction_y = 0
        self.id = id
    def draw(self,win):
        win.blit(self.image,self.rect)    
    def update(self,win):        
        if self.direction_x < 0 :            
            self.rect.x -= self.dx
        if self.direction_x > 0 :
            self.rect.x += self.dx
        if self.direction_y < 0:
            self.rect.y -= self.dy 
        if self.direction_y > 0: 
            self.rect.y += self.dy    
        #self.draw(win)

class Food():
    def __init__(self,x,y):        
        self.image = pygame.transform.scale(pygame.image.load('frog.png'),(SIZE,SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self,win):
        win.blit(self.image,self.rect)
    def update(self,win):
        self.draw(win)
    
run = True
head = Body('head_left.png',500,100,1)
body_list = []
for i in range(10):
    body = Body('body3.jpg',head.rect.x+SIZE*(i+1),head.rect.y,2)
    body_list.append(body)
food = Food(300,200)

direction_x = -1
direction_y = 0
turning_x = []
turning_y = []
body_collision = False
def redrawwindow():
    global score,body_collision
    win.fill((0,0,0)) 
    #check collision with body
    for i in range(len(body_list)):
        if i == 0:
            continue
        if head.rect.colliderect(body_list[i].rect):
            body_collision = True
    if not (body_collision or head.rect.x+20 >= WIDTH or head.rect.x <= 0 or head.rect.y+20>= HEIGHT or head.rect.y<=0):               
        head.update(win)    
    head.draw(win)
    #collision with food
    if head.rect.colliderect(food.rect):
        score = score + 1                      
        food.rect.x = random.randint(0,WIDTH-40)
        food.rect.y = random.randint(0,HEIGHT-40)
        last_body = len(body_list)-1
        if body_list[last_body].direction_x < 0:
            body = Body('body3.jpg',body_list[last_body].rect.x+20,body_list[last_body].rect.y,2)
            body.direction_x = body_list[last_body].direction_x
            body.direction_y = body_list[last_body].direction_y
        if body_list[last_body].direction_x > 0:
            body = Body('body3.jpg',body_list[last_body].rect.x-20,body_list[last_body].rect.y,2)
            body.direction_x = body_list[last_body].direction_x
            body.direction_y = body_list[last_body].direction_y
        if body_list[last_body].direction_y < 0:
            body = Body('body3.jpg',body_list[last_body].rect.x,body_list[last_body].rect.y+20,2)
            body.direction_x = body_list[last_body].direction_x
            body.direction_y = body_list[last_body].direction_y
        if body_list[last_body].direction_y > 0:
            body = Body('body3.jpg',body_list[last_body].rect.x,body_list[last_body].rect.y-20,2)
            body.direction_x = body_list[last_body].direction_x
            body.direction_y = body_list[last_body].direction_y

        body_list.append(body)
    count = 'Score: ' +str(score)  
    textsurface1 = myfont.render(count, False, (34, 56, 200))
    win.blit(textsurface1,(2,2))    
    #move body till turning point in given direction
    if not (body_collision or head.rect.x+20 >= WIDTH or head.rect.x <= 0 or head.rect.y+20>= HEIGHT or head.rect.y<=0):
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
    else:
        for i in range(len(body_list)):
            body_list[i].draw(win)
    food.update(win)
    pygame.display.update()

while run:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                head.image = pygame.transform.scale(pygame.image.load('head_up.png'),(SIZE,SIZE))
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
                head.direction_y = -1
                head.direction_x = 0
            if event.key == pygame.K_DOWN:
                head.image = pygame.transform.scale(pygame.image.load('head_down.png'),(SIZE,SIZE))
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
                head.direction_y = 1
                head.direction_x = 0
            if event.key == pygame.K_RIGHT:
                head.image = pygame.transform.scale(pygame.image.load('head_right.png'),(SIZE,SIZE))
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
                head.direction_x = 1 
                head.direction_y = 0
            if event.key == pygame.K_LEFT:   
                head.image = pygame.transform.scale(pygame.image.load('head_left.png'),(SIZE,SIZE))           
                turning_x.append(head.rect.x)
                turning_y.append(head.rect.y)
                head.direction_x = -1
                head.direction_y = 0
            if event.key == pygame.K_r:
                body_collision = False
                score = 0
                turning_x = []
                turning_y = []
                head = Body('head_left.png',500,100,1)
                body_list = []
                for i in range(10):
                    body = Body('body3.jpg',head.rect.x+SIZE*(i+1),head.rect.y,2)
                    body_list.append(body)
    redrawwindow()
pygame.quit()