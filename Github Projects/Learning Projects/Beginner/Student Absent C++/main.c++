#include <iostream>
#include <vector>
#include <string>
#include "add.h"
#include "remove.h"
#include "student_list.h"

using namespace std;

int main() {
    vector<string> students;
    int choice;
    string name;

    do {
        cout << "\n====== STUDENT MENU ======" << endl;
        cout << "1. Add Student\n2. Remove Student\n3. View Students\n4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore(); // Clear newline

        switch (choice) {
            case 1:
                cout << "Enter student name to add: ";
                getline(cin, name);
                add_student(students, name);
                break;
            case 2:
                cout << "Enter student name to remove: ";
                getline(cin, name);
                remove_student(students, name);
                break;
            case 3:
                show_students(students);
                break;
            case 4:
                cout << "Goodbye!\n";
                break;
            default:
                cout << "Invalid choice.\n";
        }
    } while (choice != 4);

    return 0;
}
