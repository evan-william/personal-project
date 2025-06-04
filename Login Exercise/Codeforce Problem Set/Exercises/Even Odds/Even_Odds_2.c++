#include <iostream>
#include <vector>

using namespace std;

int main() {
    unsigned long long numSeq;
    short index;

    cin >> numSeq >> index;

    unsigned long long newSequence [numSeq]; // 0 0 0 0 0 0 0
    unsigned long long counterEven = 0;
    unsigned long long counterOdd = 0;

    int divider;

    // Divider
    if (numSeq % 2 == 0){
        divider = numSeq / 2;
    }
    else {
        divider = numSeq / 2 + 1;
    }
        

    for (unsigned long long x = 1; x <= numSeq ; x ++) {
        if (x % 2 == 1) {
            newSequence[counterOdd] = x;
            counterOdd += 1;
        }
        else if (x % 2 == 0) {
            newSequence[counterEven + divider] = x;
            counterEven += 1;
        }
    }

    cout << newSequence[index - 1] << endl;
}