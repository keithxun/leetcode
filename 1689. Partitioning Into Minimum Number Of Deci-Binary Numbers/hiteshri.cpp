#include <iostream>
#include <string>
using namespace std;

/**
 * Find the largest digit in this string, "maxDigit"
 * 
 * Since a deci-binary number only has 1s and 0s, need AT LEAST "maxDigit" 1s 
 * to build this number. So minimally, that is required for sure. 
 */

int minPartitions(string n) {

    int maxDigit = 0;
    for(char c : n) maxDigit = max(maxDigit, (int)(c - '0'));
    return maxDigit;
}

int main(){
    string s = "27346209830709182346";
    int result = minPartitions(s);
    cout << result << endl;
}