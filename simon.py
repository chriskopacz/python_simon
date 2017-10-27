#Author: Chris Kopacz
#created: 24 October 2017
#filename: simon.py
#play the 4-color, sequence repeating game using the pygame module

import pygame
from pygame.locals import *
import time
import random
import os

#function to clear the console
def clear_con():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    random.seed(a=None) #make more random!
    #an array to store the computer generated sequence of numbers
    comp_sequence = []
    #an array to store the sequence entered by human
    human_sequence=[]
    counter = 1
    correct_check = 1
    correct_count = 0

    #while1
    #while(counter < 5 and correct_check == 1): #testing loop
    while(correct_check == 1): #real loop
        #temporary variable for generating random numbers
        #generate random integer s.t. 1 <= temp <= 4
        temp = random.randint(1,4)

        #add temp to the end of comp_sequence
        comp_sequence.append(temp)

        #this printing loop is just for testing
        #it will be modified to output the sequence via pygame in the future
        for iter in range(0,len(comp_sequence)):
            clear_con()
            print "comp:\n-"
            time.sleep(.5)
            clear_con()
            print "comp:"
            print comp_sequence[iter] #print one element at a time
            time.sleep(1) #pause output for 1 second

        clear_con()
        user_in = raw_input("Enter the sequence:\n") #take user input
        user_list = user_in.split(' ') #store user in in a list
        for iter in range(0,len(user_list)):
            human_sequence.append(int(user_list[iter]))

        #compare the computer's sequence to the human's sequence
        #update correct check as necessary
        #correct_check = 1 -> human got it right
        #correct_check = 0 -> human got it wrong
        if(len(human_sequence) == len(comp_sequence)):
            if(human_sequence == comp_sequence):
                clear_con()
                print "correct\n"
                #while loop to clear the human_sequence array
                while(len(human_sequence) != 0):
                    human_sequence.pop()
                correct_count = correct_count + 1
                time.sleep(2)
            else:
                clear_con()
                print "incorrect\n"
                correct_check = 0
                time.sleep(2)
        else:
            clear_con()
            print "incorrect\n"
            correct_check = 0
            time.sleep(2)

        counter = counter + 1 #increment counter
    #while1

    clear_con()
    print "end of game"
    print "final score: " + str(correct_count)

if __name__ == "__main__":
    main()
