#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 11:57:28 2022

@author: rajgupta
"""

from PIL import Image
import random
end=100
def show_board():
    img = Image.open('snake.jpeg')
    img.show()
show_board()
def check_ladder(points) :
    if points==1:
        print('Ladder')
        return 38
    elif points==4:
        
        print('ladder')
        return 14
    elif points==9:
        print('ladder')
        return 31
    elif points==21:
        print('ladder')
        return 42
    elif points==28:
        print('ladder')
        return 84
    elif points==51:
        print('ladder')
        return 67
    elif points==71:
        print('ladder')
        return 91
    
    elif points==80:
        print('ladder')
        return 100
        
    else:
        #no ladder
       return points
   
def check_snake(points):
     if points==17:
        print('snake')
        return 7
     elif points==54:
        print('snake')
        return 34
    
     elif points==62:
        print('snake')
        return 19
    
     elif points==64:
        print('snake')
        return 60
    
     elif points==87:
        print('snake')
        return 24
    
     elif points==93:
        print('snake')
        return 73
    
     elif points==95:
        print('snake')
        return 75
     elif points==98:
        print('snake')
        return 78
     else:
        #no snake 
        return points
def reached_end(points):
    if points==end:
        return True
    else:
        return False
        
def play():
    #input player 1 name 
    p1_name = input('Player 1 , Please enter your name:')
    #input player 2 name
    p2_name = input('Player 2 , Please enter your name:')
    #INTIAL POINTS OF PLAYER 1 
    pp1= 0
    #INTIAL POINTS OF PLAYER 2
    pp2=0
    
    turn=0
    
    while(1):
        if turn%2==0:
            # Player 1 turn
            print(p1_name,'your turn')
            #ask player to countinue
            c = input('Press 1 to continue,0 to quit:')
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quitting the game ,Thanks for playing')
                break
            #generate a random number from 1,2,3,4,5,6
            dice = random.randint(1,6)
            print('Dice snowed:',dice)
            #add points
            pp1 = pp1 + dice
            
            pp1 = check_ladder(pp1)
            
            pp1 = check_snake(pp1)
            #check if the player reach beyond the board 
            
            if pp1 >end:
                pp1=end
            
            print(p1_name,'Your score:',pp1)
            
            if reached_end(pp1):
               print(pp1,'Won')
               break
            turn=turn+1 
        else:
            # Player 2 turn
            print(p2_name,'your turn')
            #ask player to countinue
            c = input('Press 1 to continue,0 to quit:')
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quitting the game ,Thanks for playing')
                break
            #generate a random number from 1,2,3,4,5,6
            dice = random.randint(1,6)
            print('Dice snowed:',dice)
            #add points
            pp2 = pp2 + dice
            
            pp2 = check_ladder(pp2)
            
            pp2 = check_snake(pp2)
            #check if the player reach beyond the board 
            
            if pp2 >end:
                pp2=end
            
            print(p2_name,'Your score:',pp2)
            
            if reached_end(pp2):
               print(p2_name,'Won')
               
               break
            turn=turn+1            
 
play()