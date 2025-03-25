import random
from stats import get_stats

COMMON_ENEMIES = {
    "Plains": ["Bandit", "Knight", "Thief", "Wild Boar"],
    "Graveyard": ["Zombie", "Skeleton", "Ghost", "Vampire"],
    "Cave": ["Goblin", "Troll", "Bat", "Serpent"]
}

RARE_ENEMIES = {
    "Plains": ["King"],
    "Graveyard": ["Ghast"],
    "Cave": ["Golem"]
}

BASE_STATS = {
    "Bandit": {"health": 10, "attack": 3, "defense": 2},
    "Knight": {"health": 20, "attack": 6, "defense": 6},
    "Thief": {"health": 8, "attack": 4, "defense": 1},
    "Wild Boar": {"health": 10, "attack": 2, "defense": 5},

    "Zombie": {"health": 8, "attack": 2, "defense": 2},
    "Skeleton": {"health": 5, "attack": 1, "defense": 1},
    "Ghost": {"health": 10, "attack": 4, "defense": 0},
    "Vampire": {"health": 12, "attack": 10, "defense": 4},

    "Goblin": {"health": 8, "attack": 3, "defense": 1},
    "Troll": {"health": 30, "attack": 8, "defense": 4},
    "Bat": {"health": 3, "attack": 1, "defense": 0},
    "Serpent": {"health": 10, "attack": 4, "defense": 7},

    # RARE BOYS
    "King": {"health": 50, "attack": 10, "defense": 10},
    "Ghast": {"health": 30, "attack": 14, "defense": 8},
    "Golem": {"health": 80, "attack": 20, "defense": 12}
}

def generate_enemy(map_name):
    player = get_stats() 

    enemy_count = random.randint(1, 4)  
    enemies = [] 

    for _ in range(enemy_count):
        is_rare = random.random() < 0.04  
        if is_rare:
            enemy_name = random.choice(RARE_ENEMIES[map_name]) 
        else:
            enemy_name = random.choice(COMMON_ENEMIES[map_name])

        base_stats = BASE_STATS[enemy_name]

        enemy_level = max(1, player["level"] + random.randint(-1, 1))
        enemy_health = base_stats["health"] + (player["health"] // 3)
        enemy_attack = base_stats["attack"] + (player["attack"] // 3)
        enemy_defense = base_stats["defense"] + (player["defense"] // 3)

        enemies.append({
            "name": enemy_name,
            "level": enemy_level,
            "health": enemy_health,
            "attack": enemy_attack,
            "defense": enemy_defense,
            "rare": is_rare
        })

    return enemies  

def display_enemies(enemies):
    print("\n👹 Enemies Encountered:")
    for i, enemy in enumerate(enemies, start=1):
        rarity = " (RARE!)" if enemy["rare"] else ""
        print(f"\n⚔️  Enemy {i}: {enemy['name']}{rarity} (Level {enemy['level']})")
        print(f"  - Health: {enemy['health']}")
        print(f"  - Attack: {enemy['attack']}")
        print(f"  - Defense: {enemy['defense']}")
