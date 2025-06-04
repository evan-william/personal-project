#include <iostream>
#include <vector>

using namespace std;

template <typename T> T compute(T &a, T &b, T &c) {
    int cost = 0;
    int final_cost = 0;

    for (unsigned int x = 1; x <= c ; x ++) {
        cost = a * x;
        final_cost = final_cost + cost;
    }

    return final_cost;
}

int main () {
    int k {0}; // Cost of Banana
    int n {0}; // Initial Dollar
    int w {0}; // Numbers of Banana Wanted

    cin >> k >> n >> w;

    int result = compute(k,n,w);
    
    int final = n - result;

    if (final > 0) {
        final = 0;
    } else {
        final = abs(final);
    }

    cout << final;
}