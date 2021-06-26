// https://www.hackerrank.com/challenges/time-conversion/problem

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {
    /*
     * Write your code here.
     */
    string hour = s.substr(0, s.find(":"));
    stringstream ss;
    string day = s.substr(s.find("M") - 1);
    ss << hour;
    int h = 0;
    stringstream sa;
    ss >> h;
    if (day.compare("AM") == 0 && h == 12) {
        sa << "00";
    } else
    if (day.compare("PM") == 0 && h < 12) {
        h+=12;
        sa << h;
    } else if (h < 12) {
        sa << "0" << h;
    } else {
        sa << "12";
    }
    sa << s.substr(2, s.length() - 4);
    return sa.str();

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
