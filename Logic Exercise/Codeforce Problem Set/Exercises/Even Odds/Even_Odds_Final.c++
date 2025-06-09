#include <iostream>
using namespace std;

int main() {
    unsigned long long numSeq;
    unsigned long long index;

    cin >> numSeq >> index;

    // Calculate how many odd numbers are in the first half
    unsigned long long oddCount = (numSeq + 1) / 2;

    if (index <= oddCount) {
        // Index lies in the odd part
        cout << 2 * index - 1 << endl;
    } else {
        // Index lies in the even part
        cout << 2 * (index - oddCount) << endl;
    }

    return 0;
}
