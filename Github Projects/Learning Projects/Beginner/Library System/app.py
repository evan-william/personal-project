import inquirer
import time
import platform
import subprocess
import os
from pyfiglet import Figlet

class Books:
    def __init__(self):
        self.books = []
    
    def add_book(self, title):
        self.books.append(title)
    
    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            return True
        return False
    
    def get_books(self):
        return self.books
    
    def is_book_available(self, title):
        return title in self.books

class Customer:
    def __init__(self):
        self.borrowed = []
        self.returned = []
    
    def borrow_book(self, title):
        self.borrowed.append(title)
    
    def return_book(self, title):
        if title in self.borrowed:
            self.borrowed.remove(title)
        self.returned.append(title)
    
    def get_borrowed(self):
        return self.borrowed
    
    def get_returned(self):
        return self.returned

class Library:
    def __init__(self):
        self.books_manager = Books()
        self.customer_manager = Customer()
        self.transaction = 0
    
    def ascii_title(self):
        f = Figlet(font='slant')
        return f.renderText("Library")
    
    def firstmenu(self):
        title = self.ascii_title()
        return f"""
{title}
                        By: Evan William
                        Version: 1.0
    """
    
    def clear_screen(self):
        if platform.system() == "Windows":
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear", shell=True)
    
    def books_info(self):
        self.clear_screen()
        questions = [
            inquirer.List(
                "choice",
                message="Welcome! What do you want to do?",
                choices=["1. Add Books", "2. Remove Books", "3. Show Book List", "4. Back to Menu"],
            )
        ]
        answer = inquirer.prompt(questions)
        print(f"You selected: {answer['choice']}")
        time.sleep(1)

        if answer["choice"] == "1. Add Books":
            tempo_books = input("Add Title: ")
            self.books_manager.add_book(tempo_books)
            print("Book is added to the library!")
            input("\nPress Enter to return to Main Menu...")
            self.start_menu()
      
        elif answer["choice"] == "2. Remove Books":
            tempo_books = input("Add Title: ")
            if not self.books_manager.is_book_available(tempo_books):
                print("No such book is found!")
            else:
                self.books_manager.remove_book(tempo_books)
            print("Book is removed from the library!")
            input("\nPress Enter to return to Main Menu...")
            self.start_menu()
        
        elif answer["choice"] == "3. Show Book List":
            counter = 1
            for book in self.books_manager.get_books():
                print(counter, ".", book)
                counter += 1
            input("\nPress Enter to return to Main Menu...")
            self.start_menu()

        elif answer["choice"] == "4. Back to Menu":
            print("Opening Menu...")
            time.sleep(2)
            self.clear_screen()
            self.start_menu()

    def customer_info(self):
        self.clear_screen()
        questions = [
            inquirer.List(
                "choice",
                message="Welcome! What do you want to do?",
                choices=["1. Borrow Books", "2. Return Books", "3. Show Borrowed", "4. Show Returned", "5. Back to Menu"],
            )
        ]
        answer = inquirer.prompt(questions)
        print(f"You selected: {answer['choice']}")
        time.sleep(1)

        if answer["choice"] == "1. Borrow Books":
            tempo_books = input("Add Title: ")
            if self.books_manager.is_book_available(tempo_books):
                self.books_manager.remove_book(tempo_books)
                self.customer_manager.borrow_book(tempo_books)
            else:
                print("Book is not in the list!")
            input("\nPress Enter to return to Main Menu...")
            self.start_menu()
      
        elif answer["choice"] == "2. Return Books":
            tempo_books = input("Return Title: ")
            self.books_manager.add_book(tempo_books)
            self.customer_manager.return_book(tempo_books)
            input("\nPress Enter to return to Main Menu...")
            self.start_menu()

        elif answer["choice"] == "3. Show Borrowed":
            print("Opening Menu...")
            time.sleep(2)
            counter = 1
            for book in self.customer_manager.get_borrowed():
                print(counter, ".", book)
                counter += 1
            input("\nPress Enter to return to Main Menu...")
            self.start_menu()

        elif answer["choice"] == "4. Show Returned":
            print("Opening Menu...")
            time.sleep(2)
            counter = 1
            for book in self.customer_manager.get_returned():
                print(counter, ".", book)
                counter += 1
            input("\nPress Enter to return to Main Menu...")
            self.start_menu()

        elif answer["choice"] == "5. Back to Menu":
            print("Opening Menu...")
            time.sleep(2)
            self.clear_screen()
            self.start_menu()

    def start_menu(self):
        self.clear_screen()
        print(self.firstmenu())
        questions = [
            inquirer.List(
                "choice",
                message="Welcome! What do you want to do?",
                choices=["1. Books Info", "2. Customer Info", "3. Exit"],
            )
        ]
        answer = inquirer.prompt(questions)
        print(f"You selected: {answer['choice']}")
        time.sleep(1)

        if answer["choice"] == "1. Books Info":
            self.books_info()
        elif answer["choice"] == "2. Customer Info":
            self.customer_info()
        else:
            print("Exiting App...")
            time.sleep(1)
            os._exit(0)

def main():
    library = Library()
    library.start_menu()

if __name__ == "__main__":
    main()