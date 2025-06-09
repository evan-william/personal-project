#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

void compute(const vector<int>& ln) {
    vector<int> stack;

    for (int num : ln) {
        if (!stack.empty() && stack.back() != num) {
            stack.pop_back(); 
        } else {
            stack.push_back(num);
        }
    }

    cout << stack.size() << endl;
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
