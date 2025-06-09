#include <iostream>
#include <vector>

using namespace std;

long long iceCreamFirst, testCase, distressed = 0, iceCreamNeeded;
char symbol;
vector <char> symbols;
vector <int> needs;

void system() {
    for (unsigned int x = 0; x < testCase ; x ++ ) {
        if (symbols[x] == '+') {
            iceCreamFirst += needs[x];
        }
        else if (symbols[x] == '-') {       
            if (iceCreamFirst - needs[x] < 0) {
                distressed += 1;
            }
            else {
                iceCreamFirst -= needs[x];
            }
        }
    }

    cout << iceCreamFirst << " " << distressed;
}

int main () {
    cin >> testCase >> iceCreamFirst;

    // TestCase Input
    for (int x = 0; x < testCase; x ++ ) {
        cin >> symbol >> iceCreamNeeded;
        symbols.push_back(symbol);
        needs.push_back(iceCreamNeeded);
    }

    // Counting
    system();

    return 0;
}