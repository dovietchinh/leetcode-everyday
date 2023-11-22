#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution {
    public:
        int balancedStringSplit(string s) {
            
        }
};

int main(int argc, char** argv){
    Solution a;
    vector<string> input{"RLRRLLRLRL","RLRRRLLRLL","LLLLRRRR"};
    for(string i : input){
        int r = a.balancedStringSplit("LLLLRRRR");
        cout << "r: " << r << endl;
    };
    return 1;  
};