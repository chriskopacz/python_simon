#Author: Chris Kopacz
#created: 31 October 2017
#filename: hlight_squares.py
#test code for highlighting the individual squares of the simon game

import pygame
import time
import pygame.gfxdraw

GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
GREY_T = (71,71,71,127)
BLACK_T = (0,0,0,180)

#===============================user defined functions
def square_highlight(screen,a):
    #first, draw all squares
    pygame.draw.rect(screen,GREEN,(0,0,150,150),0)
    pygame.draw.rect(screen,RED,(151,0,150,150),0)
    pygame.draw.rect(screen,YELLOW,(0,151,150,150),0)
    pygame.draw.rect(screen,BLUE,(151,151,150,150),0)

    #second, draw grey/black box
    #pygame.gfxdraw.box(screen,pygame.Rect(0,0,300,300),GREY_T)
    pygame.gfxdraw.box(screen,pygame.Rect(0,0,300,300),BLACK_T)

    #depending on the value of 'a' highlight corresponding square
    if(a==1):
        pygame.draw.rect(screen,GREEN,(0,0,150,150),0)
    elif(a==2):
        pygame.draw.rect(screen,RED,(151,0,150,150),0)
    elif(a==3):
        pygame.draw.rect(screen,YELLOW,(0,151,150,150),0)
    elif(a==4):
        pygame.draw.rect(screen,BLUE,(151,151,150,150),0)
    else:
        print("error in drawing computer sequence squares, a = " + str(a))

    pygame.display.update()
    time.sleep(1)
    pygame.draw.rect(screen,GREEN,(0,0,150,150),0)
    pygame.draw.rect(screen,RED,(151,0,150,150),0)
    pygame.draw.rect(screen,YELLOW,(0,151,150,150),0)
    pygame.draw.rect(screen,BLUE,(151,151,150,150),0)
    pygame.gfxdraw.box(screen,pygame.Rect(0,0,300,300),BLACK_T)
    pygame.display.update()
    time.sleep(.25)


#=============main
def main():

    counter = 0
    pygame.init()
    screen = pygame.display.set_mode((300,300))
    #screen.fill((255,255,255))
    #pygame.gfxdraw.box(screen,pygame.Rect(0,0,200,200),(255,0,0,50))
    #pygame.display.update()

    comp_sequence = [1,1,2,1,2,3,1,2,3,4]

    while(counter<len(comp_sequence)):
        '''
        #print all squares first
        pygame.draw.rect(screen,GREEN,(0,0,150,150),0)
        pygame.draw.rect(screen,RED,(151,0,150,150),0)
        pygame.draw.rect(screen,YELLOW,(0,151,150,150),0)
        pygame.draw.rect(screen,BLUE,(151,151,150,150),0)
        #print transparent grey box
        #pygame.gfxdraw.box(screen,pygame.Rect(0,0,300,300),GREY_T)
        pygame.gfxdraw.box(screen,pygame.Rect(0,0,300,300),BLACK_T)

        #cycle through highlighting each color
        if(counter%4==0):
            pygame.draw.rect(screen,GREEN,(0,0,150,150),0)
        elif(counter%4==1):
            pygame.draw.rect(screen,RED,(151,0,150,150),0)
        elif(counter%4==2):
            pygame.draw.rect(screen,YELLOW,(0,151,150,150),0)
        elif(counter%4==3):
            pygame.draw.rect(screen,BLUE,(151,151,150,150),0)
        '''
        square_highlight(screen,comp_sequence[counter])

        #update display, pause for one second, iterate counter
        #pygame.display.update()
        #time.sleep(1)
        counter = counter + 1

    pygame.quit()
    print("exit")




#===============================
if __name__ == "__main__":
    main()
