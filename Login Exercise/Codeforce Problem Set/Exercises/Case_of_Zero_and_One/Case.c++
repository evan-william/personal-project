#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

void compute(vector<int>& ln) {
    bool all_same = true;
    for (int i = 1; i < ln.size(); i++) {
        if (ln[i] != ln[0]) {
            all_same = false;
            break;
        }
    }
    
    if (all_same) {
        cout << ln.size() << endl;  
        return;
    }

    while (true) {
        if (ln.size() < 2) break; 

        bool changed = false;
        for (unsigned x = 0; x < ln.size() - 1; x++) {
            if (ln[x] != ln[x + 1]) {
                ln.erase(ln.begin() + x, ln.begin() + x + 2);
                changed = true;
                break; 
            }
        }
        if (!changed) break; 
    }

    cout << ln.size();
}

int main() {
    int testcase = 0;
    string input;

    cin >> testcase;
    cin >> input;

    string& get = input;

    vector<int> line;
    for (char each : get) {
        line.push_back(each - '0'); 
    }

    if (line.size() != testcase) {
        exit(0);
    }

    compute(line);
    return 0;
}
