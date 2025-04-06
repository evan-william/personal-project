import inquirer
from stats import player_stats, equip_item, shop_items
from menus import clear_screen


def startshop():
    clear_screen()
    print("\n🏪 Welcome to the Shop!")
    while True:
        choice = [
            inquirer.List(
                "category",
                message="What do you want to buy?",
                choices=["Weapons", "Armor", "Exit"]
            )
        ]
        answer = inquirer.prompt(choice)

        if answer["category"] == "Weapons":
            buy_item("weapon")
        elif answer["category"] == "Armor":
            buy_item("armor")
        else:
            clear_screen()
            print("Exiting the shop...")
            from logic import begin
            begin()
            break

def buy_item(item_type):
    items = shop_items[item_type]
    
    choices = [f"{item['name']} (+{item.get('attack', item.get('defense'))}) - {item['price']} Gold"
               for item in items]
    choices.append("Cancel")

    question = [
        inquirer.List("item", message="Choose an item to buy:", choices=choices)
    ]
    answer = inquirer.prompt(question)

    if answer["item"] == "Cancel":
        clear_screen()
        startshop()
        return

    selected_item = next(item for item in items if item["name"] in answer["item"])
    
    if player_stats["gold"] >= selected_item["price"]:
        player_stats["gold"] -= selected_item["price"]
        stat_boost = selected_item.get("attack", selected_item.get("defense"))
        equip_item(item_type, selected_item["name"], stat_boost)
    else:
        print("❌ Not enough gold!")
