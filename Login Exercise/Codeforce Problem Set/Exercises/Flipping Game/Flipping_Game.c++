#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    int totalOnes = 0;

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        if (arr[i] == 1) {
            totalOnes++;
            arr[i] = -1; // flipping 1 becomes -1 (bad)
        } else {
            arr[i] = 1;  // flipping 0 becomes 1 (good)
        }
    }

    // Kadane's Algorithm for maximum subarray sum
    int maxGain = arr[0];
    int currentGain = arr[0];

    for (int i = 1; i < n; ++i) {
        currentGain = max(arr[i], currentGain + arr[i]);
        maxGain = max(maxGain, currentGain);
    }

    // if all were 1, flipping any subarray must reduce at least one 1
    if (totalOnes == n) {
        cout << n - 1 << endl;
    } else {
        cout << totalOnes + maxGain << endl;
    }

    return 0;
}
