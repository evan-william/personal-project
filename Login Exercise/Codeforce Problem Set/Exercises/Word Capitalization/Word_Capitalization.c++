#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

int main(){
    string word;
    cout << "";
    cin >> word;

    word[0] = toupper(word[0]);
    cout << word;

    return 0;
}