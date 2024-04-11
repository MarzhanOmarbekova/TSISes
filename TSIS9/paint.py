"""3 Paint.
Extend example project from Lab 8 and add following tasks:

Draw square
Draw right triangle
Draw equilateral triangle
Draw rhombus
Comment your code"""

import pygame as pg
import math

pg.init()

height = 600
width = 800

screen = pg.display.set_mode((width,height))
base_layer = pg.Surface((width,height))
base_layer.fill('white')

LMBpressed = False

thickness = 2
currX = 0
currY = 0
prevX = 0
prevY = 0

draw_all_False = {
    "drawLine" : False, 
    "drawCircle" : False, 
    "drawRect" : False, 
    "eraser" : False, 
    "drawSquare" : False, 
    "drawRightTriangle" : False, 
    "drawTriangle" : False, 
    "drawRhombus" : False , 
    "drawEqTriangle" : False
}
draw = draw_all_False.copy()

screen.fill((255,255,255))

colorRED = (255,0,0)
colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0,0,255)
colorYELLOW = (255,255,0)
drawing_color = colorBLACK

class Botton():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    # function draws rect on given surface
    def draw(self , win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pg.draw.rect(win, colorBLACK, (self.x, self.y, self.width, self.height), 2)
    
    # checking 
    def clicked (self, pos):
        x , y = pos
        if not(x >= self.x and x <= self.x+self.width):
            return False
        if not(y >= self.y and y <= self.y+self.height):
            return False
        return True

botton_len = 20
bottons = [
    Botton(710, 10, botton_len, botton_len, colorRED),
    Botton(740, 10, botton_len, botton_len, colorBLACK),
    Botton(770, 10, botton_len, botton_len, colorBLUE),
    Botton(710, 40, botton_len, botton_len, colorGREEN),
    Botton(740, 40, botton_len, botton_len, colorWHITE),
    Botton(770, 40, botton_len, botton_len, colorYELLOW)
]

#drawing menu
for botton in bottons:
    botton.draw(screen)
    botton.draw(base_layer)

#dividing line the menu and  surface to draw
pg.draw.line(screen, colorBLACK, (0,70), (800,70))
pg.draw.line(base_layer, colorBLACK, (0,70), (800,70))


def coor_circle_center(currX, currY, prevX, prevY):
    maxX = max(prevX, currX)
    maxY = max(prevY, currY)
    minX = min(prevX, currX)
    minY = min(prevY, currY)
    return tuple((((maxX - minX)/2)+minX , ((maxY- minY)/2)+minY )), (maxX - minX)/2

def calculate_triangle_points(x1, y1, x2, y2):
    # Assigning the y coordinate of the second point to the y coordinate of the first point;
    # this way we assure that our bottom side is always at 0 degrees
    y1 = y2
    # Midpoint of the bottom side, from (x1, y1) to (x2, y2)
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    
    # Side length 
    side_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Height
    height = (math.sqrt(3) / 2) * side_length
    
    # Position of the third point
    third_x = mid_x 
    third_y = mid_y - height
    
    return [(x1, y1), (x2, y2), (third_x, third_y)]

done = False 
while not done :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_EQUALS:
                thickness += 1
            if event.key == pg.K_MINUS:
                thickness -= 1
            if event.key == pg.K_r:
                draw = draw_all_False.copy()
                draw['drawRect'] = True
            elif event.key == pg.K_c:
                draw = draw_all_False.copy()
                draw['drawCircle'] = True    
            elif event.key == pg.K_l:
                draw = draw_all_False.copy()
                draw['drawLine'] = True
            elif event.key == pg.K_e:
                draw = draw_all_False.copy()
                draw['eraser'] = True
            elif event.key == pg.K_s: #when key == s , can draw square
                draw = draw_all_False.copy()
                draw['drawSquare'] = True
            elif event.key == pg.K_9: #when key == 9
                draw = draw_all_False.copy()
                draw['drawRightTriangle'] = True
            elif event.key == pg.K_t: #when key == 9
                draw = draw_all_False.copy()
                draw['drawTriangle'] = True
            elif event.key == pg.K_x: 
                draw = draw_all_False.copy()
                draw['drawRhombus'] = True
            elif event.key == pg.K_3: 
                draw = draw_all_False.copy()
                draw['drawEqTriangle'] = True
        
        #checking if sth was chosen from menu
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1]<70: 
            for botton in bottons:
                if botton.clicked(event.pos):
                    drawing_color = botton.color # changing color to botton's color

        # to not to save every drawing , when mouse moving
        if LMBpressed:
            screen.blit(base_layer, (0,0))

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1]>70:
            # print("lmb pressed")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            # to draw dot when we just press and release in the beginning
            if draw['drawLine'] : 
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pg.MOUSEMOTION:
            if LMBpressed :  
                # changing current position to mouse's pos
                currX = event.pos[0]
                currY = event.pos[1]

                # calculating top left 
                min_X = min(prevX, currX)
                min_Y = min(prevY, currY) 

                # absolute value of difference of changes in x and y
                abs_dx = abs(currX-prevX)
                abs_dy = abs(currY-prevY) 

                if draw['drawRect']:
                    pg.draw.rect(screen,drawing_color, (min_X, min_Y, abs_dx, abs_dy), thickness)
                if draw['drawCircle']:
                    tup,  rad = coor_circle_center(currX, currY, prevX, prevY)
                    pg.draw.circle(screen, drawing_color, tup, rad, thickness)
                if draw['drawLine']:
                    pg.draw.line(screen,drawing_color, (prevX,prevY), (currX,currY) , thickness )
                if draw['eraser']:
                    pg.draw.rect(screen,'white', (currX,currY, thickness,thickness))
                    base_layer.blit(screen, (0,0))
                if draw['drawSquare'] :
                    pg.draw.rect(screen, drawing_color, (min_X, min_Y, max(abs_dy, abs_dx), max(abs_dy, abs_dx) ), thickness )
                if draw['drawRightTriangle'] :
                    if prevX < currX:
                        if prevY < currY :
                            pg.draw.lines(screen, drawing_color, True, list(((prevX,prevY),(prevX,currY),(currX, currY))) ,thickness)
                        else:
                            pg.draw.lines(screen, drawing_color, True, list(((prevX,prevY),(prevX,currY),(currX, prevY))) ,thickness)
                    else:
                        if prevY < currY :
                            pg.draw.lines(screen, drawing_color, True, list(((prevX,currY),(currX,currY),(currX, prevY))) ,thickness)
                        else:
                            pg.draw.lines(screen, drawing_color, True, list(((prevX,prevY),(currX,currY),(currX, prevY))) ,thickness)
                if draw['drawTriangle'] :
                    if prevX < currX:
                        if prevY < currY :
                            pg.draw.polygon(screen, drawing_color , list(((prevX+(currX-prevX)/2,prevY),(prevX,currY),(currX, currY))) ,thickness)
                        else:
                            pg.draw.polygon(screen, drawing_color , list(((prevX,prevY),(prevX+(currX- prevX)/2, currY ),(currX, prevY))) ,thickness)
                    else:
                        if prevY < currY :
                            pg.draw.polygon(screen, drawing_color , list(((currX+(prevX-currX)/2,prevY),(currX,currY),(prevX, currY))) ,thickness)
                        else:
                            pg.draw.polygon(screen, drawing_color , list(((prevX,prevY),(currX+(prevX-currX)/2,currY),(currX, prevY))) ,thickness)
                if draw['drawRhombus'] :
                    if prevX < currX:
                        if prevY < currY :
                            pg.draw.polygon(screen, drawing_color , list(((prevX+(abs_dx/2),prevY),(prevX,prevY+abs_dy/2 ),(prevX+(abs_dx/2), currY),( currX,prevY+(abs_dy/2)))) ,thickness)
                        else:
                            pg.draw.polygon(screen, drawing_color , list(((prevX+(abs_dx/2),prevY),(currX, currY+abs_dy/2 ),(prevX+abs_dx/2, currY), (prevX ,currY+abs_dy/2 ))) ,thickness)
                    else:
                        if prevY < currY :
                            pg.draw.polygon(screen, drawing_color , list(((currX+(abs_dx/2),prevY),(prevX,prevY+abs_dy/2 ),(prevX-(abs_dx/2), currY),( currX,currY-(abs_dy/2)))) ,thickness)
                        else:                           
                            pg.draw.polygon(screen, drawing_color , list(((prevX-abs_dx/2,prevY),(prevX,currY+abs_dy/2),(currX+abs_dx/2, currY),(currX,currY+abs_dy/2))) ,thickness)
                if draw['drawEqTriangle']:
                    pg.draw.polygon(screen, drawing_color , calculate_triangle_points (prevX,prevY,currX,currY), thickness)
                    
        
        if event.type == pg.MOUSEBUTTONUP and event.button == 1 and event.pos[1]>70:
            # print("lmb is released")
            LMBpressed = False
            if not draw['drawLine']: # last pos for figures , etc
                currX = event.pos[0]
                currY = event.pos[1]
            if draw['drawRect']:
                pg.draw.rect(screen,drawing_color, (min(prevX, currX), min(prevY, currY), abs(currX-prevX), abs(currY-prevY) ), thickness)
            if draw['drawCircle']:
                tup,  rad = coor_circle_center(currX, currY, prevX, prevY)
                pg.draw.circle(screen, drawing_color, tup, rad, thickness)
            if draw['drawSquare'] :
                pg.draw.rect(screen, drawing_color , (min(prevX,currX), min(prevY,currY), max(abs(prevY-currY) , abs(currX-prevX)) , max(abs(prevY-currY) , abs(currX-prevX)) ) , thickness )
            if draw['drawRightTriangle'] :
                if prevX < currX:
                    if prevY < currY :
                        pg.draw.lines(screen, drawing_color , True, list(((prevX,prevY),(prevX,currY),(currX, currY))) ,thickness)
                    else:
                        pg.draw.lines(screen, drawing_color , True, list(((prevX,prevY),(prevX,currY),(currX, prevY))) ,thickness)
                else:
                    if prevY < currY :
                        pg.draw.lines(screen, drawing_color , True, list(((prevX,currY),(currX,currY),(currX, prevY))) ,thickness)
                    else:
                        pg.draw.lines(screen, drawing_color , True, list(((prevX,prevY),(currX,currY),(currX, prevY))) ,thickness)
            if draw['drawTriangle'] :
                if prevX < currX:
                    if prevY < currY :
                        pg.draw.polygon(screen, drawing_color , list(((prevX+(currX-prevX)/2,prevY),(prevX,currY),(currX, currY))) ,thickness)
                    else:
                        pg.draw.polygon(screen, drawing_color , list(((prevX,prevY),(prevX+(currX- prevX)/2, currY ),(currX, prevY))) ,thickness)
                else:
                    if prevY < currY :
                        pg.draw.polygon(screen, drawing_color , list(((currX+(prevX-currX)/2,prevY),(currX,currY),(prevX, currY))) ,thickness)
                    else:
                        pg.draw.polygon(screen, drawing_color , list(((prevX,prevY),(currX+(prevX-currX)/2,currY),(currX, prevY))) ,thickness)
            if draw['drawRhombus'] :
                if prevX < currX:
                    if prevY < currY :
                        pg.draw.polygon(screen, drawing_color , list(((prevX+(abs_dx/2),prevY),(prevX,prevY+abs_dy/2 ),(prevX+(abs_dx/2), currY),( currX,prevY+(abs_dy/2)))) ,thickness)
                    else:
                        pg.draw.polygon(screen, drawing_color , list(((prevX+(abs_dx/2),prevY),(currX, currY+abs_dy/2 ),(prevX+abs_dx/2, currY), (prevX ,currY+abs_dy/2 ))) ,thickness)
                else:
                    if prevY < currY :
                        pg.draw.polygon(screen, drawing_color , list(((currX+(abs_dx/2),prevY),(prevX,prevY+abs_dy/2 ),(prevX-(abs_dx/2), currY),( currX,currY-(abs_dy/2)))) ,thickness)
                    else:                           
                        pg.draw.polygon(screen, drawing_color , list(((prevX-abs_dx/2,prevY),(prevX,currY+abs_dy/2),(currX+abs_dx/2, currY),(currX,currY+abs_dy/2))) ,thickness)

            if draw['drawEqTriangle']:
                pg.draw.polygon(screen, drawing_color , calculate_triangle_points (prevX,prevY,currX,currY) ,thickness)

            # saving after drawing
            base_layer.blit(screen, (0,0))
    
    if draw['drawLine']: 
        prevX = currX
        prevY = currY
        #to save every (line) mousemotion 
        base_layer.blit(screen, (0,0))
    
    pg.display.flip()