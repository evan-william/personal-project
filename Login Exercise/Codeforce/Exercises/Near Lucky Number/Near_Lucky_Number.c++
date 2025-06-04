#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main (){
  string number;
  int counter = 0;
  
  cin >> number;
  
  for (auto x : number) {
       if (x == '7' || x == '4') {
        counter += 1;
       }
    }

  if (counter == 4 || counter == 7) {
    cout << "YES" << endl;
  }
  else {
    cout << "NO" << endl;
  }
}