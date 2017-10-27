#Author: Chris Kopacz
#created: 24 October 2017
#filename: simon.py
#play the 4-color, sequence repeating game using the pygame module

import pygame
from pygame.locals import *
import time
import random
import os

def main():

    #an array to store the computer generated sequence of numbers
    comp_sequence = []
    #an array to store the sequence entered by human
    human_sequence=[]
    counter = 1

    while(counter < 5):
        #temporary variable for generating random numbers
        #generate random integer s.t. 1 <= temp <= 4
        temp = random.randint(1,4)

        #add temp to the end of comp_sequence
        comp_sequence.append(temp)

        for iter in range(0,len(comp_sequence)):
            os.system('cls' if os.name == 'nt' else 'clear')
            print "-"
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear') #clear console
            print comp_sequence[iter] #print one element at a time
            time.sleep(1) #pause output for 1 second

        os.system('cls' if os.name == 'nt' else 'clear') #clear console
        user_in = raw_input("Enter the sequence:\n") #take user input
        counter = counter + 1 #increment counter



if __name__ == "__main__":
    main()
