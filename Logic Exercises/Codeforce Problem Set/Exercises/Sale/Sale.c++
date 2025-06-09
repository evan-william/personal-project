 #include <iostream>
 #include <vector>
 #include <algorithm>

 using namespace std;
 int main () {
    int TvOnSale;
    int CarryCapacity;

    int Money = 0;

    cin >> TvOnSale >> CarryCapacity;

    vector<int> Price(TvOnSale); 
    for(int x = 0; x < TvOnSale ; x ++) { 
        cin >> Price[x];
    }

    sort(Price.begin(), Price.end());

    for (int y = 0; y < CarryCapacity; y ++) {
        if(Price[y] < 0) {
            Money += abs(Price[y]);
        }
    }

    cout << Money << endl;
    return 0;
 }