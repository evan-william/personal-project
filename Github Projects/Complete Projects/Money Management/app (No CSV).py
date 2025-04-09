import inquirer
import time
import os
import platform
import subprocess
from calendar import month_name
from datetime import datetime
from pyfiglet import Figlet
from collections import defaultdict


# Manage Balance
class Balance():
    def __init__(self):
        self.balance = 0
        self.nominaldivider = 3
        self.status = 1
        self.planner_income = defaultdict(list)   
        self.planner_outcome = defaultdict(list) 


    def showbalance(self):
        TempoBalance = str(self.balance)[::-1]
        result = ""

        for i in range(0, len(TempoBalance), self.nominaldivider):
            result += TempoBalance[i:i + self.nominaldivider] + "."
        formatted_balance = result[::-1].lstrip(".")  

        if self.balance < 0:
            self.status = 0
            formatted_balance = formatted_balance.lstrip(".")
            print(f"Balance: Rp {formatted_balance} (Indebt)")
        elif self.balance > 0:
            self.status = 1
            print(f"Balance: Rp {formatted_balance}")

    def updateBalanceManual(self, system):
        questions = [
        inquirer.List(
            "choice",
            message="Welcome! What do you want to do?",
            choices=["1. Add Balance", "2. Remove Balance", "3. Back to Menu"],
            )
        ]
        answer = inquirer.prompt(questions)
        print(f"You selected: {answer['choice']}")
        time.sleep(1)

        if answer["choice"] == "1. Add Balance":
            self.add = int(input("Input Income: "))
            self.balance += self.add
            input("\nPress Enter to return to Main Menu...")
            main(system, self)
      
        elif answer["choice"] == "2. Remove Balance":
            self.remove = int(input("Input Outcome: "))
            self.balance -= self.remove
            input("\nPress Enter to return to Main Menu...")
            main(system, self)
            
        elif answer["choice"] == "3. Back to Menu":
            print("Opening Menu...")
            time.sleep(2)
            system.clear_screen()
            main(system, self)

    def updateBalanceAuto(self, system):
        while True:
            questions = [
                inquirer.List(
                    "first_choice",
                    message="Automatic Balance Update Menu:",
                    choices=[
                        "1. Check Planner and Update",
                        "2. Back to Main Menu"
                    ]
                )
            ]
            answer = inquirer.prompt(questions)
            choice = answer["first_choice"]

            if choice == "1. Check Planner and Update":
                system.clear_screen()
                while True:
                    choices = []
                    month_order = list(month_name)[1:]

                    for month in month_order:
                        if self.planner_income[month]:
                            for idx, (amount, note) in enumerate(self.planner_income[month]):
                                choices.append((f"[INCOME] {month} +Rp{amount:,} ({note})", ("income", month, idx)))
                        if self.planner_outcome[month]:
                            for idx, (amount, note) in enumerate(self.planner_outcome[month]):
                                choices.append((f"[OUTCOME] {month} -Rp{amount:,} ({note})", ("outcome", month, idx)))

                    if not choices:
                        print("No planner data found. Add some planner entries first!")
                        input("\nPress Enter to return to Automatic Update Menu...")
                        system.clear_screen()
                        break

                    choices.append(("Back to Automatic Update Menu", "back"))

                    questions = [
                        inquirer.List(
                            "selected",
                            message="Select a planned entry to apply to real balance:",
                            choices=[label for label, _ in choices],
                        )
                    ]
                    answer = inquirer.prompt(questions)
                    selected_label = answer["selected"]

                    selected_action = None
                    for label, action in choices:
                        if label == selected_label:
                            selected_action = action
                            break

                    if selected_action == "back":
                        print("Returning to Automatic Update Menu...")
                        time.sleep(1)
                        system.clear_screen()
                        break

                    entry_type, month, index = selected_action
                    if entry_type == "income":
                        amount, note = self.planner_income[month].pop(index)
                        self.balance += amount
                        print(f"\n✅ Applied income: +Rp{amount:,} from '{note}' ({month}) to real balance.")
                    elif entry_type == "outcome":
                        amount, note = self.planner_outcome[month].pop(index)
                        self.balance -= amount
                        print(f"\n✅ Applied outcome: -Rp{amount:,} from '{note}' ({month}) to real balance.")

                    input("\nPress Enter to continue...")
                    system.clear_screen()

            elif choice == "2. Back to Main Menu":
                print("Returning to Main Menu...")
                time.sleep(1)
                system.clear_screen()
                main(system, self)
                return

    def showplanner(self, system):
        while True:
            current_month_index = datetime.now().month
            months = list(month_name)[current_month_index:]

            questions = [
                inquirer.List(
                    "choice",
                    message="What do you want to plan?",
                    choices=[
                        "1. Incoming Income", 
                        "2. Incoming Outcome", 
                        "3. Check Possible Balance", 
                        "4. Back to Menu"
                    ],
                )
            ]
            answer = inquirer.prompt(questions)
            print(f"You selected: {answer['choice']}")
            time.sleep(1)

            if answer["choice"] == "1. Incoming Income":
                system.clear_screen()
                month_input = input("For which month(s)? (e.g., May June July or All): ").capitalize().strip()
                amount = int(input("Input expected income (Rp): "))
                note = input("Description (e.g., 'Paycheck'): ")

                if month_input.lower() == "all":
                    for month in months:
                        self.planner_income[month].append((amount, note))
                    print(f"Planned +Rp{amount:,} for ALL months ({', '.join(months)}) for: {note}")
                else:
                    selected_months = [m for m in month_input.split() if m in months]
                    for m in selected_months:
                        self.planner_income[m].append((amount, note))
                    print(f"Planned +Rp{amount:,} for {', '.join(selected_months)} for: {note}")

                input("\nPress Enter to continue...")
                system.clear_screen()

            elif answer["choice"] == "2. Incoming Outcome":
                system.clear_screen()
                month_input = input("For which month(s)? (e.g., June July or All): ").capitalize().strip()
                amount = int(input("Input expected outcome (Rp): "))
                note = input("Description (e.g., 'Tuition'): ")

                if month_input.lower() == "all":
                    for month in months:
                        self.planner_outcome[month].append((amount, note))
                    print(f"Planned -Rp{amount:,} for ALL months ({', '.join(months)}) for: {note}")
                else:
                    selected_months = [m for m in month_input.split() if m in months]
                    for m in selected_months:
                        self.planner_outcome[m].append((amount, note))
                    print(f"Planned -Rp{amount:,} for {', '.join(selected_months)} for: {note}")

                input("\nPress Enter to continue...")
                system.clear_screen()

            elif answer["choice"] == "3. Check Possible Balance":
                system.clear_screen()
                print("\n--- Possible Balance Until December ---\n")
                current_balance = self.balance
                print(f"Current Balance: Rp{current_balance:,}")

                for month in months:
                    total_income = sum([x[0] for x in self.planner_income[month]])
                    total_outcome = sum([x[0] for x in self.planner_outcome[month]])
                    current_balance += total_income - total_outcome
                    print(f"\n{month}:")
                    if total_income > 0:
                        print(f"  +Rp{total_income:,} (Income)")
                    if total_outcome > 0:
                        print(f"  -Rp{total_outcome:,} (Outcome)")
                    print(f"  Possible Balance: Rp{current_balance:,}")

                input("\nPress Enter to continue...")
                system.clear_screen()

            elif answer["choice"] == "4. Back to Menu":
                print("Loading Menu...")
                time.sleep(1)
                system.clear_screen()
                system.startmenu(system, self)
 
# Manage System
class System():
    # Clear Screen
    def clear_screen(self):
        if platform.system() == "Windows":
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear", shell=True)

    # ASCII for First Menu
    def ascii_title(self):
        f = Figlet(font='slant')
        return f.renderText("FinPlanner")

    # First Menu (Decoration)
    def firstmenu(self):
        title = System.ascii_title(self)
        return f"""
{title}
                        By: Evan William
                        Version: 1.0
                        Currency Support: Rupiah (Indonesian Currency)
    """

    # First Menu 
    def startmenu(self, system, balance):
        system.clear_screen()
        print(system.firstmenu())

        questions = [
        inquirer.List(
            "choice",
            message="Welcome! What do you want to do?",
            choices=["1. Show Balance", "2. Update Balance (Manual)", "3. Update Balance (Automatic)", "4. Planner", "5. Exit"],
            )
        ]
        answer = inquirer.prompt(questions)
        print(f"You selected: {answer['choice']}")
        time.sleep(1)

        if answer["choice"] == "1. Show Balance":
            print("Loading Balance...")
            time.sleep(2)
            system.clear_screen()
            balance.showbalance()

            input("\nPress Enter to return to Main Menu...")
            main(system, balance)

        elif answer["choice"] == "2. Update Balance (Manual)":
            print("Loading System...")
            time.sleep(2)
            system.clear_screen()
            balance.updateBalanceManual(system)
           
        elif answer["choice"] == "3. Update Balance (Automatic)":
            print("Loading System...")
            time.sleep(2)
            system.clear_screen()
            balance.updateBalanceAuto(system)

        elif answer["choice"] == "4. Planner":
             print("Loading Dates...")
             time.sleep(1)
             system.clear_screen()
             balance.showplanner(self)

        else:
            print("Exiting App...")
            time.sleep(1)
            os._exit(0)


def main(system=None, balance=None):
    if not system:
        system = System() # Initialize Instance
    if not balance:
        balance = Balance() # Initialize Instance

    system.clear_screen() 
    system.startmenu(system, balance) # Initialize Main


if __name__ == "__main__":
    main()