import random

def get_hint(guess, target, difference):
    if guess == target:
        return "Perfect! You got it! 🎉"
    
    # CALCULATE DIFFERENCES FOR HINTS
    if guess < target:
        if difference <= 2:
            return "Oh my gosh, you're SO close! Just a tiny bit higher!"
        elif difference <= 5:
            return "You're really close now! Go up a little more!"
        elif difference <= 10:
            return "Getting warmer! Try going higher!"
        elif difference <= 20:
            return "Not bad! You need to go higher though."
        elif difference <= 50:
            return "Too low! Think bigger!"
        else:
            return "Way too low! You're not even close yet!"
    else:  # GUESS > TARGET
        if difference <= 2:
            return "Ooh, you're super close! Just come down a bit!"
        elif difference <= 5:
            return "Almost there! Go a little lower!"
        elif difference <= 10:
            return "Getting warm! Try going lower!"
        elif difference <= 20:
            return "Pretty good guess, but go lower!"
        elif difference <= 50:
            return "Too high! Think smaller!"
        else:
            return "Way too high! Come way down!"

def play_game():
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("=" * 50)
    
    # ASK FOR RANGE
    while True:
        try:
            max_num = int(input("What's the highest number I can pick? (minimum 10): "))
            if max_num < 10:
                print("Come on, make it at least 10 to keep it interesting!")
                continue
            break
        except ValueError:
            print("That's not a number! Try again!")
    
    #  GENERATE NUM
    secret_number = random.randint(1, max_num)
    attempts = 0
    max_attempts = min(max_num // 3 + 5, 15)  # SCALE ATTEMPS
    
    print(f"\nOkay, I've picked a number between 1 and {max_num}!")
    print(f"You have {max_attempts} attempts to guess it!")
    print("Let's see how good you are at this!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt #{attempts + 1}: What's your guess? "))
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
        play_game()
        
        while True:
            play_again = input("\nWant to play again? (yes/y or no/n): ").lower().strip()
            if play_again in ['yes', 'y']:
                print("\n" + "="*50)
                break
            elif play_again in ['no', 'n']:
                print("Thanks for playing! See you next time!")
                return
            else:
                print("Just type 'yes' or 'no' please!")

if __name__ == "__main__":
    main()
