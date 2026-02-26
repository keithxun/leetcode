#include <iostream>
#include <string>
using namespace std;

void addOne(string &s){
    int n = s.size()-1;
    while(n >= 0 && s[n] == '1') s[n--] = '0';  // convert all trailing '1's to '0'
    if(n >= 0) s[n] = '1'; 
    else s = '1' + s; // string has all '1's; need to add a leading '1'
}

int numSteps(string s){
    int steps = 0;
    while(s != "1"){
        if(s[s.size()-1] == '0')s.pop_back(); // divide by 2 by removing the last bit
        else addOne(s);
        steps += 1;
    }
    return steps;
}

int main(){
    string s = "1101";
    int steps = numSteps(s);
    cout << steps << endl;
}