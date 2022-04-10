/*
link : https://leetcode.com/problems/roman-to-integer/

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

*/
#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
class Solution {
public:
    map<char,int> dict = {
        {'I',1},
        {'V',5},
        {'X',10},
        {'L',50},
        {'C',100},
        {'D',500},
        {'M',1000},
    };

    int romanToInt(string s) {
        vector<int> vec;
        for(int i=0;i<s.size();i++){
            char x = s.at(i);
            if(dict.count(x)!=0){
                int temp = this->dict[x];
                vec.push_back(temp);
            }
            else{
                cout << "error:" << x <<endl;
            }

        }
        for(auto x: vec){
            cout << x <<endl;
        }
        return 1;
    }

};
int main(int argc, char** argv){
    vector<string> opt;
    for(int i=1;i<argc;i++){
        opt.push_back(string(argv[i]));
    }
    Solution solution;
    for(auto x:opt){
        cout <<solution.romanToInt(x) <<endl;
    }
    return EXIT_SUCCESS;
}
