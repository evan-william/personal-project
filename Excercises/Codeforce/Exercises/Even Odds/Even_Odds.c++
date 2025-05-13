#include <iostream>
#include <vector>

using namespace std;

int main() {
    unsigned long long numSeq;
    short index;
    vector<unsigned long long> Even;
    vector<unsigned long long> Odd;

    vector<unsigned long long> newSequence;

    cin >> numSeq >> index;

    for (int x = 1; x <= numSeq ; x ++) {
        if (x % 2 == 0) {
            Even.push_back(x);
        }
        else if (x % 2 == 1) {
            Odd.push_back(x);
        }
    }

    // New Sequence
    for (char each : Odd) {
        newSequence.push_back(each);
        Odd.clear(); // Clean Up After
    }

    for (char each: Even) {
        newSequence.push_back(each);
        Even.clear(); // Clean Up After
    }

    cout << newSequence[index - 1] << endl;
}