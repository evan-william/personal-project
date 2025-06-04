#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int year;
    cin >> year;

    while (true) {
        year += 1; 
        string strYear = to_string(year); // CHANGE FROM INTEGER TO STRING 
        vector<char> Tempo;
        bool isUnique = true;

        for (char each : strYear) {
            if (find(Tempo.begin(), Tempo.end(), each) != Tempo.end()) {
                isUnique = false;
                break;
            }
            Tempo.push_back(each);
        }

        if (isUnique) {
            cout << year << endl;
            break;
        }
    }

    return 0;
}
