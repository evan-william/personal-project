#include <iostream>
#include <string>
#include <algorithm>
#include "counter.h" 
#include "clearscreen.h"

using namespace std;

const string RED     = "\033[31m";
const string GREEN   = "\033[32m";
const string YELLOW  = "\033[33m";
const string BLUE    = "\033[34m";
const string MAGENTA = "\033[35m";
const string CYAN    = "\033[36m";
const string RESET   = "\033[0m";

void show_ascii_title() {
    cout << RED << R"(
 __        __   _                            _         
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
)" << YELLOW << R"( 
  ______        _______                  _            
 |  ____|      |__   __|                | |           
 | |____      __ | | ___ ___  _   _ _ __| |_ ___ _ __ 
 |  __\ \ /\ / / | |/ __/ _ \| | | | '__| __/ _ \ '__|
 | |___\ V  V /  | | (_| (_) | |_| | |  | ||  __/ |   
 |______\_/\_/   |_|\___\___/ \__,_|_|   \__\___|_|   
)" << RESET << CYAN << R"(
        >> Word Counter (v1.0) by Evan William <<
--------------------------------------------------------
)" << RESET << endl;
}

void runWordCounter() {
    string input;

    cout << GREEN << ">> Enter your sentence or paragraph below:" << RESET << endl;
    cout << YELLOW << "> " << RESET;
    getline(cin, input);

    cout << CYAN << "\n>> Analyzing your input...\n" << RESET << endl;
    count_word(input); 
}

int main() {
    while (true) {
        clearScreen();
        show_ascii_title();

        runWordCounter();

        cout << "\n" << GREEN << ">> Done. Thanks for using Word Meter!" << RESET << endl;

        string choice;
        cout << "\n" << MAGENTA << ">> Do you want to analyze another sentence? [Y/N]: " << RESET;
        getline(cin, choice);

        transform(choice.begin(), choice.end(), choice.begin(), ::tolower);
        if (choice != "y" && choice != "yes") {
            cout << CYAN << "\n>> Exiting Word Meter. Goodbye!\n" << RESET << endl;
            break;
        }
    }

    return 0;
}