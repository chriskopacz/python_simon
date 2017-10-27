#Author: Chris Kopacz
#created: 26 October 2017
#filename: squares.py
#test code for generating the 4-colored simon squares

import pygame
from pygame.locals import *
import time

def main():
    #color values
    GREEN = (0,255,0) #upper left
    RED = (255,0,0) #upper right
    YELLOW = (255,255,0) #lower left
    BLUE = (0,0,255) #lower right

    #window dimensions
    WIN_H = 500
    WIN_W = 500
    s_h = WIN_H/2   #square height
    s_w = WIN_W/2   #square width

    #other values
    mouse_xy = (0,0)


    #if pygame is already initiated, stop it
    if pygame.display.get_init() == 1:
        pygame.display.quit()

    #initiate the screen
    screen = pygame.display.set_mode((WIN_W,WIN_H))
    #draw the squares
    pygame.draw.rect(screen,GREEN,(0,0,s_w,s_h),0) #green
    pygame.draw.rect(screen,RED,((WIN_W/2 + 1),0,s_w,s_h),0) #red
    pygame.draw.rect(screen,YELLOW,(0,(WIN_H/2 + 1),s_w,s_h),0) #yellow
    pygame.draw.rect(screen,BLUE,((WIN_H/2 + 1),(WIN_W/2 + 1),s_w,s_h),0) #blue
    pygame.display.update()
    #time.sleep(3)


    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_xy = pygame.mouse.get_pos()
                    aColor = screen.get_at(mouse_xy)
                    print(str(mouse_xy[0]) + ',' + str(mouse_xy[1]))
                    if aColor == GREEN:
                        print "green"
                    elif aColor == RED:
                        print "red"
                    elif aColor == YELLOW:
                        print "yellow"
                    elif aColor == BLUE:
                        print "blue"
                    else:
                        print('null')



    #clean exit
    pygame.quit()








if __name__ == "__main__":
    main()
