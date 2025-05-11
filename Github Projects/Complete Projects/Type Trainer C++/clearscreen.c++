#include <cstdlib>
#include "clearscreen.h"

    void clearScreen() {
        #ifdef _WIN32
            system("cls");
        #else
            system("clear");
        #endif
    }