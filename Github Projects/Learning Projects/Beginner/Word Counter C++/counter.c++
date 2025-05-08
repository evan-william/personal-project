#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

// Helper function to trim leading and trailing spaces
string trim(const string &str) {
    int first = str.find_first_not_of(' ');
    int last = str.find_last_not_of(' ');
    if (first == string::npos) return ""; // no non-space characters
    return str.substr(first, last - first + 1);
}

void count_word(string &wordInput) {
    string trimmedInput = trim(wordInput);

    if (trimmedInput.empty()) {
        cout << "There are 0 words!" << endl;
        return;
    }

    int countWord = count(trimmedInput.begin(), trimmedInput.end(), ' ') + 1;

    if (countWord == 1) {
        cout << "There is exactly " << countWord << " word!" << endl;
    } else {
        cout << "There are approximately " << countWord << " words!" << endl;
    }
}
