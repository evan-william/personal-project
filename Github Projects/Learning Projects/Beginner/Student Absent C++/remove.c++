#include "remove.h"
#include <iostream>
#include <algorithm>

using namespace std;

void remove_student(vector<string>& list, const string& name) {
    auto it = find(list.begin(), list.end(), name);
    if (it != list.end()) {
        list.erase(it);
        cout << name << " removed from the list.\n";
    } else {
        cout << name << " not found.\n";
    }
}
