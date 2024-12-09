import time
import os
import keyboard

def clear():
    os.system('cls')

cat = r"""
        /\     /\       мур
       {  `---'  }     
 мур   {  O   O  }       
       ~~>  V  <~~  
         `-----'____  мур
         /     \    \_ 
        {       }\  )_\      мур
        |  \_/  ) / /   
        \__/  /(_/     
          (__/           
        """
        
cats = r"""
        /\     /\       
 мур   {  `---'  }     мур
       {  _   _  }  мур     
       ~~>  3  <~~  
         `-----'____ 
    мур  /     \    \____
        {       }\ _______)
        / \_/  )\  \
        |  |/  /  \  \
        (__(__/    (__|    
    """

while True:
    clear()
    print(cat)
    time.sleep(0.5)
    clear()
    print(cats)
    time.sleep(0.5)
    if keyboard.is_pressed('o'):
      print("ХОБА!")
      break 
