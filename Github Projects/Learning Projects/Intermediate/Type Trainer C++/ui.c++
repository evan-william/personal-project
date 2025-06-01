#include <iostream>
#include <thread>    
#include <chrono>    
#include <string>

using namespace std;

void typeText(const string& text, int delayMs = 30) {
    for (char c : text) {
        cout << c << flush; 
        this_thread::sleep_for(chrono::milliseconds(delayMs));
    }
}