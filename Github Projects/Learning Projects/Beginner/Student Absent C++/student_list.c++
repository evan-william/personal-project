#include "student_list.h"
#include <iostream>

using namespace std;

void show_students(const vector<string>& list) {
    cout << "Student List:\n";
    if (list.empty()) {
        cout << "No students in the list.\n";
        return;
    }

    for (size_t i = 0; i < list.size(); ++i) {
        cout << i + 1 << ". " << list[i] << endl;
    }
}
