#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int main() {
    vector<char> row1(4), row2(4), row3(4), row4(4); // initialize with size 4
    bool correction {true};
    int counter = 0;

    // Input 4 chars like ####
    for (int x = 0; x < 4; x++) cin >> row1[x];
    for (int x = 0; x < 4; x++) cin >> row2[x];
    for (int x = 0; x < 4; x++) cin >> row3[x];
    for (int x = 0; x < 4; x++) cin >> row4[x];

    // Compare rows
    for (int x = 0; x < 4; x++) {
        if (row1[x] != row3[x]) {
            correction = false;
            counter += 1;
            if (counter >= 2) {
                cout << "NO";
                exit(0);
            }
        }
        if (row2[x] != row4[x]) {
            correction = false;
            counter += 1;
            if (counter >= 2) {
                cout << "NO";
                exit(0);
            }
        }
    }

    if (correction) {
        cout << "NO";
    }
    else {
        cout << "YES";
    }

    return 0;
}
