// https://www.hackerrank.com/challenges/counting-valleys/problem

#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
    bool inValley = false;
    int level = 0;
    int num = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s.at(i) == 'U') level++;
        if (s.at(i) == 'D') level--;
        if (level >= 0) inValley = false;
        if (level < 0 && !inValley) {
            num++;
            inValley = true;
        }
    }
    return num;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
