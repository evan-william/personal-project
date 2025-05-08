#include "add.h"
#include <iostream>

using namespace std;

void add_student(vector<string>& list, const string& name) {
    list.push_back(name);
    cout << name << " added to the list.\n";
}
