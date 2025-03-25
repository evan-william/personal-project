import random
import inquirer
from stats import get_stats, gain_experience

Round = 1
def battle(player, enemies):
    player = get_stats
    print("\n⚔️  Battle Started!")
    display_enemies(enemies)

    defending = False  

    while True:
        print("\n🎮 Your Turn!")
        print(f"Round: {Round}")
        player = get_stats()
        player_action = player_turn()

        if player_action == "Attack":
            attack_enemy(player, enemies)
        elif player_action == "Defend":
            defending = True
            player["defense"] *= 2 
            print("🛡️ You brace yourself for incoming attacks!")
        elif player_action == "Flee":
            if random.random() < 0.5:  
                print("🏃 You successfully escaped!")
                return "Fled"
            else:
                print("❌ Escape failed! The enemies block your way!")

        enemies = [enemy for enemy in enemies if enemy["health"] > 0]
        if not enemies:
            print("\n🎉 You have defeated all enemies!")
            return "Victory"

        print("\n💀 Enemy Turn!")
        enemy_attack(player, enemies)

        if defending:
            player["defense"] //= 2  
            defending = False

        if player["health"] <= 0:
            print("\n☠️  You have been defeated...")
            return "Defeat"

def player_turn():
    choices = [
        inquirer.List(
            "action",
            message="Choose your action!",
            choices=["Attack", "Defend", "Flee"]
        )
    ]
    answer = inquirer.prompt(choices)
    return answer["action"]

def attack_enemy(player, enemies):
    choices = [
        inquirer.List(
            "enemy",
            message="Choose an enemy to attack!",
            choices=[f"{enemy['name']} (HP: {enemy['health']})" for enemy in enemies]
        )
    ]
    answer = inquirer.prompt(choices)
    
    enemy_name = answer["enemy"].split(" (")[0]
    enemy = next(e for e in enemies if e["name"] == enemy_name)

    is_crit = random.random() < 0.1
    damage_multiplier = 1

    if is_crit:
        damage_multiplier = 3

    damage = max(1, player["attack"] - enemy["defense"]) * damage_multiplier
    enemy["health"] -= damage 
    
    if is_crit:
        print(f"\n⚔️ You land a critical to {enemy['name']} for {damage} damage!")
    else:
        print(f"\n⚔️ You attack {enemy['name']} for {damage} damage!")

    if enemy["health"] <= 0:
        exp_reward = random.randint(10, 25) 
        gold_reward = random.randint(5, 15)  
        print(f"💀  {enemy['name']} has been defeated!")
    
        gain_experience(exp_reward, gold_reward)  


def enemy_attack(player, enemies):
    global Round
    
    alive_enemies = [enemy for enemy in enemies if enemy["health"] > 0]

    if alive_enemies:  
        attacking_enemy = random.choice(alive_enemies) 
        
        damage = max(1, attacking_enemy["attack"] - player["defense"])
        player["health"] -= damage
        print(f"⚔️  {attacking_enemy['name']} attacks you for {damage} damage!")
        print(f"❤️ Your current health: {player['health']}")
        
    Round += 1  

def display_enemies(enemies):
    print("\n👹 Enemies in Battle:")
    for i, enemy in enumerate(enemies, start=1):
        rarity = " (RARE!)" if enemy.get("rare", False) else ""
        print(f"\n⚔️  Enemy {i}: {enemy['name']}{rarity} (Level {enemy['level']})")
        print(f"  - Health: {enemy['health']}")
        print(f"  - Attack: {enemy['attack']}")
        print(f"  - Defense: {enemy['defense']}")
