// CodeForce Round 360 (Div.2)
#include <iostream>
#include <vector>

using namespace std;

int Opponents;
int Days;
int win;

int TempoDays = 0;
int ConsDays = 0;

string Tempo;

vector <string> Enemy;

int compute () {
    // Computes
    for (signed int x = 0; x < size(Enemy); x ++) {
        int Tempo2 = 0;
        for (auto each : Enemy[x]) {
            // Day 1 Check
            if (each == '1') {
                Tempo2 += 1;
           }}
        
        if (Tempo2 == Opponents) { // Cannot Win
            TempoDays = 0;
        } else {
            TempoDays += 1; }

        if (ConsDays < TempoDays) {
            ConsDays = TempoDays;
        }
   }

   return ConsDays;
}

int main () {
    // Input First Line
    cin >> Opponents >> Days; // 2 2 
    
    // Second Line and Forward
    for (unsigned x = 0; x < Days ; x ++) {
        cin >> Tempo;
        Enemy.push_back(Tempo);
    }

    auto answer = compute();
    cout << answer;
}


