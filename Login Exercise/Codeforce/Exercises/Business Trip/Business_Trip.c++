#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;
int main () {
    int target;
    int currentGrowth = 0;

    vector <int> GrowthPer(12);

    cin >> target;

    for(int x = 0; x < 12 ; x ++) { // Takes Input
        cin >> GrowthPer[x];

    }

    if(target == 0) {
        cout << '0' << endl;
    }
    else {
        int total = accumulate(GrowthPer.begin(), GrowthPer.end(), 0);
        
        if (total >= target) {
            int counter = 0;
            sort(GrowthPer.begin(), GrowthPer.end(), greater<int>()); // Sort From Highest

            while(currentGrowth < target) {
                currentGrowth += GrowthPer[counter];
                counter += 1;   
            }
            cout << counter << endl;
        }
        else if (total < target) {
            cout << "-1" << endl;
        }
    }
}