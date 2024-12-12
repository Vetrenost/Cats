import time
import os
import keyboard
import pygame

pygame.mixer.init()
pygame.mixer.music.load('Flute.wav')

def clear():
    os.system('cls')

snake = r"""
       __
      {0O}
      \__/
      /^/
     ( (              
     \_\_____
     (_______)
    (_________()Oo         
        """
        
snake2 = r"""
       __
      {0O}
      \__/
      ( |
      ( (             
      _\ \___
     (_______)
    (_________()Oo 
    """
    
snake3 = r"""
        __
       {0O}
       \__/
        (^)
        \ \            
      __|  )_
     (_______)
    (_________()Oo 
    """

snake4 = r"""
          __
         {0O}
         \__/
         ( )
         | \          
      ___(  \
     (_______)   o
    (_________()O 
    """

while True:
    pygame.mixer.music.play()
    clear()
    print(snake)
    time.sleep(0.5)
    clear()
    print(snake2)
    time.sleep(0.5)
    clear()
    print(snake3)
    time.sleep(0.5)
    clear()
    print(snake4)
    time.sleep(0.5)

    if keyboard.is_pressed('o'):
      print("ХОБА!")
      break 
