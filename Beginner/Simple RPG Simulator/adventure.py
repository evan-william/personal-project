import inquirer
from menus import clear_screen, menuplains, menugrave, menucave
from enemies import generate_enemy, display_enemies
from battle import battle  
from stats import get_stats 
import time

def startadventure():
    adventure = [
        inquirer.List(
            "action1",
            message="Choose a map to begin!",
            choices=["Plains", "Graveyard", "Cave", "Return"]
        )
    ]
    answer = inquirer.prompt(adventure)

    if answer["action1"] == "Plains":
        Plains()
    elif answer["action1"] == "Graveyard":
        Graveyard()
    elif answer["action1"] == "Cave":
        Cave()
    else:
        clear_screen()
        from logic import begin
        begin()

def Plains():
    clear_screen()
    print("🌿 You entered the Plains...")
    print(menuplains()) 

    player = get_stats()  
    enemies = generate_enemy("Plains") 
    display_enemies(enemies)  

    print("\n⚔️ Prepare for battle! ⚔️")
    time.sleep(5)
    clear_screen()
    result = battle(player, enemies)  

    handle_battle_result(result) 

def Graveyard():
    clear_screen()
    print("🪦 You entered the Graveyard...")
    print(menugrave())  

    player = get_stats()
    enemies = generate_enemy("Graveyard")
    display_enemies(enemies)

    print("\n⚔️ Prepare for battle! ⚔️")
    time.sleep(5)
    clear_screen()
    result = battle(player, enemies)

    handle_battle_result(result)

def Cave():
    clear_screen()
    print("🕳️ You entered the Cave...")
    print(menucave())  

    player = get_stats()
    enemies = generate_enemy("Cave")
    display_enemies(enemies)

    print("\n⚔️ Prepare for battle! ⚔️")
    time.sleep(5)
    clear_screen()
    result = battle(player, enemies)

    handle_battle_result(result)

def handle_battle_result(result):
    if result == "Victory":
        print("\n🎉  You survived the battle!")
    elif result == "Defeat":
        print("\n☠️  You lost the battle...")
        exit()  
    elif result == "Fled":
        print("\n🏃  You successfully ran away!")

    time.sleep(2)
    clear_screen()
    startadventure() 
