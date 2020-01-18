from time import sleep
import keyboard
import pygame as pg
pg.init()

#переменные----------------------
width_OSwin = 1000
heigth_OSwin = 500
width_igrok = 20
heigth_igrok = 35
jump_count = 10
is_jump = False
jump_minus = 1
x_igrok = width_OSwin//2 - width_igrok
y_igrok = heigth_OSwin - heigth_igrok
speed_igrok_left = 5
speed_igrok_right = 5
igrok_left = False
igrok_right = False
#переменые окурающего мира-----------
list_x = []
list_y = []
list_w = []
list_h = []
list_c = []
#конец переменный окружающего мира---
#онец переменнных----------------

cikl_play = True
OSwin = pg.display.set_mode((width_OSwin,heigth_OSwin))
def new_object_rect(x,y,w,h,c):
    global list_x
    global list_y
    global list_h
    global list_w
    global list_c
    x = x
    y = y
    w = w
    h = h
    c = c
    list_x.append(x)
    list_y.append(y)
    list_h.append(h)
    list_w.append(w)
    list_c.append(c)
    return 1
def toch(x,y,w,h,x2,y2,w2,h2,t):
    if x < x2 + w2 and x + w + t > x2 and y < y2 + h2 and y + h + t > y2:
        return 1
    else:
        return 0 
def tochX2(x,y,w,h,x2,y2,w2,h2,t):
    if t == False:
        t = 0
    else:
        t = t
    
    if x < x2 + w2 and x + w + t > x2 and y < y2 + h2 and y + h + t > y2 and x2 < x + w and x2 + w2 + t > x and y2 < y + h and y2 + h2 + t > y:
        return 1
    else:
        return 0
def toch_jump(x,y,w,h,x2,y2,w2,h2,t):
    if y < y2 + h2 and y + h + t > y2 and x < x2 + w2 and x + w + t > x2:
        return 1 
    else:
        return 0


     

f = 0
new_object_rect(20,100,20,20,(50,255,100))
new_object_rect(700,460,40,40,(200,100,130))
while cikl_play == True:
    sleep(1/15)
    pg.display.update()
    OSwin.fill((0,0,0))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            cikl_play = False


    if keyboard.is_pressed("a"):
        igrok_left = True
        igrok_right = False

    elif keyboard.is_pressed("d"):
        igrok_right = True
        igrok_left = False
    else:
        igrok_right = False
        igrok_left = False

    if keyboard.is_pressed("w"):
        is_jump = True

    for i in range(len(list_x)):
        if igrok_left == True:
            list_x[i] += speed_igrok_left
        elif igrok_right == True:
            list_x[i] -= speed_igrok_right


    if is_jump == True:
        y_igrok -= jump_count ** jump_minus
        jump_count -= 1    

    for i in range(len(list_x)):
        f += 1
        speed_igrok_left = 5
        speed_igrok_right = 5


        if tochX2(x_igrok,y_igrok,width_igrok//2,heigth_igrok,list_x[i] - (list_w[i] // 2),list_y[i],list_w[i] // 2,list_h[i],-5) == 1:
            speed_igrok_right = 0

        elif tochX2(x_igrok,y_igrok,width_igrok//2,heigth_igrok,list_x[i] + (list_w[i] // 2),list_y[i],list_w[i] // 2,list_h[i],5) == 1:
            speed_igrok_left = 0

        elif toch_jump(x_igrok,y_igrok,width_igrok,heigth_igrok,list_x[i],list_y[i],list_w[i],list_h[i],5) == 1:
            is_jump = False
            jump_count = 10
            y_igrok -= 1

        elif y_igrok + heigth_igrok >= 498:
            jump_count = 10
            is_jump = False
            y_igrok -= 1

        else:
            y_igrok += 1










    #рисунки---------------------

        
    for i in range(len(list_x)):
        pg.draw.rect(OSwin,(list_c[i]),(list_x[i],list_y[i],list_w[i],list_h[i]))

    pg.draw.rect(OSwin,(255,100,20),(x_igrok,y_igrok,width_igrok,heigth_igrok))
    #конец рисунков-------------


    
