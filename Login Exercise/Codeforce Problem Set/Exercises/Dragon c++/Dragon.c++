#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int strength;
    vector<int> dragonStrength;
    int dragonCount;
    vector<int> bonus;
    bool WinCons {false};

    int Dragon;
    int Bonus;


    // cout << "Enter Strength & DragonCount: ";
    cin >> strength >> dragonCount;

    for (int x = 0; x < dragonCount; x ++) {
        // cout << "Enter Dragon Strength & Bonus: ";
        cin >> Dragon >> Bonus;

        dragonStrength.push_back(Dragon); 
        bonus.push_back(Bonus);
    }

    vector<pair<int, int>> combined; 
    for (int y = 0; y < dragonStrength.size(); y ++) {
        combined.push_back({dragonStrength[y], bonus[y]});
    }

    sort(combined.begin(), combined.end());

    
    /* for (auto each : combined) {
        cout << "(" << each.first << ", " << each.second << ")" << endl;
    } */

    dragonStrength.clear();
    bonus.clear();

    for (auto& p : combined) {
        dragonStrength.push_back(p.first);
        bonus.push_back(p.second);
    }

    for (int z = 0; z < dragonCount; z ++) {
        if (strength > dragonStrength[z]) { // KIRITO WIN
            strength += bonus[z];
            WinCons = true;
        }
        else if (strength <= dragonStrength[z]) { // DRAGON WIN
            WinCons = false;
            break;
        }
    }

    if (WinCons == 1) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }

    return 0;
}