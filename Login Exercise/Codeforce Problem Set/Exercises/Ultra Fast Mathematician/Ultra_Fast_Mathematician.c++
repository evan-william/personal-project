#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string linex;
    string liney;
    vector <char> conclusion;


    cin >> linex; // INPUT FIRST LINE
    cin >> liney; // INPUT SECND LINE

    int size_of_Both = linex.size();

    for (int x = 0; x < size_of_Both ; x ++) {
        char line1 = linex[x];
        char line2 = liney[x];

        if (line1 == line2) {
            conclusion.push_back('0');
        }
        else if (line1 =='0' && line2 == '1') {
            conclusion.push_back('1');
        }
        else if (line1 == '1' && line2 == '0') {
            conclusion.push_back('1');
        }
    }

    for (char letter : conclusion) {
        cout << letter;
    }

    return 0;
}