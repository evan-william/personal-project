#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

void easy();
void medium();
void hard();
void insane();
void clearScreen();
int highScore = 0;

void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void menu() {
    int action;

    cout << "===== WELCOME =======" << endl;
    cout << " Choose Difficulty" << endl;
    cout << "======================" << endl;
    cout << "1. Easy" << endl;
    cout << "2. Medium" << endl;
    cout << "3. Hard" << endl;
    cout << "4. Insane" << endl;
    cout << "5. Exit" << endl;
    cout << "======================" << endl;
    cout << "Input Action: ";
    cin >> action;

    if (action == 1){
        easy();
    } else if (action == 2) {
        medium();
    } else if (action == 3) {
        hard();
    } else if (action == 4) {
        insane();
    } else if (action == 5) {
        cout << "Goodbye!" << endl;
        exit(0);
    } else { 
        cout << "Not a valid option!" << endl;
        menu(); 
    }
}

void easy() {
    int counter = 1;
    int score = 0;

    while (true) {
        cout << "\n====== QUESTION " << counter << " ======";
        int randomNumber1 = rand() % 10 + 1;
        int randomNumber2 = rand() % 10 + 1;
        int userAnswer;
        int correctAnswer = randomNumber1 + randomNumber2;

        cout << "\nWhat is " << randomNumber1 << " + " << randomNumber2 << "? ";
        cout << "\n====== 0 to Exit =======" << endl;

        cout << "Answer: ";
        cin >> userAnswer;

        if (userAnswer == correctAnswer) {
            cout << "Correct! :)" << endl;
            counter += 1;
            score += 1;
            cout << "Score + 1" << " (" << score << ")" << endl;
        } else if (userAnswer == 0) {
            cout << "Goodbye!" << endl;
            if (score > highScore) {
                highScore = score;
            }
            clearScreen();
            cout << "Last high score: " << highScore << endl << endl;
            menu();
        } else {
            cout << "Wrong! The correct answer was " << correctAnswer << "." << endl;
            counter += 1;
        }
    }
}

void medium() {
    int counter = 1;
    int score = 0;

    while (true) {
        cout << "\n====== QUESTION " << counter << " ======";
        int randomNumber1 = rand() % 100 + 1;
        int randomNumber2 = rand() % 100 + 1;
        int userAnswer;
        int correctAnswer = randomNumber1 + randomNumber2;

        cout << "\nWhat is " << randomNumber1 << " + " << randomNumber2 << "? ";
        cout << "\n====== 0 to Exit =======" << endl;

        cout << "Answer: ";
        cin >> userAnswer;

        if (userAnswer == correctAnswer) {
            cout << "Correct! :)" << endl;
            counter += 1;
            score += 2;
            cout << "Score + 2" << " (" << score << ")" << endl;
        } else if (userAnswer == 0) {
            cout << "Goodbye!" << endl;
            if (score > highScore) {
                highScore = score;
            }
            clearScreen();
            cout << "Last high score: " << highScore << endl << endl;
            menu();
        } else {
            cout << "Wrong! The correct answer was " << correctAnswer << "." << endl;
            counter += 1;
        }
    }
}

void hard() {
    int counter = 1;
    int score = 0;

    while (true) {
        cout << "\n====== QUESTION " << counter << " ======";
        int randomNumber1 = rand() % 1000 + 1;
        int randomNumber2 = rand() % 1000 + 1;
        int userAnswer;
        int correctAnswer = randomNumber1 + randomNumber2;

        cout << "\nWhat is " << randomNumber1 << " + " << randomNumber2 << "? ";
        cout << "\n====== 0 to Exit =======" << endl;

        cout << "Answer: ";
        cin >> userAnswer;

        if (userAnswer == correctAnswer) {
            cout << "Correct! :)" << endl;
            counter += 1;
            score += 5;
            cout << "Score + 5" << " (" << score << ")" << endl;
        } else if (userAnswer == 0) {
            cout << "Goodbye!" << endl;
            if (score > highScore) {
                highScore = score;
            }
            clearScreen();
            cout << "Last high score: " << highScore << endl << endl;
            menu();
        } else {
            cout << "Wrong! The correct answer was " << correctAnswer << "." << endl;
            counter += 1;
        }
    }
}

void insane() {
    int counter = 1;
    int score = 0;

    while (true) {
        cout << "\n====== QUESTION " << counter << " ======";
        int randomNumber1 = rand() % 10000 + 1;
        int randomNumber2 = rand() % 10000 + 1;
        int userAnswer;
        int correctAnswer = randomNumber1 + randomNumber2;

        cout << "\nWhat is " << randomNumber1 << " + " << randomNumber2 << "? ";
        cout << "\n====== 0 to Exit =======" << endl;

        cout << "Answer: ";
        cin >> userAnswer;

        if (userAnswer == correctAnswer) {
            cout << "Correct! :)" << endl;
            counter += 1;
            score += 12;
            cout << "Score + 12" << " (" << score << ")" << endl;
        } else if (userAnswer == 0) {
            cout << "Goodbye!" << endl;
            if (score > highScore) {
                highScore = score;
            }
            clearScreen();
            cout << "Last high score: " << highScore << endl << endl;
            menu();
        } else {
            cout << "Wrong! The correct answer was " << correctAnswer << "." << endl;
            counter += 1;
        }
    }
}

int main () {
    srand(time(0));
    string name;
    cout << "\nPlease enter your name: ";
    getline(cin, name);
    cout << "Welcome, " << name << "!" << endl << endl;

    menu();
    return 0;
}
