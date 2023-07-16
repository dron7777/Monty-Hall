import pygame
import random
import time
pygame.init()
caption = pygame.display.set_caption("Monty Hall Game ")
icon = pygame.image.load("car-toy.png")
pygame.display.set_icon(icon)
brd = pygame.image.load("images (1).jpg")
screen = pygame.display.set_mode((1200, 550))
display_surface = pygame.display.set_mode((1200, 668))
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
c=0
cnt1=0
cnt2=0
count=0
tc=0
def border():
    screen.blit(brd, (900, 26))
fnt1=pygame.font.Font('MontserratAlternates-Black.otf', 16)
def show_score():
    pr1=fnt1.render("Games Won By switching  : "+str(c),True,(0,0,0))
    screen.blit(pr1,(903,50))
    pr2=fnt1.render("Games lost By switching    : "+str(cnt1),True,(0,0,0))
    screen.blit(pr2,(903,80))
    pr3=fnt1.render("Games Won By staying      : "+str(count),True,(0,0,0))
    screen.blit(pr3,(903,113))
    pr4=fnt1.render("Games lost By staying        : "+str(cnt2),True,(0,0,0))
    screen.blit(pr4,(903,143))
    tc1=fnt1.render("Total                                      : "+str(tc),True,(0,0,0))
    screen.blit(tc1, (903, 172))


ff=False#flag checking when user clicked is true
door = pygame.image.load('cdoor.png')
background = pygame.image.load('background.jpg')
car=pygame.image.load('carimage4.png')
running = True
offset = 43
doorr = []
count=0
slp=False
j = 0
sle=0#used for time.sleep()
xx=0
opencar=False
openselec=False
flag = 0
MouseX=0
MouseY=0
r1=0
fl=0
n=0
d=8
press=False
d2=0
sk=0
dd=0
fina=0
h=True
open_door = pygame.image.load('open_.png')
redcar = pygame.image.load("carimage4.png")
goat=pygame.image.load('goat.png')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Enter No of doors you to play the game', True, green, blue)
textRect = text.get_rect()
text1 = font.render('Press 1 to switch and 2 to Stay', True, green, blue)
textRect = text1.get_rect()
X=1200
Y=668
t1=0
press=False
t=True
textRect.center = (X // 2, Y // 2)
while running:
    screen.blit(background, (0, 0))
    if t == True:
        display_surface.blit(text, textRect) #for asking the number of dd

    if h == True:
      for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_4:
                n = 4
                d = 1
                fl=1
                t=False
                h = False
            if event.key == pygame.K_6:
              n=6
              d=1
              fl=1
              t = False
              h = False
            if event.key == pygame.K_3:
              n=3
              d=1
              fl=1
              t = False
              h = False
            if event.key == pygame.K_5:
              n=5
              d=1
              fl=1
              t = False
              h = False
    #print(n)
    border()
    show_score()
    if d== 1:
      for i in range(n):
        screen.blit(door, (i * 43 + i * 143 + 43, 220))
        sum = i * 43 + i * 143 + 43
        #print(sum)
        doorr.insert(i, sum)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            #print("x = {}, y = {}".format(pos[0], pos[1]))
            pp = pos[0]
            press=True
            xx=173
            if pp > 43+xx and pp < 229+xx:
                d2 = 1
            if pp > 229+xx and pp < 415+xx:
                d2 = 2
            if pp > 415+xx and pp < 601+xx:
                d2 = 3
            if pp > 601+xx and pp < 787+xx:
                d2 = 4
            if pp > 787+xx and pp < 973+xx:
                d2 = 5
            if pp>973+xx:
                d2=6
            if fl == 1:
                r1 = random.randint(1, n-1)
                print(r1)
                print(d2)
                t1=r1
                ss = r1*43 + r1 * 143 + 43
            if r1 == d2:
                fina=1
                if d2+1 < n:
                  d2=d2+1
                else:
                  d2=d2-1
                print("same")
            sk = ss  #position of x axis of random door in which the car was inserted;
            fl = 0
            #print(r1)
            dd = d2 * 43 + d2 * 143 + 43#position of user selected door
            flag=1
            d=3
    j=0
    if flag == 1:
        screen.blit(background, (0, 0))
        if openselec == True:
            dd = 0
            text3 = font.render('You lost', True, green, blue)
            textRect = text3.get_rect()
            display_surface.blit(text3, textRect)
            ff=True
        for i in doorr:
            j=j+1
            #print(i)
            #print("Position is ",pos[0])
            if i!=dd and i!=ss:

             screen.blit(goat, (i+5, 300+100))
             screen.blit(open_door, (i, 220))
        if ff==True:
            sle = sle + 1
            if sle == 3:
                #pygame.display.update()
                time.sleep(5)
                slp = True
        if opencar == True:
            sk = 0
        for i in range(n):
         sum = i * 43 + i * 143 + 43
         if  sum==dd or sum==sk:
            screen.blit(door, (i * 43 + i * 143 + 43, 220))
         if opencar==True:
            text2 = font.render('You Won', True, green, blue)
            textRect = text2.get_rect()
            display_surface.blit(text2, textRect)
            su = t1 * 43 + t1 * 143 + 43
            screen.blit(car, (su+10, 220+180))
            screen.blit(open_door, (su, 220))
            sle=sle+1
            if sle == 3:
                pygame.display.update()
                flag=0
                time.sleep(5)
                slp=True




    if press==True:
        text1 = font.render('Press 1 to switch and 2 to Stay', True, green, blue)
        textRect = text1.get_rect()
        display_surface.blit(text1, textRect)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    if fina==1:
                        openselec=True#you lost
                        press=False
                        cnt1 = cnt1 + 1
                        print("Games lost by switching", cnt1)
                    else:
                      opencar=True #you won by switching  #open the door of the random number generated where the car is present r1
                      c = c + 1
                      print("games won by switching->", c)
                      press=False
                if event.key == pygame.K_2:
                    if fina==1:
                        opencar=True# you won by staying
                        count = count + 1
                        print("games won->", count)
                        press=False
                    else:
                        openselec=True #
                        cnt2 = cnt2 + 1
                        print("Games lost by staying", cnt2)
                        press = False
    tc=count+c+cnt1+cnt2
    if slp == True:
        T = True
        #screen.blit(background, (0, 0))
        running = True
        offset = 43
        doorr = []
        j = 0
        xx = 0
        di = 0
        rest = 0
        flag = 0
        MouseX = 0
        MouseY = 0
        n1 = 0
        r1 = 0
        fl = 0
        n = 0
        d = 8
        press = False
        d2 = 0
        sk = 0
        fina = 0
        car_id = 0
        h = True
        t1 = 0
        ddd = 0
        press = False
        t = True
        opencar=False
        sle=0
        ff=False
        openselec=False
        slp=False



    #print(d2)
    #print(r1)
    pygame.display.update()

