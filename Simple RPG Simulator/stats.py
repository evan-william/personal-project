import random
import inquirer
from menus import clear_screen

# Player Stats
player_stats = {
    "level": 1,
    "health": 100,
    "max_health": 100,
    "attack":7,
    "defense": 3,
    "gold": 0,
    "experience": 0,
    "equipment": {
        "weapon": None,
        "armor": None
    }
}

shop_items = {
    "weapon": [
        {"name": "Wood Sword", "attack": 2, "price": 5},
        {"name": "Wood Spear", "attack": 3, "price": 10},
        {"name": "Pole", "attack": 4, "price": 30},
        {"name": "Iron Sword", "attack": 5, "price": 50},
        {"name": "Golden Sword", "attack": 8, "price": 85},
        {"name": "Steel Sword", "attack": 10, "price": 100},
        {"name": "Halberd", "attack": 15, "price": 250},
        {"name": "Legendary Blade", "attack": 20, "price": 500}
    ],
    "armor": [
        {"name": "Robe", "defense": 1, "price": 5},
        {"name": "Leather Armor", "defense": 3, "price": 30},
        {"name": "Chain Armor", "defense": 4, "price": 50},
        {"name": "Iron Armor", "defense": 7, "price": 65},
        {"name": "Golden Armor", "defense": 10, "price": 90},
        {"name": "Diamond Armor", "defense": 12, "price": 120},
        {"name": "Brute Tank Armor", "defense": 15, "price": 280},
        {"name": "Dragon Plate", "defense": 20, "price": 800}
    ]
}

def level_up():
    player_stats["level"] += 1
    player_stats["experience"] -= 100  
    health_increase = random.randint(5, 15)  
    player_stats["max_health"] += health_increase
    player_stats["health"] = player_stats["max_health"]  # Restore full health after level up
    player_stats["attack"] += random.randint(2, 5)
    player_stats["defense"] += random.randint(1, 3)
    print(f"🎉 You leveled up! Now at Level {player_stats['level']}!")
    print(f"❤️ Max Health increased by {health_increase}!")

def gain_experience(exp, gold):
    player_stats["experience"] += exp
    player_stats["gold"] += gold
    print(f"✨ You gained {exp} EXP and {gold} Gold!")

    while player_stats["experience"] >= 100:
        level_up()

def get_stats():
    return player_stats

def seestats():
    print(f"\n📜 Player Stats - Level {player_stats['level']}")
    print(f"❤️ Health: {player_stats['health']}")
    print(f"⚔️ Attack: {player_stats['attack']}")
    print(f"🛡 Defense: {player_stats['defense']}")
    print(f"💰 Gold: {player_stats['gold']}")
    print(f"🌟 Experience: {player_stats['experience']}")

    weapon = player_stats["equipment"]["weapon"] or "No Weapon Equipped"
    armor = player_stats["equipment"]["armor"] or "No Armor Equipped"
    
    print(f"🗡 Weapon: {weapon}")
    print(f"🛡 Armor: {armor}\n")

    while True:
        choice = [
            inquirer.List(
                "back",
                message="Press to go back!",
                choices=["Return"]
            )
        ]
        answer = inquirer.prompt(choice)

        if answer["back"] == "Return":
            clear_screen()
            from logic import begin
            begin()
            break

def equip_item(item_type, item_name, stat_boost):
    if item_type == "weapon":
        if player_stats["equipment"]["weapon"]:
            unequip_item("weapon")
        player_stats["equipment"]["weapon"] = item_name
        player_stats["attack"] += stat_boost
    elif item_type == "armor":
        if player_stats["equipment"]["armor"]:
            unequip_item("armor")
        player_stats["equipment"]["armor"] = item_name
        player_stats["defense"] += stat_boost

    print(f"🔧 Equipped {item_name}!")

def unequip_item(item_type):
    if item_type == "weapon" and player_stats["equipment"]["weapon"]:
        old_weapon = player_stats["equipment"]["weapon"]
        player_stats["attack"] -= get_equipment_stat(old_weapon)
        player_stats["equipment"]["weapon"] = None
        print(f"❌ Unequipped {old_weapon}.")

    elif item_type == "armor" and player_stats["equipment"]["armor"]:
        old_armor = player_stats["equipment"]["armor"]
        player_stats["defense"] -= get_equipment_stat(old_armor)
        player_stats["equipment"]["armor"] = None
        print(f"❌ Unequipped {old_armor}.")

def get_equipment_stat(item_name):
    for category in ["weapon", "armor"]:
        for item in shop_items[category]:
            if item["name"] == item_name:
                return item.get("attack", item.get("defense"))
    return 0  

def reset_health():
    player_stats["health"] = player_stats["max_health"]  # Ensure health never exceeds max_health
