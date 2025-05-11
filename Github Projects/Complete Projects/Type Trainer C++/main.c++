#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <chrono>
#include "mistake_counter.h"
#include "word_generator.h"
#include "ui.h"

using namespace std;
using namespace std::chrono;

const string RED     = "\033[31m";
const string GREEN   = "\033[32m";
const string YELLOW  = "\033[33m";
const string BLUE    = "\033[34m";
const string MAGENTA = "\033[35m";
const string CYAN    = "\033[36m";
const string RESET   = "\033[0m";

void show_ascii_title() {
    cout << GREEN << R"(
 **      ** **********                            ****** 
/**     /**/////**///   **   ** ******           **////**
/**     /**    /**     //** ** /**///**  *****  **    // 
//**    **     /**      //***  /**  /** **///**/**       
 //**  **      /**       /**   /****** /*******/**       
  //****       /**       **    /**///  /**//// //**    **
   //**        /**      **     /**     //****** //****** 
    //         //      //      //       //////   //////  
)" << RESET << YELLOW << R"(
        >> Type Trainer (v1.0) by Evan William << 
--------------------------------------------------------
)" << RESET << endl;
}

void displayMenu() {
    cout << MAGENTA << "Welcome to the VTypeC Typing Trainer!" << RESET << endl;
    cout << CYAN << "This program helps you improve your typing speed and accuracy." << RESET << endl;
    cout << YELLOW << "You will be prompted to type a set of randomly generated words." << RESET << endl;
    cout << BLUE << "Your goal is to type them as quickly and accurately as possible." << RESET << endl;
    cout << "\n";
    cout << GREEN << "Ready to get started?" << RESET << endl;
}

vector<string> splitWords(const string& input) {
    stringstream ss(input);
    vector<string> result;
    string word;
    while (ss >> word) {
        result.push_back(word);
    }
    return result;
}

int main() {
    srand(time(0)); 
    show_ascii_title();
    displayMenu();  // Display the menu

    int word_count;
    cout << GREEN << ">> How many words do you want to practice? (10 - 100): " << RESET;
    cin >> word_count;
    if (word_count < 10) word_count = 10;
    if (word_count > 100) word_count = 100;
    cin.ignore();  // Clear newline character

    vector<string> words;
    string full_output = "";

    for (int x = 0; x < word_count; x++) {
        string word = generate_word();
        words.push_back(word);
        typeText(word, 40);  
        cout << " ";
        full_output += word + " ";
    }

    cout << "\n\n" << YELLOW << "Type the above words exactly:" << RESET << "\n> ";
    auto start_time = high_resolution_clock::now();
    string user_input;
    getline(cin, user_input);
    auto end_time = high_resolution_clock::now();    

    double duration_sec = duration_cast<seconds>(end_time - start_time).count();

    vector<string> expected = splitWords(full_output);
    vector<string> typed = splitWords(user_input);

    double accuracy = calculateAccuracy(expected, typed);
    double wps = calculateTypingSpeed(duration_sec, word_count);

    printAccuracyReport(full_output, user_input, accuracy, wps, duration_sec);

    return 0;
}
