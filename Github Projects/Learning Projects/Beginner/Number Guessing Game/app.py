import random
import subprocess
import platform
from pyfiglet import Figlet

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def ascii_title2():
    f = Figlet(font='slant')
    return f.renderText("Thanks for playing!")

def ascii_title():
    f = Figlet(font='slant')
    return f.renderText("Guess-IT")

def menu():
    return f"""
{ascii_title()}
                Welcome User! 
               By: Evan William
"""

def endmenu():
    return f"""
{ascii_title2()}
"""


def get_hint(guess, target, difference):
    if guess == target:
        return "Perfect! You got it! 🎉"
    
    # Define hint variations for each range
    if guess < target:
        if difference <= 1:
            hints = [
                "Whoa, you're SO close! Just bump it up by one and you're golden!",
                "Dude, you're literally touching the answer! One tiny step higher!",
                "OH MY GOD, you're right there! Just add one more!"
            ]
        elif difference <= 2:
            hints = [
                "You're practically there! Maybe try going up just a smidge?",
                "So close I can taste it! The answer is like, right above you!",
                "Holy moly, you're almost there! Just a teensy bit higher!"
            ]
        elif difference <= 5:
            hints = [
                "Okay, you're getting really warm now! Try going up a little bit more!",
                "Nice, you're in the zone! The answer is hiding just a few spots up!",
                "You're cooking with gas! But you need to turn up the heat just a tad!"
            ]
        elif difference <= 10:
            hints = [
                "Not bad, not bad! You're getting warmer - try going up some more!",
                "You're on the right track! The answer is somewhere up there, keep climbing!",
                "Getting toasty! But you still need to go higher - maybe around 5-10 more?"
            ]
        elif difference <= 20:
            hints = [
                "You're starting to feel the heat! Go up a decent chunk more!",
                "Hmm, you're in the right ballpark, but aim higher - like, noticeably higher!",
                "Warming up! The answer is up there somewhere, maybe 10-20 spots higher!"
            ]
        elif difference <= 50:
            hints = [
                "You know what? You're not totally cold! But you gotta go up quite a bit more!",
                "Eh, you're getting somewhere! Try a bigger jump upward though!",
                "I mean, you're not freezing, but the answer is way up there! Keep going!"
            ]
        elif difference <= 100:
            hints = [
                "Okay, you're kinda lukewarm? But seriously, go WAY higher!",
                "You're... getting there? But like, the answer is pretty far up from here!",
                "Room temperature vibes! But you need to really crank it up!"
            ]
        elif difference <= 200:
            hints = [
                "Alright, you're not completely lost, but you're still pretty far off! Go way up!",
                "You're in the same universe as the answer, I'll give you that! But shoot much higher!",
                "Getting slightly less cold! But honestly, you need to go A LOT higher!"
            ]
        elif difference <= 500:
            hints = [
                "Ehh, you're still pretty chilly! The answer is way, way up there!",
                "You're like, barely registering on the warmth scale! Go much, much higher!",
                "Brr! Still cold! But hey, at least you're not at absolute zero anymore!"
            ]
        elif difference <= 1000:
            hints = [
                "Yikes, you're still in the arctic zone! The answer is in a totally different neighborhood!",
                "Freezing! But I believe in you - just go REALLY high!",
                "Ice cold! The answer is like, on a different planet up there!"
            ]
        else:  # difference > 1000
            hints = [
                "Ooof, you're in Antarctica while the answer is in the Sahara! Go WAY higher!",
                "Brrr! You're practically frozen solid! The answer is on another planet!",
                "Ice age cold! But don't give up - just think REALLY big numbers!"
            ]
    else:  # GUESS > TARGET
        if difference <= 1:
            hints = [
                "Oh wow, you're SO close! Just drop it down by one and you're there!",
                "Dude, you're literally one away! Just go down by one!",
                "ARE YOU KIDDING ME? You're right there! Just minus one!"
            ]
        elif difference <= 2:
            hints = [
                "You're practically sitting on the answer! Just go down a tiny bit!",
                "So close it hurts! The answer is just barely below you!",
                "You're like, breathing on the answer! Just a smidge lower!"
            ]
        elif difference <= 5:
            hints = [
                "You're really warm! Just cool it down a little bit!",
                "Nice, you're super close! The answer is hiding just below you!",
                "You're hot, hot, hot! But dial it back just a tad!"
            ]
        elif difference <= 10:
            hints = [
                "Pretty good! You're warm, but you need to come down a bit!",
                "You're on the right track! Just slide down some more!",
                "Getting toasty! But you're a little too high - come down a bit!"
            ]
        elif difference <= 20:
            hints = [
                "You're in the warm zone! But come down a good chunk!",
                "Not bad! You're in the right area, but aim lower - like, noticeably lower!",
                "Warming up! But the answer is down there somewhere, maybe 10-20 spots lower!"
            ]
        elif difference <= 50:
            hints = [
                "You're not completely cold! But you gotta come down quite a bit!",
                "Eh, you're getting somewhere! Try a bigger drop downward though!",
                "I mean, you're not freezing, but the answer is way down there!"
            ]
        elif difference <= 100:
            hints = [
                "Okay, you're kinda lukewarm? But seriously, go WAY lower!",
                "You're... getting there? But like, the answer is pretty far down from here!",
                "Room temperature vibes! But you need to really dial it down!"
            ]
        elif difference <= 200:
            hints = [
                "Alright, you're not completely lost, but you're still pretty far off! Go way down!",
                "You're in the same universe as the answer! But drop it way lower!",
                "Getting slightly less cold! But honestly, you need to go A LOT lower!"
            ]
        elif difference <= 500:
            hints = [
                "Ehh, you're still pretty chilly! The answer is way, way down there!",
                "You're like, barely registering on the warmth scale! Go much, much lower!",
                "Brr! Still cold! But hey, at least you're not at absolute zero!"
            ]
        elif difference <= 1000:
            hints = [
                "Yikes, you're still in the arctic zone! The answer is in a totally different neighborhood!",
                "Freezing! But I believe in you - just go REALLY low!",
                "Ice cold! The answer is like, on a different planet down there!"
            ]
        else:  # difference > 1000
            hints = [
                "Ooof, you're in space while the answer is underground! Go WAY lower!",
                "You're flying way too high! The answer is back on Earth somewhere!",
                "Stratosphere cold! Come back down to the real world!"
            ]
    
    # Randomly select one of the three hints for the appropriate range
    return random.choice(hints)

def play_game():
    print(menu())
    #  INPUT RANGE
    while True:
        try:
            max_num = int(input("What's the highest number I can pick? (minimum 10): "))
            if max_num < 10:
                print("Come on, make it at least 10 to keep it interesting!")
                continue
            break
        except ValueError:
            print("That's not a number! Try again!")
    
    # GENERATE NUM
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    # DIFFICULTY SCALING
    import math
    if max_num <= 10:
        max_attempts = 3
    elif max_num <= 100:
        max_attempts = max(int(math.log2(max_num)) + 1, 4)
    else:
        max_attempts = int(math.log2(max_num)) + 8

    max_attempts = min(max_attempts, 24)  # Maximum 24 attempts
    max_attempts = max(max_attempts, 3)   # Minimum 3 attempts
    
    print(f"\nOkay, I've picked a number between 1 and {max_num}!")
    print(f"You have {max_attempts} attempts to guess it!")
    print("Let's see how good you are at this!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt #{attempts + 1}: What's your guess? "))
            attempts += 1
            
            if guess < 1 or guess > max_num:
                print(f"Hey, stay between 1 and {max_num}! That doesn't count as an attempt though.")
                attempts -= 1
                continue
            
            difference = abs(guess - secret_number)
            hint = get_hint(guess, secret_number, difference)
            print(hint)
            
            if guess == secret_number:
                print(f"\nCONGRATULATIONS! 🎉")
                print(f"You found my number {secret_number} in {attempts} attempts!")
                if attempts <= 3:
                    print("Wow, you're really good at this!")
                elif attempts <= 6:
                    print("Nice job! You've got some skill!")
                elif attempts <= 10:
                    print("Well done! Good persistence!")
                else:
                    print("You got it! Better late than never!")
                break
                
        except ValueError:
            print("Please enter a number! That one doesn't count.")
            continue
    
    else:
        print(f"\nGame Over!")
        print(f"The number I was thinking of was {secret_number}")
        print("Better luck next time!")

def main():
    while True:
        clear_screen()
        play_game()
        
        while True:
            play_again = input("\nWant to play again? (yes/y or no/n): ").lower().strip()
            if play_again in ['yes', 'y']:
                print("\n" + "="*50)
                break
            elif play_again in ['no', 'n']:
                clear_screen()
                print(endmenu())
                print("This Program is supported by my beloved ❤️")
                return
            else:
                print("Just type 'yes' or 'no' please!")

if __name__ == "__main__":
    main()
