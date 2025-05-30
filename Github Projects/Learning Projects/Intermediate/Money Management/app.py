import inquirer
import time
import os
import platform
import subprocess
import csv
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
        # Update the directory structure
        self.app_dir = "Money Management App (Data)"
        self.csv_dir = os.path.join(self.app_dir, "CSV")
        self.ensure_dirs_exist()
        self.load_data()
        
    def ensure_dirs_exist(self):
        # Create app directory if not found
        if not os.path.exists(self.app_dir):
            os.makedirs(self.app_dir)
        # Create CSV directory if not found
        if not os.path.exists(self.csv_dir):
            os.makedirs(self.csv_dir)
            
    def get_csv_path(self, filename):
        return os.path.join(self.csv_dir, filename)
        
    def load_data(self):
        # Create necessary CSV files if not found
        balance_path = self.get_csv_path('balance.csv')
        transactions_path = self.get_csv_path('transactions.csv')
        planner_path = self.get_csv_path('planner.csv')
        
        if not os.path.exists(balance_path):
            with open(balance_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['balance'])
                writer.writerow([0])  # Default balance
                
        if not os.path.exists(transactions_path):
            with open(transactions_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['date', 'type', 'amount', 'description'])
                
        if not os.path.exists(planner_path):
            with open(planner_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['type', 'month', 'amount', 'description'])
        
        # Load balance from CSV
        with open(balance_path, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                self.balance = int(row[0])
                break
                
        # Load planner data from CSV
        with open(planner_path, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 4:
                    entry_type, month, amount, description = row
                    amount = int(amount)
                    if entry_type == 'income':
                        self.planner_income[month].append((amount, description))
                    elif entry_type == 'outcome':
                        self.planner_outcome[month].append((amount, description))

    def save_balance(self):
        balance_path = self.get_csv_path('balance.csv')
        with open(balance_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['balance'])
            writer.writerow([self.balance])
            
    def save_transaction(self, transaction_type, amount, description=""):
        transactions_path = self.get_csv_path('transactions.csv')
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(transactions_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([current_date, transaction_type, amount, description])
            
    def save_planner(self, entry_type, month, amount, description):
        planner_path = self.get_csv_path('planner.csv')
        with open(planner_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([entry_type, month, amount, description])
            
    def clear_planner_item(self, entry_type, month, index):
        # Remove from memory
        if entry_type == "income":
            self.planner_income[month].pop(index)
        elif entry_type == "outcome":
            self.planner_outcome[month].pop(index)
        
        # Update CSV file by rewriting everything
        planner_path = self.get_csv_path('planner.csv')
        rows = [['type', 'month', 'amount', 'description']]
        
        for month in self.planner_income:
            for amount, description in self.planner_income[month]:
                rows.append(['income', month, amount, description])
                
        for month in self.planner_outcome:
            for amount, description in self.planner_outcome[month]:
                rows.append(['outcome', month, amount, description])
                
        with open(planner_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

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
            description = input("Description (optional): ")
            self.balance += self.add
            # Save transaction and update balance
            self.save_transaction("income", self.add, description)
            self.save_balance()
            print(f"\nAdded Rp{self.add:,} to balance. Current balance: Rp{self.balance:,}")
            input("\nPress Enter to return to Main Menu...")
            main(system, self)
      
        elif answer["choice"] == "2. Remove Balance":
            self.remove = int(input("Input Outcome: "))
            description = input("Description (optional): ")
            self.balance -= self.remove
            # Save transaction and update balance
            self.save_transaction("outcome", self.remove, description)
            self.save_balance()
            print(f"\nRemoved Rp{self.remove:,} from balance. Current balance: Rp{self.balance:,}")
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
                        amount, note = self.planner_income[month][index]
                        self.balance += amount
                        # Save transaction and update balance
                        self.save_transaction("income", amount, f"Planner: {note} ({month})")
                        self.save_balance()
                        # Remove from planner
                        self.clear_planner_item(entry_type, month, index)
                        print(f"\n✅ Applied income: +Rp{amount:,} from '{note}' ({month}) to real balance.")
                    elif entry_type == "outcome":
                        amount, note = self.planner_outcome[month][index]
                        self.balance -= amount
                        # Save transaction and update balance
                        self.save_transaction("outcome", amount, f"Planner: {note} ({month})")
                        self.save_balance()
                        # Remove from planner
                        self.clear_planner_item(entry_type, month, index)
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
                        # Save to CSV
                        self.save_planner("income", month, amount, note)
                    print(f"Planned +Rp{amount:,} for ALL months ({', '.join(months)}) for: {note}")
                else:
                    selected_months = [m.capitalize() for m in month_input.split() if m.capitalize() in month_name[1:]]
                    for m in selected_months:
                        self.planner_income[m].append((amount, note))
                        # Save to CSV
                        self.save_planner("income", m, amount, note)
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
                        # Save to CSV
                        self.save_planner("outcome", month, amount, note)
                    print(f"Planned -Rp{amount:,} for ALL months ({', '.join(months)}) for: {note}")
                else:
                    selected_months = [m.capitalize() for m in month_input.split() if m.capitalize() in month_name[1:]]
                    for m in selected_months:
                        self.planner_outcome[m].append((amount, note))
                        # Save to CSV
                        self.save_planner("outcome", m, amount, note)
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
        system = System() 
    if not balance:
        balance = Balance() 

    system.clear_screen() 
    system.startmenu(system, balance) 


if __name__ == "__main__":
    main()