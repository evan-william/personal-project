#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

vector<string> bookList;

void addBook();
void removeBook();
void showBooks();
void menu();

void addBook() {
    string bookTitle;
    cout << "Enter a title: ";
    cin.ignore(); // To handle leftover newline
    getline(cin, bookTitle);
    bookList.push_back(bookTitle);
    cout << "Book \"" << bookTitle << "\" added successfully!" << endl;
}

void removeBook() {
    if (bookList.empty()) {
        cout << "No books to remove!" << endl;
        return;
    }

    showBooks();
    int index; 
    cout << "Enter the number of the book to remove: ";
    cin >> index;

    if (index < 1 || index > bookList.size()) {
        cout << "Invalid number!" << endl;
    } else { 
        cout << "Book \"" << bookList[index - 1] << "\" removed." << endl;
        bookList.erase(bookList.begin() + index - 1);
    } 
}

void showBooks() {
    if (bookList.empty()) {
        cout << "No books in the list." << endl;
    } else {
        cout << "Book List:" << endl;
        for (int i = 0; i < bookList.size(); ++i) {
            cout << i + 1 << ". " << bookList[i] << endl;
        }
    }
}

void menu() {
    int action;
    while (true) {
        cout << "\n===== MENU =====" << endl;
        cout << "1. Add Book" << endl;
        cout << "2. Remove Book" << endl;
        cout << "3. Show Book List" << endl;
        cout << "4. Exit" << endl;
        cout << "Input Action: ";
        cin >> action;

        switch (action) {
            case 1:
                addBook();
                break;
            case 2:
                removeBook();
                break;
            case 3:
                showBooks();
                break;
            case 4:
                cout << "Goodbye!" << endl;
                exit(0);
            default:
                cout << "Invalid option. Try again." << endl;
        }
    }
}

int main () {
    string name;
    cout << "Please enter your name: ";
    getline(cin, name);
    cout << "Welcome, " << name << "!" << endl;

    menu();
}
