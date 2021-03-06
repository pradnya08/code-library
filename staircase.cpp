// https://www.hackerrank.com/challenges/staircase/problem

#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {
    for (int i = n; i > 0; i--) {
        for (int j = 1; j <= n; j++) {
            if (j >= i) {
                cout << "#";
            } else {
                cout << " ";
            }
        }
        cout << "\n";
    }

}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
