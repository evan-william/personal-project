// CodeForce Round 360 (Div.2)
#include <iostream>
#include <vector>

using namespace std;

int main () {
    int Opponents;
    int Days;
    int win;

    int TempoDays = 0;
    int ConsDays = 0;

    string Tempo;

    vector <string> Enemy;

    // Input First Line
    cin >> Opponents >> Days; // 2 2 
    
    // Second Line and Forward
    for (unsigned x = 0; x < Days ; x ++) {
        cin >> Tempo;
        Enemy.push_back(Tempo);
    }

    // Computes
    for (signed int x = 0; x < size(Enemy); x ++) {
        if (Enemy[x] == "10") {
            TempoDays += 1;
            ConsDays = TempoDays;
        }  
        else if (Enemy[x] == "01") {
            TempoDays += 1;
            ConsDays = TempoDays;
        } 
        else if (Enemy[x] == "00") {
            TempoDays += 1;
            ConsDays = TempoDays;
        } 
        else {
            TempoDays = 0;
        }

        if (TempoDays > ConsDays) {
            ConsDays = TempoDays;
        }
    }   

    cout << ConsDays;
}


