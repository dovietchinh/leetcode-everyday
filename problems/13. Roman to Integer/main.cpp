#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
class Solution {
    public:
    int romanToInt(string s){
        map<string,int> label = {{"I",1},
            {"V",5},
            {"X",10},
            {"L",50},
            {"C",100},
            {"D", 500},
            {"M", 1000},
            {"IX", 9},
            {"IV", 4},
            {"XL", 40},
            {"XC", 90},
            {"CD", 400},
            {"CM",900},
        };
        // cout << label.at("A",NULL) << endl;
        // for(int i=0;i<s.length();i++){
        //     if label.at(i)
        // }
        return 1;
    };
};

int main(int argc, char** argv){
    auto r = Solution().romanToInt("MCMXCIV");
};

