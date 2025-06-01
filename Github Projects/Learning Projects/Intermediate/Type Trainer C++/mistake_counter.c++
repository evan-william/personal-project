#include <iostream>
#include <chrono>
#include "mistake_counter.h"

using namespace std;
using namespace std::chrono;

double calculateTypingSpeed(double time_sec, int word_count) {
    return word_count / time_sec; 
}

double calculateAccuracy(const vector<string>& expected, const vector<string>& typed) {
    int correct_words = 0;
    for (size_t i = 0; i < min(expected.size(), typed.size()); i++) {
        if (expected[i] == typed[i]) {
            correct_words++;
        }
    }

    return (double(correct_words) / expected.size()) * 100.0;
}

void printAccuracyReport(const string& expectedLine, const string& typedLine, double accuracy, double wps, double time_sec) {
    cout << "\nOriginal: " << expectedLine;
    cout << "\nYou typed: " << typedLine;
    cout << "\nAccuracy: " << accuracy << "%";
    cout << "\nTime taken: " << time_sec << " seconds";
    cout << "\nTyping speed: " << wps << " words per second\n";
}
