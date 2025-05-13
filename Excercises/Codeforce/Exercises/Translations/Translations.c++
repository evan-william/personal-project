#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string Berland;
    string Birland;
    bool check {false};

    vector <char> BerlandContain;
    vector <char> BirlandContain;

    cin >> Berland;
    cin >> Birland;

    if (size(Berland) != size(Birland)) {
        cout << "NO";
    }
    else {
        int counterForward = 0;
        int counterBackward = size(Berland) - 1;
        int Length = size(Berland);
    
        for (char each: Berland) {
            BerlandContain.push_back(each);
        } 
    
        for (char each: Birland) {
            BirlandContain.push_back(each);
        } 
    
        for (int x = 0; x < Length ; x ++ ) {
            if (BerlandContain[counterForward]  == BirlandContain[counterBackward]) {
                check = true;
                counterForward += 1;
                counterBackward -= 1;
            }
            else {
                check = false;
                break;
            }
        }
    
        if (check == 1) {
            cout << "YES";
        }
        else {
            cout << "NO";
        }
    
    }
    return 0;
}

