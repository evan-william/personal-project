#include <string>
#include <vector>
#include <chrono>

double calculateAccuracy(const std::vector<std::string>& expected, const std::vector<std::string>& typed);
void printAccuracyReport(const std::string& expectedLine, const std::string& typedLine, double accuracy, double wps, double time_sec);
double calculateTypingSpeed(double time_sec, int word_count);